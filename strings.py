from collections import Counter
import string

# Input paragraph
print("Enter the paragraph (type 'END' to finish):")
line = ""
while True:
    temp = input()
    if temp.strip().upper() == "END":
        break
    line += temp + " "


line = line.lower()


translator = str.maketrans('', '', string.punctuation)
clean_line = line.translate(translator)

words = clean_line.split()


frequency = Counter(words)


vowelcount =0
for i in line:
    if(i == 'a' or i=='e' or i=='o' or i=='u' or i=='i'): vowelcount+=1


print("\n*** Text Analysis Tool ***")
print("Number of words:", len(words))
print("Word Frequency:", frequency)
print("Top 3 Frequent Words:", frequency.most_common(3))
print("Count of vowels:", vowelcount)
