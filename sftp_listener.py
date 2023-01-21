import os
import time
from dotenv import load_dotenv
import paramiko

load_dotenv()

PAUSE_TIME = 300

def connect_sftp():
    """"Connection au serveur SFTP"""
    try:
        transport = paramiko.Transport((os.getenv("SFTP_HOST"), int(os.getenv("SFTP_PORT"))))
        transport.connect(username = os.getenv("SFTP_USERNAME"), password = os.getenv("SFTP_PASSWORD"))
        return transport.open_sftp()
    except Exception as error:
        print(f'Error connecting: {error}')
        return None

if __name__ == "__main__":
    sftp = connect_sftp()
    while True:
        files = sftp.listdir()
        for file in files:
            if not os.path.exists(file):
                sftp.get(file, file)
                print(f'Nouveau fichier téléchargé : {file}')
        time.sleep(PAUSE_TIME)
    sftp.close()
