import google.generativeai as gemini
Key = "AIzaSyC-9oOoUxE0v13DNuE37qBzClAfhJrxRJs"
gemini.configure(api_key=Key)
meta = "musculoso"


modelo = gemini.GenerativeModel("gemini-1.5-flash")
# Ia = modelo.generate_content("Qual dia de hoje?")

chat = modelo.start_chat(history=[])

pergunta = input("Qual sua dúvida?\n")

while pergunta != "end":
    resposta = chat.send_message(pergunta, generation_config=gemini.GenerationConfig(max_output_tokens=150,temperature=0.2))
    print(resposta.text)
    pergunta = input("Pussuí outra dúvida?\n")