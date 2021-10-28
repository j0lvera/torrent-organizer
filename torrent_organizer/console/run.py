import click
from torrent_organizer.organize import organize


DEFAULT_EXTENSIONS = "mp4,mkv"


@click.command()
@click.argument("source", metavar="<source>")
@click.argument("destination", metavar="<destination>")
@click.option(
    "--extensions",
    help=f"Extensions separated by a comma, e.g., '{DEFAULT_EXTENSIONS}'",
    default=DEFAULT_EXTENSIONS,
    metavar="<str>",
)
def cli(source, destination, extensions):
    """
    Organizes torrent files by creating hardlinks from <source> to <destination>
    with the format "Title (Year)/Title (Year).extension".
    """

    organize(source, destination, extensions)
