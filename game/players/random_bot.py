from game.run import Player

class RandomBot(Player):
    def __init__(self, name):
        super(RandomBot, self).__init__(name)

    def act(self, card_value, declared_sum):
