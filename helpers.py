import json
import os
from typing import Generator, Tuple


def _gen_files_by_suffix(directory: str, suffix: str) -> Generator[str, None, None]:
    """A helper method that generates the paths of all files located in a given directory that end with a given suffix.

    :param directory: path to the target directory
    :param suffix: filename ending we're looking for (e.g. .json)
    :return: a generator that yields paths ending in the specified directory with the specified suffix
    """

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(suffix):
                yield os.path.join(root, filename)


def list_files_to_download(directory: str) -> list[str]:
    """This is where our "business logic" lives.

    We check all JSON files in a directory and return any that don't have an associated MP4. These are the files that contain new entries we need to download!

    :param directory: path to the directory where we should look
    :return: a generator that yields the JSON filenames that need to be downloaded
    """
    return [
        filename
        for filename in _gen_files_by_suffix(directory, ".json")
        if not os.path.exists(filename.replace(".json", ".mp4"))
    ]


def get_download_params_from_file(filename: str) -> Tuple[str, dict[str, str], str]:
    """Helper method to parse download parameters out of our JSON blob.

    :param filename: name of the file where our JSON blob is stored
    :return: the url, headers, and name of the file where this data should be saved
    """
    with open(filename) as f:
        data = json.load(f)
        return data["url"], data["headers"], filename.replace(".json", ".mp4")
