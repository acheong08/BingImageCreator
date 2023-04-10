# BingImageCreator
High quality image generation by Microsoft. Reverse engineered API.

`pip3 install --upgrade BingImageCreator`

```
usage: BingImageCreator.py [-h] [-U U] [--cookie-file COOKIE_FILE] [--output-dir OUTPUT_DIR]
                           [--debug-file DEBUG_FILE] [--quiet] [--asyncio] [--version]
                           prompt [prompt ...]

positional arguments:
  prompt                Prompt to generate images for

options:
  -h, --help            show this help message and exit
  -U U                  Auth cookie from browser
  --cookie-file COOKIE_FILE
                        File containing auth cookie
  --output-dir OUTPUT_DIR
                        Output directory
  --debug-file DEBUG_FILE
                        Path to the file where debug information will be written.
  --quiet               Disable pipeline messages
  --asyncio             Run ImageGen using asyncio
  --version             Print the version number
```

[Developer Documentation](https://github.com/acheong08/BingImageCreator/blob/main/DOCUMENTATION.md)


## Getting authentication
### Chromium based browsers (Edge, Opera, Vivaldi, Brave)
- Go to https://bing.com/.
- F12 to open console
- In the JavaScript console, type `cookieStore.get("_U").then(result => console.log(result.value))` and press enter
- Copy the output. This is used in `--U` or `auth_cookie`.

### Firefox
- Go to https://bing.com/.
- F12 to open developer tools
- navigate to the storage tab
- expand the cookies tab
- click on the `https://bing.com` cookie
- copy the value from the `_U`
