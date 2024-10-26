# 1
nome = "Marcella"
idade = "20"
print ("Meu nome é {nome} e tenho {idade} anos.")

############# 3

numero = int(input("insira um numero impar ou par: "))

if numero % 2 == 0:
    print("o numero e par")
else:
    print("o numero e impar")

############# 4

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
print("O maior número é:", maior)

############## 5

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"{celsius}°C é igual a {fahrenheit}°F")

############## 6

# Solicita ao usuário para inserir as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"A média das notas é: {media:.2f}")

############## 7

# Contagem de 1 a 10
for i in range(1, 11):
    print(i)

############## 8



