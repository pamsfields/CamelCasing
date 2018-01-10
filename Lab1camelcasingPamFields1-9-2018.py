#Camel Case

sentence = input("Please enter a sentence").lower()

words = []
words = sentence.split(' ')
capitalized = []
for word in words[1:]:
    final_words = word[0].upper() + word[1:]
    capitalized.append(final_words)
capitalized.insert(0,words[0])
output = ''.join(capitalized)
print(output)
