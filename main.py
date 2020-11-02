import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def googsheet():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    SetupMine = client.open("Charter_Setups_Editable").sheet1
    data = SetupMine.get_all_records()
    row = SetupMine.row_values(3)
    col = SetupMine.col_values(3)
    cell = SetupMine.cell(1,10)
    pprint(row)
    pprint(col)

    insertRow = ["Hello", 1990, "black"]
    pods = client.open("Charter_Setups_Editable").get_worksheet("Pods")
    pods.insert_row(insertRow,56)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   googsheet()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
