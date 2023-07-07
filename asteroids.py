import pygame
import math
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Load images
ship_img = pygame.image.load("ship.png")
asteroid_img = pygame.image.load("asteroid.png")
logo_img = pygame.image.load("logo.png")
logo_rect = logo_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))

# Ship properties
ship_x, ship_y = WIDTH // 2, HEIGHT // 2
ship_angle = 0
speed = 5
turn_speed = 5

# Asteroids properties
asteroids = []
asteroid_speed = 2

# Scale factors for asteroids
scale_factors = [0.95, 0.9, 0.85, 0.8]

# Shimmer properties
shimmer_color = (0, 128, 128, 100)  # Teal with alpha
shimmer_thickness = 10

# Bullet properties
bullets = []
bullet_speed = 10
bullet_radius = 5
bullet_color = (255, 0, 0)
bullet_timer = 0
bullet_visibility_toggle = 3

# Particles
particles = [(random.random() * WIDTH, random.random() * HEIGHT) for _ in range(100)]

# Menu properties
pygame.font.init()
custom_font = pygame.font.Font(None, 24)
game_started = False

# Health bar properties
health = 100
healthbar_width = 200
healthbar_height = 20
healthbar_border_width = 2
healthbar_border_color = (255, 255, 255)
healthbar_inner_color = (0, 255, 0)
healthbar_x = WIDTH - healthbar_width - 10
healthbar_y = 10

# High score properties
high_score = 0
score = 0
score_x = 10
score_y = 10

# Game over properties
game_over = False
game_over_text = custom_font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Main loop
running = True
frame_count = 0
while running:
    # Menu section
    while running and not game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_started = True
                if event.key == pygame.K_q:
                    running = False

        # Clear the screen
        win.fill((0, 0, 0))

        # Draw the logo
        win.blit(logo_img, logo_rect.topleft)

        # Draw instructions
        instructions_surface = custom_font.render("Press P to Play | Press Q to Quit", True, (255, 255, 255))
        instructions_rect = instructions_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        win.blit(instructions_surface, instructions_rect.topleft)

        # Update the screen
        pygame.display.flip()

    # Handle keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_angle += turn_speed
    if keys[pygame.K_RIGHT]:
        ship_angle -= turn_speed
    if keys[pygame.K_UP]:
        ship_x += math.cos(math.radians(ship_angle)) * speed
        ship_y -= math.sin(math.radians(ship_angle)) * speed
        moving = True
    else:
        moving = False

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_angle += turn_speed
            if event.key == pygame.K_RIGHT:
                ship_angle -= turn_speed
            if event.key == pygame.K_UP:
                ship_x += math.cos(math.radians(ship_angle)) * speed
                ship_y -= math.sin(math.radians(ship_angle)) * speed
                moving = True
            if event.key == pygame.K_SPACE and frame_count >= bullet_timer:
                bullet_x = ship_x + math.cos(math.radians(ship_angle)) * (ship_img.get_width() / 2)
                bullet_y = ship_y - math.sin(math.radians(ship_angle)) * (ship_img.get_height() / 2)
                bullets.append((bullet_x, bullet_y, ship_angle))
                bullet_timer = frame_count + bullet_visibility_toggle



    # Screen wrapping for ship
    ship_x = (ship_x + WIDTH) % WIDTH
    ship_y = (ship_y + HEIGHT) % HEIGHT

    # Clear the screen
    win.fill((0, 0, 0))

    # Draw particles
    for px, py in particles:
        win.set_at((int(px), int(py)), (255, 255, 255))
        px = (px + 0.5) % WIDTH
        py = (py + 0.5) % HEIGHT

    # Draw and update ship
    rotated_ship = pygame.transform.rotate(ship_img, ship_angle)
    rect = rotated_ship.get_rect(center=(ship_x, ship_y))
    win.blit(rotated_ship, rect.topleft)

    # Spawn asteroids
    if random.random() < 0.01:
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        dx, dy = random.random() * 2 - 1, random.random() * 2 - 1
        scale = random.choice(scale_factors)
        asteroids.append((x, y, dx, dy, scale))

    # Draw and update asteroids
    for i, (x, y, dx, dy, scale) in enumerate(asteroids):
        x += dx * asteroid_speed
        y += dy * asteroid_speed

        # Screen wrapping for asteroids
        x = (x + WIDTH) % WIDTH
        y = (y + HEIGHT) % HEIGHT

        # Update the asteroid's position
        asteroids[i] = (x, y, dx, dy, scale)

        # Draw the asteroid
        scaled_asteroid = pygame.transform.scale(asteroid_img, (int(asteroid_img.get_width() * scale), int(asteroid_img.get_height() * scale)))
        win.blit(scaled_asteroid, (x, y))

    # Create a list to store bullets that need to be removed
    bullets_to_remove = []

    # Draw and update bullets
    for i, (x, y, angle) in enumerate(bullets):
        dx = math.cos(math.radians(angle)) * bullet_speed
        dy = -math.sin(math.radians(angle)) * bullet_speed
        if moving:
            dx += math.cos(math.radians(ship_angle)) * speed
            dy -= math.sin(math.radians(ship_angle)) * speed

        x += dx
        y += dy

        # Remove bullets that leave the screen
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            bullets_to_remove.append(i)
        # Update the bullet's position
        bullets[i] = (x, y, angle)

        # Draw the bullet
        pygame.draw.circle(win, bullet_color, (int(x), int(y)), bullet_radius)


        # Collision detection between bullets and asteroids
        for a_index, (ax, ay, adx, ady, ascale) in enumerate(asteroids):
            scaled_asteroid_width = asteroid_img.get_width() * ascale
            scaled_asteroid_height = asteroid_img.get_height() * ascale
            for b_index, (bx, by, angle) in enumerate(bullets):
                if ax < bx < ax + scaled_asteroid_width and ay < by < ay + scaled_asteroid_height:
                    # Split the asteroid into two smaller ones
                    new_scale = ascale * 0.5
                    if new_scale > 0.1:  # Only split if the new asteroids won't be too small
                        asteroids.append((ax, ay, adx * 0.7, ady + 1, new_scale))  # To the "west"
                        asteroids.append((ax, ay, adx * 0.7, ady - 1, new_scale))  # To the "east"

                    # Remove the original asteroid
                    asteroids.pop(a_index)

                    # Remove the bullet
                    bullets.pop(b_index)

                    # Update the score
                    score += 1
                    break
            else:
                continue
            break


            # Remove the original asteroid
            asteroids.pop(a_index)

            # Remove the bullet
            bullets.pop(b_index)

            # Update the score
            score += 1
            break


    # Remove bullets that need to be removed
    for index in bullets_to_remove:
        bullets.pop(index)

    # Draw teal shimmer around border
    s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(s, shimmer_color, (0, 0, WIDTH, shimmer_thickness))
    pygame.draw.rect(s, shimmer_color, (0, 0, shimmer_thickness, HEIGHT))
    pygame.draw.rect(s, shimmer_color, (0, HEIGHT - shimmer_thickness, WIDTH, shimmer_thickness))
    pygame.draw.rect(s, shimmer_color, (WIDTH - shimmer_thickness, 0, shimmer_thickness, HEIGHT))
    win.blit(s, (0, 0))

    # Draw health bar
    pygame.draw.rect(win, healthbar_border_color, (healthbar_x, healthbar_y, healthbar_width, healthbar_height), healthbar_border_width)
    pygame.draw.rect(win, healthbar_inner_color, (healthbar_x, healthbar_y, healthbar_width * health / 100, healthbar_height))

    # Draw high score
    high_score_text = custom_font.render("High Score: " + str(high_score), True, (255, 255, 255))
    win.blit(high_score_text, (score_x, score_y))

    # Draw score
    score_text = custom_font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(score_text, (score_x, score_y + 30))

    # Check game over condition
    if health <= 0:
        game_over = True

    # Game over logic
    if game_over:
        win.blit(game_over_text, game_over_rect.topleft)

        # Reset game if 'P' is pressed
        if keys[pygame.K_p]:
            game_over = False
            score = 0
            health = 100
            bullets.clear()
            asteroids.clear()

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # Increment the frame count
    frame_count += 1

# Quit pygame
pygame.quit()  # End pygame
