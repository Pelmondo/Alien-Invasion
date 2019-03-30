import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	""" Реагирует на нажатие клавиш"""
	if event.key == pygame.K_RIGHT:
		# Переместить корабль вправо
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_SPACE:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)	

def check_keyup_events(event, ship):
	"""Реагирует на отпускание клавиш"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	""" Chekking events """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
							

def update_screen(ai_settings, screen, ship, bullets):
	""" Обновляет изоображение на экране и выводит корабль """
	# При каждом проходе цикла прорисовывается экран
	screen.fill(ai_settings.bg_color)
	# Все пули выводятся позади изоображений коробля и пришельцев
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Отображение последнего прорисованного экрана
	pygame.display.flip()		