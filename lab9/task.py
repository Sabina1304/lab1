import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры экрана и блоков
BLOCK = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Extended 🍏⏱️")

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Змейка: список координат блоков
snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK, 0)

# Очки, уровень, скорость
score = 0
level = 1
speed = 10

# Таймер и генерация еды
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - BLOCK) // BLOCK) * BLOCK
        self.y = random.randint(0, (HEIGHT - BLOCK) // BLOCK) * BLOCK
        self.weight = random.choice([1, 2, 3])  # вес еды
        self.spawn_time = time.time()          # момент появления
        self.lifetime = random.randint(5, 10)  # сколько живёт (в секундах)

    def draw(self):
        # Цвет зависит от веса еды
        if self.weight == 1:
            color = RED
        elif self.weight == 2:
            color = GOLD
        else:
            color = WHITE
        pygame.draw.rect(screen, color, (self.x, self.y, BLOCK, BLOCK))

    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime

    def position(self):
        return (self.x, self.y)

# Список еды
foods = [Food()]

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, BLOCK):
        direction = (0, -BLOCK)
    if keys[pygame.K_DOWN] and direction != (0, -BLOCK):
        direction = (0, BLOCK)
    if keys[pygame.K_LEFT] and direction != (BLOCK, 0):
        direction = (-BLOCK, 0)
    if keys[pygame.K_RIGHT] and direction != (-BLOCK, 0):
        direction = (BLOCK, 0)

    # Новая голова
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка столкновений
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake
    ):
        running = False

    snake.insert(0, head)

    # Проверка на поедание еды
    eaten = False
    for food in foods[:]:
        if head == food.position():
            score += food.weight
            foods.remove(food)
            eaten = True
            break

    if not eaten:
        snake.pop()  # если не съел — удалить хвост

    # Удаление просроченной еды
    for food in foods[:]:
        if food.is_expired():
            foods.remove(food)

    # Добавление новой еды, если их мало
    if len(foods) < 2:
        foods.append(Food())

    # Уровень увеличивается каждые 5 очков
    if score // 5 + 1 > level:
        level += 1
        speed += 2

    # Рисуем змейку
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK, BLOCK))

    # Рисуем еду
    for food in foods:
        food.draw()

    # Печатаем счёт и уровень
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(speed)

# Завершение
pygame.quit()
