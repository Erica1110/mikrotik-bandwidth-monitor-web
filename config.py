import os
from dotenv import load_dotenv

load_dotenv()

# Configurações diretas - SEM CLASSE
MIKROTIK_HOST = os.getenv('MIKROTIK_HOST', '192.168.1.183')
MIKROTIK_USER = os.getenv('MIKROTIK_USER', 'admin')
MIKROTIK_PASSWORD = os.getenv('MIKROTIK_PASSWORD', '1234')
INTERFACE_TO_MONITOR = os.getenv('INTERFACE_TO_MONITOR', 'ether1')
COLLECTION_INTERVAL_SECONDS = 1