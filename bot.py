import pyautogui 
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=678, y=415)
pyautogui.write("python@gmail.com")

#preencher senha
pyautogui.press("tab")
pyautogui.write("senha")

#botao logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#importa base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:
    pyautogui.click(x=715, y=282)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #passar para o proxim campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo =  str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs =  str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab ") #passou para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)