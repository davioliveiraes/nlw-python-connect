class MinhaClasse:
   def __enter__(self):
      print("Entrando no bloco with")
   
   def __exit__(self, exc_type, exc_value, exc_tb):
      print("Saindo do bloco with")

with MinhaClasse() as mc:
   print("Dentro do bloco with")
   