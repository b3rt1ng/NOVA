import threading,os,sys,subprocess,time
ip_list = []
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
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

def ip_finder():
	output=subprocess.getoutput("ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'")
	displayer('sucess','user ip found ', 'noreturn');print(output)
	return output

def ping(ip, thread_name, user_ip, display = None):
	try:
		process = subprocess.check_output(["ping", "-c", "1", ip])
		displayer('sucess','host up ', 'noreturn');print(ip)
		global ip_list
		ip_list.append(ip)
	except:
		if display == True:
			displayer('failure','host down ', 'noreturn');print(ip)

def scanner():
	displayer('info','scaning on network')
	ip = str(ip_finder())
	scan_range = 255
	display = False
	if ip[-2] == '.':
		ip_cropped = ip[:-1]
	if ip[-3] == '.':
		ip_cropped = ip[:-2]
	for i in range(scan_range):
		ip_inscan = ip_cropped+str(i)
		thread_name = 'thread-'+str(i)
		thread_name = threading.Thread(target = ping, args = (ip_inscan, thread_name, ip, display))
		thread_name.start()
	global ip_list
	time.sleep(2)
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
			displayer('error', 'mac format incoherent')
			hosts_temp.append('None')
		hosts_info.append(hosts_temp)
		hosts_temp = []
	return hosts_info


def main():
	hosts = infoga()
	ip_current = ip_finder()
	os.system('clear')
	def display_info(hosts):
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
			sys.stdout.write(YELLOW + '| ' + MAGENTA + ' [' + color + str(i) + MAGENTA + ']' + YELLOW + '  | ' + ip_display + ' | ' + mac_display + ' | ' + mac_vendor_display + ' | ' + '\n')
		line()
		sys.stdout.write(GREEN + 'GREEN' + BLUE + ' = ' + YELLOW + 'regular host' + '\n')
		sys.stdout.write(RED + 'RED' + BLUE + ' = ' + YELLOW + 'your machine' + '\n')
	display_info(hosts)
main()
