"""Define the command-line interface for the containschecker program."""


# TODO: Define all of the functions needed to support the command-line interface


def main(
    word: str = typer.Option(...),
    data_file: Path = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Read in a data file and then check to see if the file contains the specified word."""
    # TODO: Provide all of the required source code to implement the command-line interface
