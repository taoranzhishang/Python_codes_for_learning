import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, ismy):
        pygame.sprite.Sprite.__init__(self)
        self.ismy = ismy
        if ismy:
            self.image1 = pygame.image.load(r"..\images\bullet1.png").convert_alpha()
        else:
            self.image1 = pygame.image.load(r"..\images\bullet2.png").convert_alpha()

        self.rect = self.image1.get_rect()  # 子弹
        self.rect.left = x
        self.rect.top = y
        self.speed = 1
        self.screen = screen  # 屏幕

    def move(self):
        if self.ismy:
            self.rect.top -= self.speed
        else:
            self.rect.top += self.speed

        pass

    def show(self):
        self.screen.blit(self.image1, (self.rect.left, self.rect.top))
