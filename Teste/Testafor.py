import random
import os
import tkinter as tk

palavras = ['Marcos', 'Leandro', 'Denis', 'Alice']  # Lista de palavras

# Função para escolher uma palavra aleatória
def palavra_aleatoria():
    return random.choice(palavras).lower()

# Função para exibir o estado atual da palavra
def exibir_palavra():
    estado = ''.join(letra if letra in letras_advinhadas else '_' for letra in palavra_atual)
    estado_label.config(text=estado)
    tentativas_label.config(text=f"Tentativas restantes: {tentativas}")
    
    if all(letra in letras_advinhadas for letra in palavra_atual):
        resultado_label.config(text=f"Parabéns! Você acertou a palavra! Era: {palavra_atual.capitalize()}")
        entrada_letra.config(state='disable')
        
    elif tentativas == 0:
        resultado_label.config(text=f"Você perdeu! A palavra era: {palavra_atual.capitalize()}")
        entrada_letra.config(state='disable')

# Função que é chamada ao fazer um palpite
def palpites():
    global tentativas
    letra = entrada_letra.get().lower()  # Obtém o valor da entrada
    entrada_letra.delete(0, tk.END)  # Limpa o campo de entrada
    
    if letra and letra not in letras_advinhadas:
        letras_advinhadas.append(letra)
        if letra not in palavra_atual:
            tentativas -= 1
        exibir_palavra()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global tentativas, palavra_atual, letras_advinhadas
    tentativas = 6
    letras_advinhadas = []
    palavra_atual = palavra_aleatoria()
    exibir_palavra()

# Criando a janela principal
root = tk.Tk()
root.title("Jogo da Forca")

# Variáveis do jogo
tentativas = 6
letras_advinhadas = []
palavra_atual = palavra_aleatoria()

# Layout dos componentes
estado_label = tk.Label(root, text="", font=('Arial', 20))
estado_label.pack()

tentativas_label = tk.Label(root, text=f"Tentativas restantes: {tentativas}", font=('Arial', 15))
tentativas_label.pack()

entrada_letra = tk.Entry(root, font=('Arial', 15))
entrada_letra.pack()

adivinhar_button = tk.Button(root, text="Adivinhar", command=palpites, font=('Arial', 15))
adivinhar_button.pack()

reiniciar_button = tk.Button(root, text="Reiniciar Jogo", command=reiniciar_jogo, font=('Arial', 15))
reiniciar_button.pack()

resultado_label = tk.Label(root, text="", font=('Arial', 15))
resultado_label.pack()

# Inicializa o estado da palavra
exibir_palavra()

# Executa o loop da interface gráfica
root.mainloop()
        