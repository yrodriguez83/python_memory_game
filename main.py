import pygame
import logic
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sequence Memorization Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font settings
FONT = pygame.font.Font(None, 36)


def draw_text(surface, text, x, y):
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


def show_sequence(screen, sequence):
    screen.fill(WHITE)
    draw_text(screen, "Memorize the following sequence:", 10, 10)
    draw_text(screen, " ".join(str(x) for x in sequence), 10, 60)
    pygame.display.flip()
    pygame.time.delay(len(sequence) * 750)
    screen.fill(WHITE)


def get_user_input(screen, level):
    screen.fill(WHITE)
    draw_text(screen, f"Enter the sequence of length {level}:", 10, 10)
    pygame.display.flip()
    user_input = []
    input_index = 0
    input_done = False

    while not input_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit() and int(event.unicode) in [1, 2, 3, 4]:
                    user_input.append(int(event.unicode))
                    input_index += 1

                    if input_index == level:
                        input_done = True

    return user_input


def play_game():
    level = 1
    correct = True

    while correct:
        sequence = logic.generate_sequence(level)
        show_sequence(SCREEN, sequence)
        user_input = get_user_input(SCREEN, level)

        if user_input == sequence:
            level += 1
        else:
            correct = False

    with open("game_data.txt", "a") as f:
        f.write(f"{level - 1}\n")


def show_high_scores(screen):
    screen.fill(WHITE)
    with open("game_data.txt", "r") as f:
        scores = [int(line.strip()) for line in f.readlines()]
        scores.sort(reverse=True)
        draw_text(screen, "Top 5 high scores:", 10, 10)
        for i, score in enumerate(scores[:5]):
            draw_text(screen, f"{i + 1}. {score}", 10, 60 + i * 40)
        pygame.display.flip()
        pygame.time.delay(3000)


def main_menu():
    while True:
        SCREEN.fill(WHITE)
        draw_text(SCREEN, "Sequence Memorization Game", 10, 10)
        draw_text(SCREEN, "Press P to play or H for high scores", 10, 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_game()
                elif event.key == pygame.K_h:
                    show_high_scores
                    show_high_scores(SCREEN)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main_menu()
