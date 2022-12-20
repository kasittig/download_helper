import asyncio
from typing import Coroutine

from download import download_file
from helpers import get_download_params_from_file, list_files_to_download


async def main() -> None:
    # Simple helper function to create our download tasks
    def make_download_task(filename: str) -> Coroutine:
        url, headers, dest_filename = get_download_params_from_file(filename)
        return download_file(url, headers, dest_filename)

    await asyncio.gather(
        *[make_download_task(filename) for filename in list_files_to_download(".")]
    )


if __name__ == "__main__":
    asyncio.run(main())
