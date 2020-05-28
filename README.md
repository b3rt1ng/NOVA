# MR_SCAN v2.0
MR_SCAN_V2 is a python3 script that scan your network using pings.
The V1 is avariable [here](https://github.com/b3rt1ng/MR_SCAN)
Note that this project has been only made for Linux.

## Next updates:

* Device conection power (how much does it take connection in the network)
* Choose an adress by it's position on the scanned adress list
* Linkable to MR_SPOOF

### what do you need to run this program ?

you will need:
```
Python 3
the uuid module
the netifaces module
```

i'll ad a PIP compatible file to install thoose directly.

### Installation

```
git clone https://github.com/b3rt1ng/MR_SCAN_V2
```

### Features

You can display all the ip scanned by changing line 6
```python
no_reach = False
```
into
```python
no_reach = True
```

### What i'm working on.

```python
def resolveMac(mac):
    url = "https://api.macvendors.com/" + str(mac)        #it's actuallt using urllib but i'm planing to use curl
    b_str = urllib.request.urlopen(url).read()            #combined with grep and a string treatment, you'll get the vendor name faster
    b_str = str(b_str, 'utf-8')                           #as well, you will not need the urllib library
    return b_str
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Do not use this script for any illegal purposes.

