import zeep

URL = "http://opendata.congreso.cl/wscamaradiputados.asmx?WSDL"
cliente = zeep.Client(wsdl=URL)

api = cliente.service
