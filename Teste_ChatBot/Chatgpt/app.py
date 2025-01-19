import openai as OpenAI


def Chatgpt():
    pergunta = input("Qual sua pergunta?")
    cliente = OpenAI.OpenAI();
    chat = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "oh my god"},
            {"role": "user", "content": pergunta }
        ]
    )

Chatgpt();