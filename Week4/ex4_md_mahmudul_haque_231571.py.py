"""
Developed by Md. Mahmudul Haque
Matriculation No.: 231571
Assignment: Week 4

Note:
1. I did not understand properly the pattern
of Task 3 (b), as there is no special character
defining file5.txt, I mixed the task 3 b and c
together. Would be really helpful, if you kindly
give me some instructions over moodle for this
if I get it wrong.

2. to download the stemmer, lemmatizer, and stopwords,
uncomment these lines below in the main block:
    # print("Downloading...")
    # nltk.download('stopwords')
    # nltk.download("wordnet")
    # nltk.download("porter_test")
"""

import os
import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

def read_files(file_dir: str) -> dict:
    """reading files from the given directory
    and returning as dict of string.

    reading each files and storing as dict of string
    for each story with the corresponding filename
    as key.

    Args:
        file_dir (str): string with directory full name

    Returns:
        dict: dict with strings where filename as keys
    """
    story_dict = defaultdict(lambda: None)
    file_location_list = os.listdir(file_dir)
    for file_name in file_location_list:
        with open(
            file=f"{file_dir}/{file_name}",
            mode="r",
            encoding="utf-8") as file_object:
            lines = file_object.read()
        story_dict[file_name] = lines

    return story_dict

def filter_text(content_str: str) -> object:
    """filtering the contents with
    'Page | page number book name - J.K. Rowling '
    element from given input string.

    matches with the defined pattern and then searches
    for the pattern in the parameter string.

    Args:
        content_str (str): string input

    Returns:
        object: search object from re after a match
    """
    pattern = re.compile(r"Page \| ([0-9]+)\s([A-Za-z\s]+) - J.K. Rowling ")
    return re.search(pattern=pattern, string=content_str)

def remove_page_indicator(content_str: str) -> str:
    """removing the contents with
    'Page | page number book name - J.K. Rowling '
    element from given input string.

    matches with the defined pattern and then substitutes
    with empty string.

    Args:
        content_str (str): string input

    Returns:
        str: string with no page indicator
    """
    pattern = re.compile(r"Page \| ([0-9]+)\s([A-Za-z\s]+) - J.K. Rowling ")
    return re.sub(pattern=pattern, repl="" , string=content_str)

def remove_headers(content_str: str) -> str:
    """removing the headers with
    CAPS from given input string.

    matches with the defined pattern.
    and then returns the rest of the string
    from that matched index

    Args:
        content_str (str): string input

    Returns:
        str: string with no header
    """
    pattern = re.compile(r"\b(?:[A-Za-z]*[a-z]+[A-Z]|[A-Za-z]*[A-Z]+[a-z])[A-Za-z]*\b")
    return content_str[re.search(pattern=pattern, string=content_str).start():]

def replace_line_breaks(content_str: str) -> str:
    """replacing the '\n' with
    empty string from given input string.

    matches with the defined pattern for '\n'.
    and then returns the rest of the string
    by replacing line breaks with ''

    Args:
        content_str (str): string input

    Returns:
        str: string with no header
    """
    return content_str.replace("\n", "")

def clean_text(content_list: list) -> list:
    """cleaning text by extracting alphabets and
    then splitting into word list for each speech

    Args:
        content_list (list): list of strings

    Returns:
        list: list of list with strings.
    """
    pattern = re.compile(r"[A-Za-z]+")
    return [re.findall(pattern=pattern, string=content) for content in content_list]

def to_lowercase(input_cleaned_text: list) -> list:
    """case changing of all contents in each list
    item strings

    Args:
        cleaned_text (list): list of list with alphabets only texts

    Returns:
        list: list of lists with lowercase transformation
    """
    return [[word.lower() for word in content] for content in input_cleaned_text]

def remove_stopwords(list_of_list_words: list) -> list:
    """removing stop words from list of word list by matching
    English stop words and extracting those out

    Args:
        list_of_list_words (list): list of word lists with stop words

    Returns:
        list: stop word free list of word lists
    """
    stopword_list = stopwords.words("english")

    return [
        [word for word in word_list if word not in stopword_list]
        for word_list in list_of_list_words
    ]

def stem_words(list_of_list_words: list) -> list:
    """stemming words list from list of words
    using NLTK PorterStemmer class

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: stemming list of list of words
    """
    porter_stemmer = PorterStemmer()
    return [
        [
            porter_stemmer.stem(word)
            for word in word_list
        ]
        for word_list in list_of_list_words
    ]

def extract_word_lemma(list_of_list_words: list) -> list:
    """lemmatization of words list from list of words
    using NLTK WordNetLemmatizer class

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: lemmatized list of list of words
    """
    lemmatizer = WordNetLemmatizer()
    return [
        [
            lemmatizer.lemmatize(word)
            for word in word_list
        ]
        for word_list in list_of_list_words
    ]

def calculate_tfidf(list_of_list_words: list) -> list:
    """calculating tf-idf of each list from given
    list of list of words.

    from the list of words in the list, calculate
    tf-idf matrix and use that matrix to find the
    features. then, use the tf-idf matriz to get
    all the scores for each document and then sort
    based on top appearence. lastly, uses feature
    names that matches the top appearence indices
    and returns the top word lists of each
    document.

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: each doc based top words after tf-idf calculation
    """
    corpus = [" ".join(word_list) for word_list in list_of_list_words]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    feature_names = tfidf_vectorizer.get_feature_names_out()

    top_word_dict = defaultdict(lambda: None)
    for i, _ in enumerate(list_of_list_words):
        tfidf_scores_doc = tfidf_matrix[i, :].toarray().flatten()
        top_indices = tfidf_scores_doc.argsort()[-10:][::-1]
        top_words = [feature_names[idx] for idx in top_indices]
        top_word_dict[i] = top_words

    return top_word_dict

if __name__=="__main__":
    # print("Downloading...")
    # nltk.download('stopwords')
    # nltk.download("wordnet")
    # nltk.download("porter_test")

    print("[Task 1]:")
    stories = read_files("./Potter")
    print("\n\n[Task 1]: Keys of the dictionary:\n\n")
    print(stories.keys())
    print("\n\n[Task 1]: Length of one file:\n\n")
    print(len(stories["file1.txt"]))
    print("\n\n[Task 1]: Length of one file:\n\n")
    print(stories["file1.txt"][-100:])
    print("\n\n==============\n\n")

    print("[Task 2]:")
    new_keys = {key: match.group(2).strip() for key, value in stories.items() if (match := filter_text(value))}
    print("\n\n[Task 2]: New Keys by Book Name:\n\n")
    stories = {new_keys[old_key]: value for old_key, value in stories.items()}
    print(stories.keys())
    print("\n\n[Task 2]: Checking after Replacing the Keys with Book Name:\n\n")
    print(stories["Harry Potter and the Goblet of Fire"][-100:])
    print("\n\n==============\n\n")

    print("[Task 3]:")
    print("\n\n[Task 3(a)]: Before Page Indicator Removal\n\n")
    print(stories["Harry Potter and the Half Blood Prince"][-200:])
    print("\n\n[Task 3(a)]: After Page Indicator Removal\n\n")
    stories = {key: remove_page_indicator(value) for key, value in stories.items()}
    print(stories["Harry Potter and the Half Blood Prince"][-200:])

    print("[Task 3(b and c)]:")
    print("\n\n[Task 3(b and c)]: Before Trimming and Header Removal\n\n")
    print(stories["Harry Potter and the Order of the Phoenix"][0:100])
    stories = {key: remove_headers(value) for key, value in stories.items()}
    print("\n\n[Task 3(b and c)]: After Trimming and Header Removal\n\n")
    print(stories["Harry Potter and the Order of the Phoenix"][0:100])

    print("[Task 3(d)]:")
    print("\n\n[Task 3(d)]: Before Line Breaks Removal\n\n")
    print(stories["Harry Potter and the Chamber of Secrets"][0:100])
    stories = {key: replace_line_breaks(value) for key, value in stories.items()}
    print("\n\n[Task 3(d)]: After Line Breaks Removal\n\n")
    print(stories["Harry Potter and the Chamber of Secrets"][0:500])
    stories_list = [value for _, value in stories.items()]
    print("\n\n[Task 3(a to d) Final Output List of Lists]:\n\n")
    print(len(stories_list))
    print(stories_list[6][0:500])
    print("\n\n==============\n\n")

    print("[Task 4]:")
    print("\n\n[Task 4(a)]: After Cleaning Text\n\n")
    cleaned_text_list = clean_text(stories_list)
    print(len(cleaned_text_list))
    print(cleaned_text_list[5][0:100])

    print("\n\n[Task 4(b)]: After Converting To Lowercase Text\n\n")
    cleaned_text_list = to_lowercase(cleaned_text_list)
    print(cleaned_text_list[4][0:100])

    print("\n\n[Task 4(c)]: Removing Stopwords:\n\n")
    cleaned_text_list = remove_stopwords(cleaned_text_list)
    print(cleaned_text_list[4][0:100])

    print("\n\n[Task 4(d)]: Stemmed Words:\n\n")
    stemmed_text_list = stem_words(cleaned_text_list)
    print(stemmed_text_list[4][0:100])

    print("\n\n[Task 4(d)]: Lemmatized Words:\n\n")
    lemmatized_text_list = extract_word_lemma(cleaned_text_list)
    print(lemmatized_text_list[3][0:100])
    print("\n\n==============\n\n")

    print("[Task 5]:")
    print("\n\nTop words for story for cleaned_text_list\n\n")
    top_word_dict = calculate_tfidf(cleaned_text_list)
    key_list = list(stories.keys())
    for i, top_words in top_word_dict.items():
        print(f"{key_list[i]}: {top_words}")

    print("\n\nTop words for story for lemmatized_text_list\n\n")
    top_word_dict = calculate_tfidf(cleaned_text_list)
    key_list = list(stories.keys())
    for i, top_words in top_word_dict.items():
        print(f"{key_list[i]}: {top_words}")

    print("\n\nNot lemmatized text list nor the simple cleaned text list, none of those gave me the idea \
of what the books are about. The most probable reason according to my understanding, \
TF-IDF highlights words that are important within a \
document relative to the entire corpus, but it may not \
always capture the overall theme or topic of a document. \
Understanding the context and content of the documents is crucial for meaningful interpretation. \
Unfortunately, TF-Idf does not understand the topics.")
    print("\n\n==============\n\n")
