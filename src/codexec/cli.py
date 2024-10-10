"""Console script for codexec."""

import codexec
import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main(file_path: str, input_path: str = None):
    """Console script for codexec."""
    try:
        output = codexec.exec_code(file_path, input_path)
        typer.echo(output)
    except Exception as e:
        if str(e) != "":
            console.print(f"[red]error:[/red] {str(e)}")


if __name__ == "__main__":
    app()
