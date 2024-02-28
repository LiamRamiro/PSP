# A file transfer program which can transfer files back and forth from a remote ftp sever. 

import ftplib

def ftp_transfer(hostname, username, password, filename):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        with open(filename, 'rb') as file:
            ftp.storbinary('STOR ' + filename, file)
        ftp.quit()
        print("File transfer successful.")
    except Exception as e:
        print("Error:", e)

# Example usage
ftp_transfer('ftp.example.com', 'username', 'password', 'example_file.txt')