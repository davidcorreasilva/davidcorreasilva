from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from config import CATEGORIAS


def descobrir_categoria(extensao: str) -> str:
    """Retorna a categoria correspondente à extensão do arquivo."""
    extensao = extensao.lower()

    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria

    return "Outros"


def validar_pasta(pasta: Path) -> None:
    """Valida se o caminho existe e representa um diretório."""
    if not pasta.exists():
        raise FileNotFoundError(f"A pasta não existe: {pasta}")

    if not pasta.is_dir():
        raise NotADirectoryError(
            f"O caminho informado não é uma pasta: {pasta}"
        )


def organizar_arquivos(pasta: Path, dry_run: bool = False) -> tuple[int, int]:
    """Organiza arquivos por categoria e retorna (movidos, ignorados)."""
    validar_pasta(pasta)

    movidos = 0
    ignorados = 0

    for item in pasta.iterdir():
        if not item.is_file():
            continue

        categoria = descobrir_categoria(item.suffix)
        pasta_destino = pasta / categoria
        destino = pasta_destino / item.name

        if destino.exists():
            print(f"[IGNORADO] Já existe: {destino.name}")
            ignorados += 1
            continue

        if dry_run:
            print(f"[SIMULAÇÃO] {item.name} -> {categoria}/")
            continue

        pasta_destino.mkdir(exist_ok=True)
        shutil.move(str(item), str(destino))
        print(f"[MOVIDO] {item.name} -> {categoria}/")
        movidos += 1

    return movidos, ignorados


def criar_parser() -> argparse.ArgumentParser:
    """Cria e configura os argumentos da interface de linha de comando."""
    parser = argparse.ArgumentParser(
        description=(
            "Organiza automaticamente arquivos em categorias "
            "de acordo com suas extensões."
        )
    )

    parser.add_argument(
        "--path",
        type=Path,
        required=True,
        help="Caminho da pasta que será organizada.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula a organização sem mover os arquivos.",
    )

    return parser


def main() -> None:
    parser = criar_parser()
    argumentos = parser.parse_args()

    pasta = argumentos.path.expanduser()

    try:
        movidos, ignorados = organizar_arquivos(
            pasta=pasta,
            dry_run=argumentos.dry_run,
        )

        if argumentos.dry_run:
            print("\nSimulação concluída. Nenhum arquivo foi movido.")
            return

        print("\nOrganização concluída com sucesso.")
        print(f"Arquivos movidos: {movidos}")
        print(f"Arquivos ignorados: {ignorados}")

    except (FileNotFoundError, NotADirectoryError, PermissionError) as erro:
        print(f"\n[ERRO] {erro}")


if __name__ == "__main__":
    main()
