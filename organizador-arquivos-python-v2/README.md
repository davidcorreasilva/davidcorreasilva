# Organizador de Arquivos em Python

Aplicação de linha de comando desenvolvida em Python para organizar automaticamente arquivos por categorias e extensões.

## Funcionalidades

- Identifica arquivos pela extensão.
- Cria pastas de categorias automaticamente.
- Move arquivos para os diretórios correspondentes.
- Ignora diretórios durante a leitura.
- Evita sobrescrever arquivos com o mesmo nome.
- Valida caminhos inexistentes ou inválidos.
- Exibe resumo da execução.
- Possui modo de simulação com `--dry-run`.
- Permite informar a pasta diretamente pelo terminal com `--path`.

## Tecnologias e conceitos

- Python
- `pathlib`
- `shutil`
- `argparse`
- Interface de linha de comando (CLI)
- Tratamento de exceções
- Separação de responsabilidades
- Type hints

## Como executar

```bash
python main.py --path "CAMINHO_DA_PASTA"
```

Exemplo no Windows:

```bash
python main.py --path "C:\\Users\\David\\Downloads"
```

No Windows, caso o comando `python` não esteja configurado:

```bash
py main.py --path "C:\\Users\\David\\Downloads"
```

## Modo de simulação

O modo `--dry-run` mostra as alterações que seriam realizadas sem mover nenhum arquivo.

```bash
python main.py --path "C:\\Users\\David\\Downloads" --dry-run
```

Exemplo de saída:

```text
[SIMULAÇÃO] curriculo.pdf -> Documentos/
[SIMULAÇÃO] foto.jpg -> Imagens/
[SIMULAÇÃO] planilha.xlsx -> Planilhas/

Simulação concluída. Nenhum arquivo foi movido.
```

## Categorias suportadas

- Documentos
- Imagens
- Áudios
- Vídeos
- Planilhas
- Compactados
- Outros

## Estrutura do projeto

```text
organizador-arquivos-python/
├── main.py
├── config.py
├── README.md
└── .gitignore
```

## Próximas melhorias

- Logs persistentes em arquivo.
- Testes automatizados com `pytest`.
- Estratégia para arquivos duplicados.
- Configuração personalizada de categorias.

## Autor

David Corrêa Silva

Técnico em Tecnologia da Informação pelo Instituto Federal Fluminense (IFF) e estudante de Análise e Desenvolvimento de Sistemas.
