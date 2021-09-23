import sys

from universe import mafonction


y = mafonction(1)
reponse = 42


if y != reponse :
  print(f"Votre réponse est fausse, pensez au guide du voyageur galactique")
  raise NameError("Faute dans le résultat")
  

