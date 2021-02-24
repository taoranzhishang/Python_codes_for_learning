import pygame
import plane2.bluet


class jplane(pygame.sprite.Sprite):
    def __init__(self, planetype, bg_size, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.planetype = planetype
        if planetype == 1:
            self.image1 = pygame.image.load(r"..\images\enemy1.png").convert_alpha()
        elif planetype == 2:
            self.image1 = pygame.image.load(r"..\images\enemy2.png").convert_alpha()
        elif planetype == 3:
            self.image1 = pygame.image.load(r"..\images\enemy3_hit.png").convert_alpha()

        self.rect = self.image1.get_rect()  # 获取区域大小
        self.width = bg_size[0]
        self.height = bg_size[1]  # 区域大小
        self.rect.left = x  # 代表位置
        self.rect.top = y  # 代表位置
        self.speed = 10  # +10,-10
        self.screen = screen

        self.buletlist = []  # 子弹集合

        pass

    def moveup(self):
        if self.rect.top - 10 >= 0:
            self.rect.top -= 10

        pass

    def movedown(self):
        if self.rect.top + 10 <= 800:
            self.rect.top += 10
        pass

    def moveleft(self):
        if self.rect.left - 10 >= 0:
            self.rect.left -= 10
        pass

    def moveright(self):
        if self.rect.left + 10 <= 480:
            self.rect.left += 10
        pass

    def fire(self):
        if self.planetype == 1:
            for i in range(10):
                b1 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2, self.rect.top, self.screen, False)

                self.buletlist.append(b1)  # 加载子弹
        elif self.planetype == 2:
            for i in range(10):
                b1 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2, self.rect.top, self.screen, False)
                b2 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 + 20, self.rect.top, self.screen, False)
                b3 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 - 20, self.rect.top, self.screen, False)

                self.buletlist.append(b1)  # 加载子弹
                self.buletlist.append(b2)  # 加载子弹
                self.buletlist.append(b3)  # 加载子弹

        elif self.planetype == 3:
            for i in range(10):
                b1 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2, self.rect.top, self.screen, False)
                b2 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 + 20, self.rect.top, self.screen, False)
                b3 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 - 20, self.rect.top, self.screen, False)
                b4 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 + 40, self.rect.top, self.screen, False)
                b5 = plane2.bluet.Bullet((self.rect.left + self.rect.right) / 2 - 40, self.rect.top, self.screen, False)
                self.buletlist.append(b1)  # 加载子弹
                self.buletlist.append(b2)  # 加载子弹
                self.buletlist.append(b3)  # 加载子弹
                self.buletlist.append(b4)  # 加载子弹
                self.buletlist.append(b5)  # 加载子弹

        pass

    def show(self):
        self.screen.blit(self.image1, (self.rect.left, self.rect.top))
        for bt in self.buletlist:
            bt.show()
            bt.move()
        pass

    def reset(self):

        pass
