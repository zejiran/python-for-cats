# --------------------------------------------
print("Learn Python to be great!")
# --------------------------------------------
print('We learn Python!')
# --------------------------------------------
print("Alice's Adventures in Wonderland")
# --------------------------------------------
print("2 + 2 = 4")
# --------------------------------------------
result = ["O X X", "O X O", "X O X"]
print(*result, sep="\n")
# --------------------------------------------
print("first\nsecond\nthird")
# --------------------------------------------
print("* * * *")
print("*     *\n" * 2 + "* * * *")
# --------------------------------------------
# prints "ok" without quotes
print('ok')
# --------------------------------------------
# print(1 + 2 + 3 + 6)
print(1 + 3 + 3)
# print(1 + 2 + 3)
# --------------------------------------------
print(10)
# --------------------------------------------
for i in range(1, 11):
    print(i, end=' ')
# --------------------------------------------
print(type('int'))
print(type(394))
print(type(2.71))
# --------------------------------------------
print("""'
'"'
'"'"'
'"'"'"'""")
# --------------------------------------------
print('"""\nTHIS IS A STRING\n"""')
# --------------------------------------------
print("""Did that stop the old Grinch?
No! The Grinch simply said,
"If I can't find a reindeer,
I'll make one instead!\"""")
# --------------------------------------------
number = 1 * 1 * 10 ** 1
# --------------------------------------------
holiday = 'Cinnamon Roll Day'
# --------------------------------------------
print(1234567890 * 987654321 + 67890)
# --------------------------------------------
a = int(input())
b = int(input())
c = int(input())
r = a * b - c
print(r)
# --------------------------------------------
n = int(input())
r = n
r += n
r *= n
r -= n
r //= n
print(r)
# --------------------------------------------
word = input()
print(word * 2)
# --------------------------------------------
n = 12345
print(str(n) * 100)
# --------------------------------------------
http_response = 'mocked response'
http_error = 404
# --------------------------------------------
str_ = "Hello"
str_ = str_ + str(10)
# --------------------------------------------
str_ = "Hello"
str_ = str_ + str(10)
# --------------------------------------------
favfl = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip', 'Alice': 'orchid'}
print(favfl)
# --------------------------------------------
name = ['Helen']
print(name)
# --------------------------------------------
list_ = list(input())
print(list_)
# --------------------------------------------
jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
ages = [jack_age, alex_age, lana_age]
print(min(ages))
# --------------------------------------------
x = int(input())
y = int(input())
print(min(x, y))
# --------------------------------------------
word1 = input()
word2 = input()
words = [word1, word2]
len_words = list(map(len, words))
print(max(len_words))
# --------------------------------------------
def get_sum(a, b):
    return a + b
# --------------------------------------------
def closest_mod_5(x):
    mod = x % 5
    if mod == 0:
        return x
    return x + (5 - x % 5)
# --------------------------------------------
def captain_adder(name):
    print('captain', name)
# --------------------------------------------
user_city = "Istanbul"

def change_city(new_user_city):
    global user_city
    user_city = new_user_city

change_city("Paris")
print(user_city)
# --------------------------------------------
x, y, z = [int(x) for x in [input(), input(), input()]]
print(x + y + z)
# --------------------------------------------
a, b = [int(input()) for i in range(2)]
print(a - b)
# --------------------------------------------
n = int(input())
word = input()
print(n * word)
# --------------------------------------------
n, k = (int(input()) for i in range(2))
k //= n
print(k)
# --------------------------------------------
n = list(input())
for i in enumerate(n):
    n[i[0]] = int(i[1])
print(sum(n))
# --------------------------------------------
n = [int(input()) for i in range(3)]
print(sum((i // 2 + i % 2) for i in n))
# --------------------------------------------
a = int(input().strip())
print(a > 0)
# --------------------------------------------
n, k, v = (int(input()) for i in range(3))
tk = n * k
print(v <= tk)
# --------------------------------------------
A, B = (int(input()) for i in range(2))
odd = A / B
odd = not odd % 2 == 0
print(odd)
# --------------------------------------------
word = input()
n = len(word)
print(f'{word} has {n} letters')
# --------------------------------------------
income = int(input())
if 0 <= income <= 15527:
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
else:
    percent = 28
calculated_tax = income * percent / 100
print(f'The tax for {income} is {percent}%. That is {round(calculated_tax)} dollars!')
# --------------------------------------------
word = input()
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
if word in dictionary:
    print("Correct")
else:
    print("Incorrect")
# --------------------------------------------
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
# --------------------------------------------
i = float(input())
if i < 2:
    print('Analytic')
elif i <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
# --------------------------------------------
a, b, h = (int(input()) for i in range(3))
if h < a:
    print("Deficiency")
elif h > b:
    print("Excess")
else:
    print("Normal")
# --------------------------------------------
spin, charge = (input() for i in range(2))
class_ = 'Quark'
if spin == '1':
    particle = 'Photon'
    class_ = 'Boson'
elif charge == '0':
    particle = 'Muon'
    class_ = 'Lepton'
elif charge == '-1':
    particle = 'Electron'
    class_ = 'Lepton'
elif charge == '2/3':
    particle = 'Charm'
elif charge == '-1/3':
    particle = 'Strange'
print(f'{particle} {class_}')
# --------------------------------------------
k = int(input())
print((k * (k + 1)) // 2)
# --------------------------------------------
n = int(input())
i = 2
while i < n:
    print(i)
    i += 2
# --------------------------------------------
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for letter in string:
    if letter in vowels:
        count += 1
# --------------------------------------------
count = int(input())
sum_ = 0
for _ in range(count):
    sum_ += int(input())
print(sum_ / count)
# --------------------------------------------
word = input()
for char in word:
    if char.isupper():
        word = word.replace(char, '_' + char.lower())
print(word)
# --------------------------------------------
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
sequence = input()
for char in sequence:
    if char in vowels:
        print('vowel')
    elif char in consonants:
        print('consonant')
    else:
        break
# --------------------------------------------
supremus_cat_cafe = ['', 0]
while True:
    cafe = input().split()
    if cafe[0] == 'MEOW':
        break
    if int(cafe[1]) >= supremus_cat_cafe[1]:
        supremus_cat_cafe[1] = int(cafe[1])
        supremus_cat_cafe[0] = cafe[0]
print(supremus_cat_cafe[0])
# --------------------------------------------
from math import factorial
x = int(input())
print(factorial(x))
# --------------------------------------------
import string
print(string.digits + '\n' + string.ascii_lowercase)
# --------------------------------------------
from random import seed, randint
n = int(input())
seed(a=n, version=2)
print(randint(-100, 100))
# --------------------------------------------
import random

random.seed(int(input()))
print(random.choice('Voldemort'))
# --------------------------------------------
import random

random.seed(3)
print(random.betavariate(0.9, 0.1))
# --------------------------------------------
import random

sentence = input().split()
random.seed(43)
random.shuffle(sentence)
print(' '.join(sentence))
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
