from os import walk
import pygame

def import_folder(path):
    surface_list = []

    # 지정된 폴더에서 이미지 파일을 불러와 리스트에 추가
    # path: 이미지가 있는 폴더 경로

    # for folder_name, sub_folder, img_files in walk(path):
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
