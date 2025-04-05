import pygame  # Импортируем библиотеку pygame, которая используется для работы с мультимедиа
import os  # Импортируем библиотеку os для работы с файловой системой

# Инициализируем pygame и модуль музыки
pygame.init()  # Инициализируем все модули Pygame
pygame.mixer.init()  # Инициализируем модуль для работы с музыкой

# Создаем окно
screen = pygame.display.set_mode((400, 200))  # Создаем окно размером 400x200 пикселей
pygame.display.set_caption("Music Player")  # Устанавливаем заголовок окна

# Загружаем все песни из папки music
music_folder = "music"  # Указываем папку, где лежат песни
songs = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]  # Составляем список всех файлов с расширением .mp3 в папке music
songs.sort()  # Сортируем список песен по имени
current = 0  # Устанавливаем индекс текущей песни на 0 (первая песня)

# Функция для воспроизведения песни
def play_song():  # Функция для воспроизведения текущей песни
    pygame.mixer.music.load(os.path.join(music_folder, songs[current]))  # Загружаем текущую песню
    pygame.mixer.music.play()  # Начинаем воспроизведение песни

# Основной цикл
running = True  # Переменная для контроля состояния программы
while running:  # Бесконечный цикл, пока пользователь не закроет окно
    for event in pygame.event.get():  # Обрабатываем все события, происходящие в окне
        if event.type == pygame.QUIT:  # Если закрыли окно
            running = False  # Выход из цикла, программа завершится

        # Проверяем, нажата ли клавиша
        if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
            if event.key == pygame.K_p:  # Если нажата клавиша "p"
                play_song()  # Воспроизводим текущую песню
            elif event.key == pygame.K_s:  # Если нажата клавиша "s"
                pygame.mixer.music.stop()  # Останавливаем музыку
            elif event.key == pygame.K_n:  # Если нажата клавиша "n"
                current = (current + 1) % len(songs)  # Переключаем на следующую песню в списке (цикл)
                play_song()  # Воспроизводим новую песню
            elif event.key == pygame.K_b:  # Если нажата клавиша "b"
                current = (current - 1) % len(songs)  # Переключаем на предыдущую песню в списке (цикл)
                play_song()  # Воспроизводим новую песню

    screen.fill((30, 30, 30))  # Заполняем экран темным цветом (RGB 30, 30, 30)
    pygame.display.flip()  # Обновляем экран, чтобы отобразить изменения

pygame.quit()  # Завершаем работу с Pygame, закрываем все открытые ресурсы
