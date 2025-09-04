# word_frequency.py

# Sample sentence
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Create a dictionary to store word frequency
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display the word frequency
print("Word frequency in the sentence:")
for word, count in frequency.items():
    print(f"{word}: {count}")
