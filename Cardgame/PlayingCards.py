#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:26:10 2020

@author: shayyyyyy
"""

import random


class Card:
    def __init__(self,SuitIndex,Value):
        
        self.Value = Value
        self.SuitIndex = SuitIndex
        SuitIndex = int(SuitIndex)
        self.Suit_List = ["Ace","Clubs","Diamonds","Hearts","Spades","Jack","Queen","King"]
        

        
        if int(SuitIndex) == 0 or int(SuitIndex) > 4 :

            if SuitIndex == 0:
                self.Value = 1
                Suit = self.Suit_List[SuitIndex]
#                print("\nCard is %s with value of %s" % (Suit,self.Value))
#                print(self.Value ,Suit )


            elif SuitIndex == 5:
                self.Value = 11
                Suit = self.Suit_List[SuitIndex]
#                print("\nCard is %s with value of %s" % (Suit,self.Value))


            elif SuitIndex == 6:
                self.Value = 12
                Suit = self.Suit_List[SuitIndex]
#                print("\nCard is %s with value of %s" % (Suit,self.Value))

 
            elif SuitIndex == 7:
                self.Value = 13
                Suit = self.Suit_List[SuitIndex]
#                print("\nCard is %s with value of %s" % (Suit,self.Value))        
        else:

            pass
       
    def show1(self):
        if  self.Value == 0:
            x = random.randrange(1, 11)
            self.value = x
            Suit = self.Suit_List[self.SuitIndex]
            print("\nFirst Card is %s of %s " % (x , Suit))
            return x
        else:
#            print(self.Value,self.Suit_List[self.SuitIndex],"shay1")
            print("\nFirst Card is %s with value of %s" % (self.Suit_List[self.SuitIndex],self.Value) ) 
            return self.Value
 
    def show2(self):
        if  self.Value == 0:
            x = random.randrange(1, 11)
            self.value = x
            Suit = self.Suit_List[self.SuitIndex]
            print("\nSecond Card is %s of %s " % (x , Suit))
            return x
        else:
            print("\nSecond Card is %s with value of %s" % (self.Suit_List[self.SuitIndex],self.Value) )
            return self.Value
 
    def show3(self):
        if  self.Value == 0:
            x = random.randrange(1, 11)
            self.value = x
            Suit = self.Suit_List[self.SuitIndex]
            print("\nThird Card is %s of %s " % (x , Suit))
            return x
        else:
            print("\nThird Card is %s with value of %s" % (self.Suit_List[self.SuitIndex],self.Value) )
            return self.Value


if __name__ == '__main__':       
    x = random.randrange(1, 8)
    f = Card(2,0)
    l = Card(1,0)

    
    if f.show1() == l.show1():#testing if 2 clubs and 2 diamonds is considered the same in value, we want it t
        print("yes")



    
