import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("É necessário escolher pelo menos um tipo de caractere para gerar a senha.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Alterar parametros desejados no tamanho com numeros inteiros ou com True ou False nos demais parametros
senha = gerar_senha(tamanho=16, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True)
print("Senha gerada:", senha)
