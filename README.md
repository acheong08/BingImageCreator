# BingImageCreator
High quality image generation by Microsoft. Reverse engineered API.

`pip3 install --upgrade BingImageCreator`

```
 $ python3 -m BingImageCreator -h
usage: BingImageCreator.py [-h] -U U --prompt PROMPT [--output-dir OUTPUT_DIR]

options:
  -h, --help            show this help message and exit
  -U U                  Auth cookie from browser
  --prompt PROMPT       Prompt to generate images for
  --asyncio             Use async to sync png
  --output-dir OUTPUT_DIR
                        Output directory
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
