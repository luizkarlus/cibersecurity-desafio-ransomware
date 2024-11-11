# Cibersecurity - Desafio Ransomware

Este projeto é um estudo de caso de ransomware para fins educacionais. Ele contém dois scripts principais:
1. `encrypter.py`: criptografa todos os arquivos `.txt` no diretório atual.
2. `decrypter.py`: descriptografa os arquivos criptografados com a extensão `.ransomwaretroll`, restaurando-os para `.txt`.

> **Atenção**: Este projeto é apenas para aprendizado e deve ser executado somente em um ambiente controlado, como uma máquina virtual. Não utilize em sistemas de produção ou em computadores pessoais.

---

## Estrutura do Projeto

- `encrypter.py`: Script para criptografar arquivos `.txt`.
- `decrypter.py`: Script para descriptografar arquivos `.ransomwaretroll`.
- `requirements.txt`: Lista de dependências para o projeto.
- `README.md`: Documentação do projeto.
- `teste_1.txt`, `teste_2.txt`, `teste_3.txt`: Arquivos de exemplo para testar os scripts de criptografia e descriptografia.

## Pré-requisitos

- Python 3.x instalado
- Pyaes instalado
- Ambiente virtual (opcional, mas recomendado)

## Instalação

1. Clone o repositório e navegue até o diretório do projeto.
   ```bash
   git clone <cole_aqui_a_url_do_repositorio>
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv cibersecurity-desafio-ransomware
   source cibersecurity-desafio-ransomware/bin/activate # No Windows, use: cibersecurity-desafio-ransomware\Scripts\activate
3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
## Uso

1. Criptografar Arquivos
   O script `encrypter.py` percorre o diretório atual e criptografa todos os arquivos .txt, renomeando-os com a extensão .ransomwaretroll.

   Para executar o script de criptografia:
   ```bash
   python cibersecurity-desafio-ransomware/encrypter.py
2. Descriptografar Arquivos
   O script `decrypter.py` procura por arquivos com a extensão `.ransomwaretroll` e os descriptografa, restaurando-os para o formato `.txt`.
   Para executar o script de descriptografia:
   ```bash
   python cibersecurity-desafio-ransomware/decrypter.py
   ```
## Scripts

### encrypter.py

Este script realiza a criptografia de todos os arquivos .txt no diretório atual. Funciona da seguinte maneira:

1. Percorre o diretório atual procurando por arquivos .txt.
2. Para cada arquivo `.txt` encontrado:
   - Lê seu conteúdo.
   - Criptografa os dados usando o algoritmo AES com uma chave pré-definida.
   - Remove o arquivo original.
   - Cria um novo arquivo com o nome original seguido pela extensão `.   ransomwaretroll` e salva o conteúdo criptografado nele.

### decrypter.py

Este script reverte a criptografia de todos os arquivos `.ransomwaretroll` no diretório atual. Funciona da seguinte maneira:

1. Percorre o diretório atual procurando por arquivos `.ransomwaretroll`.
2. Para cada arquivo encontrado:
   - Lê o conteúdo criptografado.
   - Descriptografa os dados usando a mesma chave AES utilizada na criptografia.
   - Remove o arquivo `.ransomwaretroll`.
   - Restaura o arquivo original com a extensão `.txt` e salva o conteúdo descriptografado nele.

---

## Observações

- Certifique-se de que a chave utilizada nos scripts `encrypter.py` e `decrypter.py` seja a mesma para que a descriptografia funcione corretamente.
- Este projeto foi desenvolvido para demonstrar conceitos básicos de criptografia em segurança da informação e não deve ser utilizado para atividades maliciosas.