import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("enter a word: ").upper()
answer_list = [phonetic_dict[letter] for letter in word]
print(answer_list)
