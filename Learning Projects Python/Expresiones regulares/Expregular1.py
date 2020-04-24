import re
cadena="vamos a aprender expresiones regulares"
print(re.search("aprender",cadena))
lista_nombres=['http:\\pildorasinformaticas.es',
                'ftp:\\pildorasinformaticas.es',
                'http:\\pildorasinformaticas.com',
                'ftp:\\pildorasinformaticas.com',
                'ftp:\\pildorasinforñaticas.com']
for item in lista_nombres:
    if(re.findall('ftp',item)):
        print(item)
    if(re.findall('[ñ]]',item)):
        print(item)