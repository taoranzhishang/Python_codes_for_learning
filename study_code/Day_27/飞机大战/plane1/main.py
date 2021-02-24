import pygame
import pygame.midi
import pygame.locals
import plane1.myplane
import time

pygame.init()  # 初始化
pygame.mixer.init()  # 初始化，用于播放音域
bg_size = width, height = 480, 800  # 窗体大小
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("高清华打飞机")

bk = pygame.image.load(r"..\images\background.png").convert()

pygame.mixer.music.load(r"..\sound\game_music.ogg")  # 播放音乐
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

myp = plane1.myplane.myplane(bg_size)  # 创建了飞机对象

while True:
    screen.blit(bk, (0, 0))  # w位置

    for event in pygame.event.get():  # 抓取每一个事件
        if event.type == pygame.locals.QUIT:  # 关闭
            print("exit")
            exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_k:
                for myimage in myp.destroy_images:
                    screen.blit(myimage, (10, 10))
                    time.sleep(0.3)

    pygame.display.update()  # 消息循环，更新
