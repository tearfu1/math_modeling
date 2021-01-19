class Tomato:
    
    index = "мое Имя"
    states = {0 : "Отсутствует", 1 : "Цветение", 2 : "Зеленый", 3 : "Красный"}
    
    def __init__(self, index, states):
        
        self.states = states[0]
        self.index = index
    
    def grow(self):
        
        self.states += 1
        if self.states == 3:
            self.states = 3
    
    def is_ripe(self):
        
        if self.states == 3:
            return True
        else:
            return False
        
class TomatoBush:
    
    def __init__(self, tomatoes):
        
        self.tomatoes = []
        
        for i in range(self.tomatoes):
            self.tomatoes.appned(Tomato(i))
        
    def grow_all(self):
        
        for i in self.tomatoes:
            i.grow()
            
    def all_are_ripe(self):
        
        for i in self.tomatoes:
            if i.is_ripe() == False:
                return False
            return True
        
    def give_away_all(self):
        self.tomatoes = []
        
class Gardener:
    
    def __init__(self, name, bush):
        self.name = name
        self.bush = bush
        
    def work(self):
        self.bush.grow_all()
        
    def harvest(self):
        
        if self.bush.all_are_ripe == True:
            self.bush.give_away_all()
            print("молодец, все готовы")
        else:
            print("не все томаты готовы")
            
    def knowledge_base(self):
        print('123')

bush = TomatoBush(3)
gaga = Gardener("Ola", bush)
        
        