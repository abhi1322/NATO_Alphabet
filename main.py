import pandas

# reading data from csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# converting to dictionary
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# getting user input
word = input("Enter your word here : ").upper()

# adding letter to list from dictionary
NATO_alphabet_list = [alphabet_dict[letter] for letter in word]

# Printing list
print(NATO_alphabet_list)
