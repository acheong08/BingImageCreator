<a id="BingImageCreator"></a>

# BingImageCreator

<a id="BingImageCreator.debug"></a>

#### debug

```python
def debug(debug_file, text_var)
```

helper function for debug

<a id="BingImageCreator.ImageGen"></a>

## ImageGen Objects

```python
class ImageGen()
```

Image generation by Microsoft Bing

**Arguments**:

- `auth_cookie` - str
  Optional Parameters:
- `debug_file` - str
- `quiet` - bool
- `all_cookies` - List[Dict]

<a id="BingImageCreator.ImageGen.get_images"></a>

#### get\_images

```python
def get_images(prompt: str) -> list
```

Fetches image links from Bing

**Arguments**:

- `prompt` - str

<a id="BingImageCreator.ImageGen.save_images"></a>

#### save\_images

```python
def save_images(links: list, output_dir: str, file_name: str = None) -> None
```

Saves images to output directory

**Arguments**:

- `links` - list[str]
- `output_dir` - str
- `file_name` - str

<a id="BingImageCreator.ImageGenAsync"></a>

## ImageGenAsync Objects

```python
class ImageGenAsync()
```

Image generation by Microsoft Bing

**Arguments**:

- `auth_cookie` - str
  Optional Parameters:
- `debug_file` - str
- `quiet` - bool
- `all_cookies` - list[dict]

<a id="BingImageCreator.ImageGenAsync.get_images"></a>

#### get\_images

```python
async def get_images(prompt: str) -> list
```

Fetches image links from Bing

**Arguments**:

- `prompt` - str

<a id="BingImageCreator.ImageGenAsync.save_images"></a>

#### save\_images

```python
async def save_images(links: list,
                      output_dir: str,
                      file_name: str = None) -> None
```

Saves images to output directory
