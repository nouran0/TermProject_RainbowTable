# Rainbow Table

**Description**

This program can crack a password hash, where the password contains 8 ASCII characters. (**_password.txt_** file contains a sample of passwords that the program can crack. The password file can be any file as long as the passwords are 8 ASCII characters long).
The program takes approximately 4,673,699,840 ps for a password that's only letters (e.g. **_AsVszkEu_**). And approximately 3,434,545,152 ps for a password that's a combination of letters, numbers, and symbols  (e.g. **_ pg$7cw!R_**). And for a password that's only numbers it takes approximately 3,357,278,208 ps (e.g. **_12345678_**). So, the program cracks relatively faster password hashes that contains only numbers.  

**Running Instructions**

1. Open the command prompt where the python file is located.
2. Type (py main.py **_hash_**). (For the **_hash_** value, you may find hashes that the program can crack in **_password hashes.txt_** file.) 

**Program Output**

The program will output the corresponding password for the hash if it is in the **_password.txt_** file and the amount of time it took to find it. Otherwise, the program will output "No result found!" and the the amount of time it took as well.

