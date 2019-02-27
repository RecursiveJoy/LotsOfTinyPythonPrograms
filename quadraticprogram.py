
a = float(input ("Enter a value for a: "))
b = float(input ("Enter a value for b: "))
c = float(input ("Enter a value for c: "))

radicand = ((b**2)-(4*a*c))
radical = radicand ** .5
bee = (b*-1)
aa = (2*a)

x1 = format(((radical + bee) / aa), '.2f')
x2 = format(((radical - bee) / aa), '.2f')

print("x = ", x1)
print("x = ", x2)
