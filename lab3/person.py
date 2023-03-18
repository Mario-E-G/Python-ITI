class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self._mood = "Happy"
        self._healthRate = 100

    def sleep(self,hours):
        if hours == 7:
            self._mood = "Happy"
        elif hours < 7:
            self._mood = "Tired"
        else:
            self._mood = "Lazy"

    def eat(self,meals):
        if meals == 3:
            self._healthRate = "100%"
        elif meals == 2:
            self._healthRate = "75%"
        else:
            self._healthRate = "50%"

    def buy(self,items):
        if self.money >= 10:
            self.money -= 10 * items

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self,mood):
        if mood < 1000:
            self._mood = 1000
        else:
            self._mood = mood

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def mood(self, healthRate):
        if healthRate < 0 and healthRate>100:
            self._healthRate = 0
        else:
            self._healthRate = healthRate

