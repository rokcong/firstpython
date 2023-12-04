import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		  
		# 기초 셋업
		pygame.init()
		pygame.display.set_caption('Zelda The First Big Game Project')		# 창 제목 설정
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))				# 게임 창 크기 설정
		self.clock = pygame.time.Clock()									# 게임의 프레임 설정
		
		self.level = Level()		# Level 클래스 인스턴스 생성

		# sound
		main_sound = pygame.mixer.Sound('../level graphics/audio/main.ogg') 	# 주 음악 파일 로드
		main_sound.set_volume(0.5)		# 음량 설정
		main_sound.play(loops = -1)  	# 반복 재생 설정
	   
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:		# 게임 창을 닫을 때
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.level.toggle_menu()	# ESC 키를 누를 때 메뉴를 토글하는 함수 호출

			self.screen.fill(WATER_COLOR)	# 화면 배경색 설정
			self.level.run()				# Level 클래스의 run 메서드 호출
			pygame.display.update()			# 화면 업데이트
			self.clock.tick(FPS)			# FPS에 따라 딜레이 설정

if __name__ == '__main__':
	game = Game()
	game.run()		# 게임 실행
