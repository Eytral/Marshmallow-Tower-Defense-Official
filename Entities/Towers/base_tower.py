from Constants import config, sprites
from Entities.bullet import Bullet
from abc import ABC, abstractmethod

class Tower(ABC):
    def __init__(self, x_grid_pos, y_grid_pos, range=5, fire_rate=30, bullet_speed=10, bullet_damage=2, cost=10):
        self.sprite = sprites.TOWER_DEFAULT_SPRITE
        self.x_grid_pos = x_grid_pos
        self.y_grid_pos = y_grid_pos

        self.x_pos = x_grid_pos * config.GRID_CELL_SIZE
        self.y_pos = y_grid_pos * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT
    
        self.shoot_cooldown = 0
        self.target = None

        self.range = range
        self.fire_rate = fire_rate
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage

        self.bullets = []

        self.cost = cost

    def draw(self, screen):
        screen.blit(self.sprite, (self.x_pos, self.y_pos))
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot(self):
        self.bullets.append(Bullet(self.x_pos, self.y_pos, self.target, self.bullet_speed, self.bullet_damage))
        self.shoot_cooldown = self.fire_rate

    def in_range(self, enemy):
        """Checks if an enemy is within the tower's attack range in grid tiles."""

        return abs(enemy.grid_position[0] - self.x_grid_pos) <= self.range and abs(enemy.grid_position[1] - self.y_grid_pos) <= self.range

    def get_target(self, enemies):
        """Finds the first enemy in range."""
        for enemy in enemies:
            if self.in_range(enemy):
                return enemy
        return None

    def update(self, enemies):
        if self.target == None or self.target.is_dead or self.target.reached_end or not self.in_range(self.target):
            self.target = self.get_target(enemies)
        if self.shoot_cooldown <= 0:
            if self.target != None:
                print("Shooting enemy")
                self.shoot()
        else:
            self.shoot_cooldown -= 1
        self.bullets = [bullet for bullet in self.bullets if bullet.active]
        
        for bullet in self.bullets:
            bullet.update()

    @abstractmethod
    def upgrade(self):
        # upgrade logic
        pass