import os
from processfun import *

def main():
    source = input("\nEnter your file name (or type the abstract): ").strip()
    file_name = source if source.lower().endswith(".txt") else source + ".txt"
    if os.path.isfile(file_name):
        tokens = text_split(file_name)
    elif any(char.isspace() for char in source):
        tokens = tokenize(source)
    else:
        raise FileNotFoundError(f"Can't find file: {file_name}")

    search_words = input("\nEnter several key words (separated by comma): ").split(',')

    references = input("\nEnter 2 reference numbers for their longest common prefix (separated by space):\n ").split()
    if len(references) != 2:
        raise ValueError("Please enter exactly two reference numbers.")
    str1, str2 = references

    char_classify_count(tokens)

    sentences = Tokens2Sentence(tokens)
    sentences = case_normalization(sentences)
    text = "\n".join(sentences)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
    

    specify_words(search_words, tokens)

    LCP = compare(str1, str2)
    if LCP == "":
        print("\nNO LCP in these 2 reference numbers.\n")
    else:
        print(f"\nLCP in 2 ref numbers are: {LCP}\n")

    print("\nProcessed file has been stored in output.txt.\n")

if __name__ == "__main__":
    main()
