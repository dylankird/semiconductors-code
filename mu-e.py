print("This program calculates mu sub e for silicon.")

T = float(input("Temperature T in Kelvin: "))

N = float(input("Total impurity density N: "))

Tn = T/300

mu_e = 88*Tn**(-0.57) + (7.4e8*T**(-2.33)) / (1 + (N*0.88*Tn**(-0.164))/(1.26e17*Tn**2.4))

print(mu_e)
