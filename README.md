# Asynchronous MP4 file downloader

## Usage
This tool will look in this project's root directory for any JSON-formatted MP4 download config files and will start tasks to download any undownloaded files in parallel.

E.g. if your directory structure currently looks like:

```
download_helper/
    video_1.json
    video_1.mp4
    video_2.json
```

And you run this helper, it will attempt to download `video_2` to `video_2.mp4` from the URL in `video_2.json`, using the headers in `video_2.json`.

### Config formatting
Each config should have the structure:

```json
{
    "url": "http://path.to.file",
    "headers": {
        "my_header_1": "value",
        "my_header_2": "value"
    }
}
```
###### example.json (will be downloaded to example.mp4)


## Notes
This repository was written for a friend and is formatted according to their code style preferences.
