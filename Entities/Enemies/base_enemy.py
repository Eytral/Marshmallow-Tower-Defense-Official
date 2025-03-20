from Constants import sprites, config
import copy
import pygame

class Enemy():
    def __init__(self, game, start_position, reward=5, health=10, speed=2):
        self.reward = reward
        self.max_health = health
        self.damage = self.max_health//2
        self.speed = speed

        self.position = copy.deepcopy(start_position)
        self.grid_position = (copy.deepcopy(start_position[0])//config.GRID_CELL_SIZE, copy.deepcopy(start_position[1])//config.GRID_CELL_SIZE)
        self.width, self.height = config.GRID_CELL_SIZE, config.GRID_CELL_SIZE
        self.hitbox = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

        self.health = self.max_health
        self.is_dead = False
        self.reached_end = False
        self.sprite = sprites.ENEMY_DEFAULT_SPRITE

        self.game = game

    def move(self):
        for _ in range(self.speed):
            # logic for movement
            self.grid_position = self.position[0]//config.GRID_CELL_SIZE, self.position[1]//config.GRID_CELL_SIZE
            self.hitbox = pygame.Rect(self.position[0], self.position[1], config.GRID_CELL_SIZE, config.GRID_CELL_SIZE)

    def draw(self, screen):
        screen.blit(self.sprite, (self.position))

    def take_damage(self, damage, **kwargs):
        print(f"Enemy taken {damage} damage")
        self.health -= damage

    def check_is_dead(self):
        if self.health <= 0:
            self.die()

    def die(self):
        self.is_dead = True
        print(f"Enemy has reached end (of its life)")

    def update(self):
        self.move()
        self.check_is_dead()
        self.check_has_reached_end()

        