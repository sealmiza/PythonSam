age = input('how old are you: ' )
age=int(age)
if age>= 18:
    print('you are old enough to vote')

name=input('what is your name?')
name=str(name)
if name=='samuel':
    print('welcome back', name)
else:
    print('wrong user please try again')
def my_function():
    print('hello from my function')

my_function()
def my_function(fname):
    print(fname + 'hello')

my_function('samuel')
my_function('esther')
my_function('jeddie')
my_function('moraa')
def my_function(ages,area):
    print(ages , area ,'how do you think your skills will be helpful to us')

my_function( 19 , 254)
my_function(20 ,354)
def my_function(country='norway'):
    print('i come from' + country)

my_function('kenya')
my_function('zimbabwe')
my_function()
def my_function(x):
    return 5*x
print(my_function(2))
print(my_function(3))
print(my_function(4))
def my_function(food):
    for x in food:
        print(x)
fruits=['kiwi','grapes','watermelon']
fruits.append('mangoes')

my_function(fruits)
x= lambda a: a*5
print(x(3))
x= lambda a ,b :a+b
print(x(2,3))
print(x(4,5))
def my_function(n):
    return lambda a: a*n

mydoubler=my_function(2)
mytrippler=my_function(3)

print(mydoubler(5))
print(mytrippler(2))

compliment=input('do you like your classes:yes|no')
compliment=str(compliment)
if compliment=='yes':
    print('great, youre invited to our next lecture')
else:
    print('what seems to be the problem')

def display_messsage(name):
    print('hello', name ,' we are learning about functions and how to apply them')

display_messsage('sammy')
display_messsage(' clinton')

def fav_book(book):
    '''write how you feel about your fav book'''
    print('one of my fav books is' ,book)

fav_book('alice in wonderland')
fav_book('desire of ages')
def make_shirt(size,text):
    print(size ,text , " is the description of shirts i like")

make_shirt(31,"champion")
make_shirt(23, "amiri")
def describe_city(name ,country):
    print(name,country , " is the location of the club")

describe_city("nairobi" ,"kenya" )
describe_city("kigali" ,"rwanda" )


