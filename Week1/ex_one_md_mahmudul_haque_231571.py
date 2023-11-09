"""Developed by Md. Mahmudul Haque

tasks: week 1 assignment

need a sub-folder 'reviews'
"""

from collections import Counter
import os

def load_bytes(file_dir: str) -> str:
    """loading bytes from given sub-directory

    attempts to load the file and read using
    read byte mode. then returns byte string

    Args:
        file_dir (str): sub-directory string

    Returns:
        str: byte string (default 4 byte is read)
    """
    with open(file_dir, 'rb') as file:
        # first 4 byte is read
        first_4_bytes = file.read(4)
    return first_4_bytes

def read_files(file_dir: str, encoding: str='utf-8') -> list:
    """loading files from given sub-directory

    attempts to read the file from given sub-directory
    opens the file in read mode and return the lines
    in list

    Args:
        file_dir (str): sub-directory string
        encoding (str): encoding name, default to 'utf-8'

    Returns:
        (list): contents in string
    """
    # avoiding reading in binary mode as it throws error
    # for utf-16 file ecoding
    # source: https://stackoverflow.com/questions/48830535/how-to-solve-binary-mode-doesnt-take-an-encoding-argument
    line_list = []
    with open(file_dir, 'r', encoding=encoding) as file:
        # reading line by line with auto split
        lines = file.readlines()
        line_list.extend(line.strip("\n") for line in lines)
    return line_list

def detect_endcoding(four_bytes: str) -> str:
    """detection of encoding in files

    attempts to decode using the pre-set list
    of encoders. then determines the encoding
    if unable to do so, raises error.

    Args:
        four_bytes (str): first four byte string

    Returns:
        str: encoding name string
    """
    encodings_to_check = ['utf-8', 'utf-16']
    detected_encoding = None
    for byte_encoding in encodings_to_check:
        try:
            # attempt to decode the file content with
            # this encoder
            detected_encoding = four_bytes.decode(byte_encoding)
            return byte_encoding
        except UnicodeDecodeError:
            continue

    if detected_encoding:
        return f"The encoding of the file is: {detected_encoding}"
    return "Unable to determine the file's encoding with the provided encodings."

def process_text(input_text: str) -> list:
    """processing text

    processes texts with alphanumeric and spaces
    only and lower case the texts then returns
    as string

    Args:
        input_text (str): text as string

    Returns:
        (str): processed text
    """
    return "".join(
        char.lower() for char in input_text if char.isalpha() or char.isspace()
    )

def sent_to_word(input_text: str):
    """sentence to word list

    sentence split to words. splitting
    criteria by default is space

    Args:
        input_text (str): accept sentence string

    Returns:
        (list): returns list of words
    """
    return input_text.split(" ")

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

if __name__=="__main__":
    folder_name = input("Please Enter the Sub-Folder Name: ")
    file_list = os.listdir(folder_name)
    # task 2 (first part)
    text_list = []
    #=============
    for file_path in file_list:
        file_location = os.path.join(f"{os.getcwd()}/{folder_name}", file_path)
        # task 1
        four_bytes_string = load_bytes(file_location)
        file_name = os.path.basename(file_location)
        encoding = detect_endcoding(four_bytes_string)
        print(f"\n[Task 1]: Name of the file: {file_name} \nEncoding: {encoding}")
        lines = read_files(file_location, encoding)
        print("\nContents in text:")
        print("".join(lines))
        #=============

        #task 2 (second part)
        text_list.extend(iter(lines))
        #============= (some due at the end)

    #task 2 (third part)
    print("\n[Task 2]: Splitted Text List:")
    print(text_list)
    print("\n[Task 2]: List length:")
    print(len(text_list))
    #=============

    #task 3
    list_of_word_list = []
    for text in text_list:
        processed_text = process_text(text)
        list_of_word_list.append(sent_to_word(processed_text))
    print("\n[Task 3]:")
    print(list_of_word_list)
    #=============

    #task 4
    word_counter = word_counter(list_of_word_list)
    print("\n[Task 4]: 5 Most Common Words: ", word_counter.most_common(5))
    print("\n[Task 4]: No we cannot use this top words to infer what the text is about as all of the top words are stopwords")
    #=============