input = "abadabace"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - ord('a')] += 1
    not_repeating_character_array = []
    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(i + ord('a')))
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"


result = find_not_repeating_character(input)
print(result)