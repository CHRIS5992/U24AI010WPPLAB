word=input("Enter Your Word To Capitalize: ")
capitalized = ""



for i in range(len(word)):
    if i%2==0:
        capitalized = capitalized+word[i].upper()
    else:
        capitalized = capitalized+word[i].lower()
    





print(f"Original = {word} and Capitalized = {capitalized}")