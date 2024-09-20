








def hora(horario):

    if horario >5 and horario < 12:
        print('good morning')
    elif horario >12 and horario < 18:
        print('good afternoon')
    elif horario >19 and horario < 24:
        print('good night')
    else:
        print('Early morning')

while True:


    horario = float(input("Enter the time:"))

    hora(horario)
