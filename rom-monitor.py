import re
import xlsxwriter

def rom_capture():
	hostname = re.compile(r'(?:Device Name\S\s)(.+)')
	rom_version = re.compile(r'(System Bootstrap, Version )(\S+)(,)')
	workbook = xlsxwriter.Workbook('rom_version.xlsx')
	worksheet = workbook.add_worksheet("Rommon_version")
	host_dict = {}
	row = 1
	flag = False
	worksheet.write('A1', "Hostname")
	worksheet.write('B1', "Rom_version")
	
	with open ('./rom-monitor.txt','r') as f:
		for line in f:
			if hostname.match(line):
				# worksheet.write(row,0,hostname.match(line).group(1))
				hostname_final = hostname.match(line).group(1)
				host_dict[hostname_final] = None
				flag = True
			elif flag == True and rom_version.match(line):
				rom_ver_final = rom_version.match(line).group(2)
				host_dict[hostname_final] = rom_ver_final
				flag = False
	for host,ver in host_dict.items():
		worksheet.write(row,0,host)
		worksheet.write(row,1,ver)
		row+=1
	# print(host_dict)
	workbook.close()
if __name__ == "__main__":
	rom_capture()
	print("Excel generated successfuly")

	