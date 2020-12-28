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
    paginas = None

    def __init__(self):
        self.anos = range(2009, 2021)
        self.meses = range(1, 13)
        self.paginas = 5

    def trae_dotacion(self, dotacion):
        if dotacion not in self.urls:
            # TODO Gurdar Logs
            return None

        for a in self.anos:
            for m in self.meses:
                url = self.urls[dotacion].replace("%a", f"{a}").replace("%m", f"{m}")

                print(f"Obteniendo: {url}")
                lista = self.procesa_url(
                    url,
                    (
                        a,
                        m,
                    ),
                )
                print(lista)

    def procesa_url(self, url, dates):
        el_html = self.trae_url(url)
        if el_html is None:
            print("Ocurrió un error, siguiente URL")
            return None

        df = None
        df_nuevo = None
        lista = []
        try:
            df = pd.read_html(
                el_html, flavor="bs4", index_col=0, attrs={"class": "tabla"}
            )
            df[0].rename({"_2": "Apellido1"}, axis="columns", inplace=True)
        except:
            print("No hay tabla de datos, siguiente.")
            return None

        for tupla in df[0].itertuples(name="Registro"):
            lista.append(tupla)

        for p in range(2, self.paginas):
            del el_html
            del df_nuevo

            nueva_url = url.replace(".html", f"_p{p}.html")
            el_html = self.trae_url(nueva_url)
            if el_html is None:
                print(f"No existe {nueva_url}, siguiente.")
                break

            try:
                df_nuevo = pd.read_html(
                    el_html, flavor="bs4", index_col=0, attrs={"class": "tabla"}
                )
                df_nuevo[0].rename(columns={"_2": "Apellido1"})
            except:
                pass

            for tupla in df_nuevo[0].itertuples(name="Registro"):
                lista.append(tupla)

        return lista

    def trae_url(self, url):
        headers = {"user-agent": __UA__}
        pagina = requests.get(url, headers=headers)

        if pagina.status_code == 200:
            return pagina.text
        else:
            # TODO Guardar Logs
            return None
