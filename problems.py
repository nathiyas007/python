# 1 with function
def split_sentence(sentence):
    s = sentence.split("-")  
    for sp in s:
        print(sp)

sentence = "Today-heavy-rain-in-chennai"
split_sentence(sentence)


# 2 without function



def without_fun(sentence):
    temp = ""
    for i in sentence:
        if i == "-":
            print(temp)
            temp = ""
        else :
            temp = temp + i
    print(temp)

without_fun("Emma-is-a-data-scientist")


# 2

def reverse_word(word):
    print(word[::-1])
reverse_word("python")

wihtout function 

def reverse_srt(word):
    reverse_word = ""
    i = len(word) -1
    while i >= 0:
        reverse_word = reverse_word + word[i]
        i = i - 1
    print(reverse_word)
reverse_srt("Pyhton")


# 3
def count_cons(word):
    count = 0
    for i in range(len(word)):
        if word[i] not in "aeiouAEIOU ":
            count = count + 1
    print(count)

count_cons("Hello World")


# 4
def remove_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text = new_text + char
    print(new_text)  

remove_space("Python is awesome")


# 5

def is_strong_password(password):
    special_characters = "!@#$%^&*"
    count = 0
    for i in password:
        if i in special_characters:
            count += 1
    if len(password) >= 8 and count >= 1:
        print("Password is strong")
    else:
        print("Password is not strong")
is_strong_password('nathiya')
is_strong_password('nathi@2007')