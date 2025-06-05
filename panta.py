
import turtle
import time

# تنظیمات اولیه لاک‌پشت
t = turtle.Turtle()
t.speed(1)  # سرعت آهسته برای رسم نرم و آرام
t.pensize(2)
t.color("red")

# تابع رسم یک گلبرگ
def draw_petal():
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)

# رسم گل پنج‌پر
for _ in range(5):
    draw_petal()
    t.left(72)  # تقسیم 360 بر 5 برای پنج پر

# تمام‌شدن رسم
t.hideturtle()
turtle.done()
