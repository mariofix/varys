from varys.modelos import Diputado
from varys.spiders.congreso_opendata import api


def lista(periodo=None):
    if periodo:
        lista = api.getDiputados_Periodo(prmPeriodoID=periodo)
    else:
        lista = api.getDiputados_Vigentes()
    ret = []
    for d in lista:
        dip = Diputado(
            nombres=f"{d['Nombre']} {d['Nombre2']}".strip(),
            apellidos=f"{d['Apellido_Paterno']} {d['Apellido_Materno']}".strip(),
            id=int(d['DIPID']),
            fecha_nacimiento=d['Fecha_Nacimiento'],
            fecha_defuncion=d['Fecha_Defuncion'],
            email=d['Correo_Electronico'],
            militancia_actual=d['Militancia_Actual'],
            militancias_periodo=d['Militancias_Periodos']
            )
        ret.append(dip)
        del dip
    return ret
