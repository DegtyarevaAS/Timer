import pygame


pygame.init()

screen = pygame.display.set_mode((400, 25))
font = pygame.font.SysFont('Bront', 20)
color_bg = (255, 255, 255)
color_fg = (0, 0, 55)
sc = pygame.display.set_mode((400,400))
sec = 0
msec = 0
minute = 0
hour = 0

screen.fill(color_bg)
t1 = '00:00:00:000'
t2 = t1
screen.blit(font.render(t1, True, color_fg), (25, 25))
pygame.display.update()

run = False
b = -1 # счётчик 1/0
count = 0 # первая точка отсчёта
start = 0 # start-stop=время работы программы stop-start=время паузы
stop = 0
top = 50 # начальная точка по вертикали для записи истории



while True:
	for e in pygame.event.get():
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_SPACE:
				b *= -1 
				if b == 1 and count == 0: 
					# перевый старт
					count += 1 
					time_start = pygame.time.get_ticks()
				elif b == 1: 
					# последующие старты b == 1
					count += 1
					start += pygame.time.get_ticks() - time_start
					print('# ' + str(count) + ' ' + str(start - stop))
				else: 
					# стоп # b == -1
					stop += pygame.time.get_ticks() - time_start
					screen.blit(font.render(text, True, color_fg), (25, top))
					pygame.display.update()
					top += 25
					print(text)
					#print('# ' + str(count) + ' ' + str(start - stop))
		if e.type == pygame.KEYUP and count != 0:
			if e.key == pygame.K_KP_ENTER: # на нумпадовской клавиатуре
				# обнуление счётчика
				time_start = pygame.time.get_ticks()
				start = 0
				stop = 0
				text = t2
				pygame.draw.rect(screen, (255,255,255), (0,0,400,50))
				screen.blit(font.render(text, True, color_fg), (25, 25))
				pygame.display.update()
				b = -1
		if e.type == pygame.KEYUP and count != 0:
			if e.key == pygame.K_ESCAPE:
				# очистка вместе с историей
				time_start = pygame.time.get_ticks()
				start = 0
				stop = 0
				text = t2
				screen.fill(color_bg)
				screen.blit(font.render(text, True, color_fg), (25, 25))
				pygame.display.update()
				b = -1
				sc.fill(color_bg)
				top = 50
				count = 0 # чтобы больше двух раз не запускалось
		if e.type == pygame.KEYUP and count != 0:
			if e.key == pygame.K_BACKSPACE:
				# запись текущего состояния в историю
				screen.blit(font.render(text, True, color_fg), (25, top))
				pygame.display.update()
				top += 25
		if e.type == pygame.QUIT:
			pygame.quit()
	if b == 1:
		# сам счётчик
		temp_ticks = pygame.time.get_ticks() - time_start - start + stop
		msec = temp_ticks % 1000
		sec = (temp_ticks // 1000) % 60
		minute = (temp_ticks // 60000) % 60
		hour = (temp_ticks // 3600000) % 24
		
		msec = str(msec) if msec > 99 else '0' + str(msec) if msec > 9 else '00' + str(msec)
		sec = '0' + str(sec) if sec < 10 else str(sec)
		minute = '0' + str(minute) if minute < 10 else str(minute)
		hour = '0' + str(hour) if hour < 10 else str(hour)
		
		text = hour+':'+minute+':'+sec+':'+msec
		#screen.fill(color_bg)
		pygame.draw.rect(screen, (255, 255, 255), (0, 0, 400, 50))
		screen.blit(font.render(text, True, color_fg), (25, 25))
		pygame.display.update()




pygame.quit()
