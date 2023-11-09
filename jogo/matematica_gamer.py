import random
import time

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    else:
        # Para garantir que a divisão resulte em um número inteiro
        num1 = num2 * random.randint(1, 10)
        answer = num1 // num2
    
    dados = {
        'numero1': num1,
        'numero2' : num2,
        'operacao': operation,
        'resposta': answer,
    }
    #return num1, num2, operation, answer
    return dados

def iniciarPartida():
    #print("Olá! Seja bem-vindo ao Jogo de Matemática!")
   
    num1, num2, operation, correct_answer = generate_question()
    question = f"Quanto é {num1} {operation} {num2}? "

    start_time = time.time()
    player_answer = input(question)

    try:
        player_answer = int(player_answer)
    except ValueError:
        return ("Por favor, insira um número válido.")
        
    elapsed_time = time.time() - start_time

    if player_answer == correct_answer and elapsed_time <= 10:
        return ("Resposta correta! Parabéns!")
    else:
        if elapsed_time > 10:
            return ("Tempo esgotado. A resposta é dada como errada.")
        else:
            return (f"Resposta errada. A resposta certa é {correct_answer}.")

        #print("Próxima pergunta...")
    
    #print("Obrigado por jogar. Volte sempre!")
