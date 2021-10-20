# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:10:27 2019

@author: Charles
"""

import pygame

from settings import Settings   
from rocket import Rocket
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
 


def run_game():
    #initialiaze game and create a screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make play button
    play_button = Button(ai_settings, screen, "Play")
    
    #create an instance to store game stats and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
       #make a rocket
    rocket = Rocket(ai_settings, screen)
    #make bullets
    bullets = Group()
    #make aliens
    aliens = Group()
      
    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, rocket, aliens)


    
    #Start the main loop for the gameq
    while True:    
        gf.check_events(ai_settings, screen, stats, sb, play_button, rocket, 
                        aliens, bullets)
        if stats.game_active: 
            rocket.update()
            gf.update_bullets(ai_settings, screen, stats, sb, rocket, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, rocket, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, rocket, aliens, bullets, play_button)
        
run_game()
 
