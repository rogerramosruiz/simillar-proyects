import os 

PUBLIC_DIR    = os.environ.get('PUBLIC_DIR')
FILENAME_SIZE = int(os.environ.get('FILENAME_SIZE')) 
DB_HOST       = os.environ.get('DB_HOST')
DB_NAME       = os.environ.get('DB_NAME')
DB_USER       = os.environ.get('DB_USER')
DB_PASSWORD   = int(os.environ.get('DB_PASSWORD'))
DB_PORT       = int(os.environ.get('DB_PORT'))