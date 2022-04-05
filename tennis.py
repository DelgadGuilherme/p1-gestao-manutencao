# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Sets = 0
        self.p2Sets = 0
        self.zeroVictorySet = 0
        self.oneVictorySet = 1
        self.secondVictorySet = 2
        self.thirdVictorySet = 3
        self.lastVictorySet = 4

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
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Sets()
        else:
            self.P2Sets()

    def score(self):
        result = ""
        if (self.p1Sets == self.p2Sets and self.p1Sets < self.thirdVictorySet):
            if (self.p1Sets == zeroVictorySet):
                result = "Love"
            if (self.p1Sets == oneVictorySet):
                result = "Fifteen"
            if (self.p1Sets == twoVictorySet):
                result = "Thirty"
            result += "-All"
        if (self.p1Sets==self.p2Sets and self.p1Sets > self.secondVictorySet): 
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1Sets > zeroVictorySet and self.p2Sets == zeroVictorySet):
            if (self.p1Sets == oneVictorySet):
                P1res = "Fifteen"
            if (self.p1Sets == twoVictorySet):
                P1res = "Thirty"
            if (self.p1Sets == thirdVictorySet):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2Sets > zeroVictorySet and self.p1Sets == zeroVictorySet):
            if (self.p2Sets == oneVictorySet):
                P2res = "Fifteen"
            if (self.p2Sets == twoVictorySet):
                P2res = "Thirty"
            if (self.p2Sets == thirdVictorySet):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1Sets > self.p2Sets and self.p1Sets < lastVictorySet):
            if (self.p1Sets == twoVictorySet):
                P1res="Thirty"
            if (self.p1Sets == thirdVictorySet):
                P1res="Forty"
            if (self.p2Sets== oneVictorySet):
                P2res="Fifteen"
            if (self.p2Sets== twoVictorySet):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2Sets > self.p1Sets and self.p2Sets < lastVictorySet):
            if (self.p2Set == twoVictorySet):
                P2res="Thirty"
            if (self.p2Sets == thirdVictorySet):
                P2res="Forty"
            if (self.p1Sets == oneVictorySet):
                P1res="Fifteen"
            if (self.p1Sets == twoVictorySet):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1Sets > self.p2Sets and self.p2Sets >= thirdVictorySet):
            result = "Advantage " + self.player1Name
        
        if (self.p2Sets > self.p1Sets and self.p1Sets >= thirdVictorySet):
            result = "Advantage " + self.player2Name
        
        if (self.p1Sets >= lastVictorySet and self.p2Sets >= zeroVictorySet and (self.p1Sets-self.p2Sets) >= secondVictorySet):
            result = "Win for " + self.player1Name
        if (self.p2Sets >= lastVictorySet and self.p1Sets >= zeroVictorySet and (self.p2Sets-self.p1Sets) >= secondVictorySet):
            result = "Win for " + self.player2Name
        return result
    
