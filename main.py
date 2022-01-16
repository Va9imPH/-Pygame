import pygame # импортируем модуль

pygame.init() # инициализация окна
size = (500, 500) # размер окна
screen = pygame.display.set_mode(size) # установка размер окна
pygame.display.set_caption('Game') # название окна
img = pygame.image.load('pizza.png') # иконка для окна
pygame.display.set_icon(img) # установка иконки на окно

run = True
while run: # основной цикл окна
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # условия для завершения программы
            run = False