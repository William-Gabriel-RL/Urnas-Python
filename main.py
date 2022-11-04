def busca_candidato(voto, dicionario):
    if voto != "branco" and voto != "nulo":
        for numero in dicionario:
            if numero == voto:
                return CANDIDATOS[numero]


def votar(dicionario):
    confirmado = False
    while not confirmado:
        voto = input("Informe seu voto para a prefeitura de (cidade de preferência) (2 dígitos): ")
        
        if voto.isdigit():
            print(busca_candidato(int(voto),CANDIDATOS))
            escolha = input("Tecle 'y' para CONFIRMAR o voto, ou 'n' para CANCELAR ou 'c' para CORRIGIR o voto: \n")
            if escolha.lower() != "y":
                continue
            else:
                confirmado = True
                if int(voto) not in CANDIDATOS:
                    dicionario["nulos"] +=1
                else:
                    for item in CANDIDATOS[int(voto)]:
                        dicionario[item] += 1
        else:
            if voto == "branco":
                print("Voto em branco")
                escolha = input("Tecle 'y' para CONFIRMAR o voto, ou 'n' para CANCELAR ou 'c' para CORRIGIR o voto: \n")
                if escolha.lower() == "y":
                    confirmado = True
                    dicionario["brancos"] += 1
                else:
                    continue
            else:
                print("Voto nulo")
                escolha = input("Tecle 'y' para CONFIRMAR o voto, ou 'n' para CANCELAR ou 'c' para CORRIGIR o voto: \n")
                if escolha.lower() == "y":
                    confirmado = True
                    dicionario["nulos"] += 1
                else:
                    continue


def checar_mais_votado(dicionario):
    nome_mais_votado = ''
    maioria_votos = 0
    for key in dicionario:
        if key != "brancos" and key != "nulos":
            if dicionario[key] > maioria_votos:
                maioria_votos = dicionario[key]
                nome_mais_votado = key
                
    
    
    return {nome_mais_votado : maioria_votos}


def exibe_votos(dicionario):
    print("\nVotos de cada candidato\n")
    for key in dicionario:
        if key != "brancos" and key != "nulos":
            print(f"{key} = {dicionario[key]} votos")


def encerrar_votacao(dicionario):
    validos = 0
    for key in dicionario:
        if key != "brancos" and key != "nulos":
            validos += dicionario[key]
    
    print(f"\nVotos validos: {validos}")
    print(f"Votos brancos: {dicionario['brancos']}")
    print(f"Votos nulos: {dicionario['nulos']}")
    
    vencedor = checar_mais_votado(dicionario)
    
    if list(vencedor.values())[0] > validos/2:
        porcentagem_vitoria = (list(vencedor.values())[0] / validos) * 100
        print(f"\nVitória para {list(vencedor.keys())[0]} com {porcentagem_vitoria}%")
    else:
        print("\nVotos da maioria insuficientes, 2º turno será necessário")
        
    exibe_votos(dicionario)

CANDIDATOS = {
    12 : {"candidato1" : "PDT"},
    13 : {"candidato2" : "PT"},
    22 : {"candidato3" : "PSL"},
    30 : {"candidato4" : "Novo"},
    31 : {"candidato5" : "PMDB"}
}
votos = {"brancos": 0, "nulos": 0}

# Adicionar automaticamente os candidatos na computação de votos, para não ter retrabalho
for numero in CANDIDATOS:
    for item in CANDIDATOS[numero]:
        nome = item
        votos[nome] = 0
        
fim = False
while not fim:
    escolha = input("Próximo eleitor 'p' ou encerrar a votação 'e' ?")
    if escolha == "p":
        voto = votar(votos)
    else:
        encerrar_votacao(votos)
        fim = True
