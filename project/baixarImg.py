from googlesearch import search
import os
import urllib.request

# Função para baixar imagens de acordo com a pesquisa
def download_images(search_query, download_path, num_images=10):
    search_results = search(search_query, num_images=num_images, stop=num_images)

    # Certificar-se de que o diretório de download exista
    os.makedirs(download_path, exist_ok=True)

    # Baixar as imagens
    for i, url in enumerate(search_results):
        try:
            urllib.request.urlretrieve(url, os.path.join(download_path, f"{i+1}.jpg"))
            print(f"Imagem {i+1}/{num_images} baixada com sucesso.")
        except Exception as e:
            print(f"Erro ao baixar imagem {i+1}: {str(e)}")

# Exemplo de uso
search_query = "mão com 1 dedo"
download_path = "imagens_mao_1_dedo"
num_images = 5  # Número de imagens para baixar

download_images(search_query, download_path, num_images)
