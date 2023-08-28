import os
import pygame
#######################################################################
#   기본 초기화 (반드시 해야 하는 것들)    #
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JD Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
#######################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")   # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]        # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 이벤트 루프
running = True # 게임이 진행중인가?
while running: 
    dt =clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   
            running = False             
    
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리 

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update()
    
# pygame 종료
pygame.quit()

# 유튜브 코딩 : 나도코딩
# 그림 저작권 : 
# background - https://www.freepik.com/free-vector/arcade-game-world-pixel-scene_4815143.htm#query=arcade-game-world-pixel-scene&position=8
# stage - https://www.freepik.com/free-vector/urban-city-day-time-background_4708004.htm#page=5&query=brick&position=47
# character - https://opengameart.org/content/custom-sprites-for-the-crystal-palace-0
# weapon(Head) - https://www.freepik.com/free-vector/weapon-icons-set_3924829.htm#page=1&query=arrow%20weapon&position=7
# weapon(wire) - https://www.freepik.com/free-vector/barbed-wire-realistic-illustration-separate-elements-barbed-wire_3586280.htm#page=1&query=wire&position=37
# ball - https://www.freepik.com/free-vector/colored-bubbles_808278.htm#page=2&query=bubble&position=18