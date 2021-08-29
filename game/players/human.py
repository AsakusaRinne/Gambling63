#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 1:03
# @Author  : Yaohui Liu
# @Email   : 202021010321@std.uestc.edu.cn
# @File    : human.py
# @Software: PyCharm

from game.run import Player, PlayerState

import random

class HumanPlayer(Player):
    def __init__(self, name, callback_func):
        super(HumanPlayer, self).__init__(name)
        self.callback_func = callback_func

    def act(self, card_value, declared_sum):
        self.declared_value = self.callback_func()
        if self.declared_value == -1:
            self.state = PlayerState.stop
        return self.declared_value