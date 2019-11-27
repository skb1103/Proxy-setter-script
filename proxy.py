#Setting proxy in environment file "/etc/environment"
import sys
import set_function as sp
import unset_function as usp

# main function Taking argument from command line as {proxy} {port}
def main():
    sys.argv
    cm = sys.argv[1]

    if cm=='set':
        proxy = sys.argv[2]
        port = sys.argv[3]
        sp.set_proxy(proxy,port)

    elif cm=='unset':
        usp.unset_proxy()

    else:
        print('Use command: python3 proxy.py {set/unset} {proxy} {port}')


# main function
if __name__=='__main__':
    main()
