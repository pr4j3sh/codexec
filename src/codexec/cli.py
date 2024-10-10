"""Console script for codexec."""
import codexec

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for codexec."""
    console.print("Replace this message by putting your code into "
               "codexec.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
