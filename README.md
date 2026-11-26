# 📮 Consulta de CEP com ViaCEP

Mini projeto em Python que consome a API pública [ViaCEP](https://viacep.com.br/) para buscar o endereço a partir de um CEP, direto no terminal.

## 🎯 Objetivo

Praticar o consumo de APIs REST com Python: fazer requisições HTTP, ler a resposta em JSON e tratar o caso de CEP inexistente.

## ✨ Funcionalidades

- Consulta de endereço por CEP informado pelo usuário
- Validação da quantidade de dígitos (8)
- Tratamento de CEP não encontrado
- Exibição de CEP, logradouro, complemento, bairro, cidade, estado e região
- Opção de realizar uma nova consulta sem reiniciar o programa

## 🛠️ Tecnologias

- Python 3.12+
- [requests](https://pypi.org/project/requests/)

> O código usa aspas simples dentro de f-strings com aspas simples (ex.: `f'{dados['cep']}'`), o que só é permitido a partir do Python 3.12.

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/consulta-cep.git
cd consulta-cep
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

3. Instale a dependência:

```bash
pip install requests
```

4. Execute o programa:

```bash
python main.py
```

## 💻 Exemplo de uso

```text
####################
### Consulta CEP ###
####################
Digite um CEP para consulta: 30140071
--- CEP Encontrado ---
CEP: 30140-071
Logradouro: Avenida Afonso Pena
Complemento:
Bairro: Centro
Cidade: Belo Horizonte
Estado: Minas Gerais
Região: Sudeste

Deseja realizar uma nova consulta?
 1 [SIM]
 2 [SAIR]
```

CEP inexistente:

```text
Digite um CEP para consulta: 99999999
99999999 CEP Inválido!
```

Quantidade de dígitos incorreta:

```text
Digite um CEP para consulta: 123
Quantidade de digitos inválida.
```

## 🔌 Sobre a API

- **Endpoint:** `https://viacep.com.br/ws/{cep}/json/`
- **Método:** `GET`
- **Autenticação:** não é necessária

Quando o CEP tem formato válido mas não existe, a API retorna:

```json
{ "erro": true }
```

## 📁 Estrutura do projeto

```text
consulta-cep/
├── main.py     # Código do programa
├── requirements.txt
└── README.md   # Documentação
```

## 👩‍💻 Autora

**Lara Alves de Freitas**
[LinkedIn](https://linkedin.com/in/seu-perfil) · [GitHub](https://github.com/seu-usuario)
