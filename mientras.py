
'''
contra = input("contraseña ")

passw = "Cesde1*"
print(validar)
respuesta = int(input("1.si\n2.no\n"))

'''
i=1
user = "Cesde"
passw = "Cesde1*"
usuario = input("Usuario ")
contra = input("contraseña ")
validar = True if user == usuario and passw == contra else False
while validar == False:
    print(f'Intento {i}')
    if validar != False:
        print("Usuario Verificado")
        break
    else:
        print("User o pass incorrectos ")
        i +=1
        usuario = input("Usuario ")
        contra = input("contraseña ")
        validar = True if user == usuario and passw == contra else False
    if i>3:
        print('usuario Bloqueado por 24 horas')
        break


