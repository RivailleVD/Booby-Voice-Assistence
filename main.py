#execute no terminal como python3 main.py > /dev/null 2>&1
#para livrar os logs


# Importação e inicialização
from Bips.Bips import *
from Funções import Automação,front,manual
from Recognition import reconhecimento03


# Inicializa o sistema
Bip_Inicialização()
#front.front()


try:
   
    while True:
        
        
        texto_reconhecido = reconhecimento03.reconhecimento_continuo()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
except KeyboardInterrupt:
    Automação.fechar()
    print("Sistema encerrado.")
    Bip_logout() 


