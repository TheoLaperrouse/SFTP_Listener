import os
import paramiko


def test_sftp_download():
    """Teste le téléchargement de fichier SFTP"""
    transport = paramiko.Transport((os.getenv("SFTP_HOST"), 22000))
    transport.connect(username=os.getenv("SFTP_USERNAME"), password=os.getenv("SFTP_PASSWORD"))
    sftp = transport.open_sftp()
    # Création d'un fichier de test sur le serveur SFTP
    with sftp.open("test.txt", "w") as file:
        file.write("test")
    # Exécution du script de téléchargement
    os.system("python sftp_download.py")
    # Vérification de l'existence du fichier de test téléchargé
    assert os.path.exists("test.txt")
    # Suppression du fichier de test du serveur SFTP et du système local
    sftp.remove("test.txt")
    os.remove("test.txt")
    sftp.close()
    transport.close()
    