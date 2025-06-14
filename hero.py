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


class SuperHero2(SuperHero):
    sh='chekpuk'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage=damage
        self.fly=fly
    def hp(self):
        self.health_points **= 2
        self.fly =True
    def __str__(self):
        return f'fly in the True_phrase'
sh2=SuperHero2('jojo', 'fas', 'damage', 30, 'bla', 60,)
sh2.hp()
print(sh2.hp())


class SuperHero3(SuperHero2):
    sh='jelezchek'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.fly=fly
    def hp(self):
        self.health_points **= 2
        self.fly = True
    def __str__(self):
        return f'fly in the True_phrase'

sh3=SuperHero3('gad', 'gra', 'war', 40, 'gagagugu', 43)
sh3.hp()
print(sh3.hp())

class Villain(SuperHero3):
    people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        SuperHero3.__init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly)
    def gen_x(self):
        ...
    def crit(self):
        self.damage **= 2
        print(self.damage)
vil=Villain('huy', 'kui', 'very mad', 543, 'kui no huy if you kui', 535, False)
print(vil)
vil.crit()
# print(vil.damage)

