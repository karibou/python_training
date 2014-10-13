def importer():
    import os.path as osp
    print osp.sep

importer()
importer()
importer()
importer()


print '__name__', __name__

if __name__ == '__main__':
    print "je suis execute directement"
