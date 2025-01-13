class Character:
    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def output_data(self):
        return f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\n"


class Player(Character):
    def __init__(self, name, health, magic_points, lives):
        super().__init__(name, health, magic_points)
        self.lives = lives

    def am_i_alive(self):
        return "Yes" if self.lives > 0 and self.health > 0 else "No"

    def output_data(self):
        return super().output_data() + f"Lives: {self.lives}\nAlive?: {self.am_i_alive()}\n"


class Enemy(Character):
    def __init__(self, name, health, magic_points, enemy_type, strength):
        super().__init__(name, health, magic_points)
        self.enemy_type = enemy_type
        self.strength = strength 

    def output_data(self):
        return super().output_data() + f"Type: {self.enemy_type}\nStrength: {self.strength}\n"


class Orc(Enemy):
    def __init__(self, name, health, magic_points, strength, speed):
        super().__init__(name, health, magic_points, "Orc", strength)
        self.speed = speed

    def output_data(self):
        return super().output_data() + f"Speed: {self.speed}\n"


class Vampire(Enemy):
    def __init__(self, name, health, magic_points, strength, day_night):
        super().__init__(name, health, magic_points, "Vampire", strength)
        self.day_night = day_night

    def output_data(self):
        return super().output_data() + f"Day/Night?: {self.day_night}\n"


player1 = Player("David", 100, 50, 3)
vampire1 = Vampire("Boris", 45, 70, 3, "Night")
vampire2 = Vampire("Rishi", 70, 10, 75, "Day")
orc1 = Orc("Bill", 60, 5, 75, 90)
orc2 = Orc("Ted", 75, 40, 80, 45)
orc3 = Orc("Station", 35, 40, 49, 50)

characters = [player1, vampire1, vampire2, orc1, orc2, orc3]

print("🌟Generic RPG🌟")
for character in characters:
    print(character.output_data())