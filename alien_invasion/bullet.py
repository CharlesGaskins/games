# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:20:41 2019

@author: Charles
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''class to manage bullets fires from the ship'''
    
    def __init__(self, ai_settings, screen, rocket):
        '''create a bullet object at the ships current location'''
        super().__init__()
        self.screen = screen
        
        #creat a bullet rectAT (0, 0) and the set the correct position
        self.rect = pygame.Rect(0, 0, int(ai_settings.bullet_width),
            int(ai_settings.bullet_height))
        self.rect.centerx = rocket.rect.centerx
        self.rect.top = rocket.rect.top
        
        #store the bullet's position as a decimmal value
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''move the bullet up the screen'''
        #update the decimal positon of the bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        '''draw bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)