import pygame
pygame.init()

screen = pygame.display.set_mode((250, 200))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

FPS = 90
songNumber = 0
songsList = ['song.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3']
pygame.mixer.music.load(songsList[songNumber])
pygame.mixer.music.play()
font = pygame.font.Font(r'icons/font.ttf', 20)
stopImage = pygame.image.load(r'icons/pause.png')
playImage = pygame.image.load(r'icons/continue.png')
nextImage = pygame.image.load(r'icons/forward.png')
previousImage = pygame.image.load(r'icons/backward.png')
restartImage = pygame.image.load(r'icons/restart.png')
volUpImage = pygame.image.load(r'icons/volUp.png')
volDownImage = pygame.image.load(r'icons/volDown.png')
stopImageRect = stopImage.get_rect()
playImageRect = playImage.get_rect()
nextImageRect = nextImage.get_rect()
restartImageRect = restartImage.get_rect()
previousImageRect = previousImage.get_rect()
volUpImageRect = volUpImage.get_rect()
volDownImageRect = volDownImage.get_rect()
nextImageRect.x, nextImageRect.y = 200, 150
previousImageRect.x, previousImageRect.y = 10, 150
stopImageRect.x, stopImageRect.y, = 75, 150
playImageRect.x, playImageRect.y, = 135, 150
restartImageRect.x, restartImageRect.y = 5, 5
volUpImageRect.x, volUpImageRect.y, volDownImageRect.x, volDownImageRect.y = 200, 5, 200, 50

running = True
while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    songImage = font.render(songsList[songNumber], True, (200, 200, 200))
    screen.blit(songImage, ((15, 70)))
    screen.blit(stopImage, stopImageRect)
    screen.blit(playImage, playImageRect)
    screen.blit(nextImage, nextImageRect)
    screen.blit(previousImage, previousImageRect)
    screen.blit(restartImage, restartImageRect)
    screen.blit(volUpImage, volUpImageRect)
    screen.blit(volDownImage, volDownImageRect)
    pygame.draw.rect(screen, (200, 200, 200), playImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), stopImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), nextImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), previousImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), restartImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), volUpImageRect, 2)
    pygame.draw.rect(screen, (200, 200, 200), volDownImageRect, 2)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if stopImageRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.pause()
            elif playImageRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.unpause()
            elif nextImageRect.collidepoint(pygame.mouse.get_pos()):
                songNumber += 1
                if songNumber > len(songsList) - 1:
                    songNumber = 0
                pygame.mixer.music.load(songsList[songNumber])
                pygame.mixer.music.play()
            elif previousImageRect.collidepoint(pygame.mouse.get_pos()):
                songNumber -= 1
                if songNumber < 0:
                    songNumber = len(songsList) - 1
                pygame.mixer.music.load(songsList[songNumber])
                pygame.mixer.music.play()
            elif restartImageRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.play()
            elif volUpImageRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.set_volume(1)
            elif volDownImageRect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.set_volume(0.1)
pygame.quit()