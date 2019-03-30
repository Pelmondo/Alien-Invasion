import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
	# Инициализирует игру и создает объект экрана, также класс Settings
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Создание корабля
	ship = Ship(screen)
	# Запуск основного цикла игры 

	while True:
		# Отслеживание событий клавиатуры и мышки 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Прорисовка экрана 
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		# Отображение последнего прорисованного экрана
		pygame.display.flip()
run_game()				




