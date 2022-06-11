import pygame, speech, game
pygame.init()
pygame.display.set_mode((600,490))
pygame.display.set_caption('slide')
c=pygame.time.Clock()
g=game.Game()
g.initialize()

while 1:
    pygame.display.update()
    g.loop()
    g.didWin()

    for event in pygame.event.get():
        if event.type==quit:
            pygame.quit()
    c.tick(60)
