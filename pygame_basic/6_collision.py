import pygame

pygame.init()

# 화면크기 설정
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width , screen_height))


#화면 타이틀
pygame.display.set_caption("Nado_game")

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load('D:/ezen_python/pygame_basic/background.png')

#캐릭터(스프라이트) 불러오기
charactor = pygame.image.load('D:/ezen_python/pygame_basic/charactor.png')

charactor_size = charactor.get_rect().size # 이미지의 크기를 구해온다
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width / 2) - (charactor_width / 2) #화면 가로의 절반에 위치
charactor_y_pos = screen_height - charactor_height #화면 세로 크기의 가장 아래에 위치

# 이동할 좌표

to_x = 0
to_y = 0

# 이동속도

charactor_speed = 0.6


#이벤트루프
running = True

while running :
    dt = clock.tick(60) #게임화면의 초당 프레임수
         
    for event in pygame.event.get() : # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
           running = False
        
        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT :
                to_x -= charactor_speed
            elif event.key == pygame.K_RIGHT :
                to_x += charactor_speed
            elif event.key == pygame.K_UP :
                to_y -= charactor_speed
            elif event.key == pygame.K_DOWN :
                to_y += charactor_speed
                
        if event.type == pygame.KEYUP : #방향키를 떼면 멈춘다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    charactor_x_pos += to_x * dt
    charactor_y_pos += to_y * dt
    
    # 가로 경계값 처리
    if charactor_x_pos < 0 :
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width -charactor_width :
        charactor_x_pos = screen_width -charactor_width
        
    if charactor_y_pos < 0 :
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height -charactor_height :
        charactor_y_pos = screen_height -charactor_height
        
    screen.blit(background, (0,0)) # 배경그리기
    screen.blit(charactor, (charactor_x_pos,charactor_y_pos)) # 배경그리기
    
    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()