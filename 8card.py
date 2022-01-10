import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def initiate():
    # create table that holds 8 cards
    table = [0]*8
    # create deck of cards with just numbers, and shuffle
    deck = [i for i in range(1,14)]*4
    random.shuffle(deck)

    return(run_game(deck,table))

def run_game(deck,table):
    count = 0
    i = 0
    j = 1
    boole = True
    while(boole):
        if(table[i] == table[j]): # a match
            table[i] = deck[count] # replace 1st part of pair with a new card
            count += 1
            table[j] = deck[count] # replace 2nd part of pair with a new card
            count += 1			
            if(count == 52): # all cards have been played
                boole = False
            else: # back out and check all over again with new cards
                i = 0
                j = 1	
        else: # no match		
            if(j!=7): # 2nd card needs to be increased
                j += 1			
            elif(j==7 and i!=6): # 1st card needs to be increased
                i += 1
                j = i+1			
            elif(i==6 and j==7): # no match found and 1st card is penultimate and 2nd card is last
                boole = False

    return(count)

#MAIN
result = []
trials = 10000000 # Ten Million
for i in range(trials):
    result.append(initiate())

# export data as series to analyze
result_series = pd.Series(result)
result_series.to_csv("8_card_data.csv", index=False)