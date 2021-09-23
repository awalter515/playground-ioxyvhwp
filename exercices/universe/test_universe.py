from universe import mafonction


y = mafonction(1)
reponse = 42


if y != reponse :
  print(f"ERREUR Votre réponse est fausse, pensez au guide du voyageur galactique")
  raise AssertionError
  
else :
  print(\n)
  print("BRAVO, C'EST LA BONNE REPONSE")
  

