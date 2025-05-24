import pyautogui as py
import time
import os

# Configuração
py.PAUSE = 1
py.FAILSAFE = True

# Espera para você posicionar o mouse sobre o perfil
print("Posicione o mouse sobre o perfil do Chrome que você quer selecionar...")
time.sleep(5)  # 5 segundos para você posicionar o mouse

# Pega a posição atual do mouse
x, y = py.position()
print(f"Posição do mouse: ({x}, {y})")

# Tira uma captura de tela da área ao redor do mouse
# Vamos capturar uma área de 50x50 pixels ao redor do mouse
box = (x-25, y-25, 50, 50)  # (x, y, largura, altura)

# Cria a pasta images se não existir
if not os.path.exists('images'):
    os.makedirs('images')

# Tira a captura de tela e salva como perfil_trabalho.png
py.screenshot('images/perfil_trabalho.png', region=box)
print("Captura de tela salva como images/perfil_trabalho.png")

# Mostra a imagem para você confirmar
print("Mostrando a imagem capturada...")
py.screenshot('images/perfil_trabalho.png', region=box).show()
