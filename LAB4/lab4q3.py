def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
   
    if alphabet.issubset(set(s.lower())):
        print("pangram")
    else:
        print("not pangram")


sentence = input()
is_pangram(sentence)
