# Purpose: Create a program that converts the first letter of each word, to a uppercase, in a paragraph
# Author: Mihle Makapela
# Date: 19 December 2022

# Method
paragraph = input("Enter a paragraph: \n")
list_of_words = paragraph.split(" ")

# Explain line 10 to line 13
new_list_of_words = []
for index in range(0, len(list_of_words) - 1):
    each_word = list_of_words[index]
    new_list_of_words.append(each_word.title())
    
# Fix the bug in line 16
new_paragraph = new_list_of_words.join(" ")

print(new_paragraph)