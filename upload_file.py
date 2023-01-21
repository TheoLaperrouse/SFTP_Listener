import os
from dotenv import load_dotenv
import paramiko

load_dotenv()

def upload_file():
    """Teste le téléchargement de fichier SFTP"""
    transport = paramiko.Transport((os.getenv("SFTP_HOST"), int(os.getenv("SFTP_PORT"))))
    transport.connect(username=os.getenv("SFTP_USERNAME"), password=os.getenv("SFTP_PASSWORD"))
    print('Connection au SFTP réussi')
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put('upload/file2.txt','username')
    
if __name__ == "__main__":
    upload_file()
