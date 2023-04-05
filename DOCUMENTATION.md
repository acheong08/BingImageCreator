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

<a id="BingImageCreator.ImageGen.get_images"></a>

#### get\_images

```python
def get_images(prompt: str) -> list
```

Fetches image links from Bing

**Arguments**:

- `prompt` - str
  Returns a list of image links

<a id="BingImageCreator.ImageGen.save_images"></a>

#### save\_images

```python
def save_images(links: list, output_dir: str) -> None
```

Saves images to output directory
