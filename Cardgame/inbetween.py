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
except:
    pax = int(input("Please key in a valid number: "))
    
player_list =[]
for i in range(pax):
    print("\nWelcome, provide the game master with your Name and how much credit you would like to start the game with")
    Name = str(input("Please enter your name: "))
    Balance = str(input("Please enter your starting credit: "))
    class Player:
        def __init__(self, Name,ID, Balance):
            self.Name = Name
            self.ID = ID
            self.Balance = Balance
    x = Player(Name,i,Balance)
    player_dict = {"ID":x.ID,
                   "Name":x.Name,
                   "Balance":x.Balance}
    print(player_dict)
    player_list.append(player_dict)
    print(player_list)
    print("\n\nPlayer %s created with ID %s and starting credit $%s" % (x.Name,x.ID,x.Balance))
    
def play(pax):       
    
    for num in range(pax):
        player_ID = int(input("What's ur player ID?: "))        
        player_chosen = (player_list[player_ID])
        p_b = int((player_chosen['Balance']))
        print("\nPlayer %s has credit of $%s" % (player_chosen['Name'],p_b))

        
        x = random.randrange(1, 8)
        first_card = Card(x,0)
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
                if p_b - bet < 0:
                    print(int(input("Please only bet money that you actually have. We dont work on credit over here.Once again, what is the amount you wish to bet?: ")))
                    if p_b - bet < 0:
                        print("why are you playing with money you dont have ? Bad fund management.On to the next player we go.")
                        continue
                else:
                    pass
                        
             
                    
                z = random.randrange(1, 8)
                third_card = Card(z,0)               
                c = third_card.show3()
                    
                if c == a or c == b:
                    deduct(bet,p_b,player_chosen)
                    deduct(bet,p_b,player_chosen)
                    
                    print("\nPlayer %s has  $%s left" % (player_chosen['Name'],player_chosen['Balance']))
#                    print("fat L x2",p_b)
                    
                        
                elif a > b:
                    b = b+1
                    if c in range(b , a):                       
                        pay(bet,p_b,player_chosen)
                        print("\nPlayer %s has  $%s left" % (player_chosen['Name'],player_chosen['Balance']))
                    else:
                        deduct(bet,p_b,player_chosen)
                        print("\nPlayer %s has  $%s left" % (player_chosen['Name'],player_chosen['Balance']))
                        
                elif b > a:
                    a = a+1
                    if c in range(a , b):                       
                        pay(bet,p_b,player_chosen)
                        print("\nPlayer %s has  $%s left" % (player_chosen['Name'],player_chosen['Balance']))
                    else:
                        deduct(bet,p_b,player_chosen)

                        print("\nPlayer %s has  $%s left" % (player_chosen['Name'],player_chosen['Balance']))                  
                            
            elif play_or_not == str("pass"):
                print("Turn Skipped")
                continue
            
def deduct(wager,balance,player_chosen):
    balance = int(balance)
    wager = int(wager)
    new_balance = int(balance - wager)
    new = {'Balance': new_balance}
    player_chosen.update(new)

    
def pay(wager,balance,player_chosen):
    balance = int(balance)
    wager = int(wager)
    new_balance = int(balance + wager)
    new = {'Balance': new_balance}
    player_chosen.update(new)
    
       

    
    
    

play(pax)