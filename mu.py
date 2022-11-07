print("This program calculates mu sub e for silicon.")

T = float(input("Temperature T in Kelvin: "))

N = float(input("Total impurity density N: "))

Tn = T/300

mu_e = 88*Tn**(-0.57) + (7.4e8*T**(-2.33)) / (1 + (N*0.88*Tn**(-0.164))/(1.26e17*Tn**2.4))

mu_h = 54.3*(Tn**(-0.57)) + (2.406e8*(T**(-2.33))) / (1 + (N*0.88*(Tn**(-0.164)))/(2.35e17*(Tn**2.4)))

#Originally 2.406 was 1.36 but that didn't seem to work properly

print("mu sub e:",mu_e)
print("mu sub h:",mu_h)
