# get_out
get_out is under heavy developement for the moment  
The script will allow you to perform ARP poisoning by analysing your network and showing who is disponible
## Next updates:

* installation of dependecies file (for the database)
* ability to select multiple ip on the command line (you need to type them one by one rn)
* ability to send maliscious packet like deauth or arp spoof
* listen to the network and save the currents hosts by time to render a graphic and data analytics from it

### what do you need to run this program ?

For the moment you don't need to install any modules because it only use the in-builds ones

You need to get the wireshark OUI database in order to resolve the vendor name
[Here it is](https://gitlab.com/wireshark/wireshark/raw/master/manuf)

### Is there something you will improve ?
yeah, for the moment the threads are runing and expeting to get a response fastly. Some might be late and because a delay is made, it might be longer than the expected delay (wich you can change). I'll make a better way to get the response and don't miss some.  
The problem is the same for the unsuccessfull threads...

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Do not use this script for any illegal purposes.

