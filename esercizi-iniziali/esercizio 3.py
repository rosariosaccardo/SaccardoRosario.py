Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("a=")
a=2
>>> b=input("b=")
b=4
>>> c=input("c=")
c=5
>>> if a==0:
	print("Non esiste equazione di secondo grado")
else:
	delta=b**2-(4*a*c)
	if delta < 0 :
		print("L'equazione di secondo grado non ha risultati")
	elif delta == 0:
		print("L'equazione ha due soluzioni reali e coicidenti")
		X12=(-b+(math.sqrt(delta)))/(2*a)
		print("X1 = X2 =",X12)
	else:
		print("L'equazione ha due soluzioni reali e distinte")
		X1=(-b+(math.sqrt(delta)))/(2*a)
		print("X1 =",X1)
		X2=(-b-(math.sqrt(delta)))/(2*a)
		print("X2 =",X2)
		
