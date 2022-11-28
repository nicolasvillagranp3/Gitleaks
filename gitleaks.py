from git import Repo
import re
import sys
from tqdm.auto import tqdm
import time
import json
import signal
import os


def handler(signal, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = input()
    if res == 'y':
        sys.exit(1)
    else:
        print('Program will continue to run')
        time.sleep(1)
        os.system('cls')  # Limpiamos la pantalla.


def extract(repo_dir):
    repo = Repo(repo_dir)
    # Devuelve un iterable con los commits que queremos.
    commits = list(repo.iter_commits('develop'))
    return commits


def transform(commits: list, keywords) -> list:
    patron = ''
    for i in keywords:  # Lo automatizamos para que en el caso de querer buscar otras cosas no haya que meter el patron
        # a mano.
        patron += i+'|'
    patron = patron[:-1]
    found = []
    print('Procesando commits')
    for i in tqdm(range(len(commits))):  # Metemos la barra de progreso
        s = re.findall(patron, commits[i].message, re.IGNORECASE)
        if s:
            # Metemos una tupla del commit encontrado y del patron.
            found.append(
                {'commit': str(commits[i]), 'message': str(commits[i].message), 'keyword': str(s[0])})
    return found


def exportar_json(found: list):
    with open('out/encontrados.json', 'w') as file:
        # Indent 1 para que este algo espaciado.
        json.dump({'commits encontrados': found}, file, indent=1)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)  # Señal del keyboard interrupt.
    REPO_DIR = './skale/skale-manager'
    key_words = ['credentials', 'password', 'key',
                 'new password', 'username']
    commits = extract(REPO_DIR)
    found = transform(commits, key_words)
    exportar_json(found)
