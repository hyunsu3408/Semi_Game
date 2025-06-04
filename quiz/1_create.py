import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("hyunsu game2")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\quiz\\background.png")

character = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\quiz\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = (screen_height) - (character_height)

enemy = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\quiz\\enemy.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 10

to_x = 0
character_speed = 10

running = True
while running:
    dt = clock.tick(30)
    print("fps : "+str(clock.get_fps()))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    character_x_pos += to_x
    
    
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += enemy_speed
    if enemy_y_pos + enemy_height > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width-enemy_width)
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print("게임 아웃")
        running = False
    
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update()
    
pygame.quit()