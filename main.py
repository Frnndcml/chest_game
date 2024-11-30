import random

def geracaoGrade(tamanho):
    return [['-' for _ in range(tamanho)] for _ in range(tamanho)]

def exibicaoGrade(grade):
    for linha in grade:
        print(' '.join(linha))
    print() 

def distanciaTesouro(tesouro, palpite):
    return abs(tesouro[0] - palpite[0]) + abs(tesouro[1] - palpite[1])

def jogar():
    tamanhoGrade = 5
    tentativas = 5
    
    tesouro = [random.randint(0, tamanhoGrade - 1), random.randint(0, tamanhoGrade - 1)]
    grade = geracaoGrade(tamanhoGrade)
    
    print("Caça ao tesouro")
    print(f"Você tem {tentativas} tentativas para encontrar o tesouro.")
    
    for tentativa in range(1, tentativas + 1):
        print(f"\nTentativa {tentativa} de {tentativas}")
        exibicaoGrade(grade)
        
        try:
            linha = int(input(f"Escolha uma linha (0 a {tamanhoGrade - 1}): "))
            coluna = int(input(f"Escolha uma coluna (0 a {tamanhoGrade - 1}): "))
            
           
            if linha < 0 or linha >= tamanhoGrade or coluna < 0 or coluna >= tamanhoGrade:
                print("Coordenadas inválidas. Tente novamente.")
                continue
            
            palpite = [linha, coluna]
            distancia = distanciaTesouro(tesouro, palpite)
            
            if palpite == tesouro:
                print("Você conseguiu encontrar o tesouro!")
                break
            else:
                print(f"O tesouro não está aqui. Distancia do tesouro: {distancia}")
                grade[linha][coluna] = "X"
        
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
        
    else:
        print("Suas tentativas acabaram... O tesouro estava em:", tesouro)

def main():
    while True:
        jogar()
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar!")
            break


main()
