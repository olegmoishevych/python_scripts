# import turtle
#
# # Настройки черепашки
# screen = turtle.Screen()
# turtle.shape('turtle')
# turtle.speed(1)
#
# # Флаг для начала заполнения фигуры
# is_drawing = False
#
# # Функции движения
# def move_forward():
#   global is_drawing
#   print("Moving forward")
#   if not is_drawing:
#     turtle.begin_fill()
#     is_drawing = True
#   turtle.forward(10)
#
# def move_backward():
#   global is_drawing
#   print("Moving backward")
#   if not is_drawing:
#     turtle.begin_fill()
#     is_drawing = True
#   turtle.backward(10)
#
# def turn_left():
#   print("Turning left")
#   turtle.left(90)
#
# def turn_right():
#   print("Turning right")
#   turtle.right(90)
#
# def end_drawing():
#   global is_drawing
#   print("Ending drawing")
#   if is_drawing:
#     turtle.end_fill()
#     is_drawing = False
#     turtle.clear()
#
# # Добавление горячих клавиш
# screen.listen()
# screen.onkeypress(move_forward, 'w')
# screen.onkeypress(move_backward, 's')
# screen.onkeypress(turn_left, 'a')
# screen.onkeypress(turn_right, 'd')
# screen.onkeypress(end_drawing, 'e')  # Нажмите 'e' для завершения фигуры и удаления
#
# # Запуск окна черепашки
# turtle.mainloop()
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Настройки экрана
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Голова змеи
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Еда змеи
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Показание счета
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Функции управления
def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def go_right():
  if head.direction != "left":
    head.direction = "right"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

# Связывание клавиш с функциями управления
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Основной игровой цикл
try:
  while True:
    screen.update()

    # Проверка на столкновение с границей экрана
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = "stop"

      # Скрыть сегменты тела
      for segment in segments:
        segment.goto(1000, 1000)

      # Очистить список сегментов
      segments.clear()

      # Сбросить счет
      score = 0
      pen.clear()
      pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Проверка на столкновение с едой
    if head.distance(food) < 20:
      # Переместить еду в случайное место
      x = random.randint(-290, 290)
      y = random.randint(-290, 290)
      food.goto(x, y)

      # Добавить сегмент к телу змеи
      new_segment = turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("square")
      new_segment.color("grey")
      new_segment.penup()
      segments.append(new_segment)

      # Увеличить счет
      score += 10

      if score > high_score:
        high_score = score

      pen.clear()
      pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Перемещение конца змеи в обратном порядке
    for index in range(len(segments)-1, 0, -1):
      x = segments[index-1].xcor()
      y = segments[index-1].ycor()
      segments[index].goto(x, y)

    # Перемещение первого сегмента к голове
    if len(segments) > 0:
      x = head.xcor()
      y = head.ycor()
      segments[0].goto(x, y)

    move()

    # Проверка на столкновение с телом змеи
    for segment in segments:
      if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Скрыть сегменты тела
        for segment in segments:
          segment.goto(1000, 1000)

        # Очистить список сегментов
        segments.clear()

        # Сбросить счет
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
except turtle.Terminator:
  print("Turtle graphics window closed.")


