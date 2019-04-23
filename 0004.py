# Count the number of occurrences of every word in a English text
import re

file_name = "english file.txt"
with open(file_name) as file_object:
    sentence = file_object.read()
# Input the text

puntuation=",:."

sentence = re.sub(r'[{}]+'.format(puntuation)," ",sentence)
sentence = sentence.lower()
# Remove the puntuations and capitals

list1 = sentence.split()
# Split the words

list2 = list(set(list1))
# Use set to remove repetitive words

dir1 = {}
# Create a dictionary to store the data

for x in range(len(list2)):
    dir1[list2[x]]=0
    for y in range(len(list1)):
        if list2[x] == list1[y]:
            dir1[list2[x]] += 1

print(dir1)
