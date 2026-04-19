'''
Varia Voloshin
COMP112 Section 05
11th May 2022
Final Project
'''

'''
This program visualises notes and chords in a kallidescope pattern and plays the notes while doing so
It employs turtles and playsound modules
First, it asks for a note input from user
Second, it plays and draws said note
After a sufficient amount of notes has been drawn, user can choose to add chords on top
They will be asked for a chord base
Once a sufficient amount has been added, the program will screenshot the turtles file
The user will be asked to name the file before the screenshot is saved

PLEASE BE AWARE THAT BOTH THE PLAYSOUND AND TKINTER MODULES NEED TO BE MANUALLY INSTALLED ON YOUR DEVICE TO RUN THIS CODE
'''

import playsound #imports playsound module
import random #imports random function
import turtle #imports turtle module
import os #imports the operating system of computer
from tkinter import * #imports tkinter module and the screenshot function 
ts = turtle.getscreen() #getting turtle screen
t = turtle.Pen()
t.speed(0) #sets turtle speed
turtle.bgcolor("white") #sets background colour to white
os.getcwd() #gets current working directory
def list_breaker(given_l):
    '''
    sig: list -> str
    makes a string out of a list
    '''
    liststr=''
    for element in given_l:
        liststr+=' '
        liststr+=element
    print(liststr)
allnotes=['C','D','E','F','G','A','B'] #list containing all notes user can enter as input
notesdict={"C":"crimson","Cs":"light sea green","D":"honeydew","Ds":"lime green","E":"hot pink","F":"slate blue","Fs":"light steel blue" ,"G":"gold","Gs":"orchid","A":"light green","As":"honeydew","B":"orange"} #dictionary connecting note to designated colour
arp_dict={'C':['C', 'E', 'G'],'Cs':['Cs','F','Gs'],'D':['D','Fs','A'],'Ds':['Ds','Gs','B'],'E':['E','G','B'],'F':['F','A','C'],'Fs':['Fs','As','Cs'],'G':['G','B','D'],'Gs':['Gs','B','Ds'],'A':['A','Cs','E'],'As':['As','D','F'],'B':['B','Ds','Fs']} #dictionary mapping note bases to their respective chords
welcome_str="Welcome to the note visualiser!"+'\n'+"This program takes a letter note input and draws a kallidescope pattern"+'\n'+"\n"+"Before drawing the pattern for a given note, the program will also play a recording of the note at hand"+'\n'+"Once you are satisfied with your single note pickings, responding N will take you to a different function which is able to add 3-note chords on top of your existing visual"+"\n"+"\n"+"After completing these steps, the program will take a screenshot of your kallediscope"+"\n"+"You will input your desired name for it, and it will be located in the same folder as the program:"+str(os.getcwd())+"\n"+"\n"+"For the sake of the program,the possible notes library consists of" 
print(welcome_str) #prints the welcome/instructional string written above
list_breaker(allnotes) #uses listbreaker function to print out all possible notes
clar="\n"+"Make sure to press enter after you type in any response"+"\n"+"\n"
print(clar)

def bye():
    '''
    sig: NoneType -> NoneType
    last function to go in the program
    takes user input as a name
    screenshots Turtles window
    names screenshot by the input provided
    prints a goodbye string
    '''
    filename=str(input("What would you like to name your picture?"))
    fn_2=str(filename)+".eps" #adds .eps extension to file name
    ts.getcanvas().postscript(file=fn_2) #maps screenshot function to post script file name
    gb_str="A screenshot of your visual with the name of "+str(filename)+" has been added to the directory folder"+"\n"+"Thank you for your visual! That will be all :)"
    print(gb_str)

def opening():
    '''
    sig: NoneType -> NoneType
    first function to go in the program
    takes user input for a note
    calls the drawing function for the provided note
    '''
    sel=str(input("To begin, enter one note in letter form (eg: A or B or C..etc):"))
    if sel in allnotes:
        notedraw(sel) #calls notedraw function 
    elif sel not in allnotes:
        err="Sorry, that's not a valid note. Please choose one of the notes listed above"
        print(err)
        opening() #recalls opening function in case of error 

def player(inp):
    '''
    sig: str -> sound
    takes an input as a string
    uses the playsound module to play the sound with the given name
    '''
    for note in inp:
        title=(str(note)+".wav")
        playsound.playsound(title) #calls playsound module to play file with given title  

def harmonies_draw(inp):
    '''
    sig: str -> turtles visual
    takes a user input of Y/N
    subsequently asks for another input: which chord base note the individual would like
    if user is satisfied with design, moves onto last function
    '''
    chosen_base=''
    if (inp=='Y'):
        chosen_base=str(input("Which chord would you like to play? (eg: C, D, B..ec)")) #if yes, user asked which note for chord base
        if chosen_base in allnotes:
            print("You have chosen the",chosen_base,"chord!","\n","Here are the notes it contains:")
            list_breaker(arp_dict[chosen_base]) #employs listbreaker function and chrod dictionary to show which notes are in a chord
            notedraw(arp_dict[chosen_base]) #calls notedraw function with the data from from chord dictionary
            listen="And this is what it sounds like!"
            print(listen)
            player(arp_dict[chosen_base]) #plays all the chords notes in succession
            harmonies_q=str(input("Would you like to add some more chords on top? (Y/N)"))
            harmonies_draw(harmonies_q) #takes input from harmonies_q as a response to re-commence harmonies_draw or conclude program
        elif chosen_base not in allnotes:
            err="Please choose a note out of the provided list!"
            print(err)
            harmonies_q=str(input("Would you like to add some chords on top? (Y/N)"))
            harmonies_draw(harmonies_q) #cathes error in input and restarts the function 
    if (inp!='Y') and (inp!='N'):
        oops="Sorry, I don't understand. Please try again"
        print(oops)
        harmonies_q=str(input("Would you like to add some chords on top? (Y/N)"))
        harmonies_draw(harmonies_q) #cathes error in initial input and restarts the function
    if (inp=='N'):
        gb="Alright, on to naming!"
        print(gb)
        bye() #calls last function to conclude program      

def go_again():
    '''
    sig: NoneType -> NoneType
    asks for user input
    depending on that, either adds notes on top or goes on to the harmonies_draw function
    '''
    go_again_q=str(input("Here's your visual! Would you like to add some more notes on top? (Y/N)"))
    while (go_again_q!='Y') and (go_again_q!='N'):
        oops="Sorry, I don't understand. Please try again"
        print(oops)
        go_again_q=str(input("Would you like to add some more notes on top? (Y/N)")) #cathes error in input, restarts function 
    if (go_again_q=='Y'):
        sel2=str(input("Please enter one note in letter form (eg: A or B or C..etc):"))
        if sel2 not in allnotes:
            error='That is not a valid input!Try again'
            print(error)
            go_again() #cathes error in note input, restarts function 
        else:
            notedraw(sel2.split()) #if input is correct, employes notedraw function with each note in chord
            go_again() #restarts function 
    if (go_again_q=='N'):
        harmonies_q=str(input("Would you like to add some chords on top? (Y/N)"))
        harmonies_draw(harmonies_q) #if user inputs N, goes on to harmonies_draw function with the previous input as a response
        

def notedraw(selection):
    '''
    sig: str -> NoneType
    makes kallidescope pattern out of provided notes
    matches each note to a specific colour, draws each on 4 corners
    goes through notes string 5 times, generating kallidescope pattern
    '''
    for n in range(1):
        for note in selection:
            title=(str(note)+".wav") #makes the title the same as note at hand
            playsound.playsound(title) #plays sound with the title of the note
            t.pencolor(notesdict[note]) #maps the pen color to the notesdict dictionary
            size = random.randint(10,40) #random size from 10 to 40
            x = random.randrange(0, turtle.window_width()//2) #divides x panels into quarters
            y = random.randrange(0,turtle.window_height()//2) #divides y panels into quarters
            t.penup()
            t.setpos(x,y)
            t.pendown()
            for m in range(size): #first quadrant being drawn
                t.forward(m*2)
                t.left(91)
            t.penup()
            t.setpos(-x,y)
            t.pendown()
            for m in range(size): #second quadrant being drawn
                t.forward(m*2)
                t.left(91)
            t.penup()
            t.setpos(-x,-y)
            t.pendown()
            for m in range(size): #third quadrant being drawn
                t.forward(m*2)
                t.left(91)
            t.penup()
            t.setpos(x,-y)
            t.pendown()
            for m in range(size): #fourth quadrant being drawn
                t.forward(m*2)
                t.left(91)
         


opening() #beginning with opeining function 
go_again() #go_again function as direct follow up

    
    




