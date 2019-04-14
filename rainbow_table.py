import argparse
import hashlib 

parser = argparse.ArgumentParser()
parser.add_argument("hash")

args=parser.parse_args()

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
char_set = alpha_lower + alpha_Upper + numbers

def md5_hash(p):
    h_pass = {}
    for i in p:
        h_pass[i]=hashlib.md5(b'i')
    return h_pass
    
def reduction_function():
    return

if __name__=="__main__":
    hashed_password = args.hash

    

