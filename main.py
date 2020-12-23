import subprocess
import html

def xuli(s):
	# If the point is a whole number like 4 or 5, eliminate the spaces behind
	if s.find('.') == -1:
		s = s[0]
	return s
	
for count in range(2050001,2050003): # the number of examinees is 74718 
	# Get information of the examinee from the website and save to a .txt file
	sbd = '0' + str(count)
	var = subprocess.Popen('curl -F "SoBaoDanh=%s" diemthi.hcm.edu.vn/Home/Show' %sbd, stdout=subprocess.PIPE, shell=True)
	text = var.communicate()[0].decode('utf-8')
	with open('m.txt', 'w') as file:
		for i in text.splitlines():
			file.write(i)

	file.close()

	# Get the content of the file (a string)
	file = open('m.txt','r+')
	a = file.read()
	file.close()
	if a.find('Không tìm thấy')!=-1:
		continue

	# Remove the redundance of the file
	flag = True
	while flag:
		flag = False
		index1 = a.find('<')
		index2 = a.find('>')
		if index1!=-1 and index2!=-1:
			a = "".join((a[:index1],"",a[index2+1:]))
			flag = True
	
	# Get the name
	a = a[487:]
	idx = a.find('  ')
	ten = a[:idx]
	ten = html.unescape(ten) # the name gotten is in html code, so convert it to the real name

	# Get the birthday
	idx = a.find('/')
	ngay = a[idx-2:idx]
	thang = a[idx+1:idx+3]
	nam = a[idx+4:idx+8]

	# Get all the points
	idx = a.find('To&#225;n')
	toan = a[idx+13:idx+17]
	toan = xuli(toan)

	idx = a.find('Ngữ')
	nguvan = a[idx+11:idx+15]
	nguvan = xuli(nguvan)

	idx = a.find('Vật')
	if idx==-1:
		vatli = '-1'
	else:
		vatli = a[idx+15:idx+19]
		vatli = xuli(vatli)

	idx = a.find('H&#243;a')
	if idx==-1:
		hoahoc = '-1'
	else:
		hoahoc = a[idx+16:idx+20]
		hoahoc = xuli(hoahoc)

	idx = a.find('Sinh')
	if idx==-1:
		sinhhoc = '-1'
	else:
		sinhhoc = a[idx+12:idx+16]
		sinhhoc = xuli(sinhhoc)

	idx = a.find('Lịch')
	if idx==-1:
		lichsu = '-1'
	else:
		lichsu = a[idx+11:idx+15]
		lichsu = xuli(lichsu)

	idx = a.find('Địa')
	if idx==-1:
		diali = '-1'
	else:
		diali = a[idx+15:idx+19]
		diali = xuli(diali)

	idx = a.find('GDCD')
	if idx==-1:
		GDCD = '-1'
	else:
		GDCD = a[idx+8:idx+12]
		GDCD = xuli(GDCD)

	idx = a.find('KHTN')
	if idx==-1:
		KHTN = '-1'
	else:
		KHTN = a[idx+6:idx+10]
		KHTN = xuli(KHTN)


	idx = a.find('KHXH')
	if idx==-1:
		KHXH = '-1'
	else:
		KHXH = a[idx+6:idx+10]
		KHXH = xuli(KHXH)


	idx = a.find('Tiếng')
	if idx==-1:
		tienganh = '-1'
	else:
		tienganh = a[idx+13:idx+17]
		tienganh = xuli(tienganh)

	file = open('data2.txt','a')
	line = sbd+','+ten+','+ngay+','+thang+','+nam+','+toan+','+nguvan+','+vatli+','+hoahoc+','+sinhhoc+','+lichsu+','+diali+','+GDCD+','+KHTN+','+KHXH+','+tienganh+'\n'
	file.write(line)
	file.close()

