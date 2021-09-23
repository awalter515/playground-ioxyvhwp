from universe import mafonction


y = mafonction(1)
reponse = 42


if y != reponse :
  print(f"Votre réponse est fausse, pensez au guide du voyageur galactique")
  raise AssertionError("Faute dans le résultat")
  

'''
assert y ==  reponse , "Ceci n'est pas la bonne réponse"
'''
