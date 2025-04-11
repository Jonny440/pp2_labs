import pygame
import random
import sys
import psycopg2

pygame.init()
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="kaz130212",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (200, 50, 50)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

INITIAL_SPEED = 10
LEVEL_UP_SCORE = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_food(position):
    rect = pygame.Rect(position[0]*CELL_SIZE, position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)

def draw_info(score, level):
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over(score):
    global conn, cursor
    import pygame

    #ask for username
    name = input("Game Over! Enter your name: ")

    #insert into database
    cursor.execute("""
        INSERT INTO snake_leaderboard (username, score)
        VALUES (%s, %s);
    """, (name, score))
    conn.commit()

    #fetch top 10 of the leaderboard
    cursor.execute("""
        SELECT username, score
        FROM snake_leaderboard
        ORDER BY score DESC
        LIMIT 10;
    """)
    top_scores = cursor.fetchall()

    # Pygame display setup
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Top 10 Scores")
    font = pygame.font.SysFont("Arial", 24)

    screen.fill((0, 0, 0))
    y_offset = 40

    title = font.render("Top 10 Scores", True, (255, 255, 255))
    screen.blit(title, (120, 10))

    for i, (username, score) in enumerate(top_scores, 1):
        text = font.render(f"{i}. {username} - {score}", True, (255, 255, 255))
        screen.blit(text, (50, y_offset))
        y_offset += 30

    pygame.display.flip()

    # Wait for quit or key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False
                pygame.quit()
                sys.exit()


def create_walls():
    walls = []
    for x in range(GRID_WIDTH):
        walls.append((x, 0))
        walls.append((x, GRID_HEIGHT - 1))
    for y in range(GRID_HEIGHT):
        walls.append((0, y))
        walls.append((GRID_WIDTH - 1, y))
    return walls

def draw_walls(walls):
    for wall in walls:
        rect = pygame.Rect(wall[0]*CELL_SIZE, wall[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)

def generate_food(snake, walls):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

def main():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    walls = create_walls()
    food = generate_food(snake, walls)
    score = 0
    level = 1
    speed = INITIAL_SPEED
    running = True

    while running:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
        elif keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
        elif keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        if new_head in walls or new_head in snake[1:]:
            game_over(score)

        if new_head == food:
            score += 1
            food = generate_food(snake, walls)
            if score % LEVEL_UP_SCORE == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        draw_walls(walls)
        draw_info(score, level)
        pygame.display.flip()

main()
