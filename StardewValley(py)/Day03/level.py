import pygame
from settings import *
from player import Player

class Level:
    def __init__(self) :

        # 화면 표시 설정
        self.display_surface = pygame.display.get_surface()

        # sprite groups 설정
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        # 플레이어 생성 및 그룹에 추가
        self.player = Player((640, 360), self.all_sprites)        # ((x,y) group)

    def run(self, dt):
        # 화면을 검은색으로 채우기
        self.display_surface.fill('black')
        
        # 모든 sprite를 화면에 그리기
        self.all_sprites.draw(self.display_surface)

        # 모든 sprite를 업데이트
        self.all_sprites.update(dt)