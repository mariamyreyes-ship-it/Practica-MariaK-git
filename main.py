from entidades.habitacion import Habitacion
from entidades.huesped import Huesped
from entidades.reserva import Reserva
# agregar Habitaciones
def agregar_habitacion(habitaciones):
    numero = input('Número de la habitacion: ')
    tipo = input('Tipo de habitacion: ')
    precio = float(input('Precio por noche: '))
    habitacion = Habitacion(numero, tipo, precio)
    habitaciones.append(habitacion)
    print('Habitación agregada con éxito')
# registrar huesped
def registrar_huesped(huespedes):
    nombre = input('Nombre del huesped: ')
    documento_identidad = input('Documento de identidad: ')
    telefono = input('Telefono: ')
    huesped = Huesped(nombre, documento_identidad, telefono)
    huespedes.append(huesped)
# crear reserva
def crear_reserva(habitaciones, huespedes, reservas):
    documento_identidad = input('Documento de identidad: ')
    huesped = next (( h for h in huespedes if h.documento_identidad ==documento_identidad), None)
    if not huesped:
        print('Huesped no encontrado.')
        return
    numero_habitacion = input('Numero de habitacion a reservar: ')
    habitacion = next((h for h in habitaciones if h.numero ==numero_habitacion and h.disponible), None)
    if not habitacion:
        print('Habitación no disponible')
        return
    fecha_entrada = input('Fecha de entrada (yyy/mm/dd)')
    fecha_salida = input('Fecha de salida (yyy/mm/dd)')
    reserva = Reserva(habitacion, huesped, fecha_entrada, fecha_salida)
    reservas.append(reserva)
    print('Reserva creada con éxito')
# mostrar menu
def mostrar_menu():
    print('\nSistema de Reservas de Hotel')
    print('1. Agregar Habitación')
    print('2. Registrar Huesped')
    print('3. Crear Reserva')
    print('4. Mostrar Habitaciones')
    print('5. Mostrar Huespedes')
    print('6. Mostrar Reservas')
    print('7. Salir')
def main():
    habitaciones = []
    huespedes = []
    reservas = []
    while True:
        mostrar_menu()
        opcion = input('Seleccione una opcion: ')
        if opcion =='1':
            agregar_habitacion(habitaciones)
        elif opcion =='2':
            registrar_huesped(huespedes)
        elif opcion =='3':
            crear_reserva(habitaciones,huespedes,reservas)
        elif opcion =='4':
            for habitacion in habitaciones:
                print(habitacion)
        elif opcion =='5':
            for huesped in huespedes:
                print(huesped)
        elif opcion =='6':
            for reserva in reservas:
                print(reserva)
        elif opcion =='7':
            print('Salir del Sistema.')
            break
        else:
            print('Opción no válida. Intente de nuevo.')

if __name__ == '__main__':
    main()
