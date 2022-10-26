import os
import phonenumbers
import time
import pandas as pd
import connect_agenda

class Agenda:

    def __init__(self):
        self._nome = None
        self._telefone = None
        self._email = None

    def iniciar_agenda(self):
        os.system('cls')
        print('=' * 35)
        print('0 - CADASTRAR CONTATO')
        print('1 - PESQUISAR CONTATO')
        print('2 - TODOS OS CONTATOS')
        print('3 - EDITAR CONTATO')
        print('4 - EXCLUIR CONTATO')
        print('5 - EXPORTAR CONTATOS')
        print('=' * 35)
        print('SELECIONE A OPCAO DESEJADA')
        resposta = int(input())
        self.chama_funções(resposta)

    def chama_funções(self,opcao):
        if opcao == 0:
            os.system('cls')
            self.criar_contato()
        elif opcao == 1:
            os.system('cls')
            self.pesquisar_contato()
        elif opcao == 2:
            os.system('cls')
            self.mostrar_todos_contatos()
        elif opcao == 3:
            os.system('cls')
            self.editar_contato()
        elif opcao == 4:
            os.system('cls')
            self.excluir_contato()
        elif opcao == 5:
            os.system('cls')
            self.exportar_contato()

    def criar_contato(self):
        print('Digite o nome do contato')
        self._nome = input().title()
        print('Digite o telefone')
        self._telefone = input()
        self._telefone = phonenumbers.parse(self._telefone, "BR")
        self._telefone = phonenumbers.format_number(self._telefone,phonenumbers.PhoneNumberFormat.NATIONAL)
        print('Digite o email')
        self._email = input()
        connect_agenda.cadastro_sql(self._nome,self._telefone,self._email)
        print('0 - voltar ao menu inicial')
        print('1 - cadastrar novo contato')
        resposta = int(input())
        if resposta == 0:
            self.iniciar_agenda()
        elif resposta == 1:
            os.system('cls')
            self.criar_contato()

    def pesquisar_contato(self):
        print("=" * 35)
        print('Pesquisar contato')
        self._nome = input().title()
        contato = connect_agenda.pesquisar_contato_sql(self._nome)
        if contato != []:
            for id,nome,telefone,email in contato:
                print(f'Nome: {nome} | Telefone: {telefone} | Email principal: {email}')
            print('Deseja voltar ao menu inicial? 0 - SIM | 1 - NÃO')
            resposta = int(input())
            if resposta == 0:
                self.iniciar_agenda()
            elif resposta == 1:
                exit()
        else:
            print('Nenhum registro encontrado')
            print('Deseja cadastrar esse contato? 0-Sim | 1- NÃO')
            resposta = int(input())
            if resposta == 0:
                self.criar_contato()
            elif resposta == 1:
                self.iniciar_agenda()

    def mostrar_todos_contatos(self):
        contato = connect_agenda.mostrar_contatos_sql()
        if contato != []:
            for id,nome,telefone,email in contato:
                print(f'Nome: {nome} | Telefone: {telefone} | Email: {email}')
            print('')    
            print('Deseja voltar ao menu inicial? 0 - SIM/ 1 - NÃO')
            resposta = int(input())
            if resposta == 0:
                self.iniciar_agenda()
            elif resposta == 1:
                exit()

    def editar_contato(self):
        print("=" * 35)
        print('Pesquisar contato')
        self._nome = input().title()
        contato = connect_agenda.pesquisar_contato_sql(self._nome)
        if contato != []:
            for id,nome,telefone,email in contato:
                print(f'ID: {id} | Nome: {nome} | Telefone: {telefone} | Email: {email}')
            print(f'Digite o ID do contato para editar')
            opcao = int(input())
            for id,nome_bd,telefone_bd,email_bd in contato:
                if opcao == id:
                    while True:
                        print('Qual dado deseja alterar?')
                        print('0 - NOME | 1 - TELEFONE | 2 - EMAIL | 3 - VOLTAR AO MENU')
                        opcao_editar = int(input())
                        if opcao_editar == 0:
                            print(f'Editar Nome: {nome_bd}')
                            self._nome = input().title()
                            connect_agenda.editar_contato_sql(opcao,self._nome,telefone_bd,email_bd)
                            print('Nome alterado com sucesso!')
                            time.sleep(1)
                        elif opcao_editar == 1:
                            print(f'Editar Telefone: {telefone_bd}')
                            self._telefone = input()
                            self._telefone = phonenumbers.parse(self._telefone, "BR")
                            self._telefone = phonenumbers.format_number(self._telefone,phonenumbers.PhoneNumberFormat.NATIONAL)
                            connect_agenda.editar_contato_sql(opcao,nome_bd,self._telefone,email_bd)
                            print('Telefone alterado com sucesso!')
                            time.sleep(1)
                        elif opcao_editar == 2:
                            print(f'Editar Email: {email_bd}')
                            email = input()
                            connect_agenda.editar_contato_sql(opcao,nome_bd,telefone_bd,self._email)
                            print('Email alterado com sucesso!')
                            time.sleep(1)
                        elif opcao_editar == 3:
                            self.iniciar_agenda()
                            break
                        else:
                            print('Opção inválida')
                            self.editar_contato()
                        print('Deseja alterar mais algum dado?')
                        print('0 - SIM | 1 - NÃO')
                        resposta = int(input())
                        if resposta == 0:
                            pass
                        else:
                            self.iniciar_agenda()
                            break
        else:
            print('Nenhum registro encontrado')
            time.sleep(1)
            self.editar_contato()

    def excluir_contato(self):
        print("=" * 35)
        print('Pesquisar contato')
        self._nome = input().title()
        contato = connect_agenda.pesquisar_contato_sql(self._nome)
        if contato != []:
            for id,nome,telefone,email in contato:
                print(f'ID: {id} | Nome: {nome} | Telefone: {telefone} | Email: {email}')
            print(f'Digite o ID do contato para excluir')
            opcao = int(input())
            for id,nome,telefone,email in contato:
                if opcao == id:
                    print(f'Deseja remover {nome} | {telefone}? 0 - SIM/ 1 - NÃO')
                    resposta = int(input())  
                    if resposta == 0:
                        connect_agenda.excluir_contato_sql(opcao)
                        print('Contato excluído com sucesso!')
                        time.sleep(1)
                        self.iniciar_agenda()
                    elif resposta == 1:
                        self.iniciar_agenda()
        else:
            print('Indice não encontrado')
            time.sleep(1)
            os.system('cls')
            self.excluir_contato()

    def exportar_contato(self):
        lista = []
        contato = connect_agenda.mostrar_contatos_sql()
        if contato == []:
            print("Nenhum contato para exportar!")
            time.sleep(1)
            self.iniciar_agenda()
        else:
            for id,nome,telefone,email in contato:
                print(f'Nome: {nome} | Telefone: {telefone} | Email: {email}')
            print('')    
            print('Deseja exportar os contatos para csv e xlsx? 0 - SIM/ 1 - NÃO')
            resposta = int(input())
            if resposta == 0:
                for id,nome,telefone,email in contato:
                    lista.append((f'Nome: {nome} | Telefone: {telefone} | Email: {email}'))
                df = pd.DataFrame(lista)
                df.to_excel('contatos.xlsx',index=False)
                df.to_csv('contatos.csv',index=False)
                print('O dados foram exportados com sucesso!')
                time.sleep(1)
                self.iniciar_agenda()
            else:
                self.iniciar_agenda()


if __name__ == '__main__':
    agenda = Agenda()
    agenda.iniciar_agenda()
