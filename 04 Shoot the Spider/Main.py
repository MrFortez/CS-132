import os
from Constants import *
import pygame    
from Player import Player
from Enemy import Enemy
from Projectile import Projectile
import Globals


# pygame mixer init
pygame.mixer.init()

# pygame init
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
background = pygame.transform.scale(pygame.image.load(os.path.join("images", "Space3.png")), (WIDTH, HEIGHT))

# Set up the characters
kirby = Player(10, "Kirby", (60, 75), os.path.join("images", "Kirby.png"))
nightmare = Enemy(100, "Nightmare", (100, 100), os.path.join("images", "Nightmare.png"))

# Set up music
pygame.mixer.music.load(os.path.join("Sound", "Music", "It Has to Be This Way.ogg"))
pygame.mixer.music.play(loops=-1)

# Add to sprite groups
Globals.players.add(kirby)
Globals.enemies.add(nightmare)
         
# To be used once either player or enemy reaches zero health
ENDING = False

# Run until the user asks to quit
RUNNING = True
while RUNNING:

    # Update Global Timer
    Globals.globalTime = pygame.time.get_ticks()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    kirby.update(pressedKeys)
    nightmare.update(pressedKeys)
    Globals.playerProjectiles.update(pressedKeys)
    Globals.enemyProjectiles.update(pressedKeys)

    # Blit Characters to screen
    screen.blit(background, (0, 0))
    screen.blit(nightmare.surf, nightmare.rect)
    for sprite in Globals.playerProjectiles: 
        screen.blit(sprite.surf, sprite.rect)
    
    for sprite in Globals.enemyProjectiles:
        screen.blit(sprite.surf, sprite.rect)

    if (not (kirby.isInvincible and Globals.globalTime % 2 == 0)):
        screen.blit(kirby.surf, kirby.rect)

    # Draw Health Bars
    nightmare.healthbar.draw(screen)
    kirby.healthbar.draw(screen)

    # UNCOMMENT THESE TO SEE HITBOXES
    # pygame.draw.rect(screen, RED, kirby.collisionRect)
    # pygame.draw.rect(screen, RED, nightmare.collisionRect)

    # Flip the display
    pygame.display.flip()

    if (kirby.health == 0):
        pygame.mixer.music.load(os.path.join("Sound", "SFX", "Death Sound Effect.mp3"))
        pygame.mixer.music.play(loops=1)
        RUNNING = False
        ENDING = True

    if (nightmare.health == 0):
        pygame.mixer.music.load(os.path.join("Sound", "Music", "Victory Dance.mp3"))
        pygame.mixer.music.play(loops=1)
        RUNNING = False
        ENDING = True

    # Ensure program maintains a rate of 30 frames per second
    Globals.clock.tick(120)


while (ENDING):
    if (kirby.health == 0):
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                ENDING = False
            if event.type == pygame.QUIT:
                ENDING = False

        font = pygame.font.Font(None, 80)  # None specifies default font, 36 is the font size

        # Render text surface
        text = font.render("You Lose :(", True, BLACK)
        textBackground = pygame.Surface((300, 200))
        textBackground.fill(WHITE)

        # Get the rectangle containing the text surface
        textRect = text.get_rect()
        textBackgroundRect = textBackground.get_rect()

        # Center the text on the screen
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        textBackgroundRect.center = (WIDTH // 2, HEIGHT // 2)

        # Draw the text surface onto the screen
        screen.blit(textBackground, textBackgroundRect)
        screen.blit(text, textRect)
   

        pygame.display.flip()

    if (nightmare.health == 0):
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                ENDING = False
            if event.type == pygame.QUIT:
                ENDING = False

        font = pygame.font.Font(None, 80)  # None specifies default font, 36 is the font size

        # Render text surface
        text = font.render("You Win :)", True, BLACK)
        textBackground = pygame.Surface((300, 200))
        textBackground.fill(WHITE)

        # Get the rectangle containing the text surface
        textRect = text.get_rect()
        textBackgroundRect = textBackground.get_rect()

        # Center the text on the screen
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        textBackgroundRect.center = (WIDTH // 2, HEIGHT // 2)

        # Draw the text surface onto the screen
        screen.blit(textBackground, textBackgroundRect)
        screen.blit(text, textRect)
  

        pygame.display.flip()


# Done! Time to quit.
pygame.quit() 