# Leitor e Indexador da Constituição Federal

Este projeto é uma ferramenta para extrair, dividir e indexar o texto da Constituição Federal do Brasil, permitindo buscas eficientes em seu conteúdo. Ele utiliza técnicas de processamento de texto e armazenamento em memória para facilitar a consulta de tópicos específicos.

## Funcionalidades

- **Extrai o texto da Constituição Federal** diretamente de um repositório GitHub.
- **Divide o texto em seções** com base em cabeçalhos Markdown (capítulos).
- **Indexa o conteúdo** em um banco de dados em memória para buscas rápidas.
- **Permite buscas por termos** como "direitos dos trabalhadores" e retorna os trechos relevantes.

## Como Usar

### Pré-requisitos

- Python 3.7 ou superior.
- Bibliotecas Python: `requests`, `langchain`, `vectordb`.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/leitor-constituicao.git
   cd leitor-constituicao
2. Instale as dependências:
    ```
    pip install requests langchain vectordb
3. Execute o script:   
    ```
    python main.py