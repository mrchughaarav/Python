import pygame

pygame.init()

# Step 3: Create the display window
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Facts")

# Step 4: Load and scale the images
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (500, 500))

tiger = pygame.image.load("tiger.png")
tiger = pygame.transform.scale(tiger, (200, 150))

# Step 5: Position the tiger
tiger_rect = tiger.get_rect(center=(250, 250))

# Step 6: Create the text
heading_font = pygame.font.Font(None, 40)
fact_font = pygame.font.Font(None, 25)

heading = heading_font.render("TIGERS", True, (255, 255, 255))
fact = fact_font.render("Tigers are the largest wild cats.", True, (255, 255, 255))

heading_rect = heading.get_rect(center=(250, 50))
fact_rect = fact.get_rect(center=(250, 450))

# Step 7: Create the game loop
def game_loop():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Step 8: Draw everything
        screen.blit(background, (0, 0))
        screen.blit(tiger, tiger_rect)
        screen.blit(heading, heading_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()

        # Step 9: Limit to 30 FPS
        clock.tick(30)

    pygame.quit()


# Step 10: Run the application
game_loop()