class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase

    def __str__(self):
        return (f'name is hero : {self.name}')

    def hp(self):
        self.health_points *= 2

    def __str__(self):
        return (
            f'nickname is {self.nickname};\n'
            f'superpower is {self.superpower};\n'
            f'hp is {self.health_points}\n'
        )

    def __len__(self):
        return len(self.catchphrase)

sh = SuperHero("lojibar", "bony", "fly", 50, "Focusing on yourself is an investment in the future.")

sh.hp()
print(sh, sh.__len__())