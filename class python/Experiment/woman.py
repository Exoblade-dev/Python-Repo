import Ursina

app = Ursina()

# Load a 3D model of a woman (you must have 'woman.obj' or .glb file)
woman = Entity(model='woman.glb', scale=2, position=(0,0,0), texture='woman_texture.png')

 camera.position = (0, 1, -5)
 camera.look_at(woman)

 app.run()
 
 import turtle

 def draw_body():
    t = turtle.Turtle()
    t.speed(3)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.begin_fill()
    t.color("lightpink")

    # Draw the head
    t.circle(40)

    # Neck
    t.right(90)
    t.forward(20)

    # Shoulders and arms
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.left(60)
    t.forward(60)
    t.backward(60)
    t.right(30)

    # Torso
    t.forward(100)

    # Hips and legs
    t.right(30)
    t.forward(70)
    t.backward(70)
    t.left(60)
    t.forward(70)
    t.end_fill()

    t.hideturtle()
    turtle.done()

draw_body()

