def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counts = count_letters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    report(counts)
    print("--- End report ---")

    #print(f"This is the list of chars: {count}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    low_text = text.lower()
    letter_counts ={}
    for char in low_text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts


def report(counts):
    sorted_counts = dict(sorted(counts.items()))
  
    for char in sorted_counts:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_counts[char]} times")


main()