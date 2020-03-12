#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:00:35 2020

@author: shayyyyyy

"""
import random
import pydealer
from PlayingCards import *


try:
    pax = int(input("How many players are we having today?: "))
    buy_in = int(input("Dear Game Master, please key in the Buy-In amount for each player?: "))
except:
    print("\nYou have either keyed in an invalid number for the \"Number of Players\" field or the \"Buy-In\" ")
    pax = int(input("Please key in a valid number for Number of Players you wish to register for the game : "))
    buy_in = int(input("Dear Game Master, please key in a valid Buy-In amount for each player: "))


pot_list = []
player_list =[]
for i in range(pax):
    print("\nWelcome, what is your Name")
    Name = str(input("\nWelcome, what is your Name: "))
    Balance = int(buy_in * -1)
    class Player:
        def __init__(self, Name,ID, Balance):
            self.Name = Name
            self.ID = ID
            self.Balance = Balance
    x = Player(Name,i,Balance)
    player_dict = {"ID":x.ID,
                   "Name":x.Name,
                   "Balance":x.Balance}
#    print(player_dict)
    player_list.append(player_dict)

    print(player_list)
    print("\n\nPlayer %s created with ID %s and starting credit $%s" % (x.Name,x.ID,x.Balance))
    
p = int(pax * buy_in)
pot_list.append(p)
pot= sum(pot_list)
print(pot)
def play(pax):


 
    for num in range(pax):
        player_ID = int(input("What's ur player ID?: "))
        player_chosen = (player_list[player_ID])
        p_b = int((player_chosen['Balance']))
        print("\nPlayer %s has credit of $%s" % (player_chosen['Name'],(1*p_b)))


        x = random.randrange(1, 8)
        first_card = Card(2,0)
        a = first_card.show1()



        y = random.randrange(1, 8)
        second_card = Card(y,0)
        b = second_card.show2()


        if a == b:
            print("\nHand Cannot Be Played")
            pass
        else:
            play_or_not = input("Do you wish to play or not? To play please key in \"play\" if you wish to skip please key in \"pass\"  ")
            play_or_not = play_or_not.lower()
            if play_or_not == str("play"):
                bet = int(input("What is the amount you wish to bet?: "))
                if pot - bet < 0:
                    a = sum(pot_list)
                    bet = (int(input("Invalid amount key in,please dont bet more money than what is currently in the pot, $%s. Once again, what is the amount you wish to bet?: " % (a))))
                    if pot - bet < 0:                        
                        print("You are betting an invalid amount of money. It may be more money than what's in the pot.As Indiana Jones said , \"You have chose Poorly\".On to the next player we go.")
                        continue




                z = random.randrange(1, 8)
                third_card = Card(2,0)
                c = third_card.show3()

                if c == a or c == b:
                    print(pot,"1")
                    deduct2(bet,p_b,player_chosen,pot,pot_list,player_ID)
                    pot_new = sum(pot_list)
                    print("\nPlayer %s has  $%s left and there is $%s in the pot. " % (player_chosen['Name'],player_chosen['Balance'],pot_new))
                    print("TIMES 2")


                elif a > b:
                    b = b+1
                    if c in range(b , a):
#                        print(pot,"1")
                        pay(bet,p_b,player_chosen,pot,pot_list,player_ID)
                        pot_new = sum(pot_list)
#                        print(pot_new,"2")
                        print("\nPlayer %s has  $%s left and there is $%s in the pot. " % (player_chosen['Name'],player_chosen['Balance'],pot_new))
                    else:
                        
                        deduct(bet,p_b,player_chosen,pot,pot_list,player_ID)
                        pot_new = sum(pot_list)
#                        print(f,"2")
                        print("\nPlayer %s has  $%s left and there is $%s in the pot. " % (player_chosen['Name'],player_chosen['Balance'],pot_new))

                elif b > a:
                    a = a+1
                    if c in range(a , b):
#                        print(pot,"1")
                        pay(bet,p_b,player_chosen,pot,pot_list,player_ID)
                        pot_new = sum(pot_list)
                        
                        print("\nPlayer %s has  $%s left and there is $%s in the pot. " % (player_chosen['Name'],player_chosen['Balance'],pot_new))
                    else:
                        
#                        print(pot,"1")
                        deduct(bet,p_b,player_chosen,pot,pot_list,player_ID)
                        pot_new = sum(pot_list)
                        
                        print("\nPlayer %s has  $%s left and there is $%s in the pot. " % (player_chosen['Name'],player_chosen['Balance'],pot_new))

            elif play_or_not == str("pass"):
                print("Turn Skipped")
                continue

def deduct(wager,balance,player_chosen,pot,pot_list,player_ID):
    balance = int(balance)
    wager = int(wager)
    new_balance = int(balance - wager)
    new = {'Balance': new_balance}
    player_chosen.update(new)
#    print(player_chosen)
    pot = pot + wager
    pot_list[player_ID] = pot
#    print(pot_list)



def deduct2(wager,balance,player_chosen,pot,pot_list,player_ID):
    balance = int(balance)
    wager = int(2*wager)
    new_balance = int(balance - wager)
    new = {'Balance': new_balance}
    player_chosen.update(new)
#    print(player_chosen)
    pot = pot + wager
    pot_list[player_ID] = pot
#    print(pot_list)



def pay(wager,balance,player_chosen,pot,pot_list,player_ID):
    balance = int(balance)
    wager = int(wager)
    new_balance = int(balance - wager)
    new = {'Balance': new_balance}
    player_chosen.update(new)
    pot = pot - wager
    pot_list[player_ID] = pot






play(pax)
