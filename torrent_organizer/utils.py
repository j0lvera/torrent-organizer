import PTN
from itertools import chain
from pathlib import Path, PurePath
from typing import Union, List
from torrent_organizer.models import MediaFile


def get_media(
    source: Union[str, PurePath], extensions: Union[list, tuple]
) -> List[MediaFile.dict]:
    path = Path(source).absolute()
    print("path", path)
    list_of_files = []
    for extension in extensions:
        pattern = f"*.{extension}"

        # Get only the file names
        files = [
            MediaFile(name=file.name, path=str(file)).dict()
            for file in list(path.rglob(pattern))
        ]

        print("files", files)

        # Skip empty lists
        if files:
            list_of_files.append(files)

    # Flatten the list
    return list(chain.from_iterable(list_of_files))


def format_name(file_name: str, with_extension=True) -> str:
    formatted_name = PTN.parse(file_name)
    title = formatted_name.get("title")
    year = formatted_name.get("year")
    extension = str.lower(formatted_name.get("container"))
    media_name = f"{title} ({year})"
    return f"{media_name}.{extension}" if with_extension else media_name
