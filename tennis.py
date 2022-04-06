# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.zero_victory_set = 0
        self.one_victory_set = 1
        self.second_victory_set = 2
        self.third_victory_set = 3
        self.last_victory_set = 4

    def set_player_sets(self, number):
        for i in range(number):
            self.sum_player_sets()
    
    def sum_player_sets(self, player):
        player.set_sum_player_sets()
    
    def won_point(self, player):
        player.set_sum_player_sets()

    def score(self):
        result = ""
        if (self.player_one.get_player_sets() == self.player_two.get_player_sets() and self.player_one.get_player_sets() < self.thirdVictorySet):
            if (self.player_one.get_player_sets() == self.zeroVictorySet):
                result = "Love"
            if (self.player_one.get_player_sets() == self.oneVictorySet):
                result = "Fifteen"
            if (self.player_one.get_player_sets() == self.twoVictorySet):
                result = "Thirty"
            result += "-All"
        if (self.player_one.get_player_sets() == self.player_two.get_player_sets() and self.player_one.get_player_sets() > self.secondVictorySet): 
            result = "Deuce"
        
        if (self.player_one.get_player_sets() > self.zeroVictorySet and self.player_two.get_player_sets() == self.zeroVictorySet):
            if (self.player_one.get_player_sets() == self.oneVictorySet):
                self.player_one.set_player_points("Fifteen")
            if (self.player_one.get_player_sets() == self.twoVictorySet):
               self.player_one.set_player_points("Thirty")
            if (self.player_one.get_player_sets() == self.thirdVictorySet):
               self.player_one.set_player_points("Forty")
            
            self.player_two.set_player_points("Love")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        if (self.player_two.get_player_sets() > self.zeroVictorySet and self.player_one.get_player_sets() == self.zeroVictorySet):
            if (self.player_two.get_player_sets() == self.oneVictorySet):
                self.player_two.set_player_points("Fifteen")
            if (self.player_two.get_player_sets() == self.twoVictorySet):
                self.player_two.set_player_points("Thirty")
            if (self.player_two.get_player_sets() == self.thirdVictorySet):
                self.player_two.set_player_points("Forty")
            
            self.player_one.set_player_points("Love")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        
        
        if (self.player_one.get_player_sets() > self.player_two.get_player_sets() and self.player_one.get_player_sets() < self.lastVictorySet):
            if (self.player_one.get_player_sets() == self.twoVictorySet):
                self.player_one.set_player_points("Thirty")
            if (self.player_one.get_player_sets() == self.thirdVictorySet):
                self.player_one.set_player_points("Forty")
            if (self.player_two.get_player_sets() == self.oneVictorySet):
                self.player_two.set_player_points("Fifteen")
            if (self.player_two.get_player_sets() == self.twoVictorySet):
                self.player_two.set_player_points("Thirty")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        if (self.player_two.get_player_sets() > self.player_one.get_player_sets() and self.player_two.get_player_sets() < self.lastVictorySet):
            if (self.player_two.get_player_sets() == self.twoVictorySet):
                self.player_two.set_player_points("Thirty")
            if (self.player_two.get_player_sets() == self.thirdVictorySet):
                self.player_two.set_player_points("Forty")
            if (self.player_one.get_player_sets() == self.oneVictorySet):
                self.player_one.set_player_points("Fifteen")
            if (self.player_one.get_player_sets() == self.twoVictorySet):
                self.player_one.set_player_points("Thirty")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        
        if (self.player_one.get_player_sets() > self.player_two.get_player_sets() and self.player_two.get_player_sets() >= self.thirdVictorySet):
            result = "Advantage " + self.player_one.get_player_name()
        
        if (self.player_two.get_player_sets() > self.player_one.get_player_sets() and self.player_one.get_player_sets() >= self.thirdVictorySet):
            result = "Advantage " + self.player_two.get_player_name()
        
        if (self.player_one.get_player_sets() >= self.lastVictorySet and self.player_two.get_player_sets() >= zeroVictorySet and (self.player_one.get_player_sets()-self.player_two.get_player_sets()) >= self.secondVictorySet):
            result = "Win for " + self.player_one.get_player_name()
        if (self.player_two.get_player_sets() >= self.lastVictorySet and self.player_one.get_player_sets() >= zeroVictorySet and (self.player_two.get_player_sets()-self.player_one.get_player_sets()) >= self.secondVictorySet):
            result = "Win for " + self.player_one.get_player_name()
        return result


    
