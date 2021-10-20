# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:20:08 2019

@author: Charles
"""
import pygame.font
from pygame.sprite import Group
from rocket import Rocket

class Scoreboard():
    '''class to hold scoring info'''
    def __init__(self, ai_settings, screen, stats):
        '''initialize scorekeeping attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #font setting for scoring
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #prep the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_rockets()
        
    def prep_score(self):
        '''turn score into a rendered image'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        #display the score at the top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        '''turn high score into rendered image'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                    self.text_color, self.ai_settings.bg_color)
                                    
        #center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        
    def prep_level(self):
        '''turn level into rendered image'''
        self.level_image = self.font.render(str(self.stats.level), True, 
                                    self.text_color, self.ai_settings.bg_color)
        
        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_rockets(self):
        '''show how many ships a player has left'''
        self.rockets = Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket = Rocket(self.ai_settings, self.screen)
            rocket.rect.x = 10 + rocket_number * rocket.rect.width
            rocket.rect.y = 10
            self.rockets.add(rocket)
        
    def show_score(self):
        '''draw score to the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #draw rockets
        self.rockets.draw(self.screen)