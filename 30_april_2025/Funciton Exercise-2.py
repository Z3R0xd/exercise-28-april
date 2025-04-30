def sentenceGenerator(words):
    sentence = 0
    for word in words:
        if sentence == 0 :
            sentence = word
        else :
            sentence = sentence + " " + word
    return sentence

words = ["When", "I", "was", "a", "young", "boy"]

print(sentenceGenerator(words))