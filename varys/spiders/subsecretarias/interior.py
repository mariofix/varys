from varys import __UA__
import requests
from bs4 import BeautifulSoup
import click
import pandas as pd


class SpiderInterior:
    """Busca Informacion en Subsecretaria del Interior"""

    base = "https://www.interior.gob.cl/transparencia/sag/"
    urls = {
        "planta": f"{base}dotacionplanta_%a_%m.html",
        "contrata": "",
        "honorarios": "",
    }
    anos = None
    meses = None

    def __init__(self, anos=None, meses=None):
        self.anos = range(2009, 2021)
        self.meses = range(1, 13)

    def trae_dotacion(self, dotacion):
        if dotacion not in self.urls:
            # TODO Gurdar Logs
            return None

        for a in self.anos:
            for m in self.meses:
                url = (
                    self.urls[dotacion]
                    .replace("%a", f"{a}")
                    .replace("%m", f"{m}")
                )

                print(f"Obteniendo: {url}")
                self.procesa_url(url)

    def procesa_url(self, url):
        el_html = self.trae_url(url)
        if el_html is None:
            print("Ocurrió un error, siguiente URL")
            return None

        df = None
        try:
            df = pd.read_html(el_html, flavor="bs4", attrs={"class": "tabla"})
        except:
            print("No hay tabla.")

        print(df)
        click.pause()

    def trae_url(self, url):
        headers = {"user-agent": __UA__}
        pagina = requests.get(url, headers=headers)

        if pagina.status_code == 200:
            return pagina.text
        else:
            # TODO Guardar Logs
            return None
