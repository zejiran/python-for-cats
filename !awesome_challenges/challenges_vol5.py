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
class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


little_angel = Angel()
little_demon = Demon()
little_kids = (little_angel, little_demon)
for kid in little_kids:
    print(f'{kid.color}\n{kid.feature}\n{kid.home}')


# --------------------------------------------
class Human:
    species = 'Homo Sapiens'
    n_legs = 2
    n_arms = 2


# --------------------------------------------
class RockBand:
    genre, n_members, key_instruments = 'rock', 4, ['electric guitar', 'drums']


tampikos = RockBand()
print(f'{tampikos.genre}\n{tampikos.n_members}\n{tampikos.key_instruments}')


# --------------------------------------------
class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


shop = Store("GAP", "clothes")
print(shop.name, shop.category)


# --------------------------------------------
class Movie:
    def __init__(self, title, director, year):
        self.title, self.director, self.year = title, director, year


titanic, star_wars, fight_club = (Movie('Titanic', 'James Cameron', '1997'),
                                  Movie('Star Wars', 'George Lucas', '1977'),
                                  Movie('Fight Club', 'David Fincher', '1999'))


# --------------------------------------------
class Student:
    def __init__(self, name, last_name, birth_year):
        self.name, self.last_name, self.birth_year = name, last_name, birth_year
        self.id = f'{name[0]}{last_name}{birth_year}'


n, ln, by = (input() for i in range(3))
student = Student(n, ln, by)
print(student.id)


# --------------------------------------------
class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / 0.3048


# --------------------------------------------


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return round((3 * math.sqrt(3) * self.side_length ** 2) / 2, 3)


# --------------------------------------------


class Point:
    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy

    def dist(self, another_instance):
        return math.sqrt((self.xx - another_instance.xx) ** 2 + (self.yy - another_instance.yy) ** 2)


# --------------------------------------------
class House:
    def __init__(self, floors):
        self.floors = floors
        self.color = None

    def paint(self, color):
        self.color = color


# --------------------------------------------
class Stack():

    def __init__(self):
        self.my_stack = []

    def push(self, el):
        self.my_stack.append(el)

    def pop(self):
        delete = self.peek()
        self.my_stack.remove(delete)
        return delete

    def peek(self):
        return self.my_stack[-1]

    def is_empty(self):
        return bool(not self.my_stack)


# --------------------------------------------
class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        while self.cents > 99:
            self.cents -= 100
            self.dollars += 1


piggy1 = PiggyBank(2, 2)


def create_piggy(dollars, cents):
    return {'dollars': dollars, 'cents': cents}


piggy2 = create_piggy(2, 2)
# --------------------------------------------
print(' \n'.join('You are the best programmer!'.split()))
# --------------------------------------------
print(len('That is \n mine'))
# --------------------------------------------
print('\\\\')
# --------------------------------------------
print(str(45 / 9 + 16 * (5 + 8)))
print('mathematics')
# --------------------------------------------
print("""
I am = I'm
I have = I've
I will = I'll
I had / would = I'd
""")
# --------------------------------------------
print("What would I watch tonight?")
fave_tv_show = 'Re:ゼロ'
my_answer = fave_tv_show
# --------------------------------------------
age = 20
if age < 18:
    print("You can't watch Game of Thrones!")
else:
    print("You are welcome to be here. Sit, have a drink and enjoy the show!")
# --------------------------------------------
print(input().upper())
# --------------------------------------------
print(input().strip(',.!?').lower())
# --------------------------------------------
marks = ',.!?'
preprocess = ''.join(list(filter(lambda x: x not in marks, input())))
print(preprocess.lower())


# --------------------------------------------
def create_full_name(name, last_name):
    return f'{name} {last_name}'


name1, last_name1 = "John", "Lennon"
full_name1 = create_full_name(name1, last_name1)

name2, last_name2 = "Hermione", "Granger"
full_name2 = create_full_name(name2, last_name2)

name3, last_name3 = "Lady", "Gaga"
full_name3 = create_full_name(name3, last_name3)


# --------------------------------------------
def f1(x):
    return x ** 2 + 1


def f2(x):
    return 1 / x ** 2


def f3(x):
    return x ** 2 - 1


def f(x):
    if x <= 0:
        return f1(x)
    if 0 < x < 1:
        return f2(x)
    return f3(x)


# --------------------------------------------
def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature = float(temperature)
    if unit == 'F':
        print(f'{fahrenheit_to_celsius(temperature)} C')
    else:
        print(f'{celsius_to_fahrenheit(temperature)} F')


# --------------------------------------------
hand = [input() for i in range(6)]
face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
rank = 0
for card in hand:
    if card not in face_cards:
        rank += int(card)
    else:
        rank += face_cards[card]
rank /= 6
print(rank)
# --------------------------------------------
words = input().lower().split()
word_amount = dict()
for word in words:
    if word not in word_amount:
        word_amount[word] = 1
    else:
        word_amount[word] += 1
for word, count in word_amount.items():
    print(f'{word} {count}')
# --------------------------------------------
f, s = (float(input()) for i in range(2))
print('{}'.format(f + s))
# --------------------------------------------
x, y = input().split()
print(f'{x} of {y}')
# --------------------------------------------
random_numbers = [1, 22, 333, 4444, 55555]
for index, random in enumerate(random_numbers):
    random_numbers[index] = str(random)
print("\n".join(random_numbers))
# --------------------------------------------
random_numbers = [1, 22, 333, 4444, 55555]
print("\n".join(map(str, random_numbers)))
# --------------------------------------------
print(''.join([word.title() for word in input().lower().split('_')]))
# --------------------------------------------
# safe_main_module.py

name = "Juan"


def main():
    print("Hello,", name)


if __name__ == "__main__":
    main()
# --------------------------------------------
import datetime

birthday = datetime.datetime(2002, 5, 27)
# --------------------------------------------
some_date = datetime.datetime(3486, 5, 15, 23, 59)
print(some_date.time())
# --------------------------------------------
import datetime

now_time = datetime.datetime.now()
# --------------------------------------------
import math


def my_sqrt(value):
    if isinstance(value, str):
        return "The string should be converted into a numeric data type"
    if not isinstance(value, (int, float)):
        return None
    return math.sqrt(value)


# --------------------------------------------
file = open('test_file.txt', 'r', encoding='utf-16')
print(file.readline())
file.close()
# --------------------------------------------
# First letter from each line.
file = open('test.txt', 'r')
for line in file:
    print(line[0])
file.close()
# --------------------------------------------
file = open('sums.txt', 'r')
for line in file:
    numbers = line.strip('\n').split()
    for i, number in enumerate(numbers):
        numbers[i] = int(number)
    print(sum(numbers))
file.close()
# --------------------------------------------
file = open('sums.txt', 'r')
for line in file:
    print(sum(int(x) for x in line.split()))
file.close()
# --------------------------------------------
file = open('input.txt', 'w', encoding='utf-8')
file.write(input())
file.close()
# --------------------------------------------
with open('input.txt', 'w') as f:
    f.write(input())
# --------------------------------------------
with open('planets.txt', 'w', encoding='utf-8') as file:
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    for planet in planets:
        file.write(planet + '\n')
# --------------------------------------------
with open('animals.txt') as file:
    animals = file.readlines()
    animals = [animal.replace('\n', '') for animal in animals]
new_file = open('animals_new.txt', 'w')
new_file.write(' '.join(animals))
new_file.close()
# --------------------------------------------
with open('test.txt', 'w') as f:
    f.write('Tada!')
# --------------------------------------------
with open('name.txt') as f1, open('surname.txt') as f2, open('full_name.txt', 'w') as f3:
    name = f1.read()
    surname = f2.read()
    full_name = name + ' ' + surname
    f3.write(full_name)
# --------------------------------------------
for i in range(1, 11):
    with open(f'file{i}.txt', 'w') as file:
        file.write(str(i))
# --------------------------------------------
import json

colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}
json_colors = json.dumps(colors, indent=4)
with open('colors.json', 'w') as json_file:
    json_file.write(json_colors)
# --------------------------------------------
import json

colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}
with open("colors.json", "w") as file:
    json.dump(colors, file)
# --------------------------------------------
import json

json_string = input()
json_dict = json.loads(json_string)
print(f'{type(json_dict)}\n{json_dict}')
# --------------------------------------------
with open('users.json', 'r') as json_file:
    dict_from_json = json.load(json_file)
users_defined = len(dict_from_json['users'])
print(users_defined)
# --------------------------------------------
template = """
<html>
  <h2>{{ blog_name }}</h2>
</html>
"""
# --------------------------------------------
template = """
<html>
  <ul>
  {% for todo in todos %}
    <li>{{ todo }}</li>
  {% endfor %}
  </ul>
</html>
"""
# --------------------------------------------
template = """
<html>
  <div>{% if post.author != None %} {{ post.text }} 
       {% else %} No author
       {% endif %}
  </div>
</html>
"""
# --------------------------------------------
add_book(title='SAO')


# --------------------------------------------
def get_bonus(salary, percentage=35):
    return int(salary * percentage / 100)


# --------------------------------------------
def get_percentage(real, round_digits=None):
    percentage = real * 100
    return f'{round(percentage, round_digits)}%'


# --------------------------------------------

shopping_list = []

shopping_list.append("milk")
shopping_list.append("olive oil")
shopping_list.append("bananas")
shopping_list.remove("milk")
shopping_list.append("brownie")
# --------------------------------------------
shopping_list = []

shopping_list.append('milk')
shopping_list.append('olive oil')
shopping_list.append('bananas')
shopping_list[0] = 'brownie'
# --------------------------------------------
n = int(input())
list_ = [int(input()) for _i in range(n)]
print(list_)
# --------------------------------------------
from django.shortcuts import redirect, Http404
from django.views import View


class TodoView(View):
    all_todos = []

    def delete(self, request, to_do, *args, **kwargs):
        if to_do not in self.all_todos:
            raise Http404
        self.all_todos.remove(to_do)
        return redirect('/')


# --------------------------------------------
from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        to_do = request.POST.get('todo')
        if to_do not in self.all_todos:
            self.all_todos.append(to_do)
        return redirect('/')


# --------------------------------------------
from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        to_do = request.POST.get('todo')
        is_important = request.POST.get('important')
        if to_do not in self.all_todos:
            self.all_todos.insert(0, to_do) if is_important else self.all_todos.append(to_do)
        return redirect('/')


# --------------------------------------------
from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        to_do = request.POST.get('todo')
        is_important = request.POST.get('important')
        if to_do not in self.all_todos:
            if is_important:
                self.all_todos.insert(0, to_do)
            else:
                self.all_todos.append(to_do)
        return redirect('/')
# --------------------------------------------
prices = input().split()
print(prices[3 - 1])
# --------------------------------------------
numbers = [4, 1, 0, 3, 2, 5]
for i, _ in enumerate(numbers):
    numbers[i] = i
print(numbers)
# --------------------------------------------
numbers = tuple(int(n) for n in input().split())
print(numbers[-1])
# --------------------------------------------
oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
oceans = tuple(oceans)
# --------------------------------------------
singleton = ([0, 1, 1, 2, 3, 5, 8, 13, 21],)
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
