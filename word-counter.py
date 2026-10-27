import os 
import sys

file_name = "/Users/almas/Desktop/dev-house/sample.txt"
def read_file(file_name) -> list[str]:
    words = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words

def main():
    words = read_file(file_name)
    print(f"Number of words in the file: {len(words)}")

if __name__ == "__main__":
    main()