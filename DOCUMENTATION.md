<a id="BingImageCreator"></a>

# BingImageCreator

<a id="BingImageCreator.ImageGen"></a>

## ImageGen Objects

```python
class ImageGen()
```

Image generation by Microsoft Bing

**Arguments**:

- `auth_cookie` - str

<a id="BingImageCreator.ImageGen.getImages"></a>

#### getImages

```python
def getImages(prompt: str) -> list
```

Fetches image links from Bing

**Arguments**:

- `prompt` - str
  Returns a list of image links

<a id="BingImageCreator.ImageGen.saveImages"></a>

#### saveImages

```python
def saveImages(links: list, output_dir: str) -> None
```

Saves images to output directory

