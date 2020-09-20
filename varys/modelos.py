from dataclasses import dataclass
from typing import Optional


@dataclass
class Ciudadano:
    rut: Optional[int] = None
    dv: Optional[str] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    edad: Optional[int] = None
    fecha_nacimiento: Optional[str] = None
    fecha_defuncion: Optional[str] = None
    sexo: Optional[str] = None


@dataclass
class Diputado(Ciudadano):
    id: int = 0
    militancia_actual: Optional[str] = None
    militancias_periodo: Optional[str] = None
    email: Optional[str] = None
