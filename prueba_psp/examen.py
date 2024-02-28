# Importación de módulos necesarios
from scp import SCPClient  # Importa el cliente SCP para transferencia segura de archivos
from http.server import BaseHTTPRequestHandler, HTTPServer  # Importa clases para crear un servidor HTTP
import paramiko  # Importa el módulo para realizar conexiones SSH
from Crypto.PublicKey import RSA  # Importa la clase RSA para gestionar claves públicas/privadas RSA
from Crypto.Cipher import AES, PKCS1_OAEP  # Importa módulos para encriptación AES y RSA
import smtplib  # Importa módulo para el envío de correos electrónicos
from ftplib import FTP  # Importa módulo para transferencia de archivos FTP

# Definición de parámetros para el servidor HTTP
params = '', 8083 # Dirección IP y puerto del servidor , 

# Definición de un manejador de peticiones HTTP personalizado
class HelloHandler(BaseHTTPRequestHandler):
    # Método para manejar peticiones HEAD
    def do_HEAD(self):
        self.send_response(200)  # Responde con un código 200 (OK)
        self.send_header('Content-type', 'text/html')  # Especifica el tipo de contenido como HTML
        self.end_headers()  # Finaliza las cabeceras de la respuesta

    # Método para manejar peticiones GET
    def do_GET(self):
        self.do_HEAD()  # Ejecuta la función para enviar cabeceras
        # Envía una respuesta HTML al cliente
        self.wfile.write("""
            <html><head>
                <title>Examen Alejandro</title></head><body><p>HelloWorld</p>
            <form method="POST" >
            <input type="submit" value="Click me">
                <img src="https://imgs.search.brave.com/pBeJWe6LJKO24PheFi1S1IkMEiCKTaePqGQnPGY1EOg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTI2/MTM0MDQyMy92ZWN0/b3IvcmFkaW9hY3Rp/dmUtc3ltYm9sLWlj/b24tc2V0LW51Y2xl/YXItcmFkaWF0aW9u/LXdhcm5pbmctc2ln/bi1hdG9taWMtZW5l/cmd5LWxvZ28tdmVj/dG9yLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1kVVhlZVVM/SEwwUzJlN0lEYU1B/TGdoYWtCTFprM0th/MlltSVZLLUNZYml3/PQ">
                        </input>
            </form>
            </body></html>""".encode("utf-8"))  # Codifica la respuesta como UTF-8 y la envía

    # Método para manejar peticiones POST
    def do_POST(self):
        self.do_HEAD()  # Ejecuta la función para enviar cabeceras
        # Respuesta HTML para peticiones POST
        self.wfile.write("""<html><head><title>Hello
            World</title></head><body><p>Form received</p>
            </body></html>""".encode("utf-8"))  # Codifica la respuesta como UTF-8 y la envía
        self.get_Documents()  # Llama al método para obtener documentos
        
    # Método para obtener documentos
    def get_Documents(self):
        self.connectSSH()  # Se conecta a través de SSH
        self.desEncrypt()  # Desencripta datos
        self.writeEncryptedDataTofile()  # Escribe datos encriptados en un archivo
        self.sendEmail()  # Envía un correo electrónico
        self.uploadFTP()  # Sube archivos a través de FTP

    # Método para conectarse mediante SSH
    def connectSSH(self):
        print("connect SSH")

        ssh = paramiko.SSHClient()  # Crea un cliente SSH
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Configura la política de claves faltantes

        # Se conecta al servidor SSH con los parámetros especificados
        ssh.connect(hostname='127.0.0.1', port=2222, username='linuxserver', password='password')

        # Crea un cliente SCP para la transferencia segura de archivos
        # Un cliente SCP es un cliente que permite la transferencia segura de archivos entre un host local y un host remoto
        scp = SCPClient(ssh.get_transport())
        scp.get('/home/encrypted_data.bin')  # Descarga el archivo encriptado desde el servidor SSH
        scp.get('/home/private.pem') # Descarga el archivo de clave privada desde el servidor SSH
        scp.close()  # Cierra la conexión SCP
        ssh.close()  # Cierra la conexión SSH
        print("SSH end")

    # Método de devolución de llamada para la lista FTP
    def listCallback(self, line):
        print(line) # Imprime la línea recibida, que es uno de los archivos en el servidor FTP

    # Método para escribir datos encriptados en un archivo
    def writeEncryptedDataTofile(self):
        # Escribe la clave de sesión en un archivo
        file_out = open("alejandro.txt", "wb")  # Abre un archivo para escritura binaria wb=(write binary)
        file_out.write(self.session_key) # Escribe la clave de sesión en el archivo
        file_out.close() # Cierra el archivo

    # Método para cargar archivos a través de FTP
    def uploadFTP(self):
        print("Upload FTP") 

        url = 'localhost' # Dirección del servidor FTP
        
        # Se conecta al servidor FTP con los parámetros especificados
        with FTP(url) as conn:
            conn.login('admin', 'preguntaraalberto')  # Inicia sesión en el servidor FTP
            conn.cwd('/')  # Cambia al directorio raíz del servidor FTP
            print(conn.pwd())  # Imprime el directorio actual
            print(conn.getwelcome())  # Obtiene el mensaje de bienvenida del servidor FTP
            
            # Abre el archivo binario en modo lectura rb=(read binary) y lo sube al servidor FTP
            with open('encrypted_data.bin', 'rb') as file:
                conn.storbinary('STOR encrypted_data.bin', file)  # Sube el archivo al servidor FTP con el nombre albertosaz.bin STOR=(store)
            
            # Obtiene y muestra el listado de archivos en el servidor FTP con el método listCallback
            conn.retrlines('LIST', self.listCallback)   # Se envia al servidor FTP el comando LIST para obtener el listado de archivos en el servidor FTP
            
            conn.quit()  # Cierra la conexión FTP
        print("Upload FTP end")

    # Método para enviar correos electrónicos
    def sendEmail(self):
        print("Enviar email")
        client = smtplib.SMTP(host='localhost', port=1025)  # Se conecta al servidor SMTP con los parámetros especificados
        sender = 'alejandroestebangil@gmail.com'  # Dirección del remitente
        dest = 'miminecraft11@gmail.com'  # Dirección del destinatario
        message = self.session_key  # Mensaje a enviar
        message_template = 'From:%s\r\nTo:%s\r\n\r\n%s'  # Plantilla del mensaje
        client.set_debuglevel(1)  # Establece el nivel de depuración en 1. Esto sirve para ver los mensajes que se envían y reciben en la consola
        # Envía el correo electrónico
        client.sendmail(sender, dest, message_template % (sender, dest, message))
        client.quit()  # Cierra la conexión SMTP
        print("Enviar email end")

    # Método para desencriptar datos
    def desEncrypt(self):
        print("Desencriptar")

        file_in = open("encrypted_data.bin", "rb")  # Abre el archivo de datos encriptados en modo lectura binaria
        private_key = RSA.import_key(open("private.pem").read())  # Importa la clave privada RSA
        enc_session_key = file_in.read(private_key.size_in_bytes())  # Lee la clave de sesión encriptada
        file_in.close()  # Cierra el archivo de entrada

        # Desencripta la clave de sesión con la clave RSA privada
        cipher_rsa = PKCS1_OAEP.new(private_key)
        self.session_key = cipher_rsa.decrypt(enc_session_key)  # Almacena la clave de sesión desencriptada
        print(self.session_key)  # Imprime la clave de sesión desencriptada
        print("Desencriptar end")

# Creación del servidor HTTP con el manejador definido
server = HTTPServer(params, HelloHandler)

# Intento de mantener el servidor en funcionamiento indefinidamente
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

# Cierre del servidor
server.server_close()