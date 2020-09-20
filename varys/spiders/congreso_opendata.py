import zeep

cliente = zeep.Client(wsdl="http://opendata.congreso.cl/wscamaradiputados.asmx?WSDL")

api = cliente.service
