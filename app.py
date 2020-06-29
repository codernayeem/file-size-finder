import os

pth = input("Type the directory where you want to search : ")
size_in_bytes = int(input("Type the size of the file in bytes : "))

print('Searching\n\n')
c = 0
cc = 0
	
try:
	for dirpath, dirnames, filenames in os.walk(pth):
		try:
			for file_name in filenames:
				s = os.path.join(dirpath, file_name)
				cc += 1
				try:
					if size_in_bytes == os.path.getsize(s):
						print('[+] > ', s, '\n')
						c += 1
				except Exception as e:
					print(e)
		except Exception as e:
			print(e)
except Exception as e:
	print(e)

print('Done')
print('Found ', c, ' files from ', cc, ' files')
input()
