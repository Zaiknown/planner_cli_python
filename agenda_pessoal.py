import shelve
import os

"""
CORES
"""

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def mostrar_menu(agenda):
    
    """
    função que retorna o menu de opções
    """
    while True:
        os.system('cls')    
        print("\n============== MENU DE OPÇÕES ==============\n")
        print("1ª: Adicionar novo compromisso")
        print("2ª: Editar compromisso existente")
        print("3ª: Excluir compromisso existente")
        print("4ª: Mostrar números de compromissos")
        print("5ª: Filtrar compromisso por palavra-chave")
        print("6ª: Listar compromissos")
        print("7ª: Listar compromissos prioritarios")
        print("8ª: Listar dia mais ocupado")
        print("9ª: Filtrar compromissos por data")
        print("10ª: Filtrar compromissos por período")
        print("\n============================================\n")
        
        opcao = input("Digite o número da opção para selecionar (ou digite 'sair' para sair da agenda): ").lower().strip()
        
        if opcao == 'sair':
            
            print('Saindo...')
            salvar_dados(agenda)
            break
        
        elif opcao.isnumeric():
            
            opcao = int(opcao)
            
            if opcao == 1:
                adicionar_compromisso(agenda)
            elif opcao == 2:
                editar_compromisso(agenda)
            elif opcao == 3:
                excluir_compromisso(agenda)
            elif opcao == 4:
                contar_total_compromissos(agenda)
            elif opcao == 5:
                filtra_por_palavra_chave(agenda)
            elif opcao == 6:
                os.system('cls')
                listar_todos_compromissos(agenda)
            elif opcao == 7:
                listar_prioritarios(agenda)
            elif opcao == 8:
                obter_dia_mais_ocupado(agenda)
            elif opcao == 9:
                filtra_por_data(agenda)
            elif opcao == 10:
                filtrar_por_periodo(agenda)
            elif opcao > 10 or opcao < 1:
                print(f"\n#### {YELLOW}AVISO{RESET} ####")
                print(f"\n {RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
                continue
            
        else:
            
            print(f"{RED}\nVocê digitou uma opção que não existe, tente novamente!{RESET}\n")
            
def carregar_dados():
    
    """
    função que abre o banco shelve e carrega a agenda
    
    se for a primeira vez rodando retorna um dicionário vazio
    """
    
    with shelve.open('banco_da_agenda') as db:
        dados_carregados = db.get('agenda_salva', {})
        return dados_carregados

def salvar_dados(dados_atualizados):
    
    """
    função que salva o dicionário atual da agenda por cima do antigo no banco shelve
    """
    
    with shelve.open('banco_da_agenda') as db:
        db['agenda_salva'] = dados_atualizados

def adicionar_compromisso(agenda):
    
    """
    função que adiciona o compromisso na agenda
    
    o usuário deve inserir os dados de dia, mês, ano, hora inicial, hora final, a descrição e prioridade
    
    caso haja um compromisso no mesmo horário, irá retornar um erro, senão, irá cadastrar no dicionário
    """
    
    while True:
    
        dia = input("Digite o dia do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if dia == 'voltar':
            
            print("Voltando...")
            break
        
        elif dia.isnumeric():
            
            dia = int(dia)
            
            if dia < 1 or dia > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}Esse dia não existe, tente novamente{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção inexistente, tente novamente\n{RESET}")
            continue
        
        mes = input("Digite o mês do compromisso (ou 'voltar' para voltar o menu principal): ").lower().strip()
        
        if mes == 'voltar':
            
            print("Voltando...")
            break
        
        elif mes.isnumeric():
            
            mes = int(mes)
        
            if mes < 1 or mes > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}Esse mês não existe, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        ano = input("Digite o ano do compromisso (ou 'voltar' para voltar o menu principal): ").lower().strip()

        if ano == 'voltar':
            
            print("Voltando...")
            break
            
        elif ano.isnumeric():
            
            if len(ano) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano = int(ano)
            
            if ano < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:
                if dia > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes == 2 and dia > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
                
        else:
            
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
            
        hora_inicio = input("Digite a hora de início do compromisso (ou 'voltar' para voltar o menu principal): ").lower().strip()
        
        if hora_inicio == 'voltar':
            
            print("Voltando...")
            break
        
        elif hora_inicio.isnumeric():
            
            hora_inicio = int(hora_inicio)
            
            if hora_inicio < 0 or hora_inicio > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O horário que você digitou não existe, tente novamente{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        hora_termino = input("Digite a hora do término do compromisso (ou 'voltar' para voltar o menu principal): ").lower().strip()
        
        if hora_termino == 'voltar':
            
            print("Voltando...")
            break
            
        elif hora_termino.isnumeric():
            
            hora_termino = int(hora_termino)
            
            if hora_termino <= hora_inicio:
                
                print(f"\n{RED}A hora do término do compromisso não pode ser menor ou igual à hora do início!{RESET}\n")
                continue
                
            elif hora_termino < 0 or hora_termino > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O horário que você digitou não existe, tente novamente{RESET}\n")
                continue
            
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        desc = input("Digite a descrição do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if desc == 'voltar':
            
            print("Voltando...")
            break
        
        prioridade = input("Digite se o compromisso tem prioridade ou não, digite 1 para sim e 2 para não (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if prioridade == 'voltar':
            
            print("Voltando...")
            break
        
        elif prioridade.isnumeric():
            
            prioridade = int(prioridade)

        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        compromisso = f"{ano:04d}_{mes:02d}_{dia:02d}_{hora_inicio:02d}"
        
        if prioridade == 1:
            prioridade = True
        elif prioridade == 2:
            prioridade = False
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
            
        agenda[compromisso] = {
            "dia": dia,
            "mes": mes,
            "ano": ano,
            "hora_inicio": hora_inicio,
            "hora_termino": hora_termino,
            "descricao": desc,
            "prioridade": prioridade
            }
        salvar_dados(agenda)
        print(f"\n{GREEN}Compromisso cadastrado com sucesso!{RESET}\n")
        os.system('pause')
        break
        
def contar_total_compromissos(agenda):
    
    print(f"\nVocê tem um total de {len(agenda)} compromissos marcados na sua agenda!\n")
    os.system('pause')
        

def listar_todos_compromissos(agenda):
    
    """
    
    função que lista todos os compromissos cadastrados na agenda
    
    o sorted(agenda.items()) ordena pares de chaves com seus valores considerando
    
    a ordem da chave, a chave é "ano_mes_dia_hora_inicio"
    
    se houver um compromisso "2025_xx_xx_xx" e um "2014_xx_xx_xx"
    
    primeiro vem o 2014 e 2025 abaixo, pois 2 == 2, 0 == 0, e 1 vem antes do 2, então:
    
    "2014_xx_xx_xx, {valor}", "2025_xx_xx_xx, {valor}"
    
    após isso pula para as horas, vai do menor para o maior
    
    se houver dois compromissos na mesma data, e um começar 12h e terminar 13h
    
    e outro começar 8h e terminar 9h, por cima virá o de 8h-9h e abaixo virá o de 12h-13h
    """
    
    for chave, info in sorted(agenda.items()):
        
        if info['prioridade'] == True:
            texto_prioridade = "Urgente"
            
        else:
            texto_prioridade = "Normal"
        
        print("-" * 40)
        print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
        print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
        print(f"Descrição: {info['descricao']}")
        print(f"Prioridade: {texto_prioridade}")

    print("-" * 40)
    os.system('pause')
    
def filtra_por_data(agenda):
    
    """
    função que filtra por data
    
    o usuário deve informar dia, mês, ano e horário inicial do compromisso
    
    caso haja uma chave dentro do dicionário montada com os dados informados
    
    irá retornar o compromisso completo, caso não haja, irá retornar erro
    """
    
    while True:
        
        dia = input("Digite o dia que você marcou o compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if dia == 'voltar':
            print("Voltando...")
            break
        
        elif dia.isnumeric():
            
            dia = int(dia)
            
            if dia < 1 or dia > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O dia que você digitou não existe, tente novamente!{RESET}\n")
                continue
            
            dia = int(dia)
            
        mes = input("Digite o mês que você marcou o compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if mes == 'voltar':
            
            print("Voltando...")
            break
        
        elif mes.isnumeric():
            
            mes = int(mes)
            
            if mes < 1 or mes > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}Esse mês não existe, tente novamente!{RESET}\n")
                continue
            
        ano = input("Digite o ano que você marcou o compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if ano == 'voltar':
            
            print("voltando...")
            break
        
        elif ano.isnumeric():
            
            if len(ano) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano = int(ano)
            
            if ano < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:
                if dia > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes == 2 and dia > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
            
        else:
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
        
        encontrou = False
        
        os.system('cls')

        print(f"\n{GREEN}===== COMPROMISSOS DA DATA {dia:02d}/{mes:02d}/{ano:04d} =====\n{RESET}")
        
        for chave, info in sorted(agenda.items()):
            if info['dia'] == dia and info['mes'] == mes and info['ano'] == ano:
                encontrou = True
                
                if info['prioridade'] == True:
                    texto_prioridade = "Urgente"
                else:
                    texto_prioridade = "Normal"
                    
                print("-" * 40)
                print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
                print(f"Descrição: {info['descricao']}")
                print(f"Prioridade: {texto_prioridade}")
                
        if encontrou:
            print("-" * 40)
        else:         
            print(f"\n{YELLOW}#### AVISO ####{RESET}")
            print(f"{RED}Não há nenhum compromisso cadastrado nesta data!{RESET}\n")
            
        os.system("pause")
        break

def listar_prioritarios(agenda):
    
    """
    função que lista todos os compromissos que são prioritários
    """
    
    encontrou = False
    
    for chave, info in agenda.items():
        
        if info['prioridade'] == True:
            
            encontrou = True
            
            texto_prioridade = "Urgente"
            
            print("-" * 40)
            print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
            print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
            print(f"Descrição: {info['descricao']}")
            print(f"Prioridade: {texto_prioridade}")
        print("-" * 40)
    os.system("pause")
        
    if not encontrou:
        
        print("Você não tem nenhum compromisso prioritário na agenda!")

def filtra_por_palavra_chave(agenda):
    
    """
    função que filtra compromisso por palavra chave que existe na descrição
    
    primeiro o usuário deve informar a palavra chave que deve haver na descrição
    
    ex: usuário procura python, caso haja um compromisso que na descrição há a palavra "python"
    
    irá retornar esse compromisso
    
    caso não haja compromisso com a palavra informada pelo usuário, irá retornar erro
    """
    
    while True:
        
        encontrou = False
        
        palavra = input("Digite a palavra que está na descrição do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if palavra == 'voltar':
            
            print('Voltando...')
            break
        
        else:
            
            for chave, info in agenda.items():
                
                if palavra in info['descricao'].lower().strip().split():
                    
                    encontrou = True

                    if info['prioridade'] == True:
                        texto_prioridade = "Urgente"
                    else:
                        texto_prioridade = "Normal"

                    print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
                    print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
                    print(f"Descrição: {info['descricao']}")
                    print(f"Prioridade: {texto_prioridade}")
                    print("==============================\n")
                    
            if not encontrou:
                
                print(f"\n{YELLOW}#### AVISO ####{RESET}")
                print(f"{RED}Não há nenhum compromisso com essa palavra na descrição!{RESET}\n")
                
            os.system("pause")
            break        

def excluir_compromisso(agenda):
    
    """
    função que exclui compromisso cadastrado
    
    primeiro deve ser informado pelo usuário os dados de dia, mês, ano e hora inicial do compromisso
    
    após isso, vai ser montada a chave do compromisso, caso seja achado dentro do dicionário uma chave igual, será deletado
    
    caso não haja uma chave que bata com os dados informados pelo usuário, irá retornar erro
    """
    
    while True: 
    
        texto_prioridade = ""
        
        for chave, info in sorted(agenda.items()):
            
            if info['prioridade'] == True:
                texto_prioridade = "Urgente"
            
            else:
                texto_prioridade = "Normal"
            
            print("-" * 40)
            print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
            print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
            print(f"Descrição: {info['descricao']}")
            print(f"Prioridade: {texto_prioridade}")

        print("-" * 40)
            
        dia = input("Digite o dia do compromisso para exclusão (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if dia == 'voltar':
            
            print("Voltando...")
            break

        elif dia.isnumeric():
            
            dia = int(dia)
            
            if dia < 1 or dia > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O dia que você digitou não existe, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        mes = input("Digite o mês do compromisso para exclusão (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if mes == 'voltar':
            
            print("Voltando...")
            break
        
        elif mes.isnumeric():
            
            mes = int(mes)
            
            if mes < 1 or mes > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O mês que você digitou não existe, tente novamente!{RESET}\n")
                continue
                
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        ano = input("Digite o ano do compromisso para exclusão (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if ano == 'voltar':
            
            print("Voltando...")
            break
        
        elif ano.isnumeric():
            
            if len(ano) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente{RESET}\n")
            
            ano = int(ano)
            
            if ano < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:
                if dia > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes == 2 and dia > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        hora_inicio = input("Digite a hora que inicia o compromisso para exclusão (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if hora_inicio == 'voltar':
            
            print("Voltando...")
            break
            
        elif hora_inicio.isnumeric():
            
            hora_inicio = int(hora_inicio)
            
            if hora_inicio < 0 or hora_inicio > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}A hora que você digitou não existe, tente novamente{RESET}\n")
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        chave_montada = f"{ano:04d}_{mes:02d}_{dia:02d}_{hora_inicio:02d}"
        
        if chave_montada in agenda:
            
            del agenda[chave_montada]
            salvar_dados(agenda)
            print(f"\n{GREEN}Compromisso excluído com sucesso!{RESET}\n")
            os.system('pause')
            break
        else:
            
            print(f"\n{GREEN}Não há nenhum compromisso com esses dados na agenda!{RESET}\n")
            break
        
    
def editar_compromisso(agenda):
    
    """
    função que edita um compromisso já cadastrado
    
    primeiro deve ser informado pelo usuário os dados de dia, mes, ano e hora inicial do compromisso
    
    logo após isso, você cadastra nesse compromisso dia, mes, ano, hora que inicia, hora que termina, descrição e prioridade
    
    caso não haja um compromisso cadastrado com os dados que foi informado pelo usuário, irá fazer a edição
    
    caso haja um compromisso já cadastrado com os dados informados, irá retornar um erro
    """
    
    while True:
        
        texto_prioridade = ""
        
        os.system('cls')
    
        print("===== DATAS DA AGENDA =====")
        
        for chave, info in sorted(agenda.items()):
            
            if info['prioridade'] == True:
                texto_prioridade = "Urgente"
            
            else:
                texto_prioridade = "Normal"
            
            print("-" * 40)
            print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
            print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
            print(f"Descrição: {info['descricao']}")
            print(f"Prioridade: {texto_prioridade}")

        print("-" * 40)
        
        dia = input("Digite o dia do compromisso para edição (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if dia == 'voltar':
            
            print("Voltando...")
            return

        elif dia.isnumeric():
            
            dia = int(dia)
            
            if dia < 1 or dia > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O dia que você digitou não existe, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        mes = input("Digite o mês do compromisso para edição (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if mes == 'voltar':
            
            print("Voltando...")
            return
        
        elif mes.isnumeric():
            
            mes = int(mes)
            
            if mes < 1 or mes > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O mês que você digitou não existe, tente novamente!{RESET}\n")
                continue
            
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        ano = input("Digite o ano do compromisso para edição (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if ano == 'voltar':
            
            print("Voltando...")
            return
        
        elif ano.isnumeric():
            
            if len(ano) != 4:
                
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano = int(ano)
            
            if ano < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:
                if dia > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes == 2 and dia > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
                
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        hora_inicio = input("Digite a hora que inicia o compromisso para edição (ou 'voltar' para o voltar ao menu principal): ").lower().strip()
        
        if hora_inicio == 'voltar':
            
            print("Voltando...")
            return
            
        elif hora_inicio.isnumeric():
            
            hora_inicio = int(hora_inicio)
            
            if hora_inicio < 0 or hora_inicio > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}A hora que você digitou não existe, tente novamente{RESET}\n")
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente!{RESET}\n")
            continue
        
        chave_montada = f"{ano:04d}_{mes:02d}_{dia:02d}_{hora_inicio:02d}"
        
        if chave_montada in agenda:
            
            dia = input("Digite o novo dia do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if dia == 'voltar':
            
            print("Voltando...")
            return
        
        elif dia.isnumeric():
            
            dia = int(dia)
            
            if dia < 1 or dia > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}Esse dia não existe, tente novamente{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        mes = input("Digite o novo mês do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if mes == 'voltar':
            
            print("Voltando...")
            return
        
        elif mes.isnumeric():
            
            mes = int(mes)
        
            if mes < 1 or mes > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}Esse mês não existe, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        ano = input("Digite o novo ano do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()

        if ano == 'voltar':
            
            print("Voltando...")
            return
            
        elif ano.isnumeric():
            
            if len(ano) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano = int(ano)
            
            if ano < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:
                if dia > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes == 2 and dia > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção inexistente, tente novamente{RESET}\n")
            continue
            
        hora_inicio = input("Digite a nova hora de início do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if hora_inicio == 'voltar':
            
            print("Voltando...")
            return
        
        elif hora_inicio.isnumeric():
            
            hora_inicio = int(hora_inicio)
            
            if hora_inicio < 0 or hora_inicio > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O horário que você digitou não existe, tente novamente{RESET}\n")
                continue
        
        hora_termino = input("Digite a nova hora do término do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if hora_termino == 'voltar':
            
            print("Voltando...")
            return
            
        elif hora_termino.isnumeric():
            
            hora_termino = int(hora_termino)
            
            if hora_termino <= hora_inicio:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print("A hora do término do compromisso não pode ser menor ou igual à hora do início!")
                continue
                
            elif hora_termino < 0 or hora_termino > 23:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O horário que você digitou não existe, tente novamente{RESET}\n")
                continue
        
        desc = input("Digite a nova descrição do compromisso (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if desc == 'voltar':
            
            print("Voltando...")
            return
        
        prioridade = input("Digite se o compromisso tem prioridade ou não, digite 1 para sim e 2 para não (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if prioridade == 'voltar':
            
            print("Voltando...")
            return
        
        elif prioridade.isnumeric():
            
            prioridade = int(prioridade)

            if prioridade == 1:
                prioridade = True
            elif prioridade == 2:
                prioridade = False
            
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
            
        nova_chave = f"{ano:04d}_{mes:02d}_{dia:02d}_{hora_inicio:02d}"
                
        agenda[nova_chave] = {
                "dia": dia,
                "mes": mes,
                "ano": ano,
                "hora_inicio": hora_inicio,
                "hora_termino": hora_termino,
                "descricao": desc,
                "prioridade": prioridade
        }
                
        if nova_chave != chave_montada:
                    
            del agenda[chave_montada]
                
        os.system('cls')
            
        print(f"\n{GREEN}Compromisso editado com sucesso!{RESET}\n")
            
        salvar_dados(agenda)
        break
    os.system('pause')

def filtrar_por_periodo(agenda):
    
    """
    função que filtra compromissos em um periodo específico
    
    primeiro é informado pelo usuário dia, mês e ano iniciais, que será o ponto de partida
    
    depois é informado pelo usuário dia, mês e ano finais, que será a data limite
    
    se houver algum compromisso entre a data inicial e data final irá ser printado
    
    caso não haja, irá ser retornado erro 
    """
    
    while True:
        
        dia_inicio = input("Digite o dia inicial para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if dia_inicio == 'voltar':
            
            print("Voltando...")
            break
            
        elif dia_inicio.isnumeric():
            
            dia_inicio = int(dia_inicio)
            
            if dia_inicio < 1 or dia_inicio > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O dia que você digitou não existe, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        mes_inicio = input("Digite o mes inicial para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if mes_inicio == 'voltar':
            
            print("Voltando...")
            break
            
        elif mes_inicio.isnumeric():
            
            mes_inicio = int(mes_inicio)
            
            if mes_inicio < 1 or mes_inicio > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O mês que você digitou não existe, tente novamente!{RESET}\n")
                continue
            
            elif mes_inicio == 2 and dia_inicio > 29:
                print(f"\n{RED}O mês de fevereiro não tem mais 30 dias, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        ano_inicio = input("Digite o ano inicial para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if ano_inicio == 'voltar':
            
            print("Voltando...")
            break
            
        elif ano_inicio.isnumeric():
            
            
            if len(ano_inicio) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano_inicio = int(ano_inicio)

            if ano_inicio < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano_inicio % 4 == 0 and ano_inicio % 100 != 0 and mes_inicio == 2 or ano_inicio % 400 == 0 and mes_inicio == 2:
                if dia_inicio > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes_inicio == 2 and dia_inicio > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
            
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        dia_final = input("Digite o dia final para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if dia_final == 'voltar':
            
            print("Voltando...")
            break
            
        elif dia_final.isnumeric():
            
            dia_final = int(dia_final)

            if dia_final < 1 or dia_final > 31:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O dia que você digitou não existe, tente novamente!{RESET}\n")
                continue
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        mes_final = input("Digite o mes final para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if mes_final == 'voltar':
            
            print("Voltando...")
            break
            
        elif mes_final.isnumeric():
            
            mes_final = int(mes_final)
            
            if mes_final < 1 or mes_final > 12:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O mês que você digitou não existe, tente novamente!{RESET}\n")
                continue
            
            elif mes_final == 2 and dia_final > 29:
                print(f"\n{RED}O mês de fevereiro não tem mais de 30 dias, tente novamente!{RESET}\n")
                continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção inexistente, tente novamente{RESET}\n")
            continue
        
        ano_final = input("Digite o ano final para a filtragem (ou 'voltar' para voltar ao menu principal): ").lower().strip()
        
        if ano_final == 'voltar':
            
            print("\nVoltando...\n")
            break
            
        elif ano_final.isnumeric():
            
            if len(ano_final) != 4:
                print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
                print(f"\n{RED}O ano precisa ter 4 dígitos, tente novamente!{RESET}\n")
                continue
            
            ano_final = int(ano_final)
            
            if ano_final < 2000:
                print(f"\n{RED}O ano que você digitou não é realista, tente novamente!{RESET}\n")
                continue
            
            elif ano_final % 4 == 0 and ano_final % 100 != 0 and mes_final == 2 or ano_final % 400 == 0 and mes_final == 2:
                if dia_final > 29:
                    print(f"{RED}O mês de fevereiro em anos bissextos tem apenas 29 dias{RESET}")
                    continue
            
            else:
                if mes_final == 2 and dia_final > 28:
                    print(f"\n{RED}O mês de fevereiro em anos que não são bissextos tem apenas 28 dias{RESET}\n")
                    continue
        
        else:
            print(f"\n{YELLOW}#### AVISO ####{RESET}\n")
            print(f"\n{RED}Você digitou uma opção que não existe, tente novamente{RESET}\n")
            continue
        
        encontrou = False
        
        data_inicio = (ano_inicio, mes_inicio, dia_inicio)
        data_final = (ano_final, mes_final, dia_final)
        
        os.system('cls')
        
        for chave, info in sorted(agenda.items()):
            
            data_compromisso = (info['ano'], info['mes'], info['dia'])
            
            if data_inicio <= data_compromisso and data_compromisso <= data_final:
                
                encontrou = True
                
                if info['prioridade'] == True:
                    texto_prioridade = "Urgente"
            
                else:
                    texto_prioridade = "Normal"
        
                print("-" * 40)
                print(f"Data: {info['dia']:02d}/{info['mes']:02d}/{info['ano']:04d}")
                print(f"Horário: {info['hora_inicio']:02d}h às {info['hora_termino']:02d}h")
                print(f"Descrição: {info['descricao']}")
                print(f"Prioridade: {texto_prioridade}")
                
        if encontrou:
            print("-" * 40)    
        
        os.system('pause')
        
        if not encontrou:
            
            print(f"\n{RED}Não existem compromissos cadastrados nesse periodo!{RESET}\n")
            os.system("pause")
        break
        
def obter_dia_mais_ocupado(agenda):
    
    """
    função que conta o número de compromissos no dia e retorna o mais ocupado
    """
    
    if not agenda:
        
        print(f"\n{GREEN}A sua agenda não tem compromissos marcados!{RESET}\n")
        os.system("pause")
        return
    
    dias_ocupados = {}
    contador_votos = 0
    mais_ocupado = ""
        
    os.system('cls')
        
    for chave, info in agenda.items():
            
        chave_checagem = f"{info['ano']}_{info['mes']}_{info['dia']}"
            
        if chave_checagem in dias_ocupados:
            
            dias_ocupados[chave_checagem] = dias_ocupados[chave_checagem] + 1
            
        else:
            
            dias_ocupados[chave_checagem] = 1
        
    for data, votos in dias_ocupados.items():
            
        if votos > contador_votos:
            
            contador_votos = votos
            mais_ocupado = data
    
    ano, mes, dia = mais_ocupado.split('_')
    
    data_formatada = f"{dia}/{mes}/{ano}"
    
    print(f"{GREEN}\n O dia mais ocupada da sua agenda é {data_formatada} com {contador_votos} compromissos!{RESET}\n")
    os.system("pause")
            
minha_agenda = carregar_dados()
mostrar_menu(minha_agenda)