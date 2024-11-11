# 1.2.1

def corrigir_palavra(palavra):
    x = 1
    tamanho = len(palavra) - 1
    while x <= tamanho:
        # Uma vez que os códigos numéricos das letras maiúsculas e das minúsculas correspondentes diferem em 32:
        if ord(palavra[x]) == ord(palavra[x-1]) + 32 or ord(palavra[x]) + 32 == ord(palavra[x-1]):
            if x - 1 == 0:
                palavra = palavra[x + 1:]
            else:
                palavra = palavra[:x-1] + palavra[x+1:]
                x = x-1
        else:
            x += 1
        tamanho = len(palavra) - 1
    return palavra


# 1.2.2

def eh_anagrama(cadeia1, cadeia2):
    lista1 = list(cadeia1)
    for x in range(len(lista1)):
        if ord(lista1[x]) > 96:
            lista1[x] = chr(ord(lista1[x])-32)
    lista1 = sorted(lista1)

    lista2 = list(cadeia2)
    for y in range(len(lista2)):
        if ord(lista2[y]) > 96:
            lista2[y] = chr(ord(lista2[y]) - 32)
    lista2 = sorted(lista2)
    return lista1 == lista2


# 1.2.3

def corrigir_doc(texto):
    for car in texto:
        if ord(car) == 32 or 65 <= ord(car) <= 90 or 97 <= ord(car) <= 122:
            for indice in range(len(texto) - 1):
                if ord(texto[indice + 1]) == 32 and ord(texto[indice]) == 32:
                    raise ValueError("corrigir_doc: argumento invalido")
        else:
            raise ValueError("corrigir_doc: argumento invalido")
    texto = corrigir_palavra(texto)
    return texto

"""
    for indice1 in range(len(texto)):
        while ord(texto[indice1]) != 32:
            indice1 += 1
        cadeia1 = texto[:indice1]
        cadeia2 = texto[indice1 + 1:]
        break
    for x in range(len(cadeia2)):
        if ord(cadeia2[x]) == 32:
            cadeia_elim = cadeia2[:x]
        if eh_anagrama(cadeia1, cadeia_elim) == True:
            cadeia2 = cadeia2[x+1:] + cadeia2[:x]
            x=0
"""


# 2.2.1

def obter_posicao(caracter, inteiro):
    if caracter == "C" and inteiro not in (1, 2, 3):
        inteiro = inteiro - 3

    if caracter == "B" and inteiro not in (7, 8, 9):
        inteiro = inteiro + 3

    if caracter == "E" and inteiro not in (1, 4, 7):
        inteiro = inteiro - 1

    if caracter == "D" and inteiro not in (3, 6, 9):
        inteiro = inteiro + 1

    return inteiro


# 2.2.2

def obter_digito(cadeia, inteiro):
    for car in cadeia:
        inteiro = obter_posicao(car, inteiro)

    return inteiro


# 2.2.3

def obter_pin(tuplo):
    pin = ()
    if type(tuplo) != tuple or len(tuplo) < 4 or len(tuplo) > 10:
        raise ValueError("obter_pin: argumento inválido")
    for x in range(len(tuplo)):
        for letra in tuplo[x]:
            if type(letra) != str or letra not in ("B", "C", "E", "D"):
                raise ValueError("obter_pin: argumento inválido")
        pin = pin + (obter_digito(tuplo[x], 5), )
    return pin


# 3.2.1

def valida_entrada(entrada):
    return type(entrada) == tuple and type(entrada[0]) == str and type(entrada[1]) == list and type(entrada[2]) == tuple

def valida_letra(car):
    return 97 <= ord(car) <= 122

def eh_entrada(entrada):

    # Validação da cifra
    if valida_entrada(entrada):
        for car_cifra in entrada[0]:
            if valida_letra(car_cifra) or ord(car_cifra) == 45:

                # Validação da estrutura de controlo
                for car_controlo in entrada[1]:
                    if valida_letra(car_controlo):

                        # Validação da sequência de segurança
                        if len(entrada[2]) >= 2:
                            for num in entrada[2]:
                                if type(num) == int and num > 0:
                                    return True
    return False


# 3.2.2
def validar_cifra(cifra, controlo):
    dicionario = {}
    lista = []
    string = ""
    for caracter in cifra:
        if valida_letra(caracter):
            if caracter not in dicionario:
                dicionario[caracter] = 1
            else:
                dicionario[caracter] += 1
    for chave in dicionario:
        lista += [chave]
    for x in range(len(lista)):
        for y in range(len(lista)):
            if y > x:
                if dicionario[lista[x]] < dicionario[lista[y]] or dicionario[lista[x]] == dicionario[lista[y]] and ord(lista[x]) > ord(lista[y]):
                    lista[x], lista[y] = lista[y], lista[x]
    if len(lista) >= 5:
        lista = [lista[: 5]]
    for letra in lista:
        string += str(letra)
    return [string] == controlo

# 3.2.3
def filtrar_bdb(lista):
    res = []
    for entrada in lista:
        if not eh_entrada(entrada):
            raise ValueError("filtrar_bdb: argumento invalido")
        if not validar_cifra(entrada[0], entrada[1]):
            res += [entrada]
    return res

# 4.2.1


# 4.2.2
def obter_num_seguranca(tuplo):
    nums = []
    for x in range(len(tuplo)):
        for y in range(len(tuplo)):
            if x != y:
                if tuplo[x] > tuplo[y]:
                    nums += [x-y]
                elif tuplo[x] < tuplo[y]:
                    nums += [y - x]
                else:
                    return 0
    for z in range(len(nums) - 1):
        if nums[z+1] > nums[0]:
            nums[0] = nums[z+1]
    return nums[0]

# 4.2.3
def decifrar_texto(cifra, num):
    cifra = list(cifra)
    string = ""
    for x in range(len(cifra)):
        if cifra[x] == "-":
            cifra[x] = " "
        else:
            if x % 2 == 0:
                cod_num = ord(cifra[x])
                num = num % 26 + 1
                if cod_num + num > 122:
                    cifra[x] = cod_num + num - 26
            else:
                cod_num = ord(cifra[x])
                num = num % 26 - 1
                if cod_num + num > 122:
                    cifra[x] = cod_num + num - 26
    for simbolo in cifra:
        string += simbolo
    return string

# 4.2.4
def decifrar_bdb(lista):
    resultado = []
    for entrada in lista:
        if not eh_entrada(entrada):
            raise ValueError("decifrar_bdb: argumento invalido")
        num = obter_num_seguranca(entrada[2])
        resultado += [decifrar_texto(entrada[0], num)]
    return resultado

# 5.2.1
def eh_utilizador(dicionario):
    return type(dicionario) == dict and dicionario["name"] != "" and dicionario["pass"] != "" and type(dicionario["rule"]["vals"]) == tuple and len(dicionario["rule"]["vals"]) == 2 and valida_letra(dicionario["rule"]["char"])

# 5.2.2
def eh_senha_valida(senha, regra_ind):
    cont = 0
    rule = 0
    for x in range(len(senha)):
        if valida_letra(senha[x]):
            cont += 1
    for x in range(len(senha) - 1):
        if senha[x+1] == senha[x] and cont >= 3:
            for x in range(len(senha)):
                if senha[x] == regra_ind["char"]:
                    rule += 1
            if regra_ind["vals"][0] <= rule <= regra_ind["vals"][1]:
                return True
    return False