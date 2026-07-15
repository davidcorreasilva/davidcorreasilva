# Organizador de Arquivos em Python

Aplicação em Python para organizar automaticamente arquivos por categorias e extensões.

## Funcionalidades

- Identifica arquivos pela extensão.
- Cria pastas de categorias automaticamente.
- Move arquivos para as pastas correspondentes.
- Ignora diretórios.
- Evita sobrescrever arquivos com o mesmo nome.
- Trata caminhos inexistentes ou inválidos.

## Tecnologias

- Python
- pathlib
- shutil

## Como executar

```bash
python main.py
```

Informe o caminho da pasta que deseja organizar.

Exemplo no Windows:

```text
C:\\Users\\David\\Downloads
```

## Estrutura

```text
organizador-arquivos-python/
├── main.py
├── config.py
├── README.md
└── .gitignore
```

## Próximas melhorias

- Modo de simulação (`--dry-run`)
- Interface de linha de comando com `argparse`
- Logs
- Testes automatizados
