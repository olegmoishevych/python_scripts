import turtle

# Настройки черепашки
screen = turtle.Screen()
turtle.shape('turtle')
turtle.speed(1)

# Флаг для начала заполнения фигуры
is_drawing = False

# Функции движения
def move_forward():
  global is_drawing
  print("Moving forward")
  if not is_drawing:
    turtle.begin_fill()
    is_drawing = True
  turtle.forward(10)

def move_backward():
  global is_drawing
  print("Moving backward")
  if not is_drawing:
    turtle.begin_fill()
    is_drawing = True
  turtle.backward(10)

def turn_left():
  print("Turning left")
  turtle.left(90)

def turn_right():
  print("Turning right")
  turtle.right(90)

def end_drawing():
  global is_drawing
  print("Ending drawing")
  if is_drawing:
    turtle.end_fill()
    is_drawing = False
    turtle.clear()

# Добавление горячих клавиш
screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(end_drawing, 'e')  # Нажмите 'e' для завершения фигуры и удаления

# Запуск окна черепашки
turtle.mainloop()
