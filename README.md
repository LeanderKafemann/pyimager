# pyimager
a package for displaying images in console and creating/compressing them
## Installation
### Using *pip*
You can install pyimager via pip using
<li>in a commandline:</li><br/>

```
py -m pip install pyimager
```
<br/>
<li>in a python script:</li><br/>

```python
import os
os.system('py -m pip install pyimager')
```
## Usage
### Creating an image
If you don't want to create an image manually,<br/>
i strongly recommend using pyimagers Designer Mode, that is updated often to fix any issues.<br/>
<br/>
Use it via a commandline the following:

```bash
py -m pyimager
```
OR
use it via calling it within a Python script with:

```python
import os
os.system('py -m pyimager')
```
OR (also Python)
```python
import pyimager
print("Loading Designer module...")
d = pyimager.designer.Designer()
d.run_designer()
input("Finish designing...")
```

For more help, the Designer mode offers a dedicated help page that is accessible using the <code>!help</code> command.
### Displaying an image
Pyimagers images are saved in the ".lkim" file format.<br/>
This means you can display any valid image with the newest version of pyimager if it has LKIM format.<br/><br/>
Display an image using either:

```python
import pyimager
pyimager.display("C:/Path/To/Image.lkim")
```
OR, if you already know the files content or generated it:

```python
import pyimager
pyimager.display("display_content", "17#*#1#**#lkimcontentoffile")
```
, where the width, height and colors are seperated by <code>#*#</code> seperators.
### Compressing an image
The most compicated part is the compression.
#### Decompressing
You may use the following to decompress a LKIM file:

```python
import pyimager
pyimager.decompress("C:/Path/To/Image.lkim", "C:/Path/To/Decompressed/Image.lkim")
```
, but you may also leave the second path out and replace the image.

Also, it is possible to temporarily decompress an image via reading its content and decompressing this:

```python
from pyimager import temp_uncompress
data = "ImageDataWithoutSizeDescription"
data = temp_uncompress(data, "$", 5)
data = temp_uncompress(data, "%", 10)
data = temp_uncompress(data, "&", 20)
final_data = temp_uncompress(data, "§", 50)
```
, which uncompresses all common compressing sign codecs known by pyimager.
#### Compressing
There are also compressing functions at pyimager.<br/>
Therefore, you need to know that pyimagers compression bases on replacing frequent signs or strings with replacing signs.<br/>
In order to do that, pyimager generates very large lists with possible combinations of signs.<br/>
The currently largest list available is one with 6 signs long combinations.<br/>
To not slow down your program, it is disabled by default.<br/>
To include it, you can either set the <code>includeComb6</code> arg to <code>True</code> the first time you use the compression or:

```python
import pyimager
pyimager.compressing.addComb6()
```

Then, you can compress an image using:

```python
import pyimager
pyimager.compressing.compress("C:/Path/To/Your/Image.lkim", "C:/Path/To/File/You/Want/To/Save/New/Image.lkim")
```
, where you, again, can replace the original file via not giving the second arg.<br/>
<font color="orange">This may take a while, especially with the comb6 list.</font><br/>
<br/>
Finally, you can recompress a compressed image using <code>pyimager.compressor("C:/Path/To/Image.lkim", "C:/New/Image.lkim")</code>.
### More functions
#### about
The <code>pyimager.about()</code> function returns information about your release.
#### pyimager.data
This is the submodule for pyimagers data.<br/>
You probably won't be able to use it if you aren't developing another pyimager module.
#### pyimager.utils
This submodule has two functions for creating lists with all combinations from other lists.<br/>
<code>pyimager.utils.listComb</code> combines the lists,<br/>
<code>pyimager.utils.countDif</code> counts the number of different characters in two strings.
#### pyimager.message
Functions for colored error messages etc..<br/>
<code>pyimager.message.errorMessage</code> sends a message with a customizable color<br/>
<code>pyimager.message.errorMessageB</code> sends a message with a customizable background color.
### More coming soon...