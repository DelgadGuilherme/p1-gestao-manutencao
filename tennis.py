# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Sets = 0
        self.p2Sets = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Sets()
        else:
            self.P2Sets()
    
    def score(self):
        result = ""
        if (self.p1Sets == self.p2Sets and self.p1Sets < 3):
            if (self.p1Sets==0):
                result = "Love"
            if (self.p1Sets==1):
                result = "Fifteen"
            if (self.p1Sets==2):
                result = "Thirty"
            result += "-All"
        if (self.p1Sets==self.p2Sets and self.p1Sets>2): 
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1Sets > 0 and self.p2Sets==0):
            if (self.p1Sets==1):
                P1res = "Fifteen"
            if (self.p1Sets==2):
                P1res = "Thirty"
            if (self.p1Sets==3):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2Sets > 0 and self.p1Sets==0):
            if (self.p2Sets==1):
                P2res = "Fifteen"
            if (self.p2Sets==2):
                P2res = "Thirty"
            if (self.p2Sets==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1Sets>self.p2Sets and self.p1Sets < 4):
            if (self.p1Sets==2):
                P1res="Thirty"
            if (self.p1Sets==3):
                P1res="Forty"
            if (self.p2Sets==1):
                P2res="Fifteen"
            if (self.p2Sets==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2Sets>self.p1Sets and self.p2Sets < 4):
            if (self.p2Sets==2):
                P2res="Thirty"
            if (self.p2Sets==3):
                P2res="Forty"
            if (self.p1Sets==1):
                P1res="Fifteen"
            if (self.p1Sets==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1Sets > self.p2Sets and self.p2Sets >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.p2Sets > self.p1Sets and self.p1Sets >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1Sets>=4 and self.p2Sets>=0 and (self.p1Sets-self.p2Sets)>=2):
            result = "Win for " + self.player1Name
        if (self.p2Sets>=4 and self.p1Sets>=0 and (self.p2Sets-self.p1Sets)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Sets(self, number):
        for i in range(number):
            self.P1Sets()
    
    def SetP2Sets(self, number):
        for i in range(number):
            self.P2Sets()
    
    def P1Sets(self):
        self.p1Sets +=1
    
    
    def P2Sets(self):
        self.p2Sets +=1