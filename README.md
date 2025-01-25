# EchoChat 💬  

**EchoChat** é um aplicativo de bate-papo simples, colaborativo e em tempo real, desenvolvido com Python e utilizando a biblioteca Flet. Ele permite que os usuários enviem e recebam mensagens instantaneamente, oferecendo uma interface web interativa e amigável.

---

## Visão Geral do Projeto 📝  

### Objetivos Principais  
1. **Facilidade de Comunicação em Tempo Real**:  
   - Permitir o envio e recebimento de mensagens instantâneas entre usuários conectados.  
   - Manter o histórico de mensagens visível para todos os participantes.  

2. **Experiência Interativa**:  
   - Oferecer uma interface simples para envio de mensagens.  
   - Possibilitar a personalização do nome de usuário ao entrar no chat.  

---

## Pré-Requisitos 🛠️  

Antes de executar o script, certifique-se de ter o Python e a biblioteca Flet instalados no seu ambiente.  

### Passos para Instalação 🖥️  
1. **Instalar o Python**:  
   - Baixe e instale o Python no site oficial: [python.org](https://www.python.org/). 🐍  

2. **Instalar a Biblioteca Flet**:  
   - Use o comando abaixo para instalar o Flet:  
     ```bash
     pip install flet
     ```  

---

## Como Usar o EchoChat ⚡  

1. **Configuração Inicial**:  
   - Certifique-se de que as dependências estão instaladas.  

2. **Executar o Script**:  
   - Salve o código fornecido em um arquivo `EchoChat.py` ou.  
   - Execute o arquivo com o comando:  
     ```bash
     python EchoChat.py
     ```
    - Também pode ser executado diretamente no VS Code.

3. **Acessar o Chat**:  
   - O aplicativo será aberto automaticamente no navegador padrão.  
   - Insira seu nome no popup inicial e clique em "Entrar no Chat".  

4. **Enviar Mensagens**:  
   - Digite uma mensagem no campo de texto e clique em "Enviar".  
   - As mensagens enviadas por todos os participantes serão exibidas em tempo real.  

---

## Estrutura do Script 🧩  

1. **Interface Inicial**:  
   - Exibe um botão "Iniciar Chat".  
   - Ao clicar, abre um popup para entrada do nome do usuário.  

2. **Histórico de Chat**:  
   - Exibe todas as mensagens enviadas no chat em um formato de lista.  

3. **Envio de Mensagens**:  
   - Permite enviar mensagens através de um campo de texto e botão.  

4. **Comunicação em Tempo Real**:  
   - Utiliza o sistema `pubsub` do Flet para sincronizar mensagens entre usuários conectados.  

---

## Resultados Esperados 🎉  

- **Comunicação Eficiente**:  
  - Mensagens são entregues e exibidas instantaneamente para todos os participantes.  

- **Interface Simples**:  
  - Fácil de usar, com foco na experiência do usuário.  

---

## Melhorias Futuras 💡  

1. **Suporte a Emojis e Formatação de Texto**:  
   - Adicionar suporte para emojis e estilos de texto (negrito, itálico).  

2. **Notificações de Novos Usuários**:  
   - Exibir alertas quando um novo usuário entra no chat.  

3. **Tema Personalizável**:  
   - Permitir que os usuários escolham temas escuros ou claros.  

4. **Versão Mobile**:  
   - Otimizar a interface para dispositivos móveis.  

---

## Observações Importantes ⚠️  

- **Requisitos de Rede**:  
  - Certifique-se de que a rede permite conexões locais para múltiplos usuários.  

- **Limitações de Escalabilidade**:  
  - Este projeto foi projetado para fins de estudos e pode não suportar um número muito alto de usuários simultâneos.  

---  
