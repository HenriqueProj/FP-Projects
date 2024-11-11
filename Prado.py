# TAD posicao:

# Construtor:

def cria_posicao(x, y):
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x,y)

def cria_copia_posicao(p):
    return p


# Seletores:

def obter_pos_x(p):
    return p[0]

def obter_pos_y(p):
    return p[1]


# Reconhecedor:

def eh_posicao(arg):
    return type(arg) == tuple and len(arg) == 2 and type(obter_pos_x(arg)) == int and \
           type(obter_pos_y(arg)) == int and obter_pos_x(arg) >= 0 and obter_pos_y(arg) >= 0


# Teste:

def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and eh_posicao(p2) and \
           obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)


# Transformador:

def posicao_para_str(p):
    return str(p)


# Funções de alto nível:

def obter_posicoes_adjacentes(p):
    tuplo = ()

    # Posição adjacente de cima:
    if obter_pos_y(p) > 0:
        tuplo += (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1), )

    # Posição adjacente da direita:
    tuplo += (cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), )

    # Posição adjacente de baixo:
    tuplo += (cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1), )

    # Posição adjacente da esquerda:
    if obter_pos_x(p) > 0:
        tuplo += (cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p)), )

    return tuplo

def ordenar_posicoes(t):
    lista_t = list(t)
    lista_t = sorted(lista_t, key = lambda x: (x[1], x[0]))

    return tuple(lista_t)


# TAD animal:

def cria_animal(s, r, a):
    if type(s) != str or type(r) != int or type(a) != int or \
            s == "" or r <= 0 or a < 0:
        raise ValueError("cria_animal: argumentos invalidos")

    # O 2o elemento corresponde à idade, o 3o elemento à reprodução e o 4o elemento à alimentação:
    if a == 0:
        return list((s, [0, r]))
    return list((s, [0, r], [0, a]))

def cria_copia_animal(a):
    b = [a[0]] + [a[1].copy()]
    if eh_predador(a):
        b += [a[2].copy()]
    return b


# Seletores:

def obter_especie(a):
    return a[0]

def obter_freq_reproducao(a):
    return a[1][1]

def obter_freq_alimentacao(a):
    if len(a) == 2:
        return 0
    return a[2][1]

def obter_idade(a):
    return a[1][0]

def obter_fome(a):
    if len(a) == 2:
        return 0
    return a[2][0]


# Modificadores:

def aumenta_idade(a):
    a[1][0] += 1
    return a

def reset_idade(a):
    a[1][0] = 0
    return a

def aumenta_fome(a):
    if len(a) > 2:
        a[2][0] += 1
    return a

def reset_fome(a):
    if len(a) > 2:
        a[2][0] = 0
    return a

# Reconhecedor:

def eh_animal(arg):
    # Condições extra para os predadores:
    if len(arg) == 3:
        if len(arg[2]) != 2 or type(obter_fome(arg)) != int or \
                obter_fome(arg) < 0 or type(obter_freq_alimentacao(arg)) != int or obter_freq_alimentacao(arg) <= 0:
            return False

    # Condições gerais:
    return (len(arg) == 2 or len(arg) == 3) and len(arg[1]) == 2 and type(obter_especie(arg)) == str and \
        obter_especie(arg) != "" and type(obter_idade(arg)) == int and obter_idade(arg) >= 0 and \
        type(obter_freq_reproducao(arg)) == int and obter_freq_reproducao(arg) > 0

def eh_predador(arg):
    return eh_animal(arg) and len(arg) == 3

def eh_presa(arg):
    return eh_animal(arg) and len(arg) == 2


# Teste:

def animais_iguais(a1, a2):
    return eh_animal(a1) and eh_animal(a2) and a1 == a2


# Transformadores:

def animal_para_char(a):
    # Obtém-se letra maiúscula para predadores e letra minúscula para presas:
    if eh_predador(a):
        if 97 <= ord(obter_especie(a)[0]) <= 122:
            return chr(ord(obter_especie(a)[0]) - 32)
        else:
            return obter_especie(a)[0]
    else:
        if 97 <= ord(obter_especie(a)[0]) <= 122:
            return obter_especie(a)[0]
    return chr(ord(obter_especie(a)[0]) + 32)

def animal_para_str(a):
    if eh_predador(a):
        string = str(obter_especie(a)) + " " + str([str(obter_idade(a)) + "/" + \
            str(obter_freq_reproducao(a)) + ";" + str(obter_fome(a)) + "/" + str(obter_freq_alimentacao(a))])
    else:
        string = str(obter_especie(a)) + " " + str([str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a))])

    # Retirar as plicas da string final:
    return string.replace("'", "")

# Funções de alto nível:

def eh_animal_fertil(a):
    return obter_idade(a) >= obter_freq_reproducao(a)

def eh_animal_faminto(a):
    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)

def reproduz_animal(a):
    reset_idade(a)
    cria = cria_copia_animal(a)
    if eh_predador(cria):
        reset_fome(cria)
    return cria


# TAD prado:

def cria_prado(d, r, a, p):

    # Condições para cada elemento:
    if type(d) != tuple or len(d) != 2 or type(r) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")

    # Condições para os elementos dentro dos elementos:
    if r != ():
        for rochedo in r:
            if type(rochedo) != tuple or len(rochedo) != 2:
                raise ValueError("cria_prado: argumentos invalidos")

    for animal in a:
        for posicao_2 in p:
            if not eh_animal(animal) or not eh_posicao(posicao_2) or not eh_posicao(d):
                raise ValueError("cria_prado: argumentos invalidos")

    return (d, r, a, p)

def cria_copia_prado(m):
    return m


# Seletores:

def obter_tamanho_x(m):
    return m[0][0] + 1

def obter_tamanho_y(m):
    return m[0][1] + 1

def obter_numero_predadores(m):
    cont = 0
    for animal in m[2]:
        if eh_predador(animal):
            cont += 1
    return cont

def obter_numero_presas(m):
    cont = 0
    for animal in m[2]:
        if eh_presa(animal):
            cont += 1
    return cont

def obter_posicao_animais(m):
    return ordenar_posicoes(m[3])

def obter_animal(m, p):
    for x in range(len(m[3])):
        if m[3][x] == p:
            return m[2][x]


# Modificadores:

def eliminar_animal(m, p):
    for x in range(len(m[2])):
        if obter_animal(m, p) == m[2][x]:
            m = m[:2] + (m[2][:x] + m[2][x+1:],) + (m[3][:x] + m[3][x+1:],)
            break
    return m

def mover_animal(m, p1, p2):
    for x in range(len(m[3])):
        if m[3][x] == p1:
            m = m[:3] + (m[3][:x] + (p2, ) + m[3][x+1:], )
            break
    return m

def inserir_animal(m, a, p):
    m = m[:2] + (m[2] + (a,), ) + (m[3] + (p,), )
    return m


# Reconhecedores:

def eh_prado(arg):
    if not eh_posicao(arg[0]) or type(arg[1]) != tuple or type(arg[2]) != tuple or arg[2] == () or \
            type(arg[3]) != tuple or arg[3] == ():
        return False
    for posicao in arg[1]:
        for animal in arg[2]:
            for posicao_2 in arg[3]:
                if not eh_posicao(posicao) or not eh_animal(animal) or not \
                        eh_posicao(posicao_2):
                    return False
    return True

def eh_posicao_animal(m, p):
    for posicao in m[3]:
        if posicao == p:
            return True
    return False

def eh_posicao_obstaculo(m, p):
    # Caso a posição corresponda a montanhas:
    if p[0] == 0 or p[1] == 0 or p[0] == m[0][0] or p[1] == m[0][1]:
        return True
    for rochedo in m[1]:
        if rochedo == p:
            return True
    return False

def eh_posicao_livre(m, p):
    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)

def prados_iguais(p1, p2):
    return p1 == p2


# Transformador:

def prado_para_str(m):
    x = 1
    y = 0
    prado = ""
    # Variável cond - caso uma coordenada possua um rochedo, não verifica se possui um animal nesse ponto,
    # evitando passos desnecessários
    cond = False

    # Limites superior e inferior do prado:
    while y <= m[0][1]:
        if y == 0 or y == m[0][1]:
            prado += "+"
            while x < m[0][0]:
                prado += "-"
                x += 1
            prado += "+"
            if y == 0:
                prado += "\n"

        else:
            prado += "|"
            while x < m[0][0]:
                if eh_posicao_obstaculo(m, (x,y)):
                    prado += "@"
                    cond = True

                if not cond:
                    # Verifica se a posição corresponde a algum animal:
                    for pos_animal in obter_posicao_animais(m):
                        if x == obter_pos_x(pos_animal) and y == obter_pos_y(pos_animal):
                            prado += animal_para_char(obter_animal(m, pos_animal))
                            cond = True

                # Caso a posição esteja livre:
                if not cond:
                    prado += "."
                cond = False
                x += 1
            prado += "|\n"
        y += 1
        x = 1
    return prado


# Funções de alto nível:

def obter_valor_numerico(m, p):
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)

def obter_movimento(m, p):
    cont = 0
    cont_presas = 0
    indice = 0
    adj = list(obter_posicoes_adjacentes(p))
    adj_presas = ()

    # Verificar se as posições adjacentes se encontram dentro dos limites do prado:
    for adjacente in adj:
        if obter_tamanho_x(m) < obter_pos_x(adjacente) or obter_tamanho_y(m) < obter_pos_y(adjacente):
            adj = adj[:indice] + adj[indice + 1:]

    len_adj = len(adj)

    # A presa só se move caso as posições adjacentes estejam livres:
    if eh_presa(obter_animal(m, p)):
        while indice <= len_adj - 1:
            if eh_posicao_livre(m, adj[indice]):
                cont += 1
            else:
                adj = adj[:indice] + adj[indice + 1:]
            if len(adj) == len_adj:
                indice += 1
            len_adj = len(adj)

    else:
        while indice <= len_adj - 1:
            # Caso exista uma presa na posição adjacente:
            if eh_posicao_animal(m, adj[indice]) and eh_presa(obter_animal(m, adj[indice])):
                adj_presas += (adj[indice],)
                cont_presas += 1

            # Caso esteja livre:
            elif eh_posicao_livre(m, adj[indice]):
                cont += 1

            # Só acontece se o predador estiver rodeado de óbstaculos ou outros predadores (não se move):
            else:
                adj = adj[:indice] + adj[indice + 1:]

            # Caso o animal não se mova, o índice não é atualizado, pois é removida a posição adjacente com esse índice:
            if len(adj) == len_adj:
                indice += 1
            len_adj = len(adj)

    # Restam assim as posições adjacentes livres, no sentido horário:
    # Caso seja predador e existam presas nas posições adjacentes, apenas essas posições contam:
    if cont_presas != 0:
        return adj_presas[obter_valor_numerico(m, p) % cont_presas]
    elif cont == 0:
        return p
    return adj[obter_valor_numerico(m, p) % cont]


# Funções adicionais:

def geracao(m):
    # pos_ords corresponde às posições dos animais ordenadas segundo a ordem de leitura:
    pos_ords = obter_posicao_animais(m)

    for posicao in pos_ords:

        # Caso o animal seja presa e tenha sido comido antes do seu turno, este é saltado:
        if not eh_posicao_animal(m, posicao):

            # Função continue passa ao próximo animal:
            continue

        animal = obter_animal(m, posicao)
        animal = aumenta_idade(animal)
        if eh_predador(animal):
            animal = aumenta_fome(animal)
            if eh_animal_faminto(animal):
                m = eliminar_animal(m, posicao)

                # Função continue passa ao próximo animal caso este seja removido do prado:
                continue

        # Caso o animal não fique na mesma posição, pode reproduzir-se ou, se predador, eliminar uma presa:
        if posicao != obter_movimento(m, posicao):

            if eh_predador(animal) and eh_posicao_animal(m, obter_movimento(m, posicao)) \
                and eh_presa(obter_animal(m, obter_movimento(m, posicao))):
                m = eliminar_animal(m, obter_movimento(m, posicao))
                animal = reset_fome(animal)

            nova_pos = obter_movimento(m, posicao)
            m = mover_animal(m, posicao, nova_pos)

            # Caso o animal se reproduza:
            if eh_animal_fertil(animal):
                m = inserir_animal(m, reproduz_animal(animal), posicao)

    return m

def simula_ecossistema(f, g, v):
    prado = ()
    f_string = open(f, "r")
    linhas = f_string.readline()
    acc = 0
    indice = 0
    final = ""

    while linhas != "" and linhas != "\n":
        tuplo = eval(linhas[: -1])

        # Linha 1:
        if type(tuplo[0]) == int:
            prado += (tuplo,)

        # Rochedos:
        elif type(tuplo[0]) == tuple:
            if len(prado) == 1:
                prado += (tuplo,)
            else:
                prado == prado[: 1] + (prado[1] + (tuplo[1], ), )

        # Animais:
        else:
            if len(prado) == 2:
                prado += ((cria_animal(tuplo[0], tuplo[1], tuplo[2]), ), )
                prado += ((tuplo[3], ), )

            else:
                prado = prado[:2] + (prado[2] + (cria_animal(tuplo[0], tuplo[1], tuplo[2]), ), ) + \
                        (prado[3] + (tuplo[3], ), )
        indice += 1
        linhas = f_string.readline()

    while acc <= g:
        if acc == 0 or acc == g or v == True:

            # Caso o modo v seja verdadeiro, este processo ocorre em todas as gerações:
            final += "Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + \
                    str(obter_numero_presas(prado)) + " (Gen. " + str(acc) + ")\n"
            final += prado_para_str(prado) + "\n"

        # Tuplo final, com o nº de presas e nº de predadores:
        if acc == g:
            final += "(" + str(obter_numero_predadores(prado)) + ", " + str(obter_numero_presas(prado)) + ")"
        prado = geracao(prado)
        acc += 1

    return final