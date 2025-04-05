import pygame
import sys
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

CENTER = (200, 200)  # Центр экрана и вращения стрелок

def blit_rotate_center(surf, image, pos, origin_pos, angle):
    # Определяем прямоугольник изображения с учетом смещения от pivot-точки
    image_rect = image.get_rect(topleft=(pos[0] - origin_pos[0], pos[1] - origin_pos[1]))

    # Вычисляем вектор от центра изображения до точки вращения
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # Вращаем этот вектор на нужный угол
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # Находим новое положение центра изображения
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    # Вращаем изображение
    rotated_image = pygame.transform.rotate(image, angle)

    # Получаем прямоугольник вращенного изображения и задаем его центр
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # Рисуем изображение на поверхности (экране)
    surf.blit(rotated_image, rotated_image_rect)


# Прямоугольная стрелка
def create_hand(color):                                  # Функция принимает цвет стрелки
    hand = pygame.Surface((10, 100), pygame.SRCALPHA)     # Создаем прозрачную поверхность 10x100
    pygame.draw.rect(hand, color, (0, 0, 10, 100), border_radius=3)  # Рисуем прямоугольную стрелку с закруглением
    return hand                                           # Возвращаем готовую стрелку


minute_hand = create_hand((255, 0, 0))   # Минутная
second_hand = create_hand((0, 0, 255))   # Секундная

origin = (5, 90)  # Точка вращения стрелки (у основания)

# Загрузка картинки фона
bg_path = "mickeyclock.jfif"


bg = pygame.image.load(bg_path).convert_alpha()
bg = pygame.transform.smoothscale(bg, (400, 400))

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Текущее время
    now = datetime.datetime.now()
    second_angle = -6 * now.second
    minute_angle = -6 * now.minute

    # Рендеринг
    screen.blit(bg, (0, 0))  # Центрированный фон
    blit_rotate_center(screen, second_hand, CENTER, origin, second_angle)
    blit_rotate_center(screen, minute_hand, CENTER, origin, minute_angle)

    pygame.display.flip()

pygame.quit()
sys.exit()
