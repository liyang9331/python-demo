import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口大小
window_width = 480
window_height = 600
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('飞机大战')

# 设置游戏字体
font = pygame.font.SysFont(None, 25)

# 加载游戏素材
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
bullet_img = pygame.image.load('bullet.png')

# 设置游戏颜色
white = (255, 255, 255)

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义游戏角色类


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

# 定义玩家角色类


class Player(GameSprite):
    def __init__(self, img, x, y, speed):
        super().__init__(img, x, y, speed)
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        # 玩家边界检测
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > window_width:
            self.rect.right = window_width

    def shoot(self):
        bullet = Bullet(bullet_img, self.rect.centerx, self.rect.top, -10)
        self.bullets.add(bullet)

# 定义敌人角色类


class Enemy(GameSprite):
    def __init__(self, img, x, y, speed):
        super().__init__(img, x, y, speed)
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction

        # 敌人边界检测
        if self.rect.left < 0 or self.rect.right > window_width:
            self.direction *= -1
            self.rect.y += self.rect.height

# 定义子弹角色类


class Bullet(GameSprite):
    def __init__(self, img, x, y, speed):
        super().__init__(img, x, y, speed)

    def update(self):
        self.rect.y += self.speed


# 创建游戏角色
player = Player(player_img, window_width // 2, window_height - 50, 0)
enemies = pygame.sprite.Group()

# 创建敌人角色
for i in range(10):
    enemy = Enemy(enemy_img, random.randint(
        0, window_width - 50), random.randint(-500, -50), 5)
    enemies.add(enemy)

# 开始游戏循环
game_over = False
while not game_over:
    # 处理游戏事件
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.speed = -5
        elif event.key == pygame.K_RIGHT:
            player.speed = 5
        elif event.key == pygame.K_SPACE:
            player.shoot()
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player.speed = 0

# 更新游戏角色
player.update()
player.bullets.update()
enemies.update()

# 检测子弹是否打中敌人
for bullet in player.bullets:
    enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
    for enemy in enemies_hit:
        player.bullets.remove(bullet)

# 检测敌人是否撞到玩家
enemies_hit = pygame.sprite.spritecollide(player, enemies, False)
if enemies_hit:
    game_over = True

# 绘制游戏画面
game_display.fill(white)
game_display.blit(player.image, player.rect)
for bullet in player.bullets:
    game_display.blit(bullet.image, bullet.rect)
for enemy in enemies:
    game_display.blit(enemy.image, enemy.rect)
pygame.display.update()

# 控制游戏帧率
clock.tick(60)
