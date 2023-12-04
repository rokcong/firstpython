from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
	# CSV 레이아웃 파일을 읽어와서 2D 리스트로 변환하는 함수
	terrain_map = []
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

def import_folder(path):
	# 지정된 폴더에서 이미지 파일들을 불러와서 리스트로 반환하는 함수
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list
