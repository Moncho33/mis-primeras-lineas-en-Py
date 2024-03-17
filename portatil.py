def OpcionCompra():
    while True:
        print('1. portatil 2. pc y 3. movil  y 4 para salir')
        
        op = input("¿Que desea comprar? ->")
        if op == '4':
           print('esta fuera')
           break
        else:           
         cantidad = float(input('ingrese la cnatida desada ->'))


        precioPotatail = 7000000
        pc = 4500000
        cel = 3800000


        if op == "1":
          subtotal = cantidad * precioPotatail
          descuento = subtotal*0.20
          total = subtotal - descuento
          print(f'Usted ha comprado un portatil con un precio cada uno de {precioPotatail} y un descuente de {descuento} y un total de {total}')
        elif op == "2":
           subtotal = cantidad * pc
           descuento = subtotal*0.20
           total += subtotal - descuento
           print(f'Usted ha comprado un portatil con un precio cada uno de {precioPotatail} y un descuente de {descuento} y un total de {total}')
        elif op == "3":
            subtotal = cantidad * cel
            descuento = subtotal*0.20
            total = subtotal - descuento
            print(f'Usted ha comprado un portatil con un precio cada uno de {precioPotatail} y un descuente de {descuento} y un total de {total}')
        else:
            print("elige una opcion correcta")


if __name__ =='__main__':
      OpcionCompra()