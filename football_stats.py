import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from bs4 import BeautifulSoup

my_url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-post-category-touchdowns"

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

# print(page_soup)

containers = page_soup.findAll("div", {"id": "sortableContent"})

for container in containers:
    rs_container = container.findAll("tr",)
    player_num = 3
    team_num = 3
    status = True
    print("PLAYER", " | ", "POS", " | ", "TEAM", " | ", "TD")
    while status:
        try:
            print(rs_container[player_num].findAll("td")[0].text, " | ", rs_container[player_num].findAll("td")[1].text,
                  " | ",rs_container[player_num].findAll("td")[2].text, " | ", rs_container[player_num].findAll("td")[6].text)
            player_num += 1
        except:
            status = False
            break

"""              
                            
                PLAYER  |  POS  |  TEAM  |  TD
                Sony Michel  |  RB  |  NE  |  6
                Damien Williams  |  RB  |  KC  |  4
                Rex Burkhead  |  RB  |  NE  |  3
                C.J. Anderson  |  RB  |  LAR  |  2
                Michael Crabtree  |  WR  |  BAL  |  2
                Phillip Dorsett  |  WR  |  NE  |  2
                Ezekiel Elliott  |  RB  |  DAL  |  2
                Melvin Gordon  |  RB  |  LAC  |  2
                Todd Gurley  |  RB  |  LAR  |  2
                Dak Prescott  |  QB  |  DAL  |  2
                Keenan Allen  |  WR  |  LAC  |  1
                Amari Cooper  |  WR  |  DAL  |  1
                Keke Coutee  |  WR  |  HOU  |  1
                Eric Ebron  |  TE  |  IND  |  1
                Nick Foles  |  QB  |  PHI  |  1
                Michael Gallup  |  WR  |  DAL  |  1
                Antonio Gates  |  TE  |  LAC  |  1
                Dallas Goedert  |  TE  |  PHI  |  1
                Virgil Green  |  TE  |  LAC  |  1
                Garrett Griffin  |  TE  |  NO  |  1
                Tyler Higbee  |  TE  |  LAR  |  1
                Tyreek Hill  |  WR  |  KC  |  1
                Taysom Hill  |  QB  |  NO  |  1
                T.Y. Hilton  |  WR  |  IND  |  1
                Dontrelle Inman  |  WR  |  IND  |  1
                Travis Kelce  |  TE  |  KC  |  1
                Keith Kirkwood  |  WR  |  NO  |  1
                Marlon Mack  |  RB  |  IND  |  1
                Patrick Mahomes  |  QB  |  KC  |  1
                Jordan Matthews  |  WR  |  PHI  |  1
                
                
                """