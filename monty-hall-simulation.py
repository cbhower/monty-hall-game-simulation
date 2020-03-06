# D-Door Monty Hall Simulation
"""
Created on Mon Apr 22 07:21:59 2019

@author: Christian
"""

import numpy as np
import pandas as pd

class MontyHall:
    def __init__(self, n_doors=3, n_sims=100):
        self.n_doors = n_doors
        self.hist_first_instinct = pd.DataFrame(columns=['score'])
        self.hist_second_guess = pd.DataFrame(columns=['score'])
        self.n_sims = n_sims

    def game_init(self):
        game_doors = np.zeros(self.n_doors)
        prize_door = np.random.randint(0, self.n_doors)
        game_doors[prize_door] = 1

        return prize_door

    def guess(self):
        guess = np.random.randint(0, self.n_doors)

        return guess

    def reveal_door(self):
        prize_door = self.game_init()
        guess = self.guess()
        for door in range(self.n_doors):
            if door != guess:
                if door != prize_door:
                    reveal = door

                    break

        return reveal, guess, prize_door

    def change_guess(self):
        reveal, guess, prize_door = self.reveal_door()
        #        print('guess:', guess, 'revealed:', reveal, 'prize:', prize_door)
        for door in range(self.n_doors):
            if door != guess:
                if door != reveal:
                    guess = door
                    break

                    #        print('guess:', guess, 'revealed:', reveal, 'prize:', prize_door)

        return guess, prize_door

    def first_instinct(self):
        prize_door = self.game_init()
        guess = self.guess()

        #       print('guess:', guess, 'prize:', prize_door)

        if guess == prize_door:
            self.hist_first_instinct = self.hist_first_instinct.append({'score': 1}, ignore_index=True)
        else:
            self.hist_first_instinct = self.hist_first_instinct.append({'score': 0}, ignore_index=True)

    def second_guesser(self):
        guess, prize_door = self.change_guess()

        if guess == prize_door:
            self.hist_second_guess = self.hist_second_guess.append({'score': 1}, ignore_index=True)
        else:
            self.hist_second_guess = self.hist_second_guess.append({'score': 0}, ignore_index=True)

    def run_sim(self):
        iteration = 0
        while iteration < self.n_sims:
            mh.first_instinct()
            mh.second_guesser()
            iteration += 1

    def calc_score(self):
        first_instinct = mh.hist_first_instinct.sum(axis=0) / self.n_sims
        second_guess = mh.hist_second_guess.sum(axis=0) / self.n_sims

        print('First Instinct:', first_instinct, 'Second Guesser:', second_guess)


mh = MontyHall(n_doors=3, n_sims=100)
mh.run_sim()
mh.calc_score()
