import tkinter as tk
import paho.mqtt.client as mqtt
import json

# Configurações do Broker MQTT
broker_address = "gwqa.revolog.com.br"
broker_port = 1884
user = "tecnologia"
password = "128Parsecs!"

# Criação do cliente MQTT
client = mqtt.Client()
client.username_pw_set(user, password)
client.connect(broker_address, broker_port)

def enviar_mensagem():
    mensagem = entrada_string.get()

    if opcao_var.get() == opcao_direita["onvalue"]:
        right=1
        left=0
    else:
        right=0
        left=1

    dados = {
        "id":1,
        "left":left,
        "right":right,
        "plate": mensagem,
        "data":[]
    }
    mensagem_json = json.dumps(dados)
    
    # Envio da mensagem ao broker MQTT
    client.publish("arcelor/message", mensagem_json)

    # Exibir mensagem de sucesso
    sucesso_label.config(text="Mensagem enviada com sucesso!")

# Criação da interface gráfica
root = tk.Tk()
root.title("Envio de mensagem MQTT")

frame = tk.Frame(root)
frame.pack(padx=30, pady=30)

# Campo para entrada da string
entrada_string = tk.Entry(frame)
entrada_string.pack(pady=30)

# Opções de seleção (Direita e Esquerda)
opcao_var = tk.IntVar()
opcao_direita = tk.Checkbutton(frame, text="Direita", variable=opcao_var, onvalue=1, offvalue=0)
opcao_esquerda = tk.Checkbutton(frame, text="Esquerda", variable=opcao_var, onvalue=0, offvalue=1)
opcao_direita.pack()
opcao_esquerda.pack()

# Criação do label para exibir a mensagem de sucesso
sucesso_label = tk.Label(frame, text="")
sucesso_label.pack(pady=30)

def fechar_janela():
    # Desconecta o cliente MQTT ao fechar a aplicação
    client.disconnect()
    root.destroy()

# Botão Enviar
botao_enviar = tk.Button(frame, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(pady=30)

# Evento para fechar a janela
root.protocol("WM_DELETE_WINDOW", fechar_janela)

root.mainloop()
