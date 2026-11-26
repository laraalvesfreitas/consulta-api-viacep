# 📮 Consulta de CEP com ViaCEP

Mini projeto em Python que consome a API pública [ViaCEP](https://viacep.com.br/) para buscar o endereço completo a partir de um CEP.

## 🎯 Objetivo

Praticar o consumo de APIs REST com Python: fazer requisições HTTP, tratar a resposta em JSON e lidar com erros (CEP inválido, CEP inexistente, falha de conexão).

## ✨ Funcionalidades

- Consulta de endereço por CEP
- Validação do formato do CEP (8 dígitos)
- Tratamento de CEP inexistente
- Tratamento de erros de conexão e timeout
- Exibição formatada do resultado no terminal

## 🛠️ Tecnologias

- Python 3.8+
- [requests](https://pypi.org/project/requests/)

## 📋 Pré-requisitos

- Python 3.8 ou superior instalado
- pip

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

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o programa:

```bash
python main.py
```

## 💻 Exemplo de uso

```text
Digite o CEP (somente números): 30140071

----- Endereço encontrado -----
CEP:         30140-071
Logradouro:  Avenida Afonso Pena
Bairro:      Centro
Cidade:      Belo Horizonte
Estado:      MG
DDD:         31
-------------------------------
```

Exemplo com CEP inexistente:

```text
Digite o CEP (somente números): 99999999
CEP não encontrado.
```

## 🔌 Sobre a API

- **Endpoint:** `https://viacep.com.br/ws/{cep}/json/`
- **Método:** `GET`
- **Autenticação:** não é necessária

Exemplo de resposta:

```json
{
  "cep": "30140-071",
  "logradouro": "Avenida Afonso Pena",
  "complemento": "",
  "bairro": "Centro",
  "localidade": "Belo Horizonte",
  "uf": "MG",
  
}
```

Quando o CEP tem formato válido mas não existe, a API retorna:

```json
{ "erro": true }
```

## 📁 Estrutura do projeto

```text
consulta-cep/
├── main.py            # Ponto de entrada do programa
├── requirements.txt   # Dependências
└── README.md          # Documentação
```

## 🧪 Tratamento de erros

| Situação              | Comportamento                                   |
|-----------------------|-------------------------------------------------|
| CEP com formato inválido | Exibe mensagem pedindo 8 dígitos numéricos   |
| CEP inexistente       | Exibe "CEP não encontrado"                      |
| Sem conexão / timeout | Exibe mensagem de erro de conexão               |
| Erro HTTP (4xx/5xx)   | Exibe o código de status retornado              |

## 🔮 Próximos passos

- [ ] Buscar CEP a partir de UF, cidade e logradouro
- [ ] Salvar histórico de consultas em arquivo (CSV/JSON)
- [ ] Criar testes automatizados com `pytest`
- [ ] Adicionar interface via linha de comando com `argparse`

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.

## 👩‍💻 Autora

**Lara Alves de Freitas**
[LinkedIn](https://linkedin.com/in/laraalvesfreitas) · [GitHub](https://github.com/laraalvesfreitas)