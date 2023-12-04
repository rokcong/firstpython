import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface

        # 'object' 유형의 타일은 위치를 조정하여 생성
        if sprite_type == 'object' : 
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        
        # 충돌 박스 생성
        self.hitbox = self.rect.inflate(0, y_offset)