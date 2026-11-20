import pygame
import random
import sys

# ==============================================================================
# 1. GAME SETTINGS (Sabhi basic numbers yahan hain)
# ==============================================================================
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Physics (Bird ke girne aur udne ki speed)
GRAVITY = 1
FLAP_FORCE = -10

# Colors (Rang)
SKY_BLUE = (112, 197, 206)
GROUND_COLOR = (222, 216, 149)
GROUND_GRASS = (115, 191, 46)
BIRD_YELLOW = (255, 215, 0)
BIRD_ORANGE = (255, 140, 0)
PIPE_GREEN = (115, 190, 46)
PIPE_DARK_GREEN = (70, 130, 30)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)


# ==============================================================================
# 2. BIRD CLASS (Chidiya)
# ==============================================================================
class Bird:
    def __init__(self):
        # Shuruat me bird kahan rahegi
        self.x = 100
        self.y = 300
        self.size = 30
        self.velocity = 0

    def flap(self):
        # Space dabane par upar jana (-10)
        self.velocity = FLAP_FORCE

    def update(self):
        # Har frame me gravity lagti hai aur bird neeche girti hai
        self.velocity += GRAVITY
        self.y += self.velocity

    def get_rect(self):
        # Collision check karne ke liye bird ka box
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        # Bird ki yellow body
        body_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.ellipse(screen, BIRD_YELLOW, body_rect)
        pygame.draw.ellipse(screen, BLACK, body_rect, 2)

        # Bird ke pankh (Wing)
        wing_rect = pygame.Rect(self.x + 4, self.y + 10, 14, 10)
        pygame.draw.ellipse(screen, BIRD_ORANGE, wing_rect)

        # Bird ki aankh (Eye)
        pygame.draw.circle(screen, WHITE, (self.x + 22, self.y + 8), 5)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 8), 2)

        # Bird ki choch (Beak)
        beak_points = [
            (self.x + 28, self.y + 12),
            (self.x + 36, self.y + 15),
            (self.x + 28, self.y + 18)
        ]
        pygame.draw.polygon(screen, BIRD_ORANGE, beak_points)
        pygame.draw.polygon(screen, BLACK, beak_points, 1)


# ==============================================================================
# 3. PIPE CLASS (Raste ke Khambhe)
# ==============================================================================
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = 150
        self.speed = 3
        self.passed = False

        # Upar wale pipe ki height random set hoti hai
        self.top_height = random.randint(80, 350)
        # Neeche wale pipe ka starting point
        self.bottom_y = self.top_height + self.gap

    def update(self):
        # Pipe ko left side move karna
        self.x -= self.speed

    def is_offscreen(self):
        # Check karna ki pipe screen se bahar chala gaya ya nahi
        return self.x + self.width < 0

    def is_colliding(self, bird_rect):
        # Check karna ki bird pipe se takrayi ya nahi
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, SCREEN_HEIGHT - self.bottom_y)
        return top_rect.colliderect(bird_rect) or bottom_rect.colliderect(bird_rect)

    def draw(self, screen):
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, SCREEN_HEIGHT - self.bottom_y)

        # Upar aur neeche wale green pipes draw karna
        pygame.draw.rect(screen, PIPE_GREEN, top_rect)
        pygame.draw.rect(screen, PIPE_DARK_GREEN, top_rect, 2)

        pygame.draw.rect(screen, PIPE_GREEN, bottom_rect)
        pygame.draw.rect(screen, PIPE_DARK_GREEN, bottom_rect, 2)


# ==============================================================================
# 4. MAIN GAME LOOP
# ==============================================================================
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird Simple Game")
    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont("Arial", 36, bold=True)
    font_small = pygame.font.SysFont("Arial", 20, bold=True)

    # Game ke variables
    bird = Bird()
    pipes = []
    score = 0
    game_state = "START"  # "START", "PLAYING", "GAME_OVER"
    pipe_timer = 0

    running = True
    while running:
        # 1. USER INPUT (Keyboard dabana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # SPACE key dabane par
                if event.key == pygame.K_SPACE:
                    if game_state == "START":
                        game_state = "PLAYING"
                        bird.flap()
                    elif game_state == "PLAYING":
                        bird.flap()
                    elif game_state == "GAME_OVER":
                        # Restart karna
                        bird = Bird()
                        pipes = []
                        score = 0
                        game_state = "PLAYING"
                        bird.flap()

                # ESC dabane par game band karna
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 2. GAME LOGIC (Update)
        if game_state == "PLAYING":
            # Bird ki movement update karo
            bird.update()

            # Zameen ya Aasman se takrayi? (Ground or Ceiling collision)
            if bird.y < 0 or bird.y + bird.size >= SCREEN_HEIGHT:
                game_state = "GAME_OVER"

            # Har 90 frames me naya pipe spawn karna
            pipe_timer += 1
            if pipe_timer >= 90:
                pipes.append(Pipe(SCREEN_WIDTH))
                pipe_timer = 0

            # Sabhi pipes ko update karo aur collision check karo
            for pipe in pipes:
                pipe.update()

                # Collision check
                if pipe.is_colliding(bird.get_rect()):
                    game_state = "GAME_OVER"

                # Score badhana jab bird pipe ko paar kar le
                if not pipe.passed and bird.x > pipe.x + pipe.width:
                    pipe.passed = True
                    score += 1

            # Screen se bahar gaye pipes ko hatana
            pipes = [pipe for pipe in pipes if not pipe.is_offscreen()]

        # 3. DRAWING (Screen par sab kuch banana)
        # Background Sky
        screen.fill(SKY_BLUE)

        # Pipes draw karo
        for pipe in pipes:
            pipe.draw(screen)

        # Ground (Zameen) draw karo
        ground_height = 50
        pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))
        pygame.draw.rect(screen, GROUND_GRASS, (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, 10))
        pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - ground_height), (SCREEN_WIDTH, SCREEN_HEIGHT - ground_height), 2)

        # Bird draw karo
        bird.draw(screen)

        # Text Messages
        if game_state == "START":
            title = font_big.render("FLAPPY BIRD", True, WHITE)
            hint = font_small.render("Press SPACE to Fly", True, BLACK)
            screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 180))
            screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 240))

        elif game_state == "PLAYING":
            score_text = font_big.render(str(score), True, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 40))

        elif game_state == "GAME_OVER":
            over_text = font_big.render("GAME OVER", True, (255, 60, 60))
            final_score = font_small.render(f"Final Score: {score}", True, WHITE)
            restart_hint = font_small.render("Press SPACE to Restart", True, (255, 215, 0))

            screen.blit(over_text, (SCREEN_WIDTH // 2 - over_text.get_width() // 2, 200))
            screen.blit(final_score, (SCREEN_WIDTH // 2 - final_score.get_width() // 2, 260))
            screen.blit(restart_hint, (SCREEN_WIDTH // 2 - restart_hint.get_width() // 2, 310))

        # Screen update karo
        pygame.display.flip()

        # 60 FPS speed maintain karo
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
