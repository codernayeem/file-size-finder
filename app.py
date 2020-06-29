import os

pth = "C:"              # directory
size_in_bytes = 100025  # size

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
input()
