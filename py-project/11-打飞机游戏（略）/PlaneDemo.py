import pygame
from pygame.locals import *


def main():
    # 首先创建一个窗口
    screen = pygame.display.set_mode((350, 500))

    # 设置背景图片
    background = pygame.image.load('./11-打飞机游戏/resources/background.jpg')

    # 设置一个标题
    pygame.display.set_caption("打飞机游戏")

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./11-打飞机游戏/resources/bgm.mp3')
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)  # -1表示无限循环

    # 添加玩家图片

    while True:
        # 显示背景图片，居中显示
        screen.blit(background, (0, 0))
        # 获取键盘事件
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == QUIT:
                print("退出")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:  # 如果是左键
                    print("left")
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                elif event.key == K_SPACE:
                    print("space")
        # 更新显示内容
        pygame.display.update()


if __name__ == '__main__':
    main()
