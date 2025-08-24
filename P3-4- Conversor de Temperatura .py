"""4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

# Solicita os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

# Primeiro, converter a origem para Celsius
if origem == "C":
    temp_celsius = temperatura
elif origem == "F":
    temp_celsius = (temperatura - 32) * 5/9
elif origem == "K":
    temp_celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Agora, converter de Celsius para a unidade de destino
if destino == "C":
    resultado = temp_celsius
elif destino == "F":
    resultado = (temp_celsius * 9/5) + 32
elif destino == "K":
    resultado = temp_celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

# Exibir resultado formatado
print(f"{temperatura:.2f}°{origem} = {resultado:.2f}°{destino}")