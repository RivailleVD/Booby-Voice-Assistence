from Bips.Bips import *
#from Recognition import reconhecimento03
import os
from time import sleep, time
import pyautogui
import subprocess
from pynput.keyboard import Controller, Key

def abrircalculadora():
    '''Função utilizada para executar a calculadora'''
    
    print("Processando...")
    sleep(1)
    Bip_aleatorio()
    os.system('gtk-launch org.kde.kcalc')
    print("Execusão Concluída!")
    
    

def ligarteclado():
    '''Função utilizada para acender os leds do teclado'''
    
    print("Processando...")
    sleep(1)
    Bip_aleatorio()
    os.system('xset led 3')
    print("Execusão Concluída!")
    
    
def apagarteclado():
    '''Função utilizada para apagar os leds do teclado'''
    
    print("Processando...")
    sleep(1)
    Bip_aleatorio()
    os.system('xset led off')
    print("Execusão Concluída!")  
    
def abrircode():
    '''Função utilizada para abrir o visual studio code'''
    
    print("Processando")
    sleep(1)
    Bip_aleatorio()
    os.system('code')
    print("Execusão concluida!")
    

def abrirnavegador():
    '''Função utilizada para abrir o navegador padrão do sistema'''
    
    print("Carregando...")
    Bip_Carregamento()

    # Obter o navegador padrão
    navegador_default = os.popen('xdg-settings get default-web-browser').read().strip()

    # Mapear o arquivo .desktop para o nome do executável
    if "vivaldi" in navegador_default:      #recomendo definir o caminho do executavel manualmente para o vivaldi, outros navegadores executarão sem problemas
        navegador_executavel = "vivaldi"
    elif "firefox" in navegador_default:
        navegador_executavel = "firefox"
    elif "chrome" in navegador_default:
        navegador_executavel = "google-chrome"
    else:
        print(f"Não foi possível identificar o navegador padrão: {navegador_default}")
        return

    print(f"Abrindo o navegador: {navegador_executavel}")
    os.system(navegador_executavel)



def abrirmensageiro():
    '''Função para abrir o Watsie, cliente do whatsapp para o linux'''
    
    print("Processando...")
    Bip_aleatorio()  # A chamada correta para o som aleatório
    os.system('whatsie &')  # Executa o aplicativo 'whatsie' em segundo plano
    time.sleep(3)  # Aguarda 3 segundos para garantir que o app abriu

    # Simula pressionar Ctrl + C
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    
    print("Tarefa concluída com sucesso!")
    
    
def abrirdiscord():
    '''Função utilizada para abrir o Discord'''
    
    print("Processando...")
    Bip_aleatorio()
    os.system('discord')
    print("Tarefa concluída com sucesso!")
    
    
def abrirficheiro():
    '''Função utilizada para abrir o gerenciardor de arquivos do sistema'''
    
    print("Processando...")
    Bip_aleatorio()
    
    # Simula pressionar Ctrl + C
    keyboard = Controller()
    keyboard.press(Key.Meta)
    keyboard.press('E')
    print("Tarefa concluida com sucesso!")
    
def abrirkrita():
    '''Função utilizada para abrir o Krita'''
    print("Processando...")
    Bip_aleatorio()
    os.system('krita')
    print("Tarefa executada com sucesso!")
    
    

def alternarjanela():
    '''Função responsavel por alternar as janelas abertas na área de trabalho'''
    
    print("Processando...")
    Bip_aleatorio()
    keyboard = Controller()
    # Simula a combinação Alt + Tab para alternar janelas
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    # Libera as teclas para finalizar a ação
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)

# funções de controle de multimidia para o YouTube no navegador vivaldi

'''def avançar():
   
    
    print("Processando...")
    Bip_aleatorio()
    keyboard = Controller()
    keyboard.press('l')
    
def retroceder():
    
    
    print("Processando...")
    Bip_aleatorio()
    keyboard = Controller()
    keyboard.press('j')
    
def pausa():
   
    print('Processando...')
    Bip_aleatorio()
    keyboard = Controller()
    keyboard.press('k')
    
def reproduzir():
    
    
    print('Processando...')
    Bip_aleatorio()
    keyboard = Controller()
    keyboard.press('k')'''

    
    
#funções para controle de multimidia com atalhos do teclado
#funciona com KDE Conect

def proximamusica():
    '''Função responsável por pular a
    música no smartphone 
    com o KDE Connect 
    atráves dos atalhos do teclado'''
    
    print('Processando...')
    Bip_aleatorio()
    os.system('playerctl next')
    print('Tarefa executada com sucesso!')
    
def musicaanterior():
    '''Função responsável por voltar a
    música no smartphone 
    com o KDE Connect 
    atráves dos atalhos do teclado'''
    
    print('Processando...')
    Bip_aleatorio()
    os.system('playerctl previous')
    os.system('playerctl previous')
    print('Tarefa executada com sucesso!')
    
def pararmusica():
    '''Função responsável por pausar a
    música no smartphone 
    com o KDE Connect 
    atráves dos atalhos do teclado'''
    
    print('Processando...')
    Bip_aleatorio()
    os.system('playerctl play-pause')
    print('Tarefa executada com sucesso!')
    
def reproduzirmusica():
    '''Função responsável por reproduzir a
    música no smartphone 
    com o KDE Connect 
    atráves dos atalhos do teclado'''
    
    print('Processando...')
    Bip_aleatorio()
    os.system('playerctl play-pause')
    print('Tarefa executada com sucesso!')
    

def fechar():
    '''Função responsável por Finalizar o programa atraves dos atalhos do teclado'''
    
    pyautogui.press('Ctrl' + 'c')
    #Bip_logout()
    print("Sistema encerrado.")
    
      

    
           
    
    
    
    
    
    
    
 # Verifica se o texto contém "paz do senhor"
#if "paz do senhor" in recognized_text:
 #       print("Deus abençoe")"""