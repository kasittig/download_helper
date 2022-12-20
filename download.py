import os

import aiohttp
import tqdm


async def download_file(url: str, headers: dict[str, str], filename: str,) -> bool:
    """This is a simple helper method that asynchronously downloads a file from a URL to a specified target.

    If our download fails, we'll clean up by deleting the partial download before exiting.

    :param url: the URL where the file to download is located
    :param headers: any headers our HTTP client should use to download this file
    :param filename: the path where the data we download should be stored
    :return: True after the download completes
    """

    try:
        # We wrap our entire download block in a try / except block so we can clean up any partially downloaded files on failure
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                # This gets the total size of the file so we can keep our progress bar updated
                file_size = int(response.headers["Content-Length"])

                # Create a progress bar using TQDM
                with tqdm.tqdm(
                    total=file_size,
                    unit="B",
                    unit_scale=True,
                    desc=f"{filename} download",
                ) as progress_bar:

                    # We write the data in chunks so we can update our progress bar
                    with open(filename, "wb+") as f:
                        async for chunk, _ in response.content.iter_chunks():
                            f.write(chunk)
                            progress_bar.update(len(chunk))
    except Exception as e:
        # Generic exception handler - if there are any errors, remove the download and re-raise the exception
        os.remove(filename)
        raise e
    else:
        # Only executed if no exception was raised
        return True
