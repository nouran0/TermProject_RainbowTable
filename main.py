import argparse
import time
from rainbow_table import crack

def main():
    
    '''
    This is the main method for running the password hashes cracker program using a rainbow table
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("hash")
    args=parser.parse_args()
    
    hashed_password = args.hash
    start = (time.time()) * 10**12
    password = crack(hashed_password)
    end = (time.time()) * 10**12
    print('The password:',password,", Time taken:",end-start,'ps')
    
if __name__=="__main__":
    main()

