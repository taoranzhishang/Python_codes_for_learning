import pygame

# 800*600尺寸，0，
screen = pygame.display.set_mode((480, 800), 0, 32)  # 创建一个窗体，
# 载入文件图片到内存，
# bk=pygame.image.load(r"C:\Users\Tsinghua-yincheng\Desktop\day27down\code\images\background.png").convert()
bk = pygame.image.load(r"images\background.png").convert()  # 相对

while True:
    screen.blit(bk, (0, 0))  # w位置
    pygame.display.update()  # 消息循环，更新
