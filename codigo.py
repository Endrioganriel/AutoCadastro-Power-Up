# Python Power Up: Automação de Tarefas
# Passo 1: Abrir o sistema da empresa
#    Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login

# Passo 3: Importar a base de dados dos produtos

# Passo 4: Cadastrar 1 produto

# Passo 5: Repetir o passo 4 ate acabar todos os produtos

# pip install pyautogui
# pyautogui.press -> pressionar uma tecla
# pyautogui.click -> clicar
# pyautogui.write -> escrever
# pyautogui.hotkey -> para atalhos(ex: ctrl, c)
import pyautogui 
import time
import pandas as pd

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")  
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=428, y=371)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pedir 3 segundos pra execuatar

time.sleep(3)

pyautogui.click(x=466, y=363)
pyautogui.write("endrio_gabriel@hotmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
tabela = pd.read_csv("produtos.csv")

time.sleep(3)


# Passo 4: Cadastrar 1 produto
# codigo,marca,tipo,categoria,preco_unitario,custo,obs
# MOLO000251,Logitech,Mouse,1,25.95,6.50,

for linha in tabela.index:

    pyautogui.click(x=415, y=246)#clic no 1 campo

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
   # if not pd.isna(obs):
     #   pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(1)#vou colocar esse time aqui pra nao correr risco de duplo clique
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim