def file_write(path, content):
    f = open(path, 'a+')
    f.write(content)
    f.close()
