import argparse
from Bio import Entrez
# import numpy as np
# import matplotlib.pyplot as plt

Entrez.email = "joserodelmar@gmail.com"

# Paso de parametros por argumentos
parser = argparse.ArgumentParser(description="Busqueda de terminos en pubmed")
parser.add_argument("-w", "--word",
                    metavar="word of interest",
                    type=str,
                    help="Terminos a buscar",
                    required=True)

# Search by country and year of publication.
parser.add_argument("-c", "--country",
                    metavar="country of publication",
                    type=str,
                    help="Pais donde se desean buscar las publicaciones",
                    required=True)

parser.add_argument("-y", "--year",
                    metavar="year of publication",
                    type=int,
                    help="Fecha de publicacion del articulo",
                    required=True)

args = parser.parse_args()

search = args.country + "[CNTY] AND " + args.year + "[PDAT] AND (" + args.word + ")"

### through handle the terms in "search" will be looked for in pubmed database

handle = Entrez.esearch(db="pubmed", term=search)

# The results that coincide with the terms in "search" are stored in result
result = Entrez.read(handle)

# in archiv, the list with the corresponding IDs will be stored
archiv = result["IdList"]
handle.close()

