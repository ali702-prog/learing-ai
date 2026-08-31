# Open and read the file
file = open("address.txt", "r")
text = file.read()
file.close()

# Count the words
word_count = len(text.split())

# Append the word count
file = open("address.txt", "a")
file.write("\nWord Count: " + str(word_count))
file.close()

print("Word Count:", word_count)