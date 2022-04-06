class Player:
    def __init__(self, player_name, player_sets, player_points):
        self.player_name = player_name
        self.player_sets = player_sets
        self.player_points = player_points

    def get_player_name(self):
        return self.player_name

    def get_player_sets(self):
        return self.player_sets

    def get_player_points(self):
        return self.player_points

    def set_sum_player_sets(self):
        return self.player_sets += 1

    def set_player_points(self, point):
        return self.player_points = point
