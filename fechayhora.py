from datetime import date, datetime

hoy = date.today()
hoy = str(hoy)
hoy = hoy.split('-')
hoy = hoy[::-1]
hoy = "-".join(hoy)
print(hoy)

print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.today().weekday())

mes = ['Enero', 'Febrero', 'Marzo', 'Abril']
diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves']

fecha = "Hoy " + str(diasSemana[date.today().weekday(
)]) + ' ' + str(date.today().day) + ' de ' + str(mes[(date.today().month) - 1]) + ' de ' + str(date.today().year)

print(fecha)

print(datetime.now())
print(datetime.now().second)
print(datetime.now().minute)
print(datetime.now().hour)
print(datetime.now().microsecond)

print(datetime.now().strftime("%d-%m-%y %H:%M:%S"))

print(datetime.today().weekday())
