import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)


def create_word():
    user_word = input("Enter a word to see it phonetically: ").upper()
    try:
        nato_answer = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Only letters in the Alphabet please.")
        create_word()
    else:
        print(nato_answer)


create_word()
