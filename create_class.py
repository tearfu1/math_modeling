class Ball:
    
    # Создадим атрибуты класса
    
    color  = "red"
    radius = 5
    
    def update_parameter(self):
        print('изменили цвет мячика')
        
    def move_ball(self, vx0=0):
        print(f'Мячик преобрел скорость {vx0}')
    
    # Экземпляры класса
    
ball_1 = Ball()
ball_2 = Ball()

print(type(ball_1))
ball_1.move_ball()

print(ball_2.color)

print(dir(ball_1))