#!/usr/bin/env python3
# NYARI APA NGAB... CODE INI SUDAH DI ENCRYPT OLEH SANZPROJECT
import os
original_file = 'app.py.enc'
os.system(f'openssl enc -d -aes-256-cbc -in {original_file} -pass pass:"" | python3 -')  # Dekripsi dan jalankan tanpa menyimpan
