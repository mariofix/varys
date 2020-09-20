from varys.personas import diputado
from columnar import columnar
from click import style

dip = diputado.lista(9)
cabeceras = ["ID", "Nombre"]
lista = []
for d in dip:
    lista.append([d.id, f"{d.nombres} {d.apellidos}"])
tabla = columnar(lista, cabeceras)
print(tabla)
seleccion = input(style("Ingrese el ID de Diputado que desea ver: ", fg='green'))


