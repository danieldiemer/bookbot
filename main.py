def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # print(f"Word Count: {word_count(text)}")
    # print(f"Character Count: {char_count(text)}")
    book_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string_input):
    return len(string_input.split())

def char_count(string_input):
    char_dict={}
    string_input=string_input.lower()
    for i in string_input:
        if i in char_dict:
            char_dict[i] += 1
        elif i.isalpha():
            char_dict[i] = 1
    return char_dict

def book_report(text):
    print("--- Begin Book Report ---")
    print(f"Word Count: {word_count(text)}")
    char_dict = char_count(text)
    print(f"\nSorted by count\n")
    for thing in char_list(char_dict):
        print(f" Character '{thing['character']}' was found {thing['count']} times")
    print("--- End Book Report ---")

def myKey(e):
    return e['count']

def char_list(char_dict):
    new_list = []
    for i in char_dict:
        new_list.append({"character": i, "count": char_dict[i]})
    new_list.sort(reverse=True, key=myKey)
    return new_list

main()
