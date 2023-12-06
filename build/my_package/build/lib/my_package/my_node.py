import re
# dicionário de intenções
intent_dict = {
    r'Vá para (.+)': 'mover',
    r'Me leve para (.+)': 'mover'
}
# função de movimento do robô (substitua isso com sua lógica real)
def mover_robo_para_destino(destino):
    print(f"Movendo para {destino}")
# dicionário de ações
action_dict = {
    'mover': mover_robo_para_destino
}
# função principal do chatbot
def processar_comando(comando):
    for pattern, intent in intent_dict.items():
        match = re.match(pattern, comando)
        if match:
            acao = action_dict.get(intent)
            if acao:
                acao(match.group(1))
                return f"Ação {intent} compreendida e executada. Movendo para {match.group(1)}"
    return "Comando não compreendido."
# exemplo de uso
comando_usuario = "Me leve para a biblioteca"
resposta = processar_comando(comando_usuario)
print(resposta)