# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:27:20 2016

@author: Taoran Huo
Group C Homework 2
"""
#Overall Comment: Very good exercise ! The logic goes well and efficient, your comments shows your own understanding of the
#corresponding code. Happy to see your growth !
def is_palindrome(file):
    '''
    1. Write a version of a palindrome recogniser that accepts a file
    name from the user, reads each line, and prints the line to the
    screen if it is a palindrome.
    '''
string=open(file).read()#open a file and read each line
string=string.lower()#make each letter to be lower case
puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
for l in string:
    if l in puncspace:
        string=string.replace(l,'') #remove the punctuation and space
new='' #creat an empty string
for i in range(len(string)):
    new+=string[-i-1] #backward string
if new==string: #use if loop, if the backward string equals to itself
    return True #return true
else:
    return False #else, return false
                
is_palindrome('names.txt')#test the function with a local file


def semord(file):
    '''
    2. According to Wikipedia, a semordnilap is a word or phrase that
    spells a different word or phrase backwards. ("Semordnilap" is
    itself "palindromes" spelled backwards.) Write a semordnilap
    recogniser that accepts a file name (pointing to a list of words)
    from the user and finds and prints all pairs of words that are
    semordnilaps to the screen.
    '''
list1=list(open(file).read().split()) #open a text file and convert it into a list
new=[] #creat an empty list
for i in list1: #for each index in list1
    if i[::-1] in list1 and len(i)>1: #ise if loop, if the length of word is not 1 and the backward word in the list
            new.append(i+' '+i[::-1]) #make each word to be word+space+backward
return new
    
semord('names.txt') #test the function with a local file


def char_freq_table(file):
    '''
    3. Write a procedure char_freq_table()that, when run in a terminal,
    accepts a file name from the user, builds a frequency listing of
    the characters contained in the file, and prints a sorted and
    nicely formatted character frequency table to the screen.
    '''
string=open(file).read()#open a file and read each line
dic={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
    'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,
    'w':0,'x':0,'y':0,'z':0}#formated table
string=string.lower()#lower case of each letter
puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
for k in string:
    if k in puncspace:
        string=string.replace(k,'')#no spaces and punctuations in string
for i in string:
    dic[i]+=1#check frequency
return dic
    
char_freq_table('names.txt') #test the function with a local file


d={'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
'y':'yankee', 'z':'zulu'} #define dictionary d
import os
import time
def speak_ICAO(string,ICAOpause,wordpause):
    '''
    4. Your task in this exercise is to write aprocedure speak_ICAO()able 
    to translate any text (i.e. any string)
    into spoken ICAO words. You need to import at least two libraries:
    osand time. On a mac, you have access to the system TTS
    (Text-To-Speech) as follows:os.system('say'+msg), wheremsgis the
    string to be spoken. (Under UNIX/Linux and Windows, something
    similar might exist.) Apart from the text to be spoken, your
    procedure also needs to accept two additional parameters: a float
    indicating the length of the pause between each spoken ICAO
    word, and a float indicating the length of the pause between each
    word spoken.
    '''
for k in string.split(): #use for loop, split a string into characters
    for i in k: #use for loop, i represents each character
        if i not in "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?": #use if loop, the character is not punctuation
            os.system('say'+d[i.lower()]) #speak
            time.sleep(ICAOpause) #pasue between ICAO words
time.sleep(wordpause) #pause between words

print(speak_ICAO('Do you want to go swimming',1,3))


def hapax(file):
    '''
    5. A hapax legomenon (often abbreviated to hapax) is a word which
    occurs only once in either the written record of a language, the
    works of an author, or in a single text. Define a function that given
    the file name of a text will return all its hapaxes. Make sure your
    program ignores capitalization.
    '''
string=open(file).read()#open a file and read each line of the file
string=string.lower()#make each character to be lower case
puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
for k in string: #use for loop
    if k in puncspace: #use if loop
        string=string.replace(k,'')#remove the punctuation and space
hapaxes=[]#create an empty list
for i in string.split():#use for loop
    if string.count(i)==1:#if the word shows up only once
        hapaxes.append(i)#put it into the created list
return hapaxes

hapax('names.txt') #test the function with a local file    
    
    
def numberfile(file):
    '''
    6. Write a program that given a text file will create a new text file in
    which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file).
    '''
file1=open(file).readlines()#open a file to read
file2=open('new'+file,'w')#open a new empty file
for i in range(len(file1)):
    file2.write('line'+str(i+1)+': '+file1[i])#add 'line' to the begining of each line, put them together into line2
file2.close()#save the file2 and close

numberfile('names.txt')#test the function with a local text file


def ave(file):
    '''
    7. Write a program that will calculate the average word length of a text
    stored in a file (i.e the sum of all the lengths of the word tokens in
    the text, divided by the number of word tokens).
    '''
string=open(file).read()#open and read file
puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
string=string.replace('\n',' ')# no'\n' in string
wordnumber=len(string.split())#caculate the number of words
for k in string:
    if k in puncspace:
        string=string.replace(k,'')#no spaces and punctuations in string
charnumber=len(string)#caculate the number of characters
return charnumber/wordnumber

ave('names.txt')#'test the function with a local text file


name=input('What is your name? ')#input a name
    '''
    8. Write a program able to play the "Guess the number"-game, where
    the number to be guessed is randomly chosen between 1 and 20.
    (Source: http://inventwithpython.com) This is how it should work
    when run in a terminal:
    '''
chance=1
while True:
    number=int(input(name+', I am thinking of a number between 1 and 20. Take a guess. '))#input a number
    if number==18: #use if loop, if the number of the name is 18
        print('Good job, {}! You guessed my number in {} guesses!'.format(name,chance))
        break #stop the program when guess the number
    elif number<18:
        print('Your guess is too low. Take a guess.')
        chance+=1 #times calculated one more time
    else:
        print('Your guess is too high. Take a guess.')
        chance+=1 #times calculated one more time


answer='finger'#correct answer
    '''
    10. In a game of Lingo, there is a hidden word, five characters long.
    The object of the game is to find this word by guessing, and in
    return receive two kinds of clues: 1) the characters that are fully
    correct, with respect to identity as well as to position, and 2) the
    characters that are indeed present in the word, but which are
    placed in the wrong position. Write a program with which one can
    play Lingo. Use square brackets to mark characters correct in the
    sense of 1), and ordinary parentheses to mark characters correct in
    the sense of 2).
    '''
while True:
    new=''
    guess=input('')#guess a word
    for i in range(len(guess)):
        if guess[i]==answer[i]:#if identity the character and the position are both correct
            new+='['+guess[i]+']'#add '[]' to the character
        elif guess[i] in answer:#if only identity is correct
            new+='('+guess[i]+')'#add '()' to the character
        else:
            new+=guess[i]#if neither is correct, just add character
    if guess==answer:
        print('Clue: '+new)
        break #stop the program
    else:
        print('Clue: '+new)
        
        
punc='?!'
lower='abcdefghijklmnopqrstuvwxyz'
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
title=['Mr','Mrs','Dr']
punctuation="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
def splitter(file):
    '''
    11. A sentence splitter is a program capable of splitting a text into
    sentences. The standard set of heuristics for sentence splitting
    includes (but isn't limited to) the following rules:
    Sentence boundaries occur at one of "." (periods), "?" or "!", except
    that
    a. Periods followed by whitespace followed by a lower case letter
    are not sentence boundaries.
    b. Periods followed by a digit with no intervening whitespace are
    not sentence boundaries.
    c. Periods followed by whitespace and then an upper case letter,
    but preceded by any of a short list of titles are not sentence
    boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    d. Periods internal to a sequence of letters with no adjacent
    whitespace are not sentence boundaries (for example,
    www.aptex.com, or e.g).
    e. Periods followed by certain kinds of punctuation (notably comma
    and more periods) are probably not sentence boundaries.
    Your task here is to write a program that given the name of a text
    file is able to write its content with each sentence on a separate
    line. Test your program with the following short text: Mr. Smith
    bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
    Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't
    true... Well, with a probability of .9 it isn't. The result should be:
    Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e.
    he paid a lot for it. Did he mind? Adam Jones Jr. thinks he
    didn't. In any case, this isn't true...
    Well, with a probability of .9 it isn't.
    '''
string=open(file,'r').read()#open a file to read
for i in range(1,len(string)-2):
    if string[i]=='.':#period
        if string[i+1]==' 'and string[i+2] in lower:
            string=string #Periods followed by a space with a lower case letter are not sentence boundaries.
        elif string[i+1] in num:
            string=string #Periods followed by a digit with no intervening space are not sentence boundaries.
        elif (string[i-2:i] or string[i-3:i]) in title and string[i+1]==' ' and string[i+2] in cap:
            string=string #Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries
        elif string[i-1]!=' ' and string[i+1]!=' ':
            string=string #Periods internal to a sequence of letters with no adjacent space are not sentence boundaries 
        elif string[i+1] in punctuation:
            string=string #Periods followed by certain kinds of punctuation
        else:
            string=string[:i+1]+'\n'+string[i+2:] #else, add '\n' after period (new line)
    elif string[i] in punc:
            string=string[:i+1]+'\n'+string[i+2:]#for sentences end with '?' and '!', seperate new line
file1=open(file,'w')#open for write
file1.write(string)#write a string into it
file1.close()#save and close the file

splitter('names.txt') #test the function with a local file
