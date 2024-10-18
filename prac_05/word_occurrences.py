"""
Word Occurrences
Estimate: 15 minutes
Actual: 26 minutes
"""

word_to_count = {}
user_phrase = input("Text: ").lower().split()
for word in user_phrase:
    if word in user_phrase:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

user_phrase = list(word_to_count.keys())
user_phrase.sort()

longest_word = len(max(user_phrase, key=len))

for word in user_phrase:
    print(f"{word:{longest_word}} : {word_to_count[word]}")
