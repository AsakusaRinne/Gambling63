from game.run import Player, PlayerState

import random

class RandomBot(Player):
    def __init__(self, name):
        super(RandomBot, self).__init__(name)

    def act(self, card_value, declared_sum):
        if abs(declared_sum - 63) < 15:
            if random.randint(0,15) > 63 - declared_sum:
                self.state = PlayerState.stop
                self.declared_value = -1
            else:
                self.declared_value = random.randint(1,10)
        else:
            self.declared_value = random.randint(1, 10)
        return self.declared_value