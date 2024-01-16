import pygame

pygame.init()

# 화면크기 설정
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width , screen_height))

#화면 타이틀
pygame.display.set_caption("Nado_game")

#이벤트루프
running = True

while running :
    for event in pygame.event.get() : # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
           running = False

# pygame 종료
pygame.quit()