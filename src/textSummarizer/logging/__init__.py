import os
import sys
import logging

# Mendefinisikan format string untuk log
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Mendefinisikan direktori dan path file untuk menyimpan log
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Membuat direktori log jika belum ada
os.makedirs(log_dir, exist_ok=True)

# Mengkonfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        # Handler untuk menulis log ke dalam file
        logging.FileHandler(log_filepath),
        # Handler untuk menampilkan log di terminal
        logging.StreamHandler(sys.stdout)
    ]
)

# Membuat atau mendapatkan logger dengan nama spesifik
logger = logging.getLogger('textSummarizerLoger')