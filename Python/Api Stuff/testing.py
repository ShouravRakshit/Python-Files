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

# from random import randint
# import sys
#
# # generate a number 1~10
# answer = randint(1, 10)
#
# # input from user?
# # check that input is a number 1~10
# while True:
#     try:
#         guess = int(input('guess a number 1~10:  '))
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')

from PIL import Image, ImageFilter

im = Image.open("209 - pikachu.jpg")
filtered_img = im.filter(ImageFilter.BLUR)
print(im.format, im.size, im.mode)


