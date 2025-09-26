import turtle
import math

# Настройка окна
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Анимированное сердечко")
screen.setup(800, 600)

# Создание черепашки
heart = turtle.Turtle()
heart.speed(0)
heart.color("red")
heart.pensize(2)

# Функция для рисования сердца с математической формулой
def draw_heart_parametric():
    heart.penup()
    
    # Устанавливаем начальную точку
    t = 0
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    
    heart.goto(x * 10, y * 10)  # Масштабируем
    heart.pendown()
    
    heart.begin_fill()
    
    # Рисуем сердце по параметрическим уравнениям
    for angle in range(0, 360, 2):
        t = math.radians(angle)
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        heart.goto(x * 10, y * 10)
    
    heart.end_fill()

# Функция для анимации пульсации
def pulse():
    sizes = [1.0, 1.1, 1.0, 0.9, 1.0]
    
    for size in sizes:
        heart.clear()
        heart.penup()
        heart.goto(0, 0)
        
        # Рисуем сердце с разным размером
        t = 0
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        
        heart.goto(x * 10 * size, y * 10 * size)
        heart.pendown()
        
        heart.begin_fill()
        
        for angle in range(0, 360, 2):
            t = math.radians(angle)
            x = 16 * (math.sin(t) ** 3)
            y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
            heart.goto(x * 10 * size, y * 10 * size)
        
        heart.end_fill()
        
        # Небольшая пауза
        turtle.delay(100)

# Рисуем сердце
draw_heart_parametric()

# Добавляем текст
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, -200)
text.write("Я тебя люблю!", align="center", font=("Arial", 20, "bold"))

# Скрываем черепашку
heart.hideturtle()

# Анимация пульсации (раскомментируйте для включения)
# pulse()

# Завершение программы по клику
screen.exitonclick()