import pygame
import pygame.midi
import pygame.locals
import plane2.selfplane
import plane2.japanplane
import time


class Mainclass():
    def __init__(self, title):
        pygame.init()  # 初始化
        pygame.mixer.init()  # 初始化，用于播放音域
        self.bg_size = width, height = 480, 800  # 窗体大小
        self.screen = pygame.display.set_mode(self.bg_size)
        pygame.display.set_caption(title)

        self.高清华 = plane2.selfplane.myplane(self.bg_size, 0, 600, self.screen)
        self.何丰成 = plane2.selfplane.myplane(self.bg_size, 150, 600, self.screen)

        self.鬼子 = plane2.japanplane.jplane(1, self.bg_size, 0, 0, self.screen)

        # 背景
        self.bk = pygame.image.load(r"..\images\background.png").convert()
        # 音乐
        pygame.mixer.music.load(r"..\sound\game_music.ogg")  # 播放音乐
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        pass

    def go(self):
        while True:
            self.screen.blit(self.bk, (0, 0))  # w位置
            self.高清华.show()
            self.何丰成.show()
            self.鬼子.show()
            for event in pygame.event.get():  # 抓取每一个事件
                if event.type == pygame.locals.QUIT:  # 关闭
                    print("exit")
                    exit()
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_w:
                        self.高清华.moveup()
                        self.何丰成.moveup()
                        print("w")
                    elif event.key == pygame.locals.K_s:
                        self.高清华.movedown()
                        self.何丰成.movedown()
                        print("s")
                    elif event.key == pygame.locals.K_a:
                        self.高清华.moveleft()
                        self.何丰成.moveleft()
                        print("a")
                    elif event.key == pygame.locals.K_d:
                        self.高清华.moveright()
                        self.何丰成.moveright()
                        print("d")
                    elif event.key == pygame.locals.K_SPACE:
                        self.高清华.fire()
                        self.何丰成.fire()
                        self.鬼子.fire()
                        print("space")

            pygame.display.update()  # 消息循环，更新


main = Mainclass("高清华与何丰成一起打飞机")
main.go()
