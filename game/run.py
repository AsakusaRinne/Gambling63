#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 6:46
# @Author  : Yaohui Liu
# @Email   : 202021010321@std.uestc.edu.cn
# @File    : run.py
# @Software: PyCharm

import random
from enum import Enum

cards_example = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4}


class PlayerState(Enum):
    wait = 0
    playing = 1
    stop = 2


class Player(object):
    def __init__(self, name):
        self.name = name
        self.state = PlayerState.wait
        self.round = 0
        self.declared_value = 0
        self.win = False

    def act(self, card_value, declared_sum):
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
        self.win = False
        self.declared_value = 0
        self.round = 0

    def set_result(self, result):
        '''
        This method will be called when the game stops and the result was settled.
        It could be used as a callbcak method to give reward to the model.
        :param result: the result of the game.
        :return: True if win and False if lose.
        '''
        self.win = result


class GamblingContext(object):
    def __init__(self, players, max_sum=63, cards=cards_example):
        self.max_sum = max_sum
        if isinstance(players, list):
            self.players = players
        else:
            raise NotImplementedError
        self.cards = []
        for key, value in cards.items():
            self.cards += [key for i in range(value)]

        self.real_sum = 0
        self.declare_sum = 0
        self.round_num = 0
        self.records = [0] # record the real sum value of each round

    def shuffle(self):
        random.shuffle(self.cards)

    def restart(self):
        for player in self.players:
            player.reset()
        self.real_sum = 0
        self.declare_sum = 0
        self.round_num = 0
        self.start()

    def start(self):
        self.shuffle()
        for player in self.players:
            player.state = PlayerState.playing

    def is_running(self):
        player_remain = 0
        for player in self.players:
            if player.state == PlayerState.playing:
                player_remain += 1
        return player_remain > 1

    def is_waiting(self):
        player_remain = 0
        for player in self.players:
            if player.state == PlayerState.wait:
                player_remain += 1
        return player_remain > 0

    def settle(self):
        '''
        The process to execute when the game stops
        :return:
        '''
        if self.real_sum > 63:
            distance = []
            for player in self.players:
                if player.state == PlayerState.playing:
                    distance.append(9999)
                elif player.state == PlayerState.stop:
                    distance.append(abs(self.records[player.round] - 63))
                else:
                    raise ValueError

            ## if all players stop in the same round, then all the players lose
            if distance[0] * len(distance) == sum(distance):
                for player in self.players:
                    player.set_result(False)
                    return

            for player in self.players:
                if min(distance) == abs(self.records[player.round] - 63):
                    player.set_result(True)
                else:
                    player.set_result(False)
        else:
            for player in self.players:
                if player.state == PlayerState.stop:
                    player.set_result(False)
                elif player.state == PlayerState.playing:
                    player.set_result(True)
                else:
                    raise ValueError

    def get_card(self, index):
        card_value = self.cards[self.round_num + index]

        self.real_sum += card_value

        return card_value

    def next_round(self):
        self.round_num += 1
        self.records.append(self.real_sum)

        if not self.is_running() and not self.is_waiting():
            ## game over and begin to show the result
            self.settle()

    def auto_play_round(self):
        '''
        Mainly used to train the model.
        :return:
        '''
        self.round_num += 1
        player_remain = 0
        for i in range(len(self.players)):
            player = self.players[i]
            card_value = self.cards[self.round_num + i]

            self.real_sum += card_value
            self.records.append(self.real_sum)

            if player.state == PlayerState.playing:
                player.round += 1
                r = player.act(card_value, self.declare_sum)
                if r < 0:
                    player.state = PlayerState.stop
                else:
                    self.declare_sum += r
                    player_remain += 1

        if player_remain <= 1:
            ## game over and begin to show the result
            self.settle()

    def player_declare(self, index):
        player = self.players[index]
        card_value = self.cards[self.round_num + index]

        if player.state == PlayerState.playing:
            player.round += 1
            r = player.act(card_value, self.declare_sum)
            if r < 0:
                player.state = PlayerState.stop
            else:
                self.declare_sum += r
