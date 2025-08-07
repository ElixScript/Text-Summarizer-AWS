# disini adalah bagian logika dari sistem kita
# fungsi dari membuat file ini adalah membuat file yang kita perlukan dengan otomatis 


# project template creation 


# import library yang dibutuhkan
import os
from pathlib import Path
import logging

# ini adalah bagian konfigurasi logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# nama project
project_name = 'textSummarizer'

# list dari file dan direktori
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" # KOREKSI: Typo 'researcj' menjadi 'research'
]

for filepath_str in list_of_files:
    filepath = Path(filepath_str) # Menggunakan objek Path
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Membuat direktori: {filedir} untuk file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # Membuat file kosong
            logging.info(f"Membuat file kosong: {filepath}")

    else:
        logging.info(f"File '{filepath}' sudah ada dan tidak kosong.")