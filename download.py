from pathlib import Path
from zipfile import ZipFile

import requests

from utils import clear_folder, xls_to_xlsx_converter

URL_EPARH = 'https://eparh.com/File/sklad.zip'
URL_GLOBAL = 'http://beta.globengineer.ru/files/%D0%9E%D1%81%D1%82%D0%B0%D1%82%D0%BA%D0%B8%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2%20%D0%BD%D0%B0%20%D1%81%D0%BA%D0%BB%D0%B0%D0%B4%D0%B5.xls'
BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    filename_eparh = URL_EPARH.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    clear_folder(downloads_dir)
    archive_path_eparh = downloads_dir / filename_eparh
    archive_path_global = downloads_dir / 'global.xls'
    response = requests.get(URL_EPARH)
    with open(archive_path_eparh, 'wb') as file:
        file.write(response.content)
    with ZipFile(archive_path_eparh, "r") as myzip:
        myzip.extractall(path=downloads_dir)
    response = requests.get(URL_GLOBAL)
    with open(archive_path_global, 'wb') as file:
        file.write(response.content)
    xls_to_xlsx_converter(['./downloads/Остатки.xls',
                           './downloads/global.xls'])




