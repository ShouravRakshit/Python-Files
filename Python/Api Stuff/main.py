# from googletrans import Translator
#
# f = open("test1.txt", "r")
# text = (f.readlines())
# new_text = ""
# for letters in text:
#     new_text = new_text + letters
#
# translator = Translator()
# print(translator.translate(new_text, dest='ja'))
# print("This is a comment")
#
# f.close()

def do_stuff(num):
    try:
        return 5 / int(num)
    except ValueError as err:
        return err
    except ZeroDivisionError as err:
        return err

