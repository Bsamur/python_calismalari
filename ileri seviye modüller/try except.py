import sys

try:
  a=0
  while a<100:
    sayı = int(input("bir sayı giriniz:"))
    a+=1

    if sayı%3==0 and sayı%5==0:
      print("FIZZ-BUZZ")
    elif sayı%3==0:
      print("FIZZ")
    elif sayı%5==0:
      print("BUZZ")
    else:
      print("lütfen 3 ve 5 in katı bir tam sayı girin")
except ValueError:
  print("lütfen tam sayı girin")

