file_name = 'code_test.txt'
with open(file_name) as file_handle:
	lines=file_handle.readlines()

#list_t = list()
string_t = ''
for line in lines:
	#list_t.append(line.strip())
	string_t += line.replace('python', 'c')
#content=file_name.read()

print(string_t)