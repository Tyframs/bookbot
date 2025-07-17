from stats import count_words, count_letters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    return get_book_text("books/frankenstein.txt")

# print("============ BOOKBOT ============")
# print("Analyzing book found at books/frankenstein.txt...")
# print("----------- Word Count ----------")

num_words = count_words(main())
print(f"Found {num_words} total words")

# print("--------- Character Count -------")

num_letters = count_letters(main())
letters = sort_dict(count_letters(main()))
filtered_letters = {letter['key']: letter['num'] for letter in letters if letter['key'].isalpha()}

for k, v in filtered_letters.items():
    print(f"{k}: {v}")

# print("============= END ===============")