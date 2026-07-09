#Trabalhando com o módulo de desenho do Python(Turtle)

from turtle import Turtle, Screen

x = Turtle()
print(x)
x.shape("turtle") 
x.color("blue")
x.forward(300)
exibir = Screen()

print(exibir.canvheight)
exibir.exitonclick()
