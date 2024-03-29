# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:44:43 2019

@author: Charles
"""

class Settings():
    '''class to store all setting for tthe game'''
    
    def __init__(self):
        '''initialize the game's static settings'''
        #sceen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #ship settings
        self.rocket_speed_factor = 1.5
        self.rocket_limit = 3
        
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet directon 1 reps right; -1 left
        self.fleet_direction = 1
        
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point values increas
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''initialize setting that change throughout the game'''
        self.rocket_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 reps right; -1 left
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50
        
    def increase_speed(self):
        '''increase speed settings and alien point values'''
        self.rocket_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        
        
        
        
        
        
        
        