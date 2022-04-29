import os

solutionsPath = './solutions'
binariesPath = './amd64'

binaries = os.listdir(binariesPath)
folders = os.listdir(solutionsPath)

for binary in binaries:
	print(binary)
	if not binary in folders:
		os.mkdir('{}/{}'.format(solutionsPath, binary))
	fb = open('{}/{}'.format(binariesPath, binary), 'rb')
	binaryContent = fb.read()
	newBinaryPath = '{}/{}/{}'.format(solutionsPath, binary, binary)
	f = open(newBinaryPath, 'wb')
	f.write(binaryContent)
	f.close()
	os.system('chmod +x {}'.format(newBinaryPath))
