import pyautogui as py
import time

print("Posicione o mouse sobre o perfil do Chrome que você quer selecionar...")
time.sleep(5)  # 5 segundos para você posicionar o mouse

# Pega a posição atual do mouse
x, y = py.position()
print(f"Coordenadas encontradas: ({x}, {y})")
print("Agora você pode usar essas coordenadas no seu script")
