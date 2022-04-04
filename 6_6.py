#write function that recieves a list of words then determine and print duplicate in sentance

def removeDuplicate(sentence):
    y = set({})
    for z in sentence:
        y.add(z.lower())
    for z in sorted(y, reverse=False):
        print(z)
sentence = ["ABCD", "CRAYON", "xylophone", "tetris", "tetris"]
    


removeDuplicate(sentence)


