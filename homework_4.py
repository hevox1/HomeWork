class One:
    def __init__(self, name):
        self.name=name

class Two:
    def __init__(self, age):
        self.age=age

class Three(One):
    def hel(self):
        return print(f'hello {self.name}')

class Four(Two):
    def rejuvenation(self):
        return print(self.age - 1)

class Five(One, Two):
    def __init__(self, name, age):
        One.__init__(self, name)
        Two.__init__(self, age)
        self._name=Three(name)
        self._age=Four(age)

    def hel(self):
        return self._name.hel()

    def rejuvenation(self):
        return self._age.rejuvenation()

    def __len__(self):
        return len(self.name)

o=One('dima')
t=Two(16)
th=Three(o.name)
f=Four(t.age)
fi=Five(o.name, t.age)

fi.hel()
fi.rejuvenation()
print(len(fi))


