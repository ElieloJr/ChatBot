import openai
import requests

from openai import OpenAIError


# Inicializa o cliente OpenAI com a sua chave de API
# A chave de API pode ser passada diretamente ou lida da variável de ambiente OPENAI_API_KEY
client = openai.OpenAI(api_key="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")

#Função para gerar texto a partir do modelo de liguaguem

def gera_texto(texto):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Você é a Xanete, uma assistente virtual simpática e prestativa da empresa Kubiko."},
                {"role": "user", "content": texto}
            ],
            model="gpt-3.5-turbo",
            max_tokens = 150,
            n = 1,
            temperature = 0.8,
        )
        # Retorna o conteúdo da resposta se a chamada à API for bem-sucedida
        return response.choices[0].message.content.strip()
    # Captura qualquer exceção que ocorra durante a chamada à API
    except OpenAIError as e:
        # Imprime o erro no console (opcional, para debug)
        print(f"Ocorreu um erro ao chamar a API da OpenAI: {e}")
        
        # Retorna uma mensagem de erro para o usuário
        return "Desculpe, não consegui gerar uma resposta no momento. Por favor, tente novamente mais tarde."
    # Você pode adicionar outros tipos de exceções aqui se souber que outros erros específicos podem ocorrer.
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")
        return "Ocorreu um erro inesperado. Por favor, tente novamente mais tarde."


#Função principal do programa em Python
def main():

    print("\nOlá me nome é Xanete, como posso ajudar hoje?")
    print("www.kubiko.com.ao")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    #Loop
    while True:

        #Coleta a pergunta digitada pelo usuário.
        user_message = input("\nVocê: ")

        #Se a mensagem digitatda pelo usuário for "sair", finalizar o programa.

        if user_message.lower() == "sair":
            break

        #Colocar a menasgem digitada pelo usuário na váriavel Python chamada gpt4_prompt
        # Ajuste o prompt para ser apenas a mensagem do usuário, pois o role 'user' já indica isso
        gpt_prompt = user_message

        #Obtém a resposta do modelo executando a fução gera-texto().
        xanete_response = gera_texto(gpt_prompt)

        #Imprime a resposta do chatbot.
        print(f"\nXanete: {xanete_response}")
        #Execução do progarama (bloco main) em Python
if __name__ == "__main__":
    main()
