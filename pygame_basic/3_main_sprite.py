import pygame

pygame.init()

# 화면크기 설정
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width , screen_height))


#화면 타이틀
pygame.display.set_caption("Nado_game")

#배경이미지 불러오기
background = pygame.image.load('D:/ezen_python/pygame_basic/background.png')

#캐릭터(스프라이트) 불러오기
charactor = pygame.image.load('D:/ezen_python/pygame_basic/charactor.png')

charactor_size = charactor.get_rect().size # 이미지의 크기를 구해온다
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]
charactor_x_pos = (screen_width / 2) - (charactor_width / 2) #화면 가로의 절반에 위치
charactor_y_pos = screen_height - charactor_height #화면 세로 크기의 가장 아래에 위치


#이벤트루프
running = True

while running :
    for event in pygame.event.get() : # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
           running = False
           
    screen.blit(background, (0,0)) # 배경그리기
    screen.blit(charactor, (charactor_x_pos,charactor_y_pos)) # 배경그리기
    
    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()