import os
import pyaes

# chave de descriptografia (deve ser a mesma usada na criptografia)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# listar arquivos no diretório atual
for file_name in os.listdir():
    # verificar se o arquivo tem extensão .ransomwaretroll
    if file_name.endswith(".ransomwaretroll"):
        # abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            crypto_data = file.read()

        # descriptografar o conteúdo do arquivo
        file_data = aes.decrypt(crypto_data)

        # remover o arquivo criptografado
        os.remove(file_name)

        # restaurar o arquivo original .txt
        original_file_name = file_name.replace(".ransomwaretroll", "")
        with open(original_file_name, "wb") as original_file:
            original_file.write(file_data)

        print(f"Arquivo {original_file_name} restaurado com sucesso!")
