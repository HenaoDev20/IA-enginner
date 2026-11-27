# primera_llamada.py
import os

from openai import OpenAI

cliente = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

respuesta = cliente.chat.completions.create(
    model=os.environ["MODELO"],
    temperature=0,
    messages=[
        {"role": "system", "content": "Respondes en español de Colombia, en máximo tres frases."},
        {"role": "user", "content": "¿Qué es una API y para qué sirve?"},
    ],
)


print(respuesta.choices[0].message.content)
print("Tokens usados:", respuesta.usage.total_tokens)