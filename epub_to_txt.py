#!python3

from time import sleep
import pypandoc
import subprocess

from mytools import MyTools


mt = MyTools()

files = mt.get_all_files_list('./epub', ['.epub'])

def pandoc_convert():
    for f in files:
        name = f.split('.')[0]
        print(name)
        outputfile = './txt/' + name + '.txt'
        pypandoc.convert_file(f, to='plain', outputfile=outputfile)


def ebook_convert():
    for fichier in files:
        print("fichier:", fichier)
        name = fichier.split('.')[0][5:]
        print("name:", name)
        outputfile = ' ./txt/' + name + '.txt'
        print("outputfile", outputfile)

        cmd = "ebook-convert " + fichier + outputfile
        print("cmd:", cmd, '\n')
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        sleep(5)


ebook_convert()
