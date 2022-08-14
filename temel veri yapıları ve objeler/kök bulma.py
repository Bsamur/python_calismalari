print("DENKLEM KÖKÜNÜ BULMA")

x=int(input("denlklemin birinci değeri"))
y=int(input("denlemin ikinci değeri"))
z=int(input("denlklemin üçüncü değeri"))

delta=y**2-4*x*z
x1=(-y-(delta**0.5)/(2*x))
x2=(-y+(delta**0.5)/(2*x))
print("birinci kök:{}\nikinci kök:{}\n".format(x1,x2))
