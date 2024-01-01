prompt = "Qual sua idade?"
prompt += "\n Digite 'quit' para fechar o programa.:\n"
message = ""

while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    idade = int(message)
    if idade < 3:
        print("Seu ingresso é gratuito!")
    elif idade >= 3 and idade <=12:
        print("Seu ingresso custa 10 dólares.")
    elif idade > 12:
        print("Seu ingresso custa 15 dólares.")
