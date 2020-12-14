import click
from varys.spiders.subsecretarias.interior import SpiderInterior

interior = SpiderInterior()
print(interior.trae_dotacion("planta"))
