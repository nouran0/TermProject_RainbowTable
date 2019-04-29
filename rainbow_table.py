import argparse
import hashlib
import base64

def md5_hash(p, t):
    '''
    This method return hashed password/passwords using MD5 hash
    :param p: password
    :param t: list of passwords or one password
    :return: hashed password/passwords
    '''
    h_pass = {}
    if t.lower() == 'list':
        for i in p:
            h_pass[i]=hashlib.md5(i.encode())
    else:
       h_pass[p]=hashlib.md5(p.encode()) 
    return h_pass
   
def reduction_function(h,max_chain,passwd=None):
    '''
    This method reduce a password hash into multiple chains
    :param h: the hash
    :param max_chain: the maximum number of chains
    :param passwd:  the original password (optional)
    :return: a tuple of the original password (if provided) and the last chain for the hashed password
    '''
    hash_bytes = bytes.fromhex(h)
    hash_bytes_toInt = int.from_bytes(hash_bytes, byteorder='big')
    
    i=0
    while i <= max_chain:
        last_chain = (hash_bytes_toInt+i)%35**8
        new_hash = md5_hash(str(last_chain),'password')
        hash_bytes = bytes.fromhex(new_hash[str(last_chain)].hexdigest())
        hash_bytes_toInt = int.from_bytes(hash_bytes, byteorder='big')
        i+=1
        
    last_chain = base64.b64encode(bytes(str(last_chain),'ascii')) 
    return (passwd, last_chain.decode('utf-8'))

def find(chain):
    '''
    Search for a chain in the chains file
    :param chain: a given chain for a password
    :return: The password if it is found. Otherwise, false.
    '''
    
    with open('chains.txt') as f:
        for line in f:
            curr = line.strip()
            last_chain = curr.split(',')
            if chain == last_chain[1]:
                return curr[:curr.index(",")]
            
    return False


    
def crack (h):
    '''
    Crack a given hash to find the password
    :param h: a hash
    :return: the password if found
    '''
    h_lastChain = reduction_function(h,100)[1]
    result = find(h_lastChain)
    if result is not False:
        return result
    else:
        chain_count = 99
        while chain_count>=1:
            h_lastChain = reduction_function(h,chain_count)[1]
            result = find(h_lastChain)
            if result is not False:
                return result
            else:
                chain_count-=1
        return 'No result found!'

def get_passwords(filename):
    '''
    This method retrieve passwords from a given file
    :param filename: the name of the file that has the passwords
    :return: list of passwords
    '''
    passwords = []
    with open(filename) as f:
        
        for line in f:
            passwords.append(line.strip())

    return passwords

def save_to_file (d,filename):
    '''
    saves data to a file
    :param d: data
    :param filename: the name of the file to save the data
    '''
    with open(filename,'a+') as f:
        f.write(d)
    f.close()

if __name__=="__main__":
    
    ''' 
    This program generates a rainbow table
    '''
    
    with open('chains.txt','w'): #To clean up the file when a new rainbow table is generated
        pass

    with open('password hashes.txt','w'): #To clean up the file when a new rainbow table is generated
        pass
    
    passwds = get_passwords("passwords.txt")
    hashed_passwds = md5_hash(passwds,'list')
    count = 0
    for key, value in hashed_passwds.items():
        chain = reduction_function(hashed_passwds[key].hexdigest(),100,passwds[count])
        if count != len(hashed_passwds)-1:
            save_to_file(str(chain[0])+','+str(chain[1])+'\n','chains.txt')
            save_to_file(str(key)+' , '+ str(hashed_passwds[key].hexdigest())+'\n','password hashes.txt') 
            
        else:
            save_to_file(str(chain[0])+','+str(chain[1]),'chains.txt')
            save_to_file(str(key)+' , '+ str(hashed_passwds[key].hexdigest()),'password hashes.txt')
        count+=1
    


    
    

