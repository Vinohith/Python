import os

path = 'directory_path'

print(os.path.isdir(path))

if os.path.isdir(path):
	for i, filename in enumerate(os.listdir(path)):
		os.rename(path+filename, path+'train'+str(i)+'.jpg')