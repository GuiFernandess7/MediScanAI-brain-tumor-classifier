import gspread
from pathlib import Path
from oauth2client.service_account import ServiceAccountCredentials
import os

BASE_DIR = Path(__file__).resolve().parent.parent

creds_path = os.path.join(BASE_DIR, '.creds/service.json')

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
gc = gspread.authorize(credentials)
spreadsheet_key = '1Kyrdepsi5eYpOQv6-LNhWy84LB0qrgnuuTe9VpNIRf0'

def set_sheet(sheet_name):
    worksheet = gc.open_by_key(spreadsheet_key).worksheet(sheet_name)
    return worksheet