import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("hyunsu game") # 게임이름

# 배경이미지
background = pygame.image.load("C:\\Users\\hyunsu\\study\\python2\\background.png")



# 이벤트 루프 (이벤트 루프가 있어야 창이 안꺼짐)
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 하였는가?
            running = False # 게임이 진행중이 아님
    
    # screen.fill((0, 0, 255)) # rgb로 색깔 채우기
    screen.blit(background, (0,0)) # 배경 그리고, 좌표
    
    pygame.display.update() # 게임 화면 다시그리기!

# pygame 종료
pygame.quit()