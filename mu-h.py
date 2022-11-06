print("This program calculates mu sub h for silicon.")

T = float(input("Temperature T in Kelvin: "))

N = float(input("Total impurity density N: "))

Tn = T/300

mu_h = 54.3*Tn**(-0.57) + (2.406e8*T**(-2.33)) / (1 + (N*0.88*Tn**(-0.164))/(2.35e17*Tn**2.4))

#Originally 2.406 was 1.36 but that didn't seem to work properly

print(mu_h)
