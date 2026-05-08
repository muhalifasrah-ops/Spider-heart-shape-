import turtle
import time

# Konfigurasi layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  # Matiin auto-update di awal

# Kura-kura untuk gambar hati
heart_pen = turtle.Turtle()
heart_pen.hideturtle()
heart_pen.color("red")

# Kura-kura untuk gambar laba-laba
spider_pen = turtle.Turtle()
spider_pen.hideturtle()
spider_pen.color("black")

scale = 0.8
heart_sizes = [20, 50, 80, 110, 160]

def draw_heart_outline(size):
    heart_pen.penup()
    heart_pen.goto(0, -size/2)
    heart_pen.pendown()
    
    heart_pen.left(140)
    step_length = size / 200
    for _ in range(200):
        heart_pen.forward(step_length)

    for _ in range(200):
        heart_pen.right(1)
        heart_pen.forward(size * 0.009)

    heart_pen.left(120)

    for _ in range(200):
        heart_pen.right(1)
        heart_pen.forward(size * 0.009)

    for _ in range(200):
        heart_pen.forward(step_length)

    heart_pen.penup()
    heart_pen.setheading(0)

def draw_filled_heart(size):
    heart_pen.penup()
    heart_pen.goto(0, -size/2)
    heart_pen.pendown()
    
    heart_pen.begin_fill()
    heart_pen.left(140)
    step_length = size / 200
    for _ in range(200):
        heart_pen.forward(step_length)

    for _ in range(200):
        heart_pen.right(1)
        heart_pen.forward(size * 0.009)

    heart_pen.left(120)

    for _ in range(200):
        heart_pen.right(1)
        heart_pen.forward(size * 0.009)

    for _ in range(200):
        heart_pen.forward(step_length)

    heart_pen.end_fill()
    heart_pen.penup()
    heart_pen.setheading(0)

def draw_spider():
    # Posisi tengah tepat di sumbu Y
    spider_pen.penup()
    spider_pen.goto(0, 50 * scale)
    spider_pen.pendown()

    # Kepala laba-laba
    spider_pen.begin_fill()
    spider_pen.circle(18 * scale)
    spider_pen.end_fill()

    # Badan laba-laba
    spider_pen.penup()
    spider_pen.goto(0, 50 * scale)
    spider_pen.setheading(270)
    spider_pen.left(60)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.forward(18 * scale)
    spider_pen.right(80)
    spider_pen.forward(60 * scale)
    spider_pen.right(147)
    spider_pen.forward(60 * scale)
    spider_pen.right(80)
    spider_pen.forward(18 * scale)
    spider_pen.end_fill()

    # Kaki atas kanan 1
    spider_pen.penup()
    spider_pen.goto(9 * scale, 87 * scale)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.left(20)
    spider_pen.forward(22 * scale)
    spider_pen.right(60)
    spider_pen.forward(45 * scale)
    spider_pen.left(120)
    spider_pen.forward(72 * scale)
    spider_pen.right(175)
    spider_pen.forward(85 * scale)
    spider_pen.right(127)
    spider_pen.forward(57 * scale)
    spider_pen.left(60)
    spider_pen.forward(16 * scale)
    spider_pen.end_fill()

    # Kaki atas kanan 2
    spider_pen.penup()
    spider_pen.goto(12 * scale, 77 * scale)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.left(90)
    spider_pen.left(90)
    spider_pen.forward(18 * scale)
    spider_pen.right(60)
    spider_pen.forward(72 * scale)
    spider_pen.left(125)
    spider_pen.forward(117 * scale)
    spider_pen.right(175)
    spider_pen.forward(130 * scale)
    spider_pen.right(128)
    spider_pen.forward(85 * scale)
    spider_pen.left(60)
    spider_pen.forward(18 * scale)
    spider_pen.end_fill()

    # Kaki atas kiri 1
    spider_pen.penup()
    spider_pen.goto(-9 * scale, 87 * scale)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.right(80)
    spider_pen.forward(22 * scale)
    spider_pen.left(60)
    spider_pen.forward(45 * scale)
    spider_pen.right(120)
    spider_pen.forward(72 * scale)
    spider_pen.left(175)
    spider_pen.forward(85 * scale)
    spider_pen.left(127)
    spider_pen.forward(57 * scale)
    spider_pen.right(60)
    spider_pen.forward(16 * scale)
    spider_pen.end_fill()

    # Kaki atas kiri 2
    spider_pen.penup()
    spider_pen.goto(-12 * scale, 77 * scale)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.left(90)
    spider_pen.left(90)
    spider_pen.forward(18 * scale)
    spider_pen.left(60)
    spider_pen.forward(72 * scale)
    spider_pen.right(125)
    spider_pen.forward(117 * scale)
    spider_pen.left(175)
    spider_pen.forward(130 * scale)
    spider_pen.left(128)
    spider_pen.forward(85 * scale)
    spider_pen.right(60)
    spider_pen.forward(18 * scale)
    spider_pen.end_fill()

    # Kaki bawah kanan 1
    spider_pen.penup()
    spider_pen.goto(13 * scale, 65 * scale)
    spider_pen.left(60)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.forward(18 * scale)
    spider_pen.right(40)
    spider_pen.forward(85 * scale)
    spider_pen.right(100)
    spider_pen.forward(120 * scale)
    spider_pen.right(175)
    spider_pen.forward(108 * scale)
    spider_pen.left(90)
    spider_pen.forward(72 * scale)
    spider_pen.left(40)
    spider_pen.forward(18 * scale)
    spider_pen.end_fill()

    # Kaki bawah kanan 2
    spider_pen.penup()
    spider_pen.goto(10 * scale, 62 * scale)
    spider_pen.left(150)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.forward(22 * scale)
    spider_pen.right(10)
    spider_pen.forward(58 * scale)
    spider_pen.right(95)
    spider_pen.forward(63 * scale)
    spider_pen.right(175)
    spider_pen.forward(54 * scale)
    spider_pen.left(85)
    spider_pen.forward(58 * scale)
    spider_pen.left(15)
    spider_pen.forward(13 * scale)
    spider_pen.end_fill()

    # Kaki bawah kiri 1
    spider_pen.penup()
    spider_pen.goto(-13 * scale, 65 * scale)
    spider_pen.right(3)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.forward(18 * scale)
    spider_pen.left(40)
    spider_pen.forward(85 * scale)
    spider_pen.left(100)
    spider_pen.forward(120 * scale)
    spider_pen.left(175)
    spider_pen.forward(108 * scale)
    spider_pen.right(90)
    spider_pen.forward(72 * scale)
    spider_pen.right(40)
    spider_pen.forward(18 * scale)
    spider_pen.end_fill()

    # Kaki bawah kiri 2
    spider_pen.penup()
    spider_pen.goto(-10 * scale, 62 * scale)
    spider_pen.right(90)
    spider_pen.right(60)
    spider_pen.pendown()
    spider_pen.begin_fill()
    spider_pen.forward(22 * scale)
    spider_pen.left(10)
    spider_pen.forward(58 * scale)
    spider_pen.left(95)
    spider_pen.forward(63 * scale)
    spider_pen.left(175)
    spider_pen.forward(54 * scale)
    spider_pen.right(85)
    spider_pen.forward(58 * scale)
    spider_pen.right(15)
    spider_pen.forward(13 * scale)
    spider_pen.end_fill()
    
#ANIMASI YANG UDAH DIATUR ULANG

# 1. Gambar semua garis hati kosong (ANIMASI KELIHATAN, CEPAT)
screen.tracer(1) # Nyalain animasi
heart_pen.speed(0)
for size in heart_sizes:
    draw_heart_outline(size)
    screen.update() # Langsung tampilkan setelah satu hati selesai

time.sleep(0.2) # Jeda agak lama dikit biar puas lihat garisnya

# 2. Isi warna hati (Satu-satu, ada jeda dikit biar urutannya kelihatan)
screen.tracer(0) # Matikan animasi proses gambar
for size in heart_sizes:
    draw_filled_heart(size) # Gambar di belakang layar
    screen.update() # Langsung tampilkan hati yang baru diisi
    time.sleep(0.2) # Jeda dikit (0,2 detik) sebelum ke hati berikutnya

# 3. Munculin laba-laba (ANIMASI KELIHATAN, LAMBAT)
screen.tracer(1) # Nyalain lagi buat laba-laba
spider_pen.speed(3)
draw_spider()

turtle.done()
#hasil nya sih gak terlalu simetris saya gunakan beberapa template di github