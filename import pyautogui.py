import pyautogui as py
import time


py.click
# Aumentando o tempo de pausa entre comandos para 1 segundo
py.PAUSE = 1.0
py.hotkey('win', 'r')
time.sleep(1)
py.write('notepad')
time.sleep(1)
py.press('enter')
time.sleep(1)
py.hotkey('ctrl', 'v')
# Definindo uma função para mover e clicar com mais precisão
#def move_and_click(x, y):
    # Primeiro move o cursor para a posição
 #   py.moveTo(x=1313, y=663, duration=0.5)  # Movimento mais suave
    # Aguarda um pouco para garantir que o cursor chegou
 #   time.sleep(0.5)
    # Clica
 #   py.click()
    # Aguarda mais um pouco para garantir que o clique foi registrado
 #   time.sleep(0.5)

# Testando o movimento para a posição (1231, 49)
move_and_click(x=1231, y=49)

# Você pode adicionar mais movimentos e cliques aqui

# print(py.onScreen(x=1919, y=1080))
# move_and_click(outra_posicao_x, outra_posicao_y)

# Abri um site

#clicar em algum elemento
# digitar algo
# clicar em algum elemento
#fechar o site