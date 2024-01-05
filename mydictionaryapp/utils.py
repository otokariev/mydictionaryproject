def add_to_file(word1, word2):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    with open("file.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    words = [line.split('-') for line in lines]
    return words
