import pygame
import pygame.locals

# 800*600尺寸，0，
screen = pygame.display.set_mode((480, 800), 0, 32)  # 创建一个窗体，
# 载入文件图片到内存，
# bk=pygame.image.load(r"C:\Users\Tsinghua-yincheng\Desktop\day27down\code\images\background.png").convert()
bk = pygame.image.load(r"images\background.png").convert()  # 相对路径
plane = pygame.image.load(r"images\me1.png").convert_alpha()  # 相对路径

x = 0
y = 0

while True:
    screen.blit(bk, (0, 0))  # w位置
    screen.blit(plane, (x, y))  # w位置
    for event in pygame.event.get():  # 抓取每一个事件
        if event.type == pygame.locals.QUIT:  # 关闭
            print("exit")
            exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_w:
                print("w")
                if y - 10 >= 0:
                    y -= 10
            elif event.key == pygame.locals.K_s:
                if y + 10 <= 800:
                    y += 10
            elif event.key == pygame.locals.K_a:
                print("a")
                if x - 10 >= 0:
                    x -= 10
            elif event.key == pygame.locals.K_d:
                if x + 10 <= 480:
                    x += 10

    pygame.display.update()  # 消息循环，更新
