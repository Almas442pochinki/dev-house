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

def long_word(words: list[str]) -> dict:
    max_length = 0
    longest_word = ""
    for word in words:
        if (len(word) > max_length):
            max_length = len(word)
            longest_word = word
    return {'word': longest_word, 'length': max_length}

def top_ten_words(words: list[str]) -> list[tuple[str, int]]:
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print(word_count.keys())
    return sorted_words[:10]

def main():
    words = read_file(file_name)
    print(f"Number of words in the file: {len(words)}")
    longest_word_info = long_word(words)
    print(f"Longest word: {longest_word_info['word']}, Length: {longest_word_info['length']}")
    top_words = top_ten_words(words)
    print("Top 10 words by frequency:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()