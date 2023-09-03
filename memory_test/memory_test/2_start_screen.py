import pygame

def displat_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심 좌표는 start_button이 중심 좌표를 따라가고,
    # 반지름은 60, 선 두께는 5


# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120 )

# 색쌀
BLACK = (0, 0, 0)               # RGB
WHITE = (255, 255, 255)         # RGB

# 게임 루프
running = True  # 게임이 실행 중 인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get():       # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:      # 창이 닫히는 이벤트인가?
            running = False                # 게임이 더 이상 실행 중이 아님

    # 화면 전체를 까맣게 색칠
    screen.fill(BLACK)

    # 시작 화면 표시 
    displat_start_screen()

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()

