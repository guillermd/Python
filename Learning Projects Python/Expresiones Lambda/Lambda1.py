def area_triangulo(base, altura):
    return (base*altura)/2

print (area_triangulo(10,3))

#los dos puntos es como return
area_tria=lambda base, altura:(base*altura)/2
al_cubo=lambda num:pow(num,3)
suma=lambda num1, num2:num1+num2
destacar_valor=lambda comision:"¡{}! €".format(comision)
comisionAna=15584
print(destacar_valor(comisionAna))

print (area_tria(20,3))
print (al_cubo(2))    
