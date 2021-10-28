from pathlib import Path, PurePath
from torrent_organizer import __version__
from torrent_organizer.utils import get_media, format_name, has_ignored_words
from torrent_organizer.config import Config


def test_version():
    assert __version__ == "0.1.0"


def test_get_media():
    base_dir = str(Path(__file__).parent.absolute())
    extensions = ("mkv", "mp4")

    example_1_path = PurePath(base_dir, "stubs/example_1")
    example_1_result = get_media(example_1_path, extensions)
    example_1_expected_name = "Toward the Terra (1980).mkv"
    example_1_expected_path = f"{example_1_path}/{example_1_expected_name}"
    print("example 1", example_1_result)
    assert example_1_result == [
        dict(
            name=example_1_expected_name,
            path=example_1_expected_path,
        )
    ]

    example_2_path = PurePath(base_dir, "stubs/example_2")
    example_2_result = get_media(example_2_path, extensions)
    example_2_expected_name = example_1_expected_name
    example_2_expected_path = (
        f"{example_2_path}/01. Toward the Terra (1980)/{example_2_expected_name}"
    )
    assert example_2_result == [
        dict(name=example_2_expected_name, path=example_2_expected_path)
    ]

    example_3_path = PurePath(base_dir, "stubs/example_3")
    example_3_result = get_media(example_3_path, extensions)
    assert example_3_result == []

    example_4_path = PurePath(base_dir, "stubs/example_4")
    example_4_result = [
        file.get("name") for file in get_media(example_4_path, extensions)
    ]
    assert example_4_result == [
        "Toward the Terra (1980).mkv",
        "Akira - 30th Anniversary Edition (1988 - 1080p TRI Audio).mkv",
        "Vampire Hunter D (1985).mp4",
    ]


def test_format_name():
    base_dir = str(Path(__file__).parent.absolute())
    extensions = ("mkv", "mp4")
    example_4_path = PurePath(base_dir, "stubs/example_4")
    example_4_result = get_media(example_4_path, extensions)

    formatted_result = [format_name(file.get("name")) for file in example_4_result]
    assert formatted_result == [
        "Toward the Terra (1980).mkv",
        "Akira - 30th Anniversary Edition (1988).mkv",
        "Vampire Hunter D (1985).mp4",
    ]


def test_has_ignored_words():
    # ignore_list = Config().ignore_list

    assert has_ignored_words("Toward the Terra - Extra (1980).mkv")
    assert has_ignored_words("Venus Wars - Extra - CPM Trailer")


# def has_ignored_words(item: str) -> bool:
#     ignore_list = Config().ignore_list
#
#     for ignore_word in ignore_list:
#         if ignore_word in item.lower():
#             return True
#
#     return False
