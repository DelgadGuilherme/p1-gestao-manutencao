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

    def can_win(self, player):
        if(player.get_player_sets() >= self.last_victory_set):
            return True
        else:
            return False
    
    def cant_win(self, player)
        if(player.get_player_sets >= self.zero_victory_set):
            return True
        else:
            return False

    def cant_have_more_game(self, player_one, player_two):
        if(player_one.get_player_sets() - player_two.get_player_sets() >= self.second_victory_set):
            return True
        else:
            return False

    def declare_victory(self, player_one, player_two):
        if(self.can_win(player_one) and self.cant_win(player_two) and self.cant_have_more_game(player_one, player_two)):
            return "Win for " + self.player_one.get_player_name()
        if(self.can_win(player_two) and self.cant_win(player_one) and self.cant_have_more_game(player_two, player_one)):
            return "Win for " + self.player_two.get_player_name()

    def declare_advantage(self, player_one, player_two):
        if (self.player_advantage(player_one, player_two) and self.is_third_or_more_set(self, player_two)):
            return "Advantage " + self.player_one.get_player_name()     
        if (self.player_advantage(player_two, player_one) and self.is_third_or_more_set(self, player_one)):
            return "Advantage " + self.player_two.get_player_name()
                
    def player_advantage(self, player_one, player_two): 
        if(player_one.get_player_set() > player_two.get_player_sets()) 
            return True

    def is_third_or_more_set(self, player):
        if(player.get_player_sets() >= self.third_victory_set)
            return True

    def score(self):
        result = ""
        if (self.player_one.get_player_sets() == self.player_two.get_player_sets() and self.player_one.get_player_sets() < self.third_victory_set):
            if (self.player_one.get_player_sets() == self.zero_victory_set):
                result = "Love"
            if (self.player_one.get_player_sets() == self.one_victory_set):
                result = "Fifteen"
            if (self.player_one.get_player_sets() == self.two_victory_set):
                result = "Thirty"
            result += "-All"
        if (self.player_one.get_player_sets() == self.player_two.get_player_sets() and self.player_one.get_player_sets() > self.secondVictorySet): 
            result = "Deuce"
        
        if (self.player_one.get_player_sets() > self.zero_victory_set and self.player_two.get_player_sets() == self.zero_victory_set):
            if (self.player_one.get_player_sets() == self.one_victory_set):
                self.player_one.set_player_points("Fifteen")
            if (self.player_one.get_player_sets() == self.two_victory_set):
               self.player_one.set_player_points("Thirty")
            if (self.player_one.get_player_sets() == self.third_victory_set):
               self.player_one.set_player_points("Forty")
            
            self.player_two.set_player_points("Love")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        if (self.player_two.get_player_sets() > self.zero_victory_set and self.player_one.get_player_sets() == self.zero_victory_set):
            if (self.player_two.get_player_sets() == self.one_victory_set):
                self.player_two.set_player_points("Fifteen")
            if (self.player_two.get_player_sets() == self.two_victory_set):
                self.player_two.set_player_points("Thirty")
            if (self.player_two.get_player_sets() == self.third_victory_set):
                self.player_two.set_player_points("Forty")
            
            self.player_one.set_player_points("Love")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        
        
        if (self.player_one.get_player_sets() > self.player_two.get_player_sets() and self.player_one.get_player_sets() < self.last_victory_set):
            if (self.player_one.get_player_sets() == self.two_victory_set):
                self.player_one.set_player_points("Thirty")
            if (self.player_one.get_player_sets() == self.third_victory_set):
                self.player_one.set_player_points("Forty")
            if (self.player_two.get_player_sets() == self.one_victory_set):
                self.player_two.set_player_points("Fifteen")
            if (self.player_two.get_player_sets() == self.two_victory_set):
                self.player_two.set_player_points("Thirty")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        if (self.player_two.get_player_sets() > self.player_one.get_player_sets() and self.player_two.get_player_sets() < self.last_victory_set):
            if (self.player_two.get_player_sets() == self.two_victory_set):
                self.player_two.set_player_points("Thirty")
            if (self.player_two.get_player_sets() == self.third_victory_set):
                self.player_two.set_player_points("Forty")
            if (self.player_one.get_player_sets() == self.one_victory_set):
                self.player_one.set_player_points("Fifteen")
            if (self.player_one.get_player_sets() == self.two_victory_set):
                self.player_one.set_player_points("Thirty")
            result = self.player_one.get_player_points() + "-" + self.player_two.get_player_points()
        
        result = self.declare_advantage(self, player_one, player_two)

        result = self.declare_victory(self, player_one, player_two)
