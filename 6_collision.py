import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("hyunsu game") # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경이미지
background = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 세로크기
character_x_pos = (screen_width/2) -(character_width/2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 세로크기
enemy_x_pos = (screen_width/2) -(enemy_width/2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2) # 화면 세로크기 가장 아래에 위치


# 이벤트 루프 (이벤트 루프가 있어야 창이 안꺼짐)
running = True # 게임이 진행중인가?
while running :
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 설정

    print("fps : "+str(clock.get_fps()))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로 이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
                
        if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x == 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y == 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False
    
    
    screen.blit(background, (0,0)) # 배경 그리고, 좌표
    
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update() # 게임 화면 다시그리기!

    
# pygame 종료
pygame.quit()