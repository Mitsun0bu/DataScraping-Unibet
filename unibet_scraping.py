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

# ~								IMPORT LIBRAIRIES							 ~ #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
#from prettytable import PrettyTable

# ~								REACH WEBSITE								 ~ #
url = 'https://unibet.fr/sport/football/ligue-1-ubereats'
s = Service('/Users/lucas/Documents/MY_PYTHON_PROJECTS/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get(url)

# ~								CLICK COOKIE BUTTON					 		 ~ #
time.sleep(5)
accept = driver.find_element(By.XPATH, '//a[@class="ui-button ui-large ui-important link-track"]')
accept.click()

# ~								INITIALIZATION								 ~ #
games = []
n_games = 0
odds = []
draw_odds = []

# ~								GETTING 'GAMES' 							 ~ #
for game in driver.find_elements(By.XPATH, '//div[@class="cell-event"]'):
	games.append(game.text)
n_games = len(games)

# ~								GETTING 'DRAW_ODDS'								 ~ #
for odd in driver.find_elements(By.XPATH, '//span[@class="ui-touchlink-needsclick price odd-price"]'):
	odds.append(odd.text)
for i in range(1, (n_games * 3 - 1), 3):
	draw_odds.append(odds[i])

# ~								QUIT WEBSITE								 ~ #
driver.quit()

# ~								STORING LISTS IN DICT_BET					 ~ #
dict_bet = {'Games': games, 'Draw Odds': draw_odds}

# ~								SHOW DATA IN DATAFRAME						 ~ #
df_bet = pd.DataFrame.from_dict(dict_bet)
print(df_bet)