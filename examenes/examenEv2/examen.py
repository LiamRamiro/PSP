from scp import SCPClient  
from http.server import BaseHTTPRequestHandler, HTTPServer  
import paramiko  
from Crypto.PublicKey import RSA  
from Crypto.Cipher import AES, PKCS1_OAEP 
import smtplib  
from ftplib import FTP 


params = '', 8083 

class HelloHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers()  

    
    def do_GET(self):
        self.do_HEAD()  
    
        self.wfile.write("""
            <html><head>
                <title>Examen Liam Ramiro Embid</title></head><body><p>HolaMundo</p>
            <form method="POST" >
            <input type="submit" value="Pulsar aqui">
                <img src="https://phantom-marca.unidadeditorial.es/55767f365b670426b45ac8927be33d46/resize/828/f/jpg/assets/multimedia/imagenes/2023/08/09/16915662020870.jpg">
                        </input>
            </form>
            </body></html>""".encode("utf-8"))  
    
    def do_POST(self):
        self.do_HEAD()  
        
        self.wfile.write("""<html><head><title>Hola
            Mundo</title></head><body><p>Form received</p>
            </body></html>""".encode("utf-8"))  
        self.get_Documents() 
        
    
    def get_Documents(self):
        print("Recibido")
        self.connectSSH()  
        self.desEncrypt()  
        self.writeEncryptedDataTofile()  
        self.sendEmail()  
        self.uploadFTP()  
    
    def connectSSH(self):
        print("Conectando a SSH")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname='192.168.1.123', port=2222, username='tresdos', password='tresdos')
        print("Conectado a SSH")
        scp = SCPClient(ssh.get_transport())
        scp.get('/home/encrypted_data.bin')
        scp.get('/home/private.pem')
        print("Descargados los archivos")
        scp.close()
        ssh.close()
        print("SSH termino")

    def desEncrypt(self):
        print("Desencriptar")

        file_in = open("encrypted_data.bin", "rb")  
        private_key = RSA.import_key(open("private.pem").read())  
        enc_session_key = file_in.read(private_key.size_in_bytes())  
        file_in.close()  

        cipher_rsa = PKCS1_OAEP.new(private_key)
        self.session_key = cipher_rsa.decrypt(enc_session_key)
        print(self.session_key)  
        print("Desencriptar termino")

    def writeEncryptedDataTofile(self):
        file_out = open("liam.txt", "wb")  
        file_out.write(self.session_key) 
        file_out.close()

    def sendEmail(self):
        print("Enviando email")
        cliente = smtplib.SMTP(host='192.168.1.123', port=1023)
        emisor = 'ramiro.emlia22@zaragoza.salesianos.edu'
        receptor = 'gorka.sanz@zaragoza.salesianos.edu'
        mensaje = self.session_key
        mensajePlantilla = 'From:%s\r\nTo:%s\r\n\r\n%s'
        cliente.set_debuglevel(1)
        cliente.sendmail(emisor, receptor, mensajePlantilla % (emisor, receptor, mensaje))
        cliente.quit()
        print("Enviar Email termino")

    def uploadFTP(self):
        print("Uploading FTP") 
        url = '192.168.1.123'
        puerto = 23
        sftp = FTP()
        sftp.connect(url, puerto)
        sftp.login('dostres', 'dostresdos') 
        
        sftp.cwd('/')
        print(sftp.pwd())
        print(sftp.getwelcome())
        
        with open('liam.txt', 'rb') as file:
            sftp.storbinary('STOR liam.txt', file)
        
        sftp.retrlines('LIST', self.listCallback)
        
        sftp.quit()
        
        print("Upload FTP termino")


    def listCallback(self, line):
        print(line)

        
server = HTTPServer(params, HelloHandler)


try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()