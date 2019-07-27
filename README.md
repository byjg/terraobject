# Terraobject

Terraobject package to share variables between terrascript components

You can use the Terraobject to parameter to several classes and share resources to be used by other terraform resources. 

# Examples:

```python
# Create the reference
from terraobject import Terraobject

# Import the terrascript resources you need
from terrascript import provider
from terrascript.digitalocean.d import digitalocean_volume

# Create the object
o = Terraobject()

# Add the providers, resources, data, as usual
o.terrascript.add(provider("digitalocean", token="tokentoken"))

# Get some info (e.g. data) and share to be used on other commands
persistent_volume = digitalocean_volume("persistent_volume", name="volume-nyc3-01", region="abc")
o.terrascript.add(persistent_volume)
o.shared['persistent_volume'] = persistent_volume

# And you can use and another place:
o.shared['persistent_volume'].name

# Dump the XML
print(o.terrascript.dump())
```

# Add to your project

```bash
pip install terraobject==0.0.1
```

# More information about terrascript:
https://github.com/mjuenema/python-terrascript

