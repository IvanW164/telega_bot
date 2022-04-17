import random

def choise_hidden_word(number):
    list1 = ['cat','dog','pig']
    list2 = ['apple', 'banana', 'orange']
    list3 = ['spain', 'france', 'germany']
    if number == 1:
        some_word = random.choice(list1)
    elif number == 2:
        some_word = random.choice(list2)
    elif number == 3:
        some_word = random.choice(list3)
    return some_word

# def replace_word(some_word):
#     res_word = ""
#     for i in range(len(some_word)):
#         res_word = res_word + "*"
#     return res_word