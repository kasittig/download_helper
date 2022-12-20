# Asynchronous MP4 file downloader

## Usage
This tool will look in this project's root directory for any JSON-formatted MP4 download config files and will start tasks to download any undownloaded files in parallel.

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