import pygame


class myplane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 载入资源图片
        self.image1 = pygame.image.load(r"..\images\me1.png").convert_alpha()
        self.image2 = pygame.image.load(r"..\images\me2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.append(pygame.image.load(r"..\images\me_destroy_1.png").convert_alpha())
        self.destroy_images.append(pygame.image.load(r"..\images\me_destroy_2.png").convert_alpha())
        self.destroy_images.append(pygame.image.load(r"..\images\me_destroy_3.png").convert_alpha())
        self.destroy_images.append(pygame.image.load(r"..\images\me_destroy_4.png").convert_alpha())

        self.rect = self.image1.get_rect()  # 获取区域大小

        pass

    def moveup(self):
        pass

    def movedown(self):
        pass

    def moveleft(self):
        pass

    def moveright(self):
        pass

    def reset(self):
        pass
