import unidecode # pip install unidecode

def convert_name(name):
	lower = name.lower()
	name = lower.strip().split(' ')
	return unidecode.unidecode(''.join(name))

print(convert_name("Phương Xinh Xinh")) #phuongxinhxinh


