#JOGO DO VAMPIRO


import random

#A chave do dicionário de ações é o que desencadeia a ação. O valor é só o nome apresentado para o jogador
#As ações que não são do jogador tomar de e engregam para o jogador o turno. Apenas elas alteram o estado da variável 'turn'.

#Dicionários de ações
opt_geral = {'sair':'Ir para outro lugar acessivel a partir daqui.', 'ficar':'Fazer algo aqui mesmo.', 'itens':'Averiguar tuas posses.'}

opt_treino = {'grgrgrgr':' "Eu não deveria demorar tanto para comer."','grgr':' "Tenho tido fome com muita frequência.','olhos':' "Olho vivo!','grande':' "Eu deveria suportar mais."','desaparecimento':' "às vezes tenho vontade de sumir."','vozes':'" Às vezes escuto um zumbido dentro da minha cabeça... às vezes parece uma voz..."'}

#Dicionários de sub-ações

#Dicionários de locais
local_Covil = {'nome':'Covil','msgm':' Estás em uma fábrica abandonada, não muito próxima da cidade. Parece um bom lugar para chamar de teu.', 'ptrl':0,'mob':0,'cvway':False,'cvstay':True,'opt_mv':{'centro':'Ir para o centro da cidade.','bairro':'Ir para um bairro residencial, não muito longe daqui.','esgoto':'Esgueirar-se para dentro de um bueiro','mata':' Explorar o matagal próximo aos fundos da fábrica.'},'opt_act':{'dormir':'Esperar até o anoitecer, mas de forma econômica.','pensar':' Tentar entender tua atual condição'}}

local_Bairro = {'nome':'Bairro Residencial', 'msgm':' Estás em um pacato bairro residencial.', 'ptrl':2,'mob':3,'cvway':False,'cvstay':False, 'opt_mv':{'covil':'Retornar ao único lugar que ainda parece seguro.', 'centro':'Ir para o centro da cidade.','esgoto':'Esgueirar-se para dentro de um bueiro'},'opt_act':{'aguardar':'Aguardar um pouco.','anoitecer':'Aguardar até parecer seguro sair do abrigo.','abrigo':'Procurar um local coberto.','caçar':'Procurar por alguém de quem se alimentar.'}}

local_Centro = {'nome':'Centro Comercial', 'msgm':' Estás no centro comercial da cidade', 'ptrl':3,'mob':5,'cvway':False,'cvstay':False, 'opt_mv':{'covil':'Retornar ao único lugar que ainda parece seguro.','bairro':'Ir para um bairro residencial, não muito longe daqui.','esgoto':'Esgueirar-se para dentro de um bueiro'},'opt_act':{'aguardar':'Aguardar um pouco.','anoitecer':'Aguardar até parecer seguro sair do abrigo.','abrigo':'Procurar um local coberto.','caçar':'Procurar por alguém de quem se alimentar.','vasculhar':'Ver se há algo.'},'item_set':['lâmina','moeda','amarra','fósforo','inflamável']}

local_Esgoto = {'nome':'Galerias de Esgoto','msgm':' Embora as luzes das ruas penetrem os bueiros, sem dúvidas é um ótimo abrigo contra o Sol','ptrl':0,'mob':0,'cvway':True,'cvstay':False,'opt_mv':{'covil':'Retornar ao único lugar que ainda parece seguro.','bairro':'Ir para um bairro residencial, não muito longe daqui.','centro':'Ir para o centro da cidade.'},'opt_act':{'aguardar':'Aguardar','abrigo':'Procurar um local coberto.'}}

local_Mata = {'nome':'Mata','msgm':' Árvores, árvores e mais ávores; um mar verde.','ptrl':0,'mob':0,'cvway':False,'cvstay':False, 'opt_mv':{'covil':'Retornar ao único lugar que ainda parece seguro.','caverna':' Uma entrada em uma pedra enorme; o caminho parece um declive e está escuro de mais para enxergar seu interior.'},'opt_act':{'aguardar':'Aguardar um pouco.','anoitecer':'Aguardar até parecer seguro sair do abrigo.','animal':'Procurar por alguma criatura da qual se alimentar.','vasculhar':'Ver se há algo.'},'item_set':['galho','amarra','pedra','inflamável']}

local_Caverna_Escura = {'nome':'Caverna','msgm':' Quase não se vê as paredes de pedra escoradas por velhas estacas de madeira. A escuridão é absoluta.','ptrl':0,'mob':0,'cvway':True,'cvstay':True, 'opt_mv':{'mata':' Retornar ao início da caverna.'},'opt_act':{'aguardar':'Aguardar um pouco.','anoitecer':'Aguardar até parecer seguro sair do abrigo.'}}

local_Caverna_Iluminada = {'nome':'Caverna','msgm':' É possível ver um altar ao fundo da caverna','ptrl':0,'mob':0,'cvway':True,'cvstay':True, 'opt_mv':{'mata':' Retornar ao início da caverna.'},'opt_act':{'aguardar':'Aguardar um pouco.','anoitecer':'Aguardar até parecer seguro sair do abrigo.','averiguar':'Averiguar o estranho altar no fundo da caverna'}}

#Dicionários de itens

catálogo = {'carta':'Um bilhete foi deixado junto a ti na tua primeira noite.',
            'arma':'Um artefato improvisado que pode ser usado como arma.',
            'moeda':'Um pequeno disco metálico. Tu não reconheces seu valor, mas certamente vale algo.',
            'lâmina':'Um objeto descartado razoavelmente incisivo.',
            'pedra':'Uma pedra. Pode ser arremessada, mas certamente não seria decisiva numa situação desesperadora.',
            'galho':'Dentre tantos outros, este parece mais resistente que a maioria.',
            'amarra':'Um barbante, fio ou arame, arequado para amarrar uma coisa a outra.',
            'fósforo':'Um palito autoinflamável, por sorte, ainda não foi usado.',
            'inflamável':'Uma substância sólida, razoavemente maleável, que serviria de combustível por um tempo considerável',
            'tocha':'Melhor deixar para utilizar em algum lugar onde seria útil.'}

list_bolso = []

bancada = []


item_carta = {'nome':'carta','txt_dir':'txt/epístola.txt','opt_act':{'ler':'Ler as instruções deixadas contigo por um anônimo.','descartar':'As informações contidas neste pedaço de papel não são mais necessárias.'}}

item_cortante = {'nome':'lâmina','opt_act':{'descartar':'Tal objeto não passa de lixo.','aproveitar':'Talvez seja mais útil como parte de algo melhor.'}}

item_moeda = {'nome':'moeda','opt_act':{'descartar':'No teu atual estilo de vida, dinheiro deixou de ter utilidade.'}}

item_amarra = {'nome':'amarra','opt_act':{'descartar':'Não há o que atar com isto.','aproveitar':'Parece útil para atar outros itens.'}}

item_pedra = {'nome':'pedra','opt_act':{'descartar':'O peso é desproporcionalmente maior que a utilidade.'}}

item_galho = {'nome':'galho','opt_act':{'descartar':'Há muito mais de onde veio este.','aproveitar':'Poderia servir de haste para algo um pouco mais elaborado.'}}

item_arma = {'nome':'arma','opt_act':{'descartar':'Não ficou tão bom. Melhor nem contar com isso.'}}

item_inflamável = {'nome':'inflamável','opt_act':{'descartar':'Guardar algo assim pode ser perigoso.','aproveitar':'Pode haver uma forma segura de aproveitar a luz ou o calor do fogo proveniente da queima desta substância.'}}

item_tocha = {'nome':'tocha','opt_act':{'descartar':'Útil, mas não por enquanto.','acender':'Dependendo do lugar, pode abrir um leque de opções que antes não se podia ver.'}}

item_phosphor = {'nome':'fósforo','opt_act':{'descartas':'A chama não duraria o bastante para fazer o que quer que seja.'}}

#Variáveis de Personagens


def charPathern():
    pass

#Variáveis Básicas
check = True
optdict = opt_geral #variável maleável, que recebe os dicionários de ações.
prevdict = opt_geral #Variável maleável, que recebe o dicionário de ações anterior.
game_over = False
vict = False
incoe = 0
sangue = 6
time = 22
cover = True
turn = 'player'
abarrot = False
alerta = 0
local_atual = local_Covil
item_atual = item_carta
patrulha = local_atual['ptrl']
pico = 1
treino = 0
clausura = False
turnos = 0
luz = True
sangue_altar = 0

#Variáveis treináveis
fome = 3
limite_sangue = 15
busca = 3
incognito = 3
bolsos = 3

#Variável de cheat. Não se esqueça de comentar o que cada cheat faz.
cheat1 = False
cheat2 = False
cheat3 = False

# Funções de limpeza do prompt.
import subprocess as sp
def clr():
    tmp = sp.call('cls', shell=True)
def inclr(prompt):
    inp = input(prompt)
    tmp = sp.call('cls', shell=True)
    return inp

# Redução limite de alerta
def reduzAlerta(a_):
    global alerta
    alerta -= a_
    if alerta < 0:
        alerta = 0

# Relógio para depois de uma ação.
def passtime(h_):
    global sangue
    global time
    global pico
    global check
    global alerta
    global incognito
    global turnos
    for i in range(0,h_):
        sangue -= 1
        turnos += 1
        check = True
        charPathern()

    if time + h_ < 24:
        time += h_
    else:
        time = time + h_ - 24
        reduzAlerta(incognito)

    if ((time >= 5) and (time <=7)) or ((time >= 17) and (time <= 19)) :
        pico = 3
    elif ((time > 7) and (time < 18)) or ((time > 19 and time <= 0)):
        pico = 2
    else:
        pico = 1

# Função treino e tempo
def passtreino(t_):
    global treino
    for i in range(t_):
        treino += 1
        if treino >= 5:
            treino = 0
            passtime(1)


# Checagem de condição, para dar informações para o jogador e verificar se o jogo acabou.
def turnset():
    global game_over
    global gnr
    global incoe
    global sangue
    global time
    global cover
    global turn
    global abarrot
    global alerta
    global local_atual
    global patrulha
    global pico
    global incognito
    global clausura
    global turnos
    global vict
    global local_atual
    global list_bolso
    global bancada

    for i in bancada:
        list_bolso.append(i)
        bancada.remove(i)

    if incoe >= 10:
        print(' ...')
        game_over = True

    if alerta + patrulha*(pico-1) > 9+(incognito*2):
        print(' Sabem que estás aqui.')
        if 'arma' in list_bolso:
            print(f' Mas tu estavas preparad{gnr}. Tu usaste um objeto cortante como arma da melhor forma que te seria possível e desvencilhaste-te de teus agressores.')
            print(' No confronto, perdeste tua arma.')
            list_bolso.remove('arma')
        else:
            print(f'E foste incapaz de defender a ti mesm{gnr}.')
            game_over = True

    if clausura == False:
        if (time >= 7) and (time <= 17):
            print(' O Sol brilha forte...')
            if cover == False:
                print(' ... e seus raios queimam a tua pele até que tu não sejas nada além brasas e cinzas.')
                game_over = True
            else:
                print(' ... mas, felizmente, estás sob uma cobertura a proteger-te.')
        elif (time >= 6 and time <7) or (time >17 and time <= 18):
            print(' O Sol não está à vista, mas há sinais de claridade no céu.')
        else:
            print(' É noite.')
    else:
        print(' Aqui, não há como saber se é dia ou noite.')

    if sangue <= 0:
        print(' ...')
        game_over = True
    elif sangue >= 1 and sangue <= fome:
        print(f' Tu estás famint{gnr}.')
    elif (sangue >= limite_sangue-2) and (sangue <= limite_sangue):
        print(f' Estás replet{gnr}. Sentes que poderias explodir (metaforicamente) a qualquer momento.')
        abarrot = True
    elif sangue > limite_sangue:
        print(f' Ingeriste mais sangue do que teu corpo seria capaz de comportar e o líquido vermelho verteu-se de ti pelos teus olhos, ouvidos, nariz e demais orifícios.')
        sangue = limite_sangue
        abarrot = True
        alerta += 1

    if turnos >= 720:
        vict = True
        print(' Encontraste os padrões que garantir-te-ão longevidade indefinidamente.')

    if sangue_altar >= 15:
        vict = True
        print(' Concluiste o próprósito desta tua nova existência.')

#Funções em ações

def manuseio():
    global incoe
    global optdict
    global opt_geral
    global item_atual
    global catálogo
    global list_bolso
    global bancada
    global item_carta
    global item_galho
    global item_pedra
    global item_amarra
    global item_moeda
    global item_arma
    global item_cortante
    global item_tocha
    global item_phosphor
    global item_inflamável

    for i in list_bolso:
        print ('['+i+'] '+catálogo[i])
    print('[retornar] Voltar para o menu inicial.')
    if len(bancada)>0:
        print('\n Os seguintes foram separados:')
        for i in bancada:
            print ('['+i+'] '+catálogo[i])

    item_selected_ = inclr('')
    if item_selected_ in list_bolso:
        if item_selected_ == 'carta':
            item_atual = item_carta
        elif item_selected_ == 'arma':
            item_atual = item_arma
        elif item_selected_ == 'moeda':
            item_atual = item_moeda
        elif item_selected_ == 'tocha':
            item_atual = item_tocha
        elif item_selected_ == 'lâmina':
            item_atual = item_cortante
        elif item_selected_ == 'amarra':
            item_atual = item_amarra
        elif item_selected_ == 'pedra':
            item_atual = item_pedra
        elif item_selected_ == 'galho':
            item_atual = item_galho
        elif item_selected_ == 'fósforo':
            item_atual = item_phosphor
        elif item_selected_ == 'inflamável':
            item_atual = item_inflamável
        optdict = item_atual['opt_act']
    elif item_selected_ == 'retornar':
        optdict = opt_geral
    else:
        incoe += 1
    

#Introdução
clr()
inclr(' Quando, ao fim de um texto, houver a palavra "ENTER" em caixa-alta e entre colchetes, por favor, aperte a tecla ENTER para continuar.\n[ENTER]')

nome = inclr(' Antes de começarmos, informe qual nome tu gostarias que fosse associado à tua personagem.\n ')
gnr = inclr(' Poderia informar o gênero da tua personagem?\n (Esta informação tem fins meramente de personalização, tendo em vista a concordância gramatical da lingua portuguesa)?\n [a] Feminino\n [o] Masculino\n')

if (gnr != 'a') and (gnr != 'o'):
    gnr = 'o'
    incoe += 1
    inclr(' Será assumido o gênero neutro da lingua portuguesa nos textos.\n[ENTER]')

if nome != 'AqD':
    while True:
        inclr(f' Boa noite, {nome}, e bem-vind{gnr} ao "Vam.py" (este foi o melhor nome em que conseguimos pensar).\n Todo jogo é composto de desafios, e neste o maior desafio (por enquanto) é compreender instruções porcamente fornecidas e responder de forma coerente (ou seja, algo que o script do jogo aceite).\n Na maioria das vezes, as respostas disponíveis serão obvias; os erros serão, normalmente, falta de atenção ou imprecisão de digitação (ou, ainda, erros propositais).\n Este aviso se deve ao fato de que boa parte das explicações foram voluntariamente descartadas (e, convenhamos, tutorial é MUITO CHATO).\n[ENTER]')
        resp1 = inclr(' Você compreendeu a mensagem anterior?\n[s] Sim\n[n] Não\n')

        if resp1 == 'n':
            inclr(' Tudo bem, eu posso mostrar novamente.\n[ENTER]')
            continue
        elif resp1 == 's':
            inclr(' Genial! Sabia que não me desapontarias. ;)\n[ENTER]')
            break
        else:
            incoe +=1
            print(' Acredite, isso foi registrado... ')
            print(incoe)
            inclr(' Você receberá uma nova chance...\n[ENTER]')
            continue



    inclr(' INICIO\n\n [ENTER]')

    inclr(' Tu não enxergas e não te lembras de quem és ou de onde estás.\n\n  Aos poucos, teus olhos se adaptam à penumbra,\n   teus ouvidos buscam qualquer ruído distinguível,\n    teu tato identifica o frio rígido do chão sobre o qual jaz teu corpo,\n     teu olfato reconhece o cheio de óleo de máquina,\n      e o paladar, por fim, é abruptamente bombardeado por um sabor lancinante de ferrugem.\n\n[ENTER]')

if inclr(' Há uma folha de papel no chão, dobrada, próxima a ti.\n [ler] Pode ser importante.\n [...]\n') == 'ler':
    list_bolso.append('carta')
    carta_aberta = open(item_atual['txt_dir'],'r')
    print(carta_aberta.read())
    inclr('')
    passtime(2)
    carta_aberta.close()

# Raiz do jogo.
while True:
    if check == True:
        turnset()
    check = False
    cover = local_atual['cvstay']
    if game_over == True or vict == True:
        inclr('[ENTER]')
        break

    print(local_atual['msgm'])
    print('\n Faça algo. Eis tuas opções:')
    for chave,valor in optdict.items(): # .items() fornece pares de tuplas, nesse formato separado por vírgula
        print('['+chave+'] '+valor)
    if (optdict != opt_geral) and (turn == 'player'):
        print('[retornar] Voltar para o menu inicial.')
    decis = inclr(" ")
    decis = decis.lower()

    ###############        CORAÇÃO       ###############
    
    # Ações Gerais
    if (decis == 'retornar') and ((optdict != opt_geral) and (turn == 'player')):
        optdict = opt_geral
        continue
    elif (decis == 'sair') and (optdict == opt_geral):
        optdict = local_atual['opt_mv']
        continue
    elif (decis == 'ficar') and (optdict == opt_geral):
        optdict = local_atual['opt_act']
        continue
    elif (decis == 'itens') and (optdict == opt_geral):
       manuseio()
       continue
    
    # Ações de movimento
    elif (decis == 'covil') and (decis in optdict.keys()):
        passtime(1)
        cover = local_atual['cvway']
        check = True
        local_atual = local_Covil
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue
    elif (decis == 'centro') and (decis in optdict.keys()):
        passtime(1)
        cover = local_atual['cvway']
        check = True
        local_atual = local_Centro
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue
    elif (decis == 'bairro') and (decis in optdict.keys()):
        passtime(1)
        cover = local_atual['cvway']
        check = True
        local_atual = local_Bairro
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue
    elif (decis == 'esgoto') and (decis in optdict.keys()):
        check = True
        local_atual = local_Esgoto
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue
    elif (decis == 'mata') and (decis in optdict.keys()):
        passtime(1)
        cover = local_atual['cvway']
        check = True
        local_atual = local_Mata
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue
    elif (decis == 'caverna') and (decis in optdict.keys()):
        passtime(1)
        cover = local_atual['cvway']
        check = True
        local_atual = local_Caverna_Escura
        patrulha = local_atual['ptrl']
        optdict = opt_geral
        continue


    # Ações de local
    elif (decis == 'aguardar') and (decis in optdict.keys()):
        passtime(1)
        check = True
        optdict = opt_geral
        continue
    elif (decis == 'anoitecer') and (decis in optdict.keys()):
        sleep = 0
        while not (time > 17 and time <= 18):
            passtime(1)
        check = True
        optdict = opt_geral
        continue

    elif (decis == 'dormir') and (decis in optdict.keys()):
        reduzAlerta(1)
        sleep = 0
        while not (time > 17 and time <= 18):
            passtime(1)
            sangue += 1
            sleep += 1
        if sleep >= 2:
            sangue -= 2
        elif sleep >= 1:
            sangue -= 1
        check = True
        optdict = opt_geral
        continue
    
    elif (decis == 'abrigo') and (decis in optdict.keys()):
        cover = True
        check = True
        optdict = opt_geral
        continue

    elif (decis == 'pensar') and (decis in optdict.keys()):
        optdict = opt_treino
        continue

    elif (decis == 'caçar') and (decis in optdict.keys()):
        if (fome-sangue+busca+pico*local_atual['mob']) > 0:
            inclr(' Encontraste um alvo satisfatório.\n [ENTER]')
            integridade_da_presa = random.randint(4, 6)
            investida = False
            while True:
                if (busca+pico*local_atual['mob']) <= 6:
                    print(' Estás num local ao ar livre.')
                if (incognito + busca - patrulha*pico - alerta) <= 0:
                    print(f' Certamente estás sendo vist{gnr}.')

                if integridade_da_presa == 0:
                    alerta += (patrulha)*2
                    optdict = opt_geral
                    inclr(' Tua presa jaz, exaurida, sem vida.\n [ENTER]')
                    break
                elif integridade_da_presa == 1:
                    print(' Tua presa encontra-se inconsciente.')
                elif integridade_da_presa == 2:
                    print(' Tua presa aparenta lânguida e não se sustenta mais sobre as próprias pernas.')
                elif integridade_da_presa == 3:
                    print(' A lividez da tua presa se faz notória.')
                
                if inclr(' Desejas prosseguir?\n [s] Sim\n [...]\n') == 's':
                    print(' Tu passas a deglutir todo nectar rubro que verte da tua vítima.')
                    investida = True
                    sangue += 3
                    if (busca+pico*local_atual['mob']) <= 6:
                        cover = False
                    if (incognito + busca - patrulha*pico - alerta) <= 0:
                        alerta += patrulha
                    integridade_da_presa -= 1
                    passtime(1)
                    continue
                else:
                    break
        else:
            passtime(1)
            inclr(' Não conseguiste encontrar uma presa satisfatória.\n [ENTER]')
        if investida and ((5-integridade_da_presa)*pico*patrulha - incognito > 0): #aumenta a patrulha no local atual
            patrulha += (5-integridade_da_presa)*pico*patrulha - incognito
        check = True
        optdict = opt_geral
        continue

    elif (decis == 'vasculhar') and (decis in optdict.keys()):
        lista_de_itens_encontrados = list(local_atual['item_set'])
        lista_itens_ = []

        for i in range(busca):
            item_encontrado_index_ = random.randint(0,len(lista_de_itens_encontrados)-1)
            lista_itens_.append(lista_de_itens_encontrados[item_encontrado_index_]) #essa lista de itens é contém as chaves dos itens disponíveis.

        lista_itens_.extend(list_bolso)
        list_bolso = []

        while len(lista_itens_)>0 and len(list_bolso)<bolsos:
            print(' Tu tens estes itens à sua disposição.')
            print(f' Tu podes levar {bolsos-len(list_bolso)} destes contigo:')
            for i in lista_itens_:
                print('['+i+'] '+catálogo[i])
            
            item_select_ = inclr('')
            
            if item_select_ in lista_itens_:
                lista_itens_.remove(item_select_)
                list_bolso.append(item_select_)
                continue
            else:
                break

        passtime(1)
        check = True
        optdict = opt_geral
        continue
    
    elif (decis == 'animal') and (decis in optdict.keys()):
        passtime(1)
        inclr(f' Não obstante tuas tentativas, todas falharam. Tu não tens capacidades físicas para tal feito.')
        optdict = opt_geral
        continue

    elif (decis == 'averiguar') and (decis in optdict.keys()) and (local_atual == local_Caverna_Iluminada):
        inclr(' ~~~ NÃO ME FAÇA DESPERDIÇAR O POUCO ALENTO QUE ME RESTA.  ~~~')
        inclr(' ~~~ ESTÁS DIANTE DO TEU ÚNICO PROPÓSITO  DE EXISTÊNCIA. ~~~')
        inclr(' ~~~ PERSCRUTA ESTE ALTAR E ENTREGA-ME PARTE DA TUA VIDA. ~~~')
        inclr(' ~~~ PROCEDA GRADATIVAMENTE PARA QUE TU NÃO PEREÇAS. ~~~')
        del local_Caverna_Iluminada['opt_act']['averiguar']
        local_Caverna_Iluminada['opt_act']['interagir'] = 'Interagir com o altar de sangue.'
        passtreino(1)
        check = True
        optdict = opt_geral
        continue

    elif (decis == 'interagir') and (decis in optdict.keys()) and (local_atual == local_Caverna_Iluminada):
        while True:
            decis_altar = inclr(' ~~~ ALIMENTA-ME ~~~\n [s] Entregar parte da tua refeição.\n [n] Não é um momento adequado.\n')
            if decis_altar == 's':
                sangue -= 1
                sangue_altar += 1
                passtime(1)
                continue
            elif (decis_altar =='n'):
                break
            else:
                inclr(' ~~~ NÃO TOLERAREI TAL OFENÇA! ~~~')
                sangue_altar += sangue
                sangue = 0
                break
        check = True
        optdict = opt_geral
        continue

        


    
    #Ações de itens
    elif (decis == 'descartar') and (decis in optdict.keys()):
        list_bolso.remove(item_atual['nome'])
        item_atual = {'':''}
        optdict = opt_geral
        continue

    elif (decis == 'aproveitar') and (decis in optdict.keys()):
        if local_atual != local_Covil:
            inclr('Este não é o local adequado para esta ação.')
        else:
            bancada.append(item_atual['nome'])
            list_bolso.remove(item_atual['nome'])
            
            if ('galho' in bancada) and ('amarra' in bancada) and ('lâmina' in bancada):
                bancada.remove('galho')
                bancada.remove('amarra')
                bancada.remove('lâmina')
                list_bolso.append('arma')
                inclr('Tua engenhosidade produziu uma arma improvisada.\n [ENTER]\n')
                passtime(1)

            if ('galho' in bancada) and ('amarra' in bancada) and ('inflamável' in bancada):
                bancada.remove('galho')
                bancada.remove('amarra')
                bancada.remove('inflamável')
                list_bolso.append('tocha')
                passtime(1)
                inclr('Tua engenhosidade produziu uma tocha.\n [ENTER]\n')
        manuseio()
        continue

    
    elif (decis == 'ler') and (decis in optdict.keys()):
        carta_aberta = open(item_atual['txt_dir'],'r')
        print(carta_aberta.read())
        inclr('')
        passtime(2)
        carta_aberta.close()
        optdict = opt_geral
        continue

    elif (decis == 'acender') and (decis in optdict.keys()):
        if (local_atual != local_Caverna_Escura):
            inclr('Este não é um local que demanda mais iluminação')
        else:
            if not (('tocha' in list_bolso) and ('fósforo' in list_bolso)):
                inclr('Não tens os itens necessários para gerar luz.')
            else:
                list_bolso.remove('tocha')
                list_bolso.remove('fósforo')
                inclr('Agora é possível ver com mais detalhes o que há neste lugar.')
                local_atual = local_Caverna_Iluminada
                check = True
                item_atual = {'':''}
        optdict = opt_geral
        continue

    
    #Ações de treino
    elif (decis == 'grgrgrgr') and (decis in optdict.keys()):
        inclr(' "Desenvolvendo o apetite."\n[ENTER]')
        passtreino(1)
        fome += 1
        optdict = opt_geral
        check = True
        continue
    elif (decis == 'grgr') and (decis in optdict.keys()):
        if fome <= 1:
            inclr(' "Não posso exagerar"')
        else:
            inclr(' "Levando o regime a sério."\n[ENTER]')
            passtreino(1)
            fome -= 1
        optdict = opt_geral
        check = True
        continue
    elif (decis == 'olhos') and (decis in optdict.keys()):
        passtreino(2)
        if sangue >= 6:
            sangue -= 4
            busca += 1
            inclr(' "Olhos de Águia!"\n[ENTER]')
        else:
            inclr(' Tu não tens forças para seguir adiante.\n[ENTER]')
        optdict = opt_geral
        check = True
        continue
    elif (decis == 'grande') and (decis in optdict.keys()):
        passtreino(2)
        if sangue >= 6:
            sangue -= 4
            limite_sangue += 2
            inclr(f' "Olhando para mim mesm{gnr}, pareço maior."\n[ENTER]')
        else:
            inclr(' Tu não tens forças para seguir adiante.\n[ENTER]')
        optdict = opt_geral
        check = True
        continue
    elif (decis == 'desaparecimento') and (decis in optdict.keys()):
        passtreino(1)
        if sangue >= 6:
            sangue -= 4
            incognito += 1
            alerta -= 2
            inclr(f' "Ninguém sentiria a minha falta."\n[ENTER]')
        else:
            inclr(' Tu não tens forças para seguir adiante.\n[ENTER]')            
        optdict = opt_geral
        check = True
        continue
    elif (decis == 'vozes') and (decis in optdict.keys()):
        voz = inclr(' ~~~ ... ~~~\n [q] "Mais alto, por favor."')
        if voz == 'q':
            voz = int(inclr(' ~~~ QUANTOS FORAM OS TEUS ERROS? ~~~\n[ENTER]\n          '))
            if voz == incoe:
                incoe = 0
                inclr(f' ~~~ PELOS PODERES A MIM CONFERIDOS, EU {gnr.upper()} DECLARO SALV{gnr.upper()} DOS TEUS ERROS. ~~~\n [ENTER]')
            else:
                incoe += 1
                inclr(' ~~~ TALVEZ EU TENHA ESPERADO MUITO DE TI. ~~~\n[ENTER]')
        else:
            incoe += 1
            inclr(' ~~~ OUTRO ERRO! ~~~\n[ENTER]')

        optdict = opt_geral
        passtime(1)
        continue

    # Código de desenvolvedor
    elif (decis == 'nerescode') and nome == 'AqD':
        if gnr == 'a':
            print(f' Acessaste o código do desenvolvedor. Estas são as informações de variáveis que tu, jogadora trapaceira, não deverias estar vendo. >(\n')
        else:
            print(f' Acessaste o código do desenvolvedor. Estas são as informações de variáveis que tu, jogador trapaceiro, não deverias estar vendo. >(\n')
        print('')
        print('local_atual = '+local_atual['nome'])
        print('')
        print('checagem de turno = '+str(check))
        print('game_over = '+str(game_over))
        print('vict = '+str(vict))
        print('')
        print('incoerências = '+str(incoe))
        print('busca = '+str(busca))
        print('')
        print('turnos = '+str(turnos))
        print('time = '+str(time))
        print('cover = '+str(cover))
        print('')
        print('alerta = '+str(alerta))
        print('patrulha = '+str(patrulha))
        print('pico = '+str(pico))
        print('incognito = '+str(incognito))
        print('')
        print('sangue = '+str(sangue))
        print('fome = '+str(fome))
        print('limite de sangue = '+str(limite_sangue))
        print('Oblação de sangue = '+str(sangue_altar))
        #print('integridade da presa = '+str(integridade_da_presa))
        print('')
        print('turn = '+str(turn))
        print('abarrot = '+str(abarrot))
        print('')
        check = True
        continue

    elif (decis == 'gameoverme'):
        game_over = True
        check = True
        continue

    elif (decis == 'victme') and nome == 'AqD':
        vict = True
        check = True
        continue

    elif (decis == 'passturn'):
        turnos += int(inclr('Quanto tempo?'))
        check = True
        continue

    elif (decis == 'feedmeup') and nome == 'AqD':
        sangue = limite_sangue
        check = True
        continue

    elif (decis == 'gimmeitem') and nome == 'AqD':
        list_bolso.append(inclr(''))
        

    else:
        incoe += 1
        optdict = opt_geral
        continue

#Game Over Screen
print(' ~~~ FIM DE JOGO. ~~~')
if game_over == True:
    print(' ~~~ FRACASSO! ~~~')
    if incoe >= 10:
        print(' ~~~ ERRASTE MAIS DO QUE SERIA POSSÍVEL PERDOAR.~~~')

    if (time >= 7) and (time <= 17) and cover == False:
        print(' ~~~ REGRA NÚMERO 1: O SOL É TEU INIMIGO. ~~~')

    if sangue == 0:
        print(f' ~~~ REGRA NÚMERO 2: MENTENHA-SE HIDRATAD{gnr.upper()} ~~~')

    if alerta + patrulha*(pico-1) > 15:
        print(' ~~~ REGRA NÚMERO 3: OS HUMANOS SÃO DADOS A REPRESÁLIAS. ~~~')

    if decis == 'gameoverme':
        print(' Suicide is painless...')

elif vict == True:
    print(' ~~~ SUCESSO! ~~~')
    if turnos >= 168:
        print(f' Se sobreviveste até então, sobreviverias para sempre. Se nada {gnr} matou até então, nada {gnr} mataria nem mesmo em 100 anos.')
    if sangue_altar >= 15:
        print(' A entidade que trouxe a ti de volta a esta existência, em fim, está livre para prosseguir com seus planos, e isso graças a ti. Ele tem um compromisso de gratidão para contigo e, possivelmente, novas tarefas num futuro próximo.')

inclr('')

if game_over == True:
    print(' Há várias formas de sofrer uma derrota neste jogo. Que tal tentar novamente e descobrir as demais formas? =D\n')
elif vict == True:
    print(' Por enquanto, está é a única forma de conseguir a vitória... mas há outras formas de terminar o jogo. Que tal tentar novamente e descobrir as demais formas? =D\n')

inclr(' Por enquanto, isso é tudo. Nos desculpe pelo transtorno.\n[ENTER]')

# Regras para inclusão de conteúdo:
    # Toda ação é composta de chave e mensagem para o jogador num dicionário.
    # Toda ação que geral alterações nos status do jogador deve ter "check = True".
    # Toda localidade tem um dicionário de movimento sob a chave "opt_mv".
    # Toda localidade tem um dicionário de ações sob a chave "opt_act"; essa lista costuma ter a opção de espera.
    # A comparação com o 'incoe' está no final do CORAÇÃO para possibilitar códigos secretos, ações não listadas. As verificações de continência ficam a cargo da inserção da ação.
    # Verifique sempre se a ação acrescentada não pode ser executada sobre outras condições. Nesse caso, apenas acrescente o parâmetro à verificação.
    # Ações efetivas passam hora.

#local_??= {'nome':'??','msgm':'??','ptrl':0,'mob':0,'cvway':'n','cvstay':'n','opt_mv':{'?lugar':'Ir para ?lugar','lugar?':'Ir para lugar?'},'opt_act':{'aguardar':'Aguardar','abrigo':'Procurar um local coberto.','especific':'Específico'}}
#Adicione as conecções a este local nos outros locais
#Adicione a ação de se mover para este local
#Adicione as ações possíveis apenas neste local

### Sempre que criar um item:
# Deve ter um dicionário de opções, que será lido no Menu Raiz, contendo, pelo menos, descartar.
# Seu dicionário de opções precisa ser alocado em optdict pela função 'manuseio()' ação geral 'itens'
# Adicione a descrição do item nos locais onde ele pode ser encontrado.
# Se é o primeiro item da localidade, adicione a ação "vasculhar" ao opt_act do lugar.
# A mesma descrição deve ser acrescentada no dicionário 'catálogo'.
# O nome do item deve ser o mesmo como: chave no dicionário de itens da localidade; chave no catálogo, valor da chave 'nome' no dicionário do próprio item; sobrenome do dicionário (item_nome).

#Lugares onde um mesmo item dele estar:
#1 - Catálogo - nome e descrição.
#2 - Dentre os dicionários de itens (ele próprio é um dicionário) - nome e dicionário de ações.
#3 - Lugares onde pode ser encontrado, se puder ser encontrado; ou na lista de itens criados. - nome.
#4 - Suas ações devem contar entre as ações de itens.
#5 - Uma chamada na ação geral 'itens', pela função de manuseio.


