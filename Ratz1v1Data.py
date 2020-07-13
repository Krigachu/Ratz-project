import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

#create file, append data to it, make it easy to add data.


def main():
    loop = True
    checkFile()
    while loop:
        print("What do you want to do \nA -> ADD DATA\nB -> LOOK AT DATA\nC -> QUIT")
        option = input("> ")
        time.sleep(1)
        if option.upper()=="A":
            print("Adding data")
            addingData()
        elif option.upper()=="B":
            print("Looking at data")
            lookingAtData()
        elif option.upper()=="C":
            print("Quitting program")
            loop = False
        else:
            print("Please re-enter option")
            time.sleep(1)

def checkFile():
    if (not path.exists("sampleData.csv")): #.csv total
        f = open("sampleData.csv", "w+")
        f.write("GAME NUMBER,KRI FRAGS,ADAM FRAGS,KRI ACCURACY,ADAM ACCURACY,WINNER,DATE")
        f.close()

def addingData():
    loop = True
    while loop:
        gameNum = file_len("sampleData.csv")
        kriFrags = input("KRI FRAGS: ")
        adamFrags = input("ADAM FRAGS: ")
        kriAccuracy = input("KRI ACCURACY: ")
        adamAccuracy = input("ADAM ACCURACY: ")
        winner = input("WINNER: ")
        currentDate = date.today()
        wantToAdd = input("Do you want to input this record? (Y/N): ")
        if (wantToAdd.upper() == "Y"):
            f = open("sampleData.csv","a+")
            record = str(gameNum) + "," + str(kriFrags) + "," + str(adamFrags) + "," + str(kriAccuracy) + "," + str(adamAccuracy) + "," + str(winner) + "," + str(currentDate)
            f.write("\n" + record)
            loop = False

def lookingAtData():
    loop = True
    while loop:
        print("What do you want to do \nA -> FRAG STATS\nB -> ACCURACY STATS\nC -> WIN STATS\nD -> RETURN TO MAIN MENU")
        option = input("> ")
        time.sleep(1)
        if option.upper()=="A":
            print("Analysing Frag stats")
            fragStats()
        elif option.upper()=="B":
            print("Analysing Accuracy stats")
            accuracyStats()
        elif option.upper()=="C":
            print("Analysing Win stats")
            winStats()
        elif option.upper()=="D":
            print("Returning to main menu")
            loop=False
        else:
            print("Please re-enter option")
            time.sleep(1)

def fragStats():
    print("Total frags (both): " + str(avgFragsAccuracy(1) + avgFragsAccuracy(2)))
    print("Total Kri frags: " + str(avgFragsAccuracy(1)))
    print("Total Adam frags: " + str(avgFragsAccuracy(2)))
    print("Avg Kri frags: " + str(avgFragsAccuracy(1) / (file_len("sampleData.csv") - 1)))
    print("Avg Adam frags: " + str(avgFragsAccuracy(2) / (file_len("sampleData.csv") - 1)))
    print("\n")

def accuracyStats():
    #highest recorded accuracy for Kri and Adam
    print("Avg Kri accuracy: " + str(avgFragsAccuracy(3) / (file_len("sampleData.csv") - 1)))
    print("Avg Adam accuracy: " + str(avgFragsAccuracy(4) / (file_len("sampleData.csv") - 1)))
    print("\n")

def winStats():
    print("Total Kri wins: " + str(wins(5)[0]))
    print("Total Adam wins: " + str(wins(5)[1]))
    print("% of Games won by Kri: " + str((wins(5)[0] / (file_len("sampleData.csv")-1))*100))
    print("% of Games won by Adam: " + str((wins(5)[1] / (file_len("sampleData.csv")-1))*100))

def avgFragsAccuracy(column):
    f = open("sampleData.csv","r")
    accumulator = 0
    firstLine = True
    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            if (not firstLine):
                lineArray = x.split(",")
                accumulator = accumulator + int(lineArray[column])
            elif firstLine:
                firstLine = False
    return accumulator

#def higestAndLowest(column):
#    f = open("sampleData.csv", "r")
#    accumulator = 0
#    firstLine = True
#    lowestFrags
#    if f.mode == "r":
#        fl = f.readlines()
#        for x in fl:
#            if (not firstLine):
#                lineArray = x.split(",")
#
#
#
#
#            elif firstLine:
#                firstLine = False
#    return accumulator

def wins(column):
    f = open("sampleData.csv", "r")
    kriCounter = 0
    adamCounter = 0
    firstLine = True
    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            if (not firstLine):
                lineArray = x.split(",")
                if(lineArray[column].upper()=="KRI"):
                    kriCounter += 1
                elif (lineArray[column].upper()=="ADAM"):
                    adamCounter += 1
                else:
                    print("Error with data on game " + lineArray[0])
            elif firstLine:
                firstLine = False
    return [kriCounter,adamCounter]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

if __name__ == "__main__":
    main()

#THINGS TO DO
#DATA ANALYSIS
    #Who wins the most
    #Highest overall accuracy
    #Maybe make temp files based on dates and analyse that like using copy shutil functions?
    #Eventually use pyplot?