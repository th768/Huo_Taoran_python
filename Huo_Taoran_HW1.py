# -*- coding: utf-8 -*-
"""
Spyder Editor

Group F Homework1
@author: Taoran Huo
"""

def max1(a, b):
    '''
1. Define a function max()that takes two numbers as arguments and
returns the largest of them. Use the if-then-else construct available in
Python.
    '''
    if a>b: #use if loop
        print(a, 'is largest') #When comparing two numbers, there are three situations. Firstly, wether a>b
    elif a==b:
        print(a, 'is largest') #Secondly, wether a=b
    else:
        print(b, 'is largest') #Thirdly, wehter a<b
max1(6,7)    

  
def max_of_three(a, b, c):
    '''
2. Define a function max_of_three()that takes three numbers as
arguments and returns the largest of them.
    '''
    if a>=b: #Firstly, test a>b by using if loop
       t=a   #create a t, let t be a, which a is the larger one
    elif b>=a: # Secondly, test b>a
         t=b #let t be b, which b is the larger one 
    if t>=c: #compare t with c
        return t #output the larger one t
    else:  #compare t with c
        return c #output the larger one c
max_of_three(7, 6, 8)   
     
def length(a):
    '''
3. Define a function that computes the length of a given list or string.
    '''
    l=0 #create a initial length l, let l be 0
    for i in a: #use for loop, for the index in string
        l=l+1 #count the number of the string
    return l #output the final result
length('mathematical')
        
 
def vowel(a):
    '''
4. Write a function that takes a character (i.e. a string of length 1) and
returns Trueif it is a vowel, Falseotherwise.
    '''
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u': #Use if loop, to test wether a is one of the five vowels
        return True # a is one the five vowels, output true
    else:
        return False # a is not one the five vowels, output false
vowel('a')

cons="qwetzpsdfghjklyxcvbnm" #list all the non-vowel character
def translate(string):
    '''
5. Write a function translate()that will translate a text into
"rövarspråket" (Swedish for "robber's language"). That is, double
every consonant and place an occurrence of "o"in between.
    '''
    a='' #create a new string
    for i in string: #use for loop, for index in the original string
        if i in cons: 
            a+=i+'o'+i
        else:
            a+=i
    return a
translate("look at this book")
    
def sum(a):
    '''
6. Define a function sum()and a function multiply()that sums and
multiplies (respectively) all the numbers in a list of numbers.
    '''
    sum=0 #create an empty sum, started with 0
    for num in a: #use for loop, count each number in the list a
        sum=sum+num #summing up the numbers
    return sum #output the result
sum([1,5,7,9])

def mutiply(a):
    '''
6. Define a function sum()and a function multiply()that sums and
multiplies (respectively) all the numbers in a list of numbers.
    '''
    mul=1 # create a mutiply, started with 1
    for num in a: #use for loop, count each number in the list a
        mul=num*mul #mutiplying the numbers
    return mul #output the result
mutiply([1,5,7,9])

def reverse(string):
    '''
    7. Define a function reverse()that computes the reversal of a string.
    '''
    a='' #create an empty string
    l=len(string) #use l as the length of the string
    for i in range(l): #use for loop, for index in the range of the length, which are from 0 to len(string)
        a+=string[-i-1] #list the string start with the last character in the original string
    return a #output the result
reverse('beautiful')

def is_palindrome(word):
    '''
    8. Define a function is_palindrome()that recognizes palindromes (i.e.
words that look the same written backwards).
    '''
    a='' #create an empty string
    for i in range(len(word)): #use for loop, for index in the range of the length of the string
        a=a+word[-i-1] #reverse the string
    if word==a: #use if loop, test wether the original string is the same as the reversed string
        return True #if the same, output true
    else:
        return False #if no the same, output false
print(is_palindrome('example')) 

def is_member(x, a):
    '''
    9. Write a function is_member()that takes a value (i.e. a number, string,
etc) xand a list of values a, and returns True if xis a member of a,
Falseotherwise. (Note that this is exactly what the inoperator does,
but for the sake of the exercise you should pretend Python did not have this operator.)
   '''
    for i in range(0,len(a)): #use for loop, for the index in the range of the length of a
        if x==a[i]: #use if loop, test wether x equals to an element of a
            return True #if yes, output true
        else:
            continue #if no, continue testing
        return False #until tested every elements in a and x did not equal to any of them. Then output false
is_member((5),(1,2,3,4,5,6,7))

def overlapping(a,b):
    '''
    10. Define a function overlapping()that takes two lists and returns True if
they have at least one member in common, False otherwise. You
may use your is_member()function, or the inoperator, but for the sake
of the exercise, you should (also) write it using two nested for-loops.
   '''
    for i in range(0,len(a)) : #use for loop, for the index in the range of the length of a
        for j in range(0,len(b)): #use for loop, for the index in the range of the length of b
            if a[i]==b[j]: #use if loop, test wether the elements in a equal to the elements in b
                return True #if they have a element or elements in common, output true
            else:
                continue #keep testing until all the elements be done
    return False #if all the elements are not the same, output false
overlapping((1,2,3,4,5),(1,3,5,6,7))

def generate_n_chars(n,c):
    '''
    11. Define a function generate_n_chars()that takes an integer nand a
character cand returns a string, ncharacters long, consisting only of
c:s. For example, generate_n_chars(5,"x")should return the string
"xxxxx". (Python is unusual in that you can actually write an
expression 5 * "x"that will evaluate to "xxxxx". For the sake of the
exercise you
   '''
    a='' #create an empty string
    for i in range(0,n): #use for loop, for index in the range from 0 to n
        a+=c #a+=means that a remains itselt and will be added c
    return a #output the result
generate_n_chars(6,'e')

def histogram(list):
    '''
    12. Define a procedure histogram()that takes a list of integers and prints
a histogram to the screen.
    '''
    a='' #create an empty string
    for i in list: #use for loop, for index in the list
        a=a+i*'*'+' ' #a is a add index times '*' and add a blank
    return a #output the result a
histogram([5,8,9])
    
def max_in_list(list):
    '''
    13. The function max()from exercise 1) and the function
max_of_three()from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number
of numbers, or suppose we cannot tell in advance how many they
are? Write a function max_in_list()that takes a list of numbers and
returns the largest one.
    '''
    a=list[0] #creat a be the first element of the list
    for i in range(len(list)): #use for loop, for the index in range of the length of list
        if a<=list[i]: #use if loop, testing which is larger
            a=list[i] #let a be the larger one
        else:
            continue #keep testing until all the elements have be tested
    return a #output the result
max_in_list([7,4,2,9])

def map_to_length(words):
    '''
    14. Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words.
    '''
    return list(map(len,words)) #use len function to measure the length of words in list and use map function to substitue length to orginal words
map_to_length(['word','map','sing'])

def find_longest_word(list1):
    '''
    15. Write a function find_longest_word()that takes a list of words and
returns the length of the longest one.
    '''
    return max(list(map(len,list1)))
print(find_longest_word(['i','enjoy','swimming'])) #list the length of each words in list and use max function to find the maximum number
  
def filter_long_words(n,list1):
    '''
    16. Write a function filter_long_words()that takes a list of words and an
integer n and returns the list of words that are longer than n.
    '''
    myList = [] #create a new empty list
    for i in range(len(list1)): #use for loop, for index in the range of the length of list1
        a=list1[i] #let a be the elements in list1
        if len(a)>=n: #use if loop, comparing each elements with n
            myList += [a] #if the element is larger than a, add it in the new list
    return myList #return the result
print(filter_long_words(7,['love','singers','beautiful','python']))
    

    