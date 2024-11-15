import random
class man:
    def __init__(self, name):
        self.name = name
        self.height = 180
        self.satiety = 100
        self.rozum = 100
        self.gladness = 100
        self.__money = 100
    def to_sleep(self):
        print('Спати хочу')
        self.gladness += 10
        self.satiety -= 15
        self.rozum -= 10

    def to_eat(self):
        print('Їсти хочу')
        self.gladness += 10
        self.satiety += 10
        self.rozum -= 3
    def to__workcplusplus(self):
        print('Вмерти хочу')
        self.rozum += 30
        self.satiety -= 20
        self.gladness -= 30
        self.__money += 10000

    def live(self,day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        a = random.randint(1,3)
        if a == 1:
            self.to_eat()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"money = {round(self.__money)}")
        if a == 2:
            self.to_sleep()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"money = {round(self.__money)}")
        if a == 3:
            self.to__workcplusplus()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"money = {round(self.__money)}")

class woman(man):
    def __init__(self,name):
        self.anlack = 0
        self.name = name
        super().__init__(name)
    def to_sleep(self):
        super().to_sleep()
    def to_eat(self):
        super().to_eat()
    def to_hotiti(self):
        print('Хочу айфон')
        self.gladness -= 20
        self.rozum -= 20
        self.anlack += 20
    def live(self,day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        a = random.randint(1,3)
        if a == 1:
            self.to_eat()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Анлачіще ну як так можна = {round(self.anlack)}")
        if a == 2:
            self.to_sleep()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Анлачіще ну як так можна = {round(self.anlack)}")
        if a == 3:
            self.to_hotiti()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Анлачіще ну як так можна = {round(self.anlack)}")
class child(man):
    def __init__(self,name):
        self.degradation = 10
        self.name = name
        super().__init__(name)
    def to_eat(self):
        super().to_eat()
    def to_sleep(self):
        super().to_eat()
    def to_play(self):
        print('гратись хочу')
        self.gladness += 10
        self.rozum += 15
        self.satiety -= 10
        self.degradation += 5

    def live(self,day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        a = random.randint(1,3)
        if a == 1:
            self.to_eat()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Деградація = {round(self.degradation)}")
        if a == 2:
            self.to_sleep()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Деградація = {round(self.degradation)}")
        if a == 3:
            self.to_play()
            print(f"Gladness = {self.gladness}")
            print(f"Ситість = {round(self.satiety, 2)}")
            print(f"Mind = {round(self.rozum)}")
            print(f"Деградація = {round(self.degradation)}")

Ivan = man(name='Ivan')
Vika = woman(name='Vika')
Nazar = child(name='Nazar')
for day in range(8):
    Ivan.live(day)
    Nazar.live(day)
    Vika.live(day)