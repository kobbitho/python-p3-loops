#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass

def happy_new_year():
    counter = 10
    while counter > 0:
        print (counter)
        counter = counter - 1
        #happy_new_year()       
        print('Happy New Year!')


def square_integers(int_list):
    # code goes here!
    pass
def square_integers(int_list):
    return [x**2 for x in int_list]


def fizzbuzz():
    # code goes here!
    pass

def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


