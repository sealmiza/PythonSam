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
    print(fname+'hello')

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


