# Importar a biblioteca Flet
import flet as ft

# Criar a função principal que será executada pelo aplicativo
def main(pagina):
    # Definir o título da aplicação
    titulo = ft.Text("EchoChat")
    
    # Função para exibir mensagens enviadas por outros usuários no chat
    def enviar_mensagem_tunel(mensagem):
        # Cria um elemento de texto com a mensagem recebida
        texto = ft.Text(mensagem)
        # Adiciona o texto ao controle de chat
        chat.controls.append(texto)
        # Atualiza a página para refletir as mudanças
        pagina.update()
        
    # Inscrever a função acima para receber mensagens através do pubsub
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        
    # Função para enviar mensagens ao chat
    def enviar_mensagem(evento):
        # Captura o nome do usuário e a mensagem digitada
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        # Envia a mensagem para todos os usuários conectados
        pagina.pubsub.send_all(mensagem)

        # Limpa o campo de entrada de mensagem e atualiza a página
        campo_enviar_mensagem.value = ""
        pagina.update()
        
    # Campo de entrada de texto para mensagens e botão para enviar
    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])  # Organiza o campo e botão em linha
    
    # Contêiner para exibir o histórico de mensagens do chat
    chat = ft.Column()
    
    # Função executada ao entrar no chat
    def entrar_chat(evento):
        # Fecha o popup de entrada e remove elementos iniciais da página
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        # Adiciona o histórico do chat e os controles de envio à página
        pagina.add(chat)
        pagina.add(linha_enviar)
        
        # Envia uma mensagem indicando que o usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        
    # Configurações do popup inicial para entrada do nome do usuário
    titulo_popup = ft.Text("Bem vindo ao EchoChat")  # Título do popup
    caixa_nome = ft.TextField(label="Digite o seu nome")  # Campo para o nome do usuário
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)  # Botão para confirmar entrada
    
    # Configuração do popup como um AlertDialog
    popup = ft.AlertDialog(
        title=titulo_popup, 
        content=caixa_nome, 
        actions=[botao_popup]
    )
    
    # Função para abrir o popup inicial
    def abrir_popup(evento):
        pagina.dialog = popup  # Define o popup como o diálogo ativo da página
        popup.open = True  # Abre o popup
        pagina.update()
        
    # Botão inicial para iniciar o chat
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    # Adiciona elementos iniciais à página
    pagina.add(titulo)
    pagina.add(botao)

# Executa a função principal com o Flet, exibindo no navegador web
ft.app(main, view=ft.WEB_BROWSER)

      