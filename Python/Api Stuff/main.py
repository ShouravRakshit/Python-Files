from googletrans import Translator

f = open("test1.txt", "r")
text = (f.readlines())
new_text = ""
for letters in text:
    new_text = new_text + letters

translator = Translator()
print(translator.translate(new_text, dest='ja'))
print("This is a comment")

f.close()
