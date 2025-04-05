import pygame  # Импортируем pygame для создания игры и рисования

# Инициализация pygame
pygame.init()

# Устанавливаем размеры экрана
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Устанавливаем заголовок окна
pygame.display.set_caption("Move the Ball")

# Определяем начальные координаты и радиус круга
x = 200  # Начальная позиция по оси X
y = 200  # Начальная позиция по оси Y
radius = 25  # Радиус круга (диаметр 50x50)

# Устанавливаем скорость перемещения
speed = 20

# Цвета
white = (255, 255, 255)  # Белый фон
red = (255, 0, 0)  # Красный цвет для мяча

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь закрывает окно
            running = False

    # Получаем состояние клавиш
    keys = pygame.key.get_pressed()

    # Перемещаем мяч в зависимости от нажатой клавиши
    if keys[pygame.K_UP] and y - radius > 0:  # Если нажата клавиша "Вверх"
        y -= speed  # Перемещаем мяч вверх
    if keys[pygame.K_DOWN] and y + radius < screen_height:  # Если нажата клавиша "Вниз"
        y += speed  # Перемещаем мяч вниз
    if keys[pygame.K_LEFT] and x - radius > 0:  # Если нажата клавиша "Влево"
        x -= speed  # Перемещаем мяч влево
    if keys[pygame.K_RIGHT] and x + radius < screen_width:  # Если нажата клавиша "Вправо"
        x += speed  # Перемещаем мяч вправо

    # Заливаем экран белым цветом
    screen.fill(white)

    # Рисуем красный круг
    pygame.draw.circle(screen, red, (x, y), radius)

    # Обновляем экран
    pygame.display.flip()

    # Ограничиваем частоту обновления экрана
    pygame.time.Clock().tick(60)

# Завершаем работу с pygame
pygame.quit()
