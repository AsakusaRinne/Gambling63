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
        raise NotImplementedError

class GamblingContext(object):
    def __init__(self, max_sum = 63, player_num = 3, cards = cards_example):
        self.max_sum = max_sum
        self.player_num = player_num
        self.cards = []
        for key, value in cards:
            self.cards += [key for i in range(value)]

    def shuffle(self):
        random.shuffle(self.cards)

    def restart(self):
        ## shuffle the cards
        pass

    def start(self):
        pass

    def next_round(self):
        pass