from pathlib import Path
import shutil

from config import CATEGORIAS


def descobrir_categoria(extensao: str) -> str:
    """Retorna a categoria correspondente à extensão do arquivo."""
    extensao = extensao.lower()

    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria

    return "Outros"


def organizar_arquivos(pasta: Path) -> None:
    """Organiza os arquivos da pasta em subpastas por categoria."""
    if not pasta.exists():
        raise FileNotFoundError(f"A pasta não existe: {pasta}")

    if not pasta.is_dir():
        raise NotADirectoryError(f"O caminho informado não é uma pasta: {pasta}")

    for item in pasta.iterdir():
        if not item.is_file():
            continue

        categoria = descobrir_categoria(item.suffix)
        pasta_destino = pasta / categoria
        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / item.name

        if destino.exists():
            print(f"[IGNORADO] Já existe: {destino.name}")
            continue

        shutil.move(str(item), str(destino))
        print(f"[MOVIDO] {item.name} -> {categoria}/")


def main() -> None:
    caminho = input("Digite o caminho da pasta que deseja organizar: ").strip()
    pasta = Path(caminho).expanduser()

    try:
        organizar_arquivos(pasta)
        print("\nOrganização concluída com sucesso.")
    except (FileNotFoundError, NotADirectoryError) as erro:
        print(f"\n[ERRO] {erro}")


if __name__ == "__main__":
    main()
