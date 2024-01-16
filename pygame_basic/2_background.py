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

#이벤트루프
running = True

while running :
    for event in pygame.event.get() : # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
           running = False
           
    screen.blit(background, (0,0)) # 배경그리기
    
    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()