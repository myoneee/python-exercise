#knife.py
from weapon import Weapon


class Knife(Weapon):
    def __init__(self, name, power, durability):
        super().__init__(name, power)
        self.durability = durability

    def attack(self):
        if self.durability < 1:
            print('공격 불가!')
            return
        else:
            super().attack()
            self.durability -= 1
            print('내구도 : %d' % self.durability)
