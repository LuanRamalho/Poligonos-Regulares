from turtle import *
def  polígono(lado, num_lados):
    #Desenha um poligono de num_lado.
    color('gray', 'orange')
    begin_fill()
    for i in range(num_lados):
        forward(lado)
        left(360/num_lados)
    end_fill()
polígono(100,8)
done()
