import os
from os import listdir
from os.path import isfile, join


pat = input("ENTER PATH :: ")
aa = [f for f in listdir(pat) if isfile(join(pat, f))]
key = int(input('Enter Key for encryption of Image : '))

for i in aa:
    path=pat+"\\"+i
    try:
	    print('The path of file : ', path)
	    fin = open(path, 'rb')
	    image = fin.read()
	    fin.close()
	    image = bytearray(image)
	    for index, values in enumerate(image):
		    image[index] = values ^ key
	    fin = open(path, 'wb')
	    fin.write(image)
	    fin.close()
	    print('Decryption Done...')
    except Exception:
	    print('Error caught : ', Exception.__name__)
