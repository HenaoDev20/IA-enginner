# primera_llamada.py
import os
from openai import OpenAI

cliente = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

modelos_list = [
    "nvidia/nemotron-3.5-lightning:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
]

for modelo in modelos_list:
    respuesta = cliente.chat.completions.create(
        model=modelo,
        temperature=0,
        messages=[
            {"role": "system", "content": "Respondes en español de Colombia, en máximo tres frases."},
            {"role": "user", "content": "¿Qué es POO, para que sirve y como lo explicarias a alguien que es nuevo en el tema?"},
        ],
    )

    print("Modelo:", modelo)
    print(respuesta.choices[0].message.content)
    print("Tokens usados:", respuesta.usage.total_tokens)
    print("-" * 60)


