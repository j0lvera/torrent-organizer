from pathlib import Path
from torrent_organizer.config import Config
from torrent_organizer.utils import get_media, format_name

config = Config()


def organize(source, destination, extensions=config.extensions):
    extensions = extensions.split(",")
    list_of_files = get_media(source, extensions)

    for file in list_of_files:
        try:
            media_file_name = file.get("name")
            media_file_path = file.get("path")

            formatted_folder_name = format_name(media_file_name, with_extension=False)
            formatted_file_name = format_name(media_file_name)

            # Create the directory
            destination_folder_path = f"{destination}/{formatted_folder_name}"
            Path(destination_folder_path).mkdir(exist_ok=True, parents=True)
            destination_file_path = f"{destination_folder_path}/{formatted_file_name}"

            # Create hard links
            original_file = Path(media_file_path)
            original_file.link_to(destination_file_path)

        except (FileExistsError, PermissionError):
            print("File exists or permission error. Skipping.")
