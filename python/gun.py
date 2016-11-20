from __future__ import print_function
from driver import GUN


CENTER = 74
HALF_RANGE = 60


class Gun:
    def __init__(self, driver):
        self.pos = 0
        self.sweep_dir = 1
        self.driver = driver

    def sweep(self, speed):
        """Sweep the gun back and forth at a given speed."""
        if self.pos <= -HALF_RANGE or HALF_RANGE <= self.pos:
            self.sweep_dir *= -1
        self.pos += speed * self.sweep_dir
        self.driver.face(GUN, CENTER + self.pos)

    def shoot(self, angle):
        """Shoot the gun at a specific target."""
        self.driver.shoot_at(CENTER + angle)

    def face(self, angle):
        self.driver.face(GUN, CENTER + angle)
