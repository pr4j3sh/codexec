"""Main module."""

import os
import requests
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.spinner import Spinner

load_dotenv()
console = Console()


def get_output(lang_code: int, input: str, code: str):
    url = os.getenv("CODE_ENGINE_URL")
    payload = {"languageCode": lang_code, "input": input, "code": code}

    with console.status("[bold green]executing code...") as status:
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


def get_lang_code(file_path: str):
    lang_code = -1
    _, ext = os.path.splitext(file_path)
    if ext[1:] == "c":
        lang_code = 50
    elif ext[1:] == "cpp":
        lang_code = 76
    elif ext[1:] == "java":
        lang_code = 62
    elif ext[1:] == "py":
        lang_code = 71
    elif ext[1:] == "js":
        lang_code = 63
    return lang_code


def read_code(file_path: str):
    with open(file_path, "r") as file:
        return file.read()


def read_input(input_path: str):
    with open(input_path, "r") as file:
        return file.read()


def exec_code(file_path: str, input_path: str):
    code = ""
    input = ""
    lang_code = -1

    if file_path and file_path != "":
        code = read_code(file_path)
        lang_code = get_lang_code(file_path)
    else:
        typer.echo("please provide a code file.", err=True)
        raise typer.Exit(code=1)

    if lang_code == -1:
        typer.echo("language not supported.", err=True)
        raise typer.Exit(code=1)

    if input_path and input_path != "":
        input = read_input(input_path)

    response = get_output(lang_code, input, code)
    if isinstance(response, dict) and "data" in response:
        output = response["data"].get("stdout", "no output available")
        if output == None:
            output = response["data"].get("compile_output", "no output available")
        return output
    else:
        typer.echo("received unexpected output format.", err=True)
        raise typer.Exit(code=1)
