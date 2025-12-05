from message_analyzer import analisar_mensagem
from link_checker import verificar_url
import os

def exibir_guia(secao):
    """Lê o arquivo guia-anti-golpe.md e exibe a seção relevante."""
    # Define o caminho do arquivo de forma segura, independente de onde o script é rodado
    caminho_guia = os.path.join(os.path.dirname(__file__), 'docs', 'guia-anti-golpe.md')
    
    try:
        with open(caminho_guia, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print("⚠️ Erro: Arquivo do guia (docs/guia-anti-golpe.md) não encontrado.")
        return

    # A divisão do arquivo Markdown é feita usando o separador '---'
    partes = conteudo.split('---')
    
    if secao == "golpes_comuns":
        # Parte 1: Golpes Mais Comuns (após o primeiro '---', índice 1)
        print("\n" + partes[1].strip())
    
    elif secao == "como_proteger":
        # Parte 2: Checklist de Segurança (após o segundo '---', índice 2)
        print("\n" + partes[2].strip())


def menu():
    while True:
        print("\n========== AntiGolpe IA ==========")
        print("1) Verificar um link")
        print("2) Analisar mensagem suspeita")
        print("3) Ver golpes mais comuns")
        print("4) Como se proteger")
        print("5) Sair")
        opcao = input("> ")

        if opcao == "1":
            url = input("Cole o link: ")
            print(verificar_url(url))

        elif opcao == "2":
            msg = input("Cole a mensagem suspeita: ")
            try:
                resultado = analisar_mensagem(msg)
                print("\n--- Resultados Técnicos ---")
                print(resultado["indicadores"])
                print("\n--- Análise com IA ---")
                print(resultado["analise_ia"])
            except Exception as e:
                print(f"❌ Erro ao rodar análise de IA: {e}")
                print("Verifique se sua chave da OpenAI está correta no ai_engine.py.")

        elif opcao == "3":
            exibir_guia("golpes_comuns")

        elif opcao == "4":
            exibir_guia("como_proteger")

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()