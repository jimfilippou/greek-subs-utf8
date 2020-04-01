import sys

def correctSubtitleEncoding(filename, newFilename, encoding_from='ISO-8859-7', encoding_to='UTF-8'):
    with open(filename, 'r', encoding=encoding_from) as fr:
        with open(newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\r\n')

def main():
    filename = sys.argv[1]
    newFileName = sys.argv[2]
    correctSubtitleEncoding(filename, newFileName)
    
main()
