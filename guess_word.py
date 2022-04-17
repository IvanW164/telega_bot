
def word_competion(letter, word_user, hid_word):
    res_str = ""
    for i in range(len(hid_word)):
        if hid_word[i] == letter:
            res_str = res_str + letter
        else:
            res_str = res_str + word_user[i]
    return res_str

def alphabet_method():
    res_alpha = ""
    for i in range(97, 123):
        res_alpha += chr(i)
    return res_alpha