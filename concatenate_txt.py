#!python3


from mytools import MyTools


mt = MyTools()

files = mt.get_all_files_list('./new_txt', ['.txt'])

one_string = ""

for f in files:
    txt = mt.read_file(f)
    one_string += txt + '\n<|endoftext|>\n\n'

fichier = 'bouquineux.txt'
mt.write_data_in_file(one_string, fichier, mode="w")
