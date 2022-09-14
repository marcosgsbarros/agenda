import os
import phonenumbers
import time
import pandas as pd

class Agenda:

    def __init__(self) -> None:
        self._contato = []
    
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
        nome = input().title()
        print('Digite o telefone')
        telefone = input()
        telefone_formulario_ajustado = phonenumbers.parse(telefone, "BR")
        telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)
        print('Digite o email')
        email = input()
        self._contato.append({'nome':nome,'telefone':telefone_formatado,'email':email})
        print('0 - voltar ao menu inicial')
        print('1 - cadastrar novo contato')
        resposta = int(input())
        if resposta == 0:
            self.iniciar_agenda()
        elif resposta == 1:
            os.system('cls')
            self.criar_contato()

    def pesquisar_contato(self):
        indices = []
        if self._contato == []:
            print('=' * 35)
            print('Nenhum contato registrado')
            print('=' * 35)
            time.sleep(1)
            self.iniciar_agenda()
        else:
            print("=" * 35)
            print('Pesquisar contato')
            nome = input().title()
            for i,contato in enumerate(self._contato):
                if nome in contato['nome']:
                    indices.append(i)
                    print('Nome: {} telefone: {} email: {} '.format(contato['nome'],contato['telefone'],contato['email']))
                else:
                    pass
            if indices == []:
                print('registro não encontrado')
                print('Deseja adicionar esse contato? 0 - SIM/ 1 - NÃO')
                resposta = int(input())
                if resposta == 0:
                    self.criar_contato()
                elif resposta == 1:
                    self.iniciar_agenda()
                else:
                    print('Opção inválida')
                    self.iniciar_agenda()

            print('Deseja voltar ao menu inicial? 0 - SIM/ 1 - NÃO')
            resposta = int(input())
            if resposta == 0:
                self.iniciar_agenda()
            elif resposta == 1:
                exit()

    def mostrar_todos_contatos(self):
        if self._contato == []:
            print('=' * 35)
            print('Nenhum contato registrado')
            print('=' * 35)
            time.sleep(1)
            self.iniciar_agenda()
        else:
            for contato in self._contato:
                print('Nome: {} telefone: {} email: {} '.format(contato['nome'],contato['telefone'],contato['email']))
            print('Deseja voltar ao menu inicial? 0 - SIM/ 1 - NÃO')
            resposta = int(input())
            if resposta == 0:
                self.iniciar_agenda()
            elif resposta == 1:
                exit()

    def editar_contato(self):
        indices = []
        if self._contato == []:
            print('=' * 35)
            print('Nenhum contato registrado')
            print('=' * 35)
            time.sleep(1)
            self.iniciar_agenda()
        else:
            print("=" * 35)
            print('Pesquisar contato')
            nome = input().title()
            for i,contato in enumerate(self._contato):
                if nome in contato['nome']:
                    indices.append(i)
                    print('[{}] Nome: {} telefone: {} email: {} '.format(i,contato['nome'],contato['telefone'],contato['email']))
                else:
                    pass
            if indices == []:            
                print('Contato não encontrado')
                time.sleep(1)
                self.editar_contato()
            else:
                print(f'Digite o indice do contato para editar')
                opcao = int(input())
                if opcao not in indices:
                    print('Indice não encontrado')
                    time.sleep(1)
                    os.system('cls')
                    self.editar_contato()
                while True:
                    for i,contato in enumerate(self._contato):
                            if opcao == i:
                                print('Qual dado deseja alterar?')
                                print('0 - NOME | 1 - TELEFONE | 2 - EMAIL | 3 - VOLTAR AO MENU')
                                opcao_editar = int(input())
                                if opcao_editar == 0:
                                    print('EDITAR NOME')
                                    nome = input().title()
                                    contato['nome'] = nome 
                                elif opcao_editar == 1:
                                    print('EDITAR TELEFONE')
                                    telefone = input()
                                    telefone_formulario_ajustado = phonenumbers.parse(telefone, "BR")
                                    telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)
                                    contato['telefone'] = telefone_formatado
                                elif opcao_editar == 2:
                                    print('EDITAR EMAIL')
                                    email = input()
                                    contato['email'] = email
                                elif opcao_editar == 3:
                                    self.iniciar_agenda()
                                else:
                                    print('Opção inválida')
                                print('Deseja alterar mais algum dado?')
                                print('0 - SIM | 1 - NÃO')
                                resposta = int(input())
                                if resposta == 0:
                                    pass
                                else:
                                    self.iniciar_agenda()
                                    break
    
    def excluir_contato(self):
        indices = []
        if self._contato == []:
            print('=' * 35)
            print('Nenhum contato registrado')
            print('=' * 35)
            time.sleep(1)
            self.iniciar_agenda()
        else:
            print("=" * 35)
            print('Pesquisar contato')
            nome = input().title()
            for i,contato in enumerate(self._contato):
                if nome in contato['nome']:
                    indices.append(i)
                    print('[{}] Nome: {} telefone: {} email: {} '.format(i,contato['nome'],contato['telefone'],contato['email']))
                else:
                    pass
            if indices == []:
                print('Contato não encontrado')
                time.sleep(1)
                os.system('cls')
                self.excluir_contato()
            print(f'Digite o indice do contato para excluir')
            opcao = int(input())
            if opcao not in indices:
                print('Indice não encontrado')
                time.sleep(1)
                os.system('cls')
                self.excluir_contato()
            else:
                for i,contato in enumerate(self._contato):
                    if opcao == i:
                        print(f'Deseja remover {contato["nome"]}? 0 - SIM/ 1 - NÃO')
                        resposta = int(input())  
                        if resposta == 0:
                            self._contato.pop(i)
                            print('Contato excluído com sucesso!')
                            time.sleep(1)
                            self.iniciar_agenda()
                        elif resposta == 1:
                            self.iniciar_agenda()
            indices.clear()
    
    def exportar_contato(self):
        if self._contato == []:
            print('=' * 35)
            print('Nenhum contato para ser exportado')
            print('=' * 35)
            time.sleep(1)
            self.iniciar_agenda()
        else:
            df = pd.DataFrame(data=self._contato)
            df.to_excel('contatos.xlsx',index=False)
            df.to_csv('contatos.csv',index=False)
            print('O dados foram exportados com sucesso!')
            print('formatos xlsx e csv.')
            time.sleep(1)
            self.iniciar_agenda()


if __name__ == '__main__':
    agenda = Agenda()
    agenda.iniciar_agenda()



