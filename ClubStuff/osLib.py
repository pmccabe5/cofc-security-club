import os


def main():
    print(os.getcwd())
    # os.chdir("/Users/patrickmccabe/Desktop/")
    # print(os.listdir())
    # os.rmdir("Test1")
    """for dirpath, dirnames, filenames in os.walk("/Users/patrickmccabe/Desktop/"):
        print("Current path:", dirpath)
        print("Directories:", dirnames)
        print("Files:", filenames)
        print()"""
    # print("Home: ", os.environ.get('HOME'))
    # os.path.join(os.environ.get('HOME'), "test.txt")
    print(os.path.basename('/usr/share'))
    print(os.path.dirname('/usr/share'))
    print(os.path.split('/usr/share'))
    print(os.path.exists('/usr/share'))
    print(os.path.isdir('/usr/share'))
    print(os.path.isfile('/usr/share'))
    print(os.path.splitext('/usr/share'))


main()
