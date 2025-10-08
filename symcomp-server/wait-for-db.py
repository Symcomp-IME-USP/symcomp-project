import os
import socket
import time
import subprocess

host = os.environ.get("DB_HOST", "postgres")
port = int(os.environ.get("DB_PORT", 5432))

print(f"Aguardando Postgres em {host}:{port}...")

while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            break
    except OSError:
        print(f"Postgres ainda não está pronto em {host}:{port}, aguardando...")
        time.sleep(2)

print("Postgres está pronto! Iniciando Django...")