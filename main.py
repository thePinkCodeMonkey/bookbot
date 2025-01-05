import pprint
def word_count(text: str) -> int:
    wordList = text.split()
    return(len(wordList))

def character_count(text: str) -> dict:
    character_dictionary = {}
    for char in text:
         
        lower_char = char.lower()
        if (lower_char) in character_dictionary:
            character_dictionary[lower_char] += 1
        else:
            character_dictionary[lower_char] = 1
        
    return character_dictionary 

def main() -> None:
    with open("books/frankenstein.txt") as f:
        text = f.read()
        count = word_count(text)
        char_dict = character_count(text)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document")

        for char in char_dict:
            print(f"The character '{char}' was found {char_dict[char]} times")
        
        print("--- End report ---")
main()