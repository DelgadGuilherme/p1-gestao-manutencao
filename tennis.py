# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_sets = 0
        self.player_two_sets = 0
        self.zero_victory_set = 0
        self.one_victory_set = 1
        self.second_victory_set = 2
        self.third_victory_set = 3
        self.last_victory_set = 4

    def set_player_one_sets(self, number):
        for i in range(number):
            self.sum_player_one_sets()
    
    def Set_player_two_sets(self, number):
        for i in range(number):
            self.sum_player_two_sets()
    
    def sum_player_one_sets(self):
        self.player_one_sets += 1
    
    def sum_player_two_sets(self):
        self.player_two_sets += 1
        
    def won_point(self, player_name):
        if player_name == self.player_one_name:
            self.sum_player_one_sets()
        else:
            self.sum_player_two_sets()

    def score(self):
        result = ""
        if (self.player_one_sets == self.player_two_sets and self.player_one_sets < self.thirdVictorySet):
            if (self.player_one_sets == zeroVictorySet):
                result = "Love"
            if (self.player_one_sets == oneVictorySet):
                result = "Fifteen"
            if (self.player_one_sets == twoVictorySet):
                result = "Thirty"
            result += "-All"
        if (self.player_one_sets==self.player_two_sets and self.player_one_sets > self.secondVictorySet): 
            result = "Deuce"
        
        player_one_pont = ""
        player_two_pont = ""
        
        if (self.player_one_sets > zeroVictorySet and self.player_two_sets == zeroVictorySet):
            if (self.player_one_sets == oneVictorySet):
                player_one_pont = "Fifteen"
            if (self.player_one_sets == twoVictorySet):
                player_one_pont = "Thirty"
            if (self.player_one_sets == thirdVictorySet):
                player_one_pont = "Forty"
            
            player_two_pont = "Love"
            result = player_one_pont + "-" + player_two_pont
        if (self.player_two_sets > zeroVictorySet and self.player_one_sets == zeroVictorySet):
            if (self.player_two_sets == oneVictorySet):
                player_two_pont = "Fifteen"
            if (self.player_two_sets == twoVictorySet):
                player_two_pont = "Thirty"
            if (self.player_two_sets == thirdVictorySet):
                player_two_pont = "Forty"
            
            player_one_pont = "Love"
            result = player_one_pont + "-" + player_two_pont
        
        
        if (self.player_one_sets > self.player_two_sets and self.player_one_sets < lastVictorySet):
            if (self.player_one_sets == twoVictorySet):
                player_one_pont="Thirty"
            if (self.player_one_sets == thirdVictorySet):
                player_one_pont="Forty"
            if (self.player_two_sets== oneVictorySet):
                player_two_pont="Fifteen"
            if (self.player_two_sets== twoVictorySet):
                player_two_pont="Thirty"
            result = player_one_pont + "-" + player_two_pont
        if (self.player_two_sets > self.player_one_sets and self.player_two_sets < lastVictorySet):
            if (self.p2Set == twoVictorySet):
                player_two_pont="Thirty"
            if (self.player_two_sets == thirdVictorySet):
                player_two_pont="Forty"
            if (self.player_one_sets == oneVictorySet):
                player_one_pont="Fifteen"
            if (self.player_one_sets == twoVictorySet):
                player_one_pont="Thirty"
            result = player_one_pont + "-" + player_two_pont
        
        if (self.player_one_sets > self.player_two_sets and self.player_two_sets >= thirdVictorySet):
            result = "Advantage " + self.player1Name
        
        if (self.player_two_sets > self.player_one_sets and self.player_one_sets >= thirdVictorySet):
            result = "Advantage " + self.player2Name
        
        if (self.player_one_sets >= lastVictorySet and self.player_two_sets >= zeroVictorySet and (self.player_one_sets-self.player_two_sets) >= secondVictorySet):
            result = "Win for " + self.player1Name
        if (self.player_two_sets >= lastVictorySet and self.player_one_sets >= zeroVictorySet and (self.player_two_sets-self.player_one_sets) >= secondVictorySet):
            result = "Win for " + self.player2Name
        return result
    
