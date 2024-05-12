def ExB(n):
  if n == 1:
      return 2
  else:
      return ExB(n - 1) - 1

resultado = ExB(3)
print(resultado)  
