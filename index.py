import socket
import os

## Limpando terminal
os.system("clear")
## Exibindo tela de menu para o usuario
print("\n")
print("\033[1;36m--------------------------------------------\033[0;0m")
print("\033[1;94m")
print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
print("\n\033[0;0m") 
print("\033[;1m\033[1;97mOFICIAL PORT SCANNER - \033[0;0m")
print("\033[1;36m--------------------------------------------\n\033[0;0m")
x = input("Porta inicial:")
y = input("Porta final:")
ip = input("IP (local-> 127.0.0.1):")

if x != '' and 'y' != '':
    x = int(x)
    y = int(y)
    
    while True:

        ## Definindo o alvo e enviando a verificacao

        socket_verification = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        alvo = (ip, x)
        resultado = socket_verification.connect_ex(alvo)

        socket_verification.close()

        ## Verificando o resultado

        if resultado == 0:
            print("\033[1;94m[HISOKA]\033[0;0m \033[1;32m "+str(x)+" aberta. \033[0;0m")
        
        if x == y:
            break
        else:
            x = x+1


else:
    print("\033[1;94m[HISOKA]\033[0;0m \033[1;31mPor favor, preencha todas as informacoes.\033[0;0m")