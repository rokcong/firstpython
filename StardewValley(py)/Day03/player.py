import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        super().__init__(group)

        # 플레이어 애니메이션과 프레임 인덱스 초기화
        self.import_assets()
        self.status = 'left_water'
        self.frame_index = 0

        # 일반적인 setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # 이동 관련 속성
        self.direction = pygame.math.Vector2()   # (x,y)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        # 플레이어의 모든 애니메이션 이미지 불러오기
        self.animations = {'up': [], 'down': [], 'left': [],'right': [],
                            'right_idle':[], 'left_idle': [], 'up_idle': [],'down_idle':[],
                            'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                            'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [], 
                            'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}

        for animation in self.animations.keys():
            full_path = 'D:/VSCode/StudyPython/stardew_Valley/graphics/character/' + animation
            self.animations[animation]  = import_folder(full_path)
        print(self.animations)

    def input(self):
        # 키 입력 받기
        keys = pygame.key.get_pressed()

        # 방향키에 따라 이동 방향 설정
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):

        # 벡터 정규화
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # 가로 이동
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # 세로 이동
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        
    def update(self, dt):
        # 매 프레임마다 호출되어야 하는 업데이트 함수
        self.input()    # 플레이어 입력 처리
        self.move(dt)   # 이동 로직 적용