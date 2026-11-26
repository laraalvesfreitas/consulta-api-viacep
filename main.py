import requests
import sys



def main():

    print(20 * '#')
    print('### Consulta CEP ###')
    print(20 * '#')

    cep_input = input('Digite um CEP para consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida. ')
        sys.exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adress_data = request.json()

    if 'erro' not in adress_data:
        print('--- CEP Encontrado ---')

        print(f'CEP: {adress_data['cep']} ')
        print(f'Logradouro: {adress_data['logradouro']} ')
        print(f'Complemento: {adress_data['complemento']} ')
        print(f'Bairro: {adress_data['bairro']} ')
        print(f'Cidade: {adress_data['localidade']} ')
        print(f'Estado: {adress_data['estado']} ')
        print(f'Região:  {adress_data['regiao']} ')


    else:
        print(f'{cep_input} CEP Inválido!')

    new_search = int(input('Deseja realizar uma nova consulta? \n 1 [SIM] \n 2 [SAIR] \n' ))
    if new_search == 1:
        main()
    else: 
        print('Saindo')

    print('--------------------------------------------------')
main()