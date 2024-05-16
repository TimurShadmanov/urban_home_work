a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 < number_2 < number_3:
    print(number_2)
elif number_1 < number_3 < number_2:
    print(number_3)
else:
    print(number_1)


color_1 = str(input())
color_2 = str(input())
color_1color_2 = color_1 + color_2
if (color_1color_2 == 'красныйсиний') or (color_1color_2 == 'синийкрасный'):
    print('фиолетовый')
elif (color_1color_2 == 'красныйжелтый') or (color_1color_2 == 'желтыйкрасный'):
    print('оранжевый')
elif (color_1color_2 == 'синийжелтый') or (color_1color_2 == 'желтыйсиний'):
    print('зеленый')
elif (color_1color_2 == 'красныйкрасный'):
    print('красный')
elif (color_1color_2 == 'синийсиний'):
    print('синий')
elif (color_1color_2 == 'желтыйжелтый'):
    print('желтый')

else:
    print("ошибка цвета")


# остальные задачи еще не решил