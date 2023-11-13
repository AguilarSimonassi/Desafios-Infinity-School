#Atividade Desafio - Conversor de Moeda 🌏💱
#Objetivo: Criar um programa em Python que permita ao usuário converter uma quantia em uma moeda para outra moeda com base em uma taxa de câmbio fornecida.
#Regras:
#Solicite ao usuário que insira a quantia de dinheiro a ser convertida 💰.
##Solicite ao usuário que insira a moeda de origem (por exemplo, USD, EUR, BRL, etc.) 🌍.
#Solicite ao usuário que insira a moeda de destino 🌎.
#Forneça uma taxa de câmbio para a conversão entre as duas moedas. A taxa de câmbio deve ser fornecida como uma variável no início do programa 💹.
#Calcule o valor convertido 🧮.
#Exiba o valor original, a moeda de origem, o valor convertido e a moeda de destino na tela 💻.
#Desafios adicionais:
#Lide com casos em que o usuário insira uma moeda não suportada pelo programa ❌.
#Ofereça a possibilidade de fazer várias conversões consecutivas sem sair do programa 🔁.
#Forneça um menu de opções para permitir ao usuário escolher entre várias moedas de origem e de destino 📝. #😊👍







resposta = input("Deseja fazer o cambiamento de moedas: Sim ou Não?").upper()

while resposta == "SIM":

    valororigem = float(input("Digite o valor que deseja converter: "))

    moedaorigem = str.upper(input("Qual a moeda de origem: USD, EUR, BRL ou GPB ?")).upper()
    usd = 3.0
    brl = 0.5
    eur = 1.9
    gpb = 5.2
    valorconversao = 0


    while moedaorigem != "USD" and moedaorigem != "BRL" and moedaorigem != "GPB" and moedaorigem != "EUR":
        moedaorigem = str.upper(input("Moéda de origem invalida, tente novamente: USD, EUR, BRL ou GPB ?")).upper()
    else:
        if moedaorigem == "USD":
            valor = valororigem
        elif moedaorigem == "BRL":
                valor = valororigem
        elif moedaorigem == "EUR":
            valor = valororigem
        elif moedaorigem == "GPB":
           valor = valororigem
    

    moedadestino = str.upper(input("Qual a moeda de destino: USD, EUR, BRL ou GPB ?")).upper()

    while moedadestino != "USD" and moedadestino != "BRL" and moedadestino != "GPB" and moedadestino != "EUR":
        moedadestino = str.upper(input("Moéda de destino invalida, tente novamente: USD, EUR, BRL ou GPB ?")).upper()
    else:
        if moedadestino == moedaorigem:
            usd = 1
            brl = 1
            eur = 1
            gpd = 1
        if moedadestino == "USD":
            print(f"Taxa de conversão para a moeda {moedadestino} é de: {usd}x em relação a sua moeda de origem que é {moedaorigem}")
            valorconversao = valor * usd
        elif moedadestino == "BRL":
            print(f"Taxa de conversão para a moeda {moedadestino} é de: {brl}x em relação a sua moeda de origem que é {moedaorigem}")
            valorconversao = valor * brl
        elif moedadestino == "EUR":
            print(f"Taxa de conversão para a moeda {moedadestino} é de: {eur}x em relação a sua moeda de origem que é {moedaorigem}")
            valorconversao = valor * eur
        elif moedadestino == "GPB":
            print(f"Taxa de conversão para a moeda {moedadestino} é de: {gpb}x em relação a sua moeda de origem que é {moedaorigem}")
        valorconversao = valor * gpb


    print(f"Será convertido {valororigem}{moedaorigem} em {moedadestino} ficando no total de: {valorconversao}{moedadestino}!")

    resposta = input("Deseja fazer o cambiamento de moedas novamento: Sim ou Não?").upper()
else: 
     print("Obrigado!")