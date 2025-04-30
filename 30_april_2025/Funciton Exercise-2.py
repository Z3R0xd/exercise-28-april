def sentenceGenerator(*args):
    sentence = ""
    for word in args:
        sentence += word
        sentence += " "
    return sentence

print(sentenceGenerator("When", "I", "was", "a", "young", "boy"))
print(sentenceGenerator("My", "Father", "took", "me", "into", "the", "city"))
print(sentenceGenerator("To", "see", "a", "marching", "band"))