inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" , round(balance1, 2))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" , round(balance2, 2))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" , round(balance3, 2))
