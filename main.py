import requests
from langchain.text_splitter import MarkdownHeaderTextSplitter
from vectordb import Memory

bruto_text =  requests.get('https://raw.githubusercontent.com/abjur/constituicao/refs/heads/main/CONSTITUICAO.md').text
bruto_text

padrao_capitulo = [
    ("##", "Capitulo"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=padrao_capitulo)
sections = markdown_splitter.split_text(bruto_text)
memory = Memory(chunking_strategy={"mode": "sliding_window", "window_size":128, "overlap":8})

for i in range (0, len(sections)):
  capitulo = sections[i].metadata
  texto = sections[i].page_content

  metadata = {'capitulo': capitulo, 'origem' : 'constituição federal'}
  memory.save(texto, metadata)
resposta  = memory.search('direitos dos trabalhadores', top_n=5)
print(resposta)