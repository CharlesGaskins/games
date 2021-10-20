# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:06:17 2019

@author: Charles
"""

import sys
from time import sleep
import pygame
from bullet import Bullet
from rocket import Rocket
from alien import Alien
from scoreboard import Scoreboard


def check_keydown_events(event, ai_settings, screen, rocket, bullets):
    '''respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a new bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, rocket, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
        
def fire_bullet(ai_settings, screen, rocket, bullets):
    '''fire a bullet if limit hasn't been reached'''
    #create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, rocket)
        bullets.add(new_bullet)
        
        
def check_keyup_events(event, rocket):
    '''respond to key releases'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False    
    

def check_events(ai_settings, screen, stats, sb, play_button, rocket, aliens, 
                 bullets):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        elif event.type == pygame.KEYDOWN:    
            check_keydown_events(event, ai_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,sb, play_button,
                              rocket, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, sb, play_button, rocket,
                      aliens, bullets, mouse_x, mouse_y):
    '''start a new game when the player clicks play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset game settings
        ai_settings.initialize_dynamic_settings()
        #hide mouse cursor
        pygame.mouse.set_visible(False)
        #reset the game stats
        stats.reset_stats()
        stats.game_active = True
        #reset the score board
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_rockets()
        #empty list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #create new fleet
        create_fleet(ai_settings, screen, rocket, aliens)
        rocket.center_rocket
        
    
def update_bullets(ai_settings, screen, stats, sb, rocket, aliens, bullets):
    '''update position of bullets and get rid of old bullets'''
    #update bullet positions
    bullets.update()
    #get rid of bullets that have gone off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collision(ai_settings, screen, stats, sb, rocket, 
                                 aliens, bullets)
    #make the most recently drawn screen visible
    pygame.display.flip()
    
    
def check_bullet_alien_collision(ai_settings, screen, stats, sb, rocket,
                                 aliens, bullets):
    '''respond to bullet-alien collision'''
    #remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        #if entire fleet is destroyed start new level
        bullets.empty()
        ai_settings.increase_speed()
        #increase level
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, rocket, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    '''determine the number of aliens that can fit in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
    
def get_number_rows(ai_settings, rocket_height, alien_height):
    '''determine the number of rows of aliens that fit on the screen'''
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - rocket_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''create an allien and place it in row'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, rocket, aliens):
    '''create a full fleet of aliens'''
    #create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, rocket.rect.height, 
        alien.rect.height)
    
    
    #creates the entire fleet
    for row_number in range(number_rows):
        #create the first row of aliens
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''respond if any aliens have reached the edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    '''drop the entire fleet and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    

def rocket_hit(ai_settings, screen, stats, sb, rocket, aliens, bullets):
    '''respond to ship being hit by alien'''
    if stats.rockets_left > 0:
    #decrease rockets_left
        stats.rockets_left -= 1
        #update scoreboard
        sb.prep_rockets()
        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, rocket, aliens)
        rocket.center_rocket()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, screen, stats, sb, rocket, aliens,
                        bullets):
    '''check if any aliens have reached the bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this the same as if the ship was hit
            rocket_hit(ai_settings, screen, stats, sb, rocket, aliens, bullets)
            break

def check_high_score(stats, sb):
    '''check to see if there's a new high score'''
    if stats.score > stats.high_score:
        stats.high_score  = stats.score
        sb.prep_high_score()

    
def update_aliens(ai_settings, screen, stats, sb, rocket, aliens, bullets):
    '''update the positions of all aliens in the fleet'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #look for alien-rocket collisions
    if pygame.sprite.spritecollideany(rocket, aliens):
        rocket_hit(ai_settings, screen, stats, sb, rocket, aliens, bullets)
        print("Ship hit!!!")
    check_aliens_bottom(ai_settings, screen, stats, sb, rocket, aliens, bullets)
    
def update_screen(ai_settings, screen, stats, sb, rocket, aliens, bullets,
                  play_button):
    '''update images on the screen and flip to the new screen'''
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    aliens.draw(screen)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #draw the score info
    sb.show_score()
    #draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    
    
    pygame.display.flip()
    

    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    