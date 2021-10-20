# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:47:10 2019

@author: Charles
"""

class GameStats():
    '''track the statistics for AI'''
    
    def __init__(self, ai_settings):
        '''initialize statistics'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #start AI in an active stats
        self.game_active = False
        #high score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.rockets_left = self.ai_settings.rocket_limit
        self.score = 0
        self.level = 1
        
        