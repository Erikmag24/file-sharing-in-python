import requests

# Imposta il tuo file da caricare
file_path = 'path_al_tuo_file.txt'

# Esegui la richiesta POST per caricare il file su Transfer.sh
response = requests.post('https://transfer.sh/', files={'file': open(file_path, 'rb')})

# Verifica se la richiesta è andata a buon fine
if response.status_code == 200:
    # Estrai il link di condivisione dalla risposta
    share_link = response.content.decode('utf-8')
    print(f"File caricato con successo. Link di condivisione: {share_link}")
else:
    print("Si è verificato un errore durante il caricamento del file.")
