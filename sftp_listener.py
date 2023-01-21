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
        transport.connect(username=os.getenv("SFTP_USERNAME"), password=os.getenv("SFTP_PASSWORD"))
        print('Connection au SFTP réussi')
        connex_sftp = paramiko.SFTPClient.from_transport(transport)
        return connex_sftp
    except Exception as error:
        print(f'Erreur de connection: {error}')
        return None

def download(sftp):
    """"Connection au serveur SFTP"""
    try:
        for file in sftp.listdir():
            local_file = f'{file}'
            if not os.path.exists(f'./download/{local_file}'):
                sftp.get(file, f'download/{local_file}')
                print(f'Téléchargement de {local_file} réussi')
    except Exception as error:
        print(f'Erreur de téléchargement: {error}')


if __name__ == "__main__":
    conn_sftp = connect_sftp()
    while True:
        download(conn_sftp)
        time.sleep(PAUSE_TIME)
    sftp.close()
