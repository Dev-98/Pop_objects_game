import pygame, sys, os
import random
from pygame.locals import *
import streamlit as st

if st.button('Play', use_container_width=True):
    st.balloons()
    index =[]
    width = 600
    height = 700
    white = (255,255,255)
    black = (0,0,0)
    clock = pygame.time.Clock()
    g = 1
    score = 0
    fps = 20
    life = 10 
    fruits = ['purple', 'spaceship',  'virus', 'purple', 'bubble', 'rocket']
    # count = 0
    pygame.init()
    # Background
    BG = pygame.transform.scale(pygame.image.load("background-black.png"), (600, 800))
    # game display
    gameDisplay = pygame.display.set_mode((width, height))
    gameDisplay.blit(BG, (0,0))


    font = pygame.font.Font('comic.ttf', 32)
    score_text = font.render(str(score), True, white)
    # life_left = font.render(str(life), True, white )

    def generate_random_fruits(fruit):
        path =f'{fruit}.png'
        data[fruit] = {
            'img' : pygame.transform.scale(pygame.image.load(path),(80, 80)),
            'x' : random.randint(0, 500),
            'y' : random.randint(0, 500),
            'speed_x' : random.randint(-2, 2),
            'speed_y' : random.randint(-2, 2),
            'throw' : False,
            't' : 1,
            'hit' : False,
        }

        if(random.random() >= 0.95):
            data[fruit]['throw'] = True
        else:
            data[fruit]['throw'] = False
    # genrate random
    data = {}
    for fruit in fruits:
        generate_random_fruits(fruit)
        
    # display update
    pygame.display.update()
    # infinit loop 
    
    while True:        

        gameDisplay.blit(BG, (0,0))
        # gameDisplay.fill(white)
        gameDisplay.blit(score_text, (0,0))
        for key,value in data.items():
            if value['throw']:
                value['x'] = value['x'] + value['speed_x']
                value['y'] = value['y'] + 15
                value['speed_y'] += (g*value['t'])
                value['t'] += 0.2

                if value['y'] <= 700:
                    gameDisplay.blit(value['img'], (value['x'],value['y']))
                else:
                    generate_random_fruits(key)

                current_position = pygame.mouse.get_pos()
                if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                    path = os.path.join(key+'.png')
                    value['img'] = pygame.transform.scale(pygame.image.load(path), (0, 0))
                    value['speed_x'] += 1
                    score += 1
                    score_text = font.render(str(score), True, white)
                    life_left = font.render(str(life), True, white )
                    # index.append(pygame.mouse.get_pos())
                    value['hit'] = True


            else:
                generate_random_fruits(key)
                

        pygame.display.update()
        clock.tick(fps)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


