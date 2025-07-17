words = {
    "madad": "help",
    "kursi": "chair",
    "pustak": "book"
}

search = input("enter the word you want meaning of").strip().lower()


if search in words:
    print("the meaning of the word is ", words[search])
else:
    print("word doesn't exist")
