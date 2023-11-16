from textblob import TextBlob
import random
from frases import frases_felizes, frases_tristes, frases_bravas, frases_ambiguas
from crauler import translate_word

def analisar_sentimento(texto):
    """
    Analisa o sentimento e a subjetividade do texto.
    """
    analise = TextBlob(texto)
    return analise.sentiment.polarity, analise.sentiment.subjectivity

def escolher_frase(sentimento, subjetividade):
    """
    Escolhe uma frase com base no sentimento e na subjetividade.
    """
    if sentimento > 0.2:
        if subjetividade > 0.5:
            return random.choice(frases_felizes)
        else:
            return "um planeta de serenidade, com harmonia e paz"
    elif -0.2 < sentimento <= 0.2:
        return random.choice(frases_ambiguas)
    else:
        if subjetividade > 0.5:
            return random.choice(frases_bravas)
        else:
            return random.choice(frases_tristes)

def gerar_descricao_planeta(frase):
    """
    Gera uma descrição imaginativa de um planeta.
    """
    return f"Cleberson: Em sua jornada, você descobre {frase}."

print('Coloque o que você sente sobre explorar planetas')
i = 1
while i == 1:
    texto_usuario = input('Eu:')
    if texto_usuario != 'sair':
        texto_usuario = (translate_word(texto_usuario))
        polaridade, subjetividade = analisar_sentimento(texto_usuario)

        frase_escolhida = escolher_frase(polaridade, subjetividade)
        descricao_planeta = gerar_descricao_planeta(frase_escolhida)
        print(descricao_planeta)
    else:
        i += 1