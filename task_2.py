
import turtle

def draw_pifagor_tree(t, length, k, levels):
    if levels == 0:
        return
    if levels > 1:
        t.pencolor("brown")  # Колір стовбура
    else:
        t.pencolor("green")  # Колір листя

    t.pensize(levels)
    # стовбур
    t.forward(length)
    # гілки
    new_length = k * length
    t.left(45)
    draw_pifagor_tree(t, new_length, k, levels - 1)
    t.right(90)
    draw_pifagor_tree(t, new_length, k, levels - 1)
    t.left(45)
    # повернення на початкову точку
    t.backward(length)

def main():
    levels = int(input("Введіть кількість рівнів не більше 10: "))

    length = 150  # Фіксована довжина стовбура
    k = 0.8  # Фіксований коефіцієнт відносно довжини

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -200)  
    t.pendown()
    t.left(90)  

    draw_pifagor_tree(t, length, k, levels)

    window.mainloop()

if __name__ == "__main__":
    main()