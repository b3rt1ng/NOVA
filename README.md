![linux_only](https://badgen.net/badge/made%20for/Linux/red) ![python_version](https://badgen.net/badge/python/3.7/yellow) ![console_only](https://badgen.net/badge/icon/terminal%20only/pink?icon=terminal&label)
# 🌌 NOVA 🌌

# ☄️ Installation ☄️ 
```
git clone https://github.com/b3rt1ng/NOVA
cd NOVA/
chmod +x install.sh
./install.sh
```  
You'll need to install [scapy](https://scapy.net/)
# 🌟 Usage 🌟
```
python3 main.py [argument]
```
Note that this script need the Super User privilege in some cases to run, so type "sudo" before your command if needed.
| Argument | Description |
| --- | --- |
| -i | Allow you to set up a custom interface by name if the script don't find anything on monitor mode. But you don't need to be on monitor mode to perform an arp spoofing attack, this feature isn't usefull yet ;) |
| -pt "value" | Set a value to change the delay to wait the pings results |
| -ip "local ip" | This command allow you to set your local ip manually if the script have trouble while finding it |
| -h | Show the help menu |
| --debug | The script will wait for you to continue before displaying the menu, it's easyer to see what's happening |  
  
  (You can use any argument at the same time)

## ✨ Specifications ✨
| status | feature |
| --- | --- |
| ✔️ | Fast network scan |
| ✔️ | Mac adress resolver |
| ✔️ | Vendor name resolver |
| ✔️ | ARP poisoning |
| ❌ | ARP poisoning (for MITM attack) |

### ⭐ What do you need to run this program ⭐

You need to have [scapy](https://scapy.net/) for python3.  

If you didn't get the wireshark OUI database by running the install file: 
[Here it is](https://gitlab.com/wireshark/wireshark/raw/master/manuf)

### 💫 troubleshooting 💫

> *Q: The scrit is not resolving any mac adress, what do I do ?*  
> R: This is most likely because you didn't ran the script as a superuser so the script cannot get the current ARP table.

> *Q: I can't install the manuf file using the instalation script.*  
> R: Just save the [manuf](https://gitlab.com/wireshark/wireshark/raw/master/manuf) file on the same folder as NOVA and just name it "manuf". The script will then be able to use it.  

  
_NOTE_: Because I want the script to be easy to modify and understandale to everyone, I do not make my programming object oriented. sorry :(  
### 👀 What it looks like 👀  
![this](https://i.imgur.com/6c0Gnrq.png)  
## License  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


#### Do not use this script for any illegal purposes.

