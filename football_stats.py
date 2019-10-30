import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from bs4 import BeautifulSoup

my_url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"

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
Aaron Jones  |  RB  |  GB  |  11
Christian McCaffrey  |  RB  |  CAR  |  10
Dalvin Cook  |  RB  |  MIN  |  9
Austin Ekeler  |  RB  |  LAC  |  8
Todd Gurley  |  RB  |  LAR  |  7
Mark Ingram  |  RB  |  BAL  |  7
Adam Thielen  |  WR  |  MIN  |  7
D.J. Chark  |  WR  |  JAC  |  6
Nick Chubb  |  RB  |  CLE  |  6
Tevin Coleman  |  RB  |  SF  |  6
James Conner  |  RB  |  PIT  |  6
Ezekiel Elliott  |  RB  |  DAL  |  6
Mike Evans  |  WR  |  TB  |  6
Chris Godwin  |  WR  |  TB  |  6
Kenny Golladay  |  WR  |  DET  |  6
Derrick Henry  |  RB  |  TEN  |  6
Jordan Howard  |  RB  |  PHI  |  6
Sony Michel  |  RB  |  NE  |  6
Chris Carson  |  RB  |  SEA  |  5
Amari Cooper  |  WR  |  DAL  |  5
Chase Edmonds  |  RB  |  ARI  |  5
Darren Fells  |  TE  |  HOU  |  5
T.Y. Hilton  |  WR  |  IND  |  5
Austin Hooper  |  TE  |  ATL  |  5
David Johnson  |  RB  |  ARI  |  5
Marvin Jones  |  WR  |  DET  |  5
Cooper Kupp  |  WR  |  LAR  |  5
Terry McLaurin  |  WR  |  WAS  |  5
Latavius Murray  |  RB  |  NO  |  5
Deshaun Watson  |  QB  |  HOU  |  5
                
                
                """