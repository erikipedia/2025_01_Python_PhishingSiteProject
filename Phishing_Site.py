import os, random, string
import csv
import urllib.parse
import requests

# setup
botId = 'bot7994182660:AAEvdI-onrB8oT_W6fJu-NpUpH2ItZ5ah1c'
chatId = '1012726266'

iterations = 1000000000

random.seed = (os.urandom(1024))
currentPath = os.getcwd()
services = [
    'PENFED CU',
    'NAVY FU',
    'GOLDEN CU',
    'ALLIANT CU',
    'MTN AMERICA CU',
    'DIGITAL FU',
    'FIRSTTECH FU',
    'BOEING CU',
    'ACU',
    'JPMORGAN',
    'CHASE',
    'BOA',
    'WELLS FARGO',
    'CITIBANK',
    'CAPITAL ONE',
    'USBANK',
    'PNC',
    'TD',
    'ALLY',
    'SYNCHRONY',
    'COINBASE',
    'KRAKEN',
    'CASHAPP',
    'GOOGLE',
    'OUTLOOK',
    'MICROSOFT',
    'YAHOO',
    'AOL',
    'ICLOUD',
    'APPLE',
    'PROTON',
    'EXCHANGE',
    'INSTAGRAM',
    'FACEBOOK',
    'TWITTER',
    'YOUTUBE',
    'TIKTOK',
    'WHATSAPP',
    'SNAPCHAT',
    'PINTREST',
    'PAYPAL',
    'VENMO',
    'METAMASK'
]

# functions
def getRandomService():
    return random.choice(services)

def getRandomIp():
    return '.'.join(str(random.randint(0,255)) for i in range(4))

def getRandomPassword():
    length = random.randint(8,16)
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    return ''.join(random.choice(chars) for i in range(length))

def getRandomCsvData(filename, colIndex):
    with open(f'{currentPath}\\{filename}', 'r') as csvFile:
        reader = csv.reader(csvFile)
        rows = list(reader)
        row = random.choice(rows)
        return row[colIndex].lower()

# actual script (let's go!)
for i in range(iterations):
    svc = getRandomService()
    userName = f'{getRandomCsvData('Popular_Baby_Names.csv', 3)}.{getRandomCsvData('surnames.csv', 0)}@{getRandomCsvData('email_domains.csv', 0)}'
    password = getRandomPassword()
    ip = getRandomIp()
    msgText = (f'|=============== {svc} LGN ================| \n| USERNAME: {userName} \n| PASSWORD: {password} \n| IP: {ip} \n|=============== {svc} LGN ================').replace(' ', '%20').replace('\n', '%0A')
    # decoded = urllib.parse.unquote(msgText)
    # print(msgText)
    # print(decoded)

    url = f'https://api.telegram.org/{botId}/sendMessage?chat_id={chatId}&text={msgText}&parse_mode=html'
    response = requests.get(url)
    print(response.content)

