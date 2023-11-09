"""
Developed by Md. Mahmudul Haque
Matriculation No.: 231571
Assignment: Week 3

Note:
to download the stemmer, lemmatizer, and stopwords,
uncomment these lines below in the main block:
    # print("Downloading...")
    # nltk.download('stopwords')
    # nltk.download("wordnet")
    # nltk.download("porter_test")
"""

import re
import nltk
from collections import Counter
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

def read_file(file_path: str) -> str:
    """reading file from given directory

    Args:
        file_path (str): file in xml format

    Returns:
        str: returning the strings from the file
    """
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        return "".join(file.readlines())

def filter_speech(content_str: str) -> list:
    """filtering the contents of "Speech" element
    from given input string

    Args:
        content_str (str): string input

    Returns:
        list: list of all contents that match the pattern
    """
    pattern = re.compile(r"<Speech>(.*)</Speech>")
    return re.findall(pattern=pattern, string=content_str)

def clean_text(speech_list: list) -> list:
    """cleaning text by extracting alphabets and
    then splitting into word list for each speech

    Args:
        speech_list (list): _description_

    Returns:
        list: list of list with strings.
    """
    pattern = re.compile(r"[A-Za-z]+")
    return [re.findall(pattern=pattern, string=speech) for speech in speech_list]

def to_lowercase(input_cleaned_text: list) -> list:
    """case changing of all contents in each list
    item strings

    Args:
        cleaned_text (list): list of list with alphabets only texts

    Returns:
        list: list of lists with lowercase transformation
    """
    return [[word.lower() for word in speech] for speech in input_cleaned_text]

def word_counter(list_of_list_word: list) -> Counter:
    """word counter from given list of word list

    count words from list of word lists and uses Counter
    class to count the words with word: count mapping

    Args:
        list_of_list_word (list): list of list with words

    Returns:
        (Counter): Counter object with dictionary stating word and frequency
    """
    all_words = [
        word
        for word_list in list_of_list_word
        for word in word_list
    ]
    return Counter(all_words)

def stem_words(list_of_list_words: list) -> list:
    """stemming words list from list of words
    using NLTK PorterStemmer class

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: stemming list of list of words
    """
    ps = PorterStemmer()
    return [[ps.stem(word) for word in word_list] for word_list in list_of_list_words]

def extract_word_lemma(list_of_list_words: list) -> list:
    """lemmatization of words list from list of words
    using NLTK PorterStemmer class

    Args:
        list_of_list_words (list): list of words inside a list

    Returns:
        list: lemmatized list of list of words
    """
    lemmatizer = WordNetLemmatizer()
    return [[lemmatizer.lemmatize(word) for word in word_list] for word_list in list_of_list_words]

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

if __name__ =="__main__":
    # print("Downloading...")
    # nltk.download('stopwords')
    # nltk.download("wordnet")
    # nltk.download("porter_test")

    print("[Task 1, Part 1]:\n")
    contents = read_file("trump.xml")
    print(contents[:500])
    print("\n=======================\n")
    print("[Task 1, Part 2]: For convenience, printing first speech's first 100 words only\n")
    speech_text = filter_speech(content_str=contents)
    print(speech_text[0][:100])
    print("\n=======================\n")

    print("[Task 2, Part 1]: For convenience, printing first speech's first 100 words only\n")
    cleaned_text = clean_text(speech_text)
    print(cleaned_text[0][:100])
    print("\n=======================\n")
    lowercased_cleaned_text = to_lowercase(cleaned_text)
    print("[Info:] Printing first 10 words only from first list")
    print(lowercased_cleaned_text[0][:10])
    print("[Task 2, Part 2]:\n")
    counted_words = word_counter(lowercased_cleaned_text)
    print("10 Most Common Words\n")
    print(counted_words.most_common(10))
    print("\n=======================\n")

    print("[Task 3, Part 1]: For convenience, 1st list's 4 to 49 words are printed from the list\n")
    stemmed_words_list = stem_words(lowercased_cleaned_text)
    print("\nStemming:\n")
    print(stemmed_words_list[0][5:50])
    word_lemma_list = extract_word_lemma(lowercased_cleaned_text)
    print("\nLemmatization:\n")
    print(word_lemma_list[0][5:50])
    print("\n=======================\n")

    print("[Task 3, Part 2]: Comparing 1st list's 100 words\n")
    for stem, lemma in zip(stemmed_words_list[0][0:100], word_lemma_list[0][0:100]):
        if stem!=lemma:
            print(f"Stem: {stem}\tLemma: {lemma}")
    print("\nWe can clearly see that some information in stemming is missing\
Such as 'evrybody' changes into 'everybodi' in stemming which is causing\
misspelling. Also some tense and parts of speech are also changing i.e.: Stem: 'say' where as\
the main word in 'saying' which is kept intact in Lemmatization.\
Lemmatization is also struggling like distinguishing 'as' and 'a' where Stemming worked well there\
But, in general, Lemmatization is doing good in comparison in this given context.")

    print("[Task 4, Part 1]: For convenience, printing 1st list's 100 words\n")
    full_cleaned_texts = remove_stopwords(word_lemma_list)
    print(full_cleaned_texts[0][0:100])
    re_counted_words = word_counter(full_cleaned_texts)
    print("\n10 Most Common Words\n")
    print(re_counted_words.most_common(10))
    print("\n=======================\n")

    print("[Task 4, Part 2]:\n")
    for with_stopwords, without_stopwords in zip(
        counted_words.most_common(10),
        re_counted_words.most_common(10)
    ):
        print(f"With Stop Words: {with_stopwords}\tWithout Stop Words: {without_stopwords}")
    print("\nThe stopwords are not there anymore.\
But also, not fully recognizable yet about the theme of the texts from top 10 most common words")
