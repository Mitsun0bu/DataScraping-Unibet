# **************************************************************************** #
#                                                          					   #
#    File name : unibet_scraping.py                                            #
#                                                                              #
#                                                                              #
#               _.'   `. ' .'   _`.                                            #
#               ,"""/`""-.-.,/. ` V'\-,`.,--/"""."-..                          #
#              ,'    `...,' . ,\-----._|     `.   /   \                        #
#             `.            .`  -'`"" .._   :> `-'   `.                        #   
#            ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L                       #   
#           .    \_ -'   `-'     ..      `.-' `.`-.'_ .|                       #   
#           |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.                       #
#           `.,' ,  |   |  `.  /'/,,.\/  |    \|   |                           #
#                `  `---'    `j   .   \  .     '   j                           #
#              ,__`"        ,'|`'\_/`.'\'        |\-'-, _,.                    #
#       .--...`-. `-`. /    '- ..      _,    /\ ,' .--"'  ,'".                 #
#     _'-""-    --  _`'-.../ __ '.'`-^,_`-""""---....__  ' _,-`                #
#   _.----`  _..--.'        |  "`-..-" __|'"'         .""-. ""'--.._           #
#  /        '    /     ,  _.+-.'  ||._'   """". .          `     .__\          #
# `---    /        /  / j'       _/|..`  -. `-`\ \   \  \   `.  \ `-..         #
#," _.-' /    /` ./  /`_|_,-"   ','|       `. | -'`._,   L  \ .  `.   |        #
#`"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .        #
#   /  '| /.,/   \--.._ `-,' ,          .  '`.'  __,., '  ''``._ \ \`,'        #
#  /_,'---  ,     \`._,-` \ //  / . \    `._,  -`,  / / _   |   `-L -          #
#   /       `.     ,  ..._ ' `_/ '| |\ `._'       '-.'   `.,'     |            #
#  '         /    /  ..   `.  `./ | ; `.'    ,"" ,.  `.    \      |            #
#   `.     ,'   ,'   | |\  |       "        |  ,'\ |   \    `    ,L            #
#   /|`.  /    '     | `-| '                  /`-' |    L    `._/  \           #
#  / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`           #
# '-""-'_|    `. `.__,._____     .    _,        ____ ,-  j     ".-'"'          # 
#        \      `-.  \/.    `"--.._    _,.---'""\/  "_,.'     /-'              #
#         )        `-._ '-.        `--"      _.-'.-""        `.                #
#        ./            `,. `".._________...""_.-"`.          _j                #
#       /_\.__,"".   ,.'  "`-...________.---"     .".   ,.  / \                #
#              \_/"""-'                           `-'--(_,`"`-`                #
#                                                                              # 
#    Author : mitsun0bu <llethuil@protonmail.com>                              #
#                                                                              #
#    Created: 2021/12/30 23:02:06 by mitsun0bu                                 #
#    Updated: 2021/12/30 23:07:30 by mitsun0bu								   #
#																			   #
# **************************************************************************** #

# ============ IMPORT LIBRAIRIES ================== #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# ================================= REACH WEBSITE ================================= #
url = 'https://unibet.fr/sport/football/ligue-1-ubereats'
s = Service('/Users/lucas/Documents/MY_PYTHON_PROJECTS/unibet_scraping/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get(url)

# ==================================== CLICK COOKIE BUTTON ===================================== #
time.sleep(5)
accept = driver.find_element(By.XPATH, '//a[@class="ui-button ui-large ui-important link-track"]')
accept.click()

# === INITIALIZATION ===#
n_games = 0
all_games = []
good_games = []
all_odds = []
draw_odds = []
good_odds  = []

# ===================== GETTING 'ALL_GAMES' LIST ====================== #
for game in driver.find_elements(By.XPATH, '//div[@class="cell-event"]'):
	all_games.append(game.text)
n_games = len(all_games)

# ==================================== GETTING 'DRAW_ODDS' LIST ==================================== #
for odd in driver.find_elements(By.XPATH, '//span[@class="ui-touchlink-needsclick price odd-price"]'):
	all_odds.append(odd.text)
for i in range(1, (n_games * 3 - 1), 3):
	draw_odds.append(all_odds[i])

# === QUIT WEBSITE=== #
driver.quit()

# ========================== KEEPING GAMES WITH 2.80 < DRAW ODDS 3.50 ========================== #
for i in range(0, n_games, 1):
	if float(draw_odds[i]) > 2.80 and float(draw_odds[i]) < 3.50 : good_odds.append(draw_odds[i])
	if float(draw_odds[i]) > 2.80 and float(draw_odds[i]) < 3.50 : good_games.append(all_games[i])

# ==== CREATING A DICTIONNARY W/ DATA OF INTEREST ==== #
bet_dico = {'Games': good_games, 'Draw Odds': good_odds}

# ========== SHOW DATA IN DATAFRAME ========== #
bet_dataframe = pd.DataFrame.from_dict(bet_dico)
print(bet_dataframe)
