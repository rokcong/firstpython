import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		# Pygame 초기화 및 화면 설정
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('The Second project Stardew Valley')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				# 종료 이벤트 처리
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
            # 경과 시간 계산
			dt = self.clock.tick() / 1000
			self.level.run(dt)
            # 화면 업데이트
			pygame.display.update()

if __name__ == '__main__':
	# 게임 인스턴스 생성 및 실행
	game = Game()
	game.run()
