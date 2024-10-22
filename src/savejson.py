import json
import main as ma
import os


def saving_to_json():

    df = ma.processing_data()
    # Criar o diretório 'clean' se não existir
    os.makedirs('clean', exist_ok=True)

    # Definir o caminho do arquivo de saída
    output_file = os.path.join('..','clean', 'data.json')

    df.to_json(output_file, orient='records', lines=True)
    print(f"Dados salvos em {output_file}")


def main():
    saving_to_json()


if __name__ == '__main__':
    main()