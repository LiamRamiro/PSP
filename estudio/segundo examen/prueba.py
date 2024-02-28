import paramiko
from scp import SCPClient 
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def examen():
    connectSSH()

def connectSSH():
    print("Conectando a SSH...")
    ssh = paramiko.SSHClient()  
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

    ssh.connect(hostname='127.0.0.1', port=2222, username='linuxserver', password='password')
    print("Conexión SSH establecida.")
    
    scp = SCPClient(ssh.get_transport())
    scp.get('/encrypted_data.bin') 
    scp.get('/private.pem') 
    print("Archivos descargados correctamente.")
    
    scp.close()  
    ssh.close()  
    print("Conexión SSH cerrada.")

def desEncrypt():
    print("Desencriptando...")
    file_in = open("encrypted_data.bin","rb")
    private_key = RSA.import_key(open("private.pem").read())
    enc_session_key = file_in.read(private_key.size_in_bytes())
    file_in.close()
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    print("Desencriptación completada.")
    return session_key

def writeEncryptedDataTofile(session_key):
    print("Escribiendo datos encriptados en un archivo...")
    file_out = open("liamsito.txt", "wb")
    file_out.write(session_key)
    file_out.close()
    print("Datos encriptados escritos en el archivo.")

session_key = desEncrypt()
writeEncryptedDataTofile(session_key)