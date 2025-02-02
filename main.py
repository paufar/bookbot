# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)

    words = file_contents.split()
    # print(len(words))

    character_count = {}

    for letter in file_contents:
      lowered_letter = letter.lower()
      if lowered_letter not in character_count:
        character_count[lowered_letter] = 1
      else:
        character_count[lowered_letter] += 1

    # print(character_count)
    alpha_list = []
    for item in character_count:
      if item.isalpha():
        alpha_list.append({"letter": item, "num": character_count[item]})

    alpha_list.sort(reverse=True, key=sort_on)
    print(alpha_list)
main()