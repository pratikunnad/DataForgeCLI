import typer
from rich import print

app = typer.Typer()

@app.command()
def hello():
    print("[bold green]Welcome to DataForge CLI 🚀[/bold green]")

if __name__ == "__main__":
    app()