
"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

# def generate_phrase(characters, phrase):
#     # iter = 0
#     list_ph = list(phrase)
#     list_char = list(characters)
#     if len(list_char) >= len(list_ph):
#         for char in list_char:
#             if char in list_ph:
#                 list_ph.remove(char)
#         return len(list_ph) == 0
#     else:
#         return False



# def generate_phrase(characters, phrase):
#     total_characters = len(characters)
#     total_phrase = len(phrase)
#     if total_characters >= total_phrase:
#         phrases = [i for i in phrase]
#         characterss = [i for i in characters]
#         for x in phrases:
#             if x in characterss:
#                 characterss.remove(x)
#         print(phrases)
#         print(characterss)


    #     new_list = list(set(characterss).intersection(phrases))
    #     print(new_list)
    #
    #
    #
    #     if count == 0:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False




# def generate_phrase(characters, phrase):
#     word = []
#     total_characters = len(characters)
#     total_phrase = len(phrase)
#     if total_characters >= total_phrase:
#         characterss = [i for i in characters]
#         for character in phrase:
#             if character not in characterss:
#                 word.append(character)
#     else:
#         return False
#
#     print(word)
#     print(characterss)







    # for x in word:
    #     if x in phrases:
    #         print(True)
    #     elif x not in phrases:
    #         print(False)

    # if len(phrase) == len(letters):
    #     for i in letters:
    #         if i in phrases:
    #             letters.remove(i)
    #             phrases.remove(i)
    #             print(phrases)
    #             print(letters)
    # else:
    #     return False





# generate_phrase(characters, phrase)



def generate_phrase(characters, phrase):
    list_ph = list(phrase)
    list_char = list(characters)
    if len(list_char) >= len(list_ph):
        [list_ph.remove(char) for char in list_char if char in list_ph]
        return len(list_ph) == 0
    else:
        return False

print(generate_phrase("cbacba", "aabbccc"))
print(generate_phrase("browws", "browws"))
print(generate_phrase("crows", "brows"))
