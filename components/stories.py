import gradio as gr
import libs.constants as cnsts
from site_var import sys, Prompt_Master

def criar(prompt : str):
    print(prompt)
    if sys.chat == None: return "KEY INVALIDA"
    else:
        resposta = sys.chain.invoke({})
        dicionario : Prompt_Master = sys.parser.parse(resposta)
        return dicionario.history, dicionario.sheets, dicionario.timeline
        

with gr.Blocks() as windows_stories:
    sys.create_prompt()
    gr.Markdown("""### Digite os detalhes da sua história que ele irá cria-la, e separar os detalhes da timeline e dos personagens. No futuro também adicionaremos fazer isso com texto, e maneira incremental de fazer os prompts.""")
    entrada = gr.Textbox(lines=3, placeholder="Press Shift+Enter to send")

    gr.Markdown("# Resultado")

    historia = gr.Textbox(label="Narrativa", placeholder="Esperando o prompt", lines=5, interactive=False, autoscroll=True)
    with gr.Row() as saidas:
        personagens = gr.JSON(label="Personagens")
        timeline = gr.JSON(label="Timeline")

    entrada.submit(criar, [entrada], [historia, personagens, timeline])
    