from varys import modelos


def test_ciudadano():
    c = modelos.Ciudadano()
    assert c.rut is None
    assert c.dv is None
    assert c.nombres is None
    assert c.apellidos is None
    assert c.edad is None
    assert c.fecha_nacimiento is None
    assert c.fecha_defuncion is None
    assert c.sexo is None


def test_diputado():
    c = modelos.Diputado()
    assert c.rut is None
    assert c.dv is None
    assert c.nombres is None
    assert c.apellidos is None
    assert c.edad is None
    assert c.fecha_nacimiento is None
    assert c.fecha_defuncion is None
    assert c.sexo is None
    assert c.id == 0
    assert c.email is None
    assert c.militancia_actual is None
    assert c.militancias_periodo is None
