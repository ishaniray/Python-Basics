"""
Rövarspråket (English: The Robber Language) is a Swedish language game.
Every consonant is doubled, and an 'o' is inserted in-between. Vowels are left intact.
For example, 'stubborn' in Rövarspråket would be expressed as 'sostotubobboborornon'.
"""

# Function to check if the character passed is a vowel
def isVowel(c):
    c = c.lower()
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        return True
    else:
        return False
# end of isVowel

# Function to check if the character passed is a punctuation mark
def isPunctuation(c):
    if(c == ' ' or c == ',' or c == ';' or c == '.' or c == '!' or c == '-' or c == '"' or c == '\'' or c == ':' or c == '(' or c == ')'):
        return True
    else:
        return False
# end of isPunctuation

choice = int(input("ROVARSPRAKET\n------------\n\n1. Encode\n2. Decode\n\nEnter your choice (1 or 2): "))

if choice == 1:
    string = input("\nEnter a string: ")

    rs_list = []    # list to hold output

    for letter in string:
        if isVowel(letter) or isPunctuation(letter):
            rs_list.append(letter)
        else:
            rs_list.append(letter)
            rs_list.append('o')
            rs_list.append(letter)

    rs_string = ''.join(rs_list)    # converting list to string

    if string.isupper():
        rs_string = rs_string.upper()

    print("\n" + string + " in Rövarspråket: " + rs_string)

else:
    rs_string = input("\nEnter a Rövarspråket string: ")

    str_list = [] # list to hold output

    i = 0
    while i < len(rs_string):
        str_list.append(rs_string[i])
        if isVowel(rs_string[i]) or isPunctuation(rs_string[i]):
            i = i + 1
        else:
            i = i + 3   # if a consonant is encountered, skip the next two letters

    string = ''.join(str_list)  # converting list to string

    if rs_string.isupper():
        string = string.upper()

    print("\nThe decoded string is: " + string)

# end of program