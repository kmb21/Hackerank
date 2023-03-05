import string
def pangrams(s):
    # Write your code here
    letters = string.ascii_lowercase
    for letter in letters:
        if s.count(letter.upper())==0 and s.count(letter)==0:
            return "not pangram"
    return "pangram"
