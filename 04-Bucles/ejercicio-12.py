text = input("Write a text: ")

word = input("Write a word: ")

count = 0
for i in text:
    if i == word:
        count += 1

print(f"The word {word} is repeted {count} times")
