# importa a biblioteca gradio e outras dependências
import gradio as gr
# importa o modelo de linguagem natural ollama
from langchain.llms import Ollama
# importa a biblioteca requests para fazer solicitações http
import requests
# importa a biblioteca json para manipulação de dados json
import json

# define a função para enviar solicitação para o modelo ollama
def send_request(question):
    url = "http://localhost:11434/api/generate"

    # dados a serem enviados no corpo da solicitação
    data = {
        "model": "security-expert",
        "prompt": question,
        "stream": False
    }
    # faz a solicitação post usando a biblioteca requests
    response = requests.post(url, json=data)

    # verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # exibe a resposta do servidor
        response = vars(response)
        response['_content'] = json.loads(response["_content"].decode('utf-8'))

        # retorna a resposta do modelo Ollama
        return str(response["_content"]["response"])

    else:
        # se a solicitação não for bem-sucedida, exibe uma mensagem de erro
        print(response.text)
        return f"Erro: {response.status_code}"

# função para gerar resposta do modelo GPT-3
def generate_response(prompt, chat_history):
    print('Making request...')
    response = send_request(prompt)
    print(response)
    chat_history.append((prompt, response))
    return "", chat_history

# cria uma interface Gradio com um chatbot
with gr.Blocks() as demo:
    title="LLM Chatbot"
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    # configura a função de callback quando uma mensagem é enviada
    msg.submit(generate_response, [msg, chatbot], [msg, chatbot])

# executa a interface gradio
if __name__ == "__main__":
    demo.launch()