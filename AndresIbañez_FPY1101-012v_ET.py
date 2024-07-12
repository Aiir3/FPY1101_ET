import random
import csv
 

trabajadores =["Juan Perez","Ana Maria","Carlos Lopez","Pedro Rodriguez","Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez" ]
sueldos=[]


def asignar_sueldos():
    global sueldos
    sueldos=[random.randint(300000,2500000) for
     _ in range(10)]
    
    print("Sueldos asignados correctamente")

def clasificar_sueldos(): 

      menores_800k=[(trabajadores[i], sueldos[i]) for i in range (10) if sueldos [i] < 800000]
    
      entre_800k_2000k=[(trabajadores[i], sueldos[i]) for i in range (10) if sueldos[i] < 2000000]

      superiores_2000k= [(trabajadores[i], sueldos[i]) for i in range (10) if sueldos[i]>2000000] 

      print("sueldos menores a $800000\TOTAL:",len(menores_800k))   
      for empleado, sueldo in menores_800k:
        print(f"Nombre empleado:{empleado,}, Sueldo: $ {sueldo:,}")
        print ("Sueldos superiores a $2000000\nTOTAL: ",len(superiores_2000k))  
      for empleado, sueldo in superiores_2000k:
            print (f"Nombre empleado:{empleado}, Sueldo: ${sueldo}")

total_sueldos=sum(sueldos)
print(f"\nTOTAL SUELDOS: ${total_sueldos:}")

def calcular_media_geometrica(numeros):
      producto=1
      for num in numeros:
            producto *=num
      return producto **(1/len(numeros))

def ver_estadisticas():
      max_sueldo=max(sueldos)
      min_sueldo=min(sueldos)
      promedio=sum(sueldos)/ len(sueldos)
      media_geometrica=calcular_media_geometrica(sueldos)
      print(f"Sueldo mas alto : ${max_sueldo}")
      print(f"Sueldo mas bajo: ${min_sueldo}")
      print(f"Promedio de sueldos: ${promedio:,.2f}")
      print(f"Media geometrica: ${media_geometrica}")

def reporte_sueldos():
      reporte=[]
      for i in range(10):

            nombre= trabajadores[i]
            sueldo_base=sueldos[i]
            descuento_salud=sueldo_base*0.07
            descuento_afp=sueldo_base*0.12
            sueldo_liquido=sueldo_base - descuento_salud - descuento_afp
            reporte.append([nombre,sueldo_base,descuento_salud,descuento_afp,sueldo_liquido])

      print(f"\n{'Nombre empleado' :<20}{'Sueldo Base': <15}{'Descuento Salud': >18}{'Descuento AFP': >15}{'Sueldo liquido'}")
      for r in reporte:
            print(f"{r[0]:<20}${r[1]:>15,.2f}${r[2]:<18,.2f}${r[3]:<15,.2f}${r[4]:,.2f}")

      with open("reporte_sueldos.csv", "w", newline="") as file:
            writer= csv.writer(file)
            writer.writerow(["Nombre empleado", "Sueldo Base","Descuento Salud", "Descuento AFP", "Sueldo liquido"])
            writer.writerows(reporte)

      print("\nReporte de sueldos guardado en 'reporte_sueldos.csv'.")

def salir():
      print("Gracias por uitilizar el programa. ¡Hasta Luego¡")
      exit()
def menu():
      while True:
            print("\n---Menu---")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar Sueldos")
            print("3. Ver estadisticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            try:
                  opcion=input("Seleccione una opcion")
                  if opcion=="1":
                        asignar_sueldos()
                  elif opcion=="2":
                        clasificar_sueldos()
                  elif opcion=="3":
                        ver_estadisticas()
                  elif opcion=="4":
                        reporte_sueldos()
                  elif opcion=="5":
                        salir()
                  else: 
                        print("Opcion no valida intente nuevamente")
            except ValueError:
                  print("Ingrese una opcion valida de 1 a 5")
menu()
                         
 