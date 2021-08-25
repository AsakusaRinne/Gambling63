#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 6:46
# @Author  : Yaohui Liu
# @Email   : 202021010321@std.uestc.edu.cn
# @File    : run.py
# @Software: PyCharm

import random
from enum import Enum

cards_example = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:4}

class PlayerState(Enum):
    wait = 0
    playing = 1
    stop = 2


class Player(object):
    def __init__(self, name):
        self.name = name
        self.state = PlayerState.wait

    def act(self):
        '''
        The act of the player in a round.

        This function should be overrided in its derived classes.
        This function should return an integer,
        which means quit the game if it's <= 0 and the value the player declares if it's >0
        :return:
        '''
        raise NotImplementedError

    def reset(self):
        self.state = PlayerState.wait

class GamblingContext(object):
    def __init__(self, players, max_sum = 63, cards = cards_example):
        self.max_sum = max_sum
        if isinstance(players, list):
            self.players = players
        else:
            raise NotImplementedError
        self.cards = []
        for key, value in cards:
            self.cards += [key for i in range(value)]

        self.real_sum = 0
        self.declare_sum = 0
        self.round_num = 0

    def shuffle(self):
        random.shuffle(self.cards)

    def restart(self):
        self.real_sum = 0
        self.declare_sum = 0
        self.round_num = 0
        self.start()

    def start(self):
        self.shuffle()

    def next_round(self):
        card_value = self.cards[self.round_num]
        self.round_num += 1
        self.real_sum += card_value
        for player in self.players:
            r = player.act()
            if r < 0:
                player.state = PlayerState.stop
            else:
                self.declare_sum += r