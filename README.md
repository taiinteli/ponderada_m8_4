# Documentação Chatbot

### Link do vídeo de funcinamento: https://youtu.be/lRWYc__x8dM?feature=shared

### Visão Geral
O chatbot simples é um componente destinado a interpretar comandos de texto e executar ações associadas a esses comandos. Ele foi projetado para integração em sistemas baseados em ROS 2.

### Principais Funcionalidades
Interpretação de Comandos: O chatbot analisa comandos de texto usando padrões predefinidos e associa esses comandos a intenções específicas.

Execução de Ações: Com base nas intenções identificadas, o chatbot executa ações correspondentes. No exemplo fornecido, a ação é mover o robô para um destino especificado. No exemplo do vídeo o destino foi a biblioteca. 

### Instalação 

1. Clone o repositório 

```git clone https://github.com/taiinteli/ponderadas_m8.git```

2. Navegue para o diretório do pacote:

```cd ponderadas_m8```

3. Construção do pacote: 

```colcon build```

4. Ativamento do ambiente 

```source install/setup.bash```

5. Executar o Chatbot: 

``ros2 run my_package chatbot``
