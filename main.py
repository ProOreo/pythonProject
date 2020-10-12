# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def download_cotdata(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
    myfile = requests.get(url)
    open('C:/Users/Lenovo/PycharmProjects/pythonProject/files/FinFutWk.txt', 'wb').write(myfile.content)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_cotdata('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
