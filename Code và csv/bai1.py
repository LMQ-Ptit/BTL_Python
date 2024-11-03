import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from functools import reduce

def crawl_base_data(soup, team_name, base_data, ok):
    """Hàm tìm dữ liệu base_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_standard_9'})
    if ok == 1:
        b = ["Team"]
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        base_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = [team_name]
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        base_data.append(tmp)

def crawl_goalkeep_data(soup, team_name, goalkeep_data, ok):
    """Hàm tìm dữ liệu goalkeep_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_keeper_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        goalkeep_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        goalkeep_data.append(tmp)

def crawl_shooting_data(soup, team_name, shooting_data, ok):
    """Hàm tìm dữ liệu shooting_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_shooting_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        shooting_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        shooting_data.append(tmp)

def crawl_passing_data(soup, team_name, passing_data, ok):
    """Hàm tìm dữ liệu passing_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_passing_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        passing_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        passing_data.append(tmp)

def crawl_passtype_data(soup, team_name, passtype_data, ok):
    """Hàm tìm dữ liệu passtype_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_passing_types_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        passtype_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        passtype_data.append(tmp)

def crawl_goalshot_data(soup, team_name, goalshot_data, ok):
    """Hàm tìm dữ liệu goalshot_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_gca_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        goalshot_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        goalshot_data.append(tmp)

def crawl_defensive_data(soup, team_name, defensive_data, ok):
    """Hàm tìm dữ liệu defensive_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_defense_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        defensive_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        defensive_data.append(tmp)

def crawl_possess_data(soup, team_name, possess_data, ok):
    """Hàm tìm dữ liệu possess_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_possession_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        possess_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        possess_data.append(tmp)

def crawl_playtime_data(soup, team_name, playtime_data, ok):
    """Hàm tìm dữ liệu playtime_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_playing_time_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        playtime_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        playtime_data.append(tmp)

def crawl_miscell_data(soup, team_name, miscell_data, ok):
    """Hàm tìm dữ liệu miscell_data của một đội bóng."""
    table = soup.find('table', {'class': 'stats_table sortable min_width', 'id': 'stats_misc_9'})
    if ok == 1:
        b = []
        thead = table.find('thead').find_all('tr')
        for x in thead[1]:
            if x.text.strip() != "":
                b.append(x.text.strip())
        miscell_data.append(b)
    tbody = table.find('tbody').find_all('tr')
    for y in tbody:
        tmp = []
        for x in y:
            tmp.append(x.text.strip() if x.text.strip() else "N/a")
        miscell_data.append(tmp)

if __name__ == "__main__":
    url = 'https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', {'class': 'stats_table sortable min_width force_mobilize', 'id': 'results2023-202491_overall'})
    
    teams_data = []
    tbody = table.find('tbody')
    teams = tbody.find_all('a', href=True)
    
    for team in teams:
        if "squads" in team['href']:
            team_name = team.text.strip()
            team_url = "https://fbref.com" + team['href']
            teams_data.append([team_name, team_url])
    
    df = pd.DataFrame(teams_data[1:], columns=teams_data[0])
    df.to_csv('team_data.csv', index=False, encoding='utf-8-sig')

    ok = 1
    base_data, goalkeep_data, shooting_data, passing_data, passtype_data, goalshot_data, defensive_data, possess_data, playtime_data, miscell_data = [], [], [], [], [], [], [], [], [], []
    
    for team in teams_data:
        print(f"Đang cào dữ liệu đội {team[0]}...")
        r = requests.get(team[1])
        soup = BeautifulSoup(r.content, 'html.parser')
        
        crawl_base_data(soup, team[0], base_data, ok)
        crawl_goalkeep_data(soup, team[0], goalkeep_data, ok)
        crawl_shooting_data(soup, team[0], shooting_data, ok)
        crawl_passing_data(soup, team[0], passing_data, ok)
        crawl_passtype_data(soup, team[0], passtype_data, ok)
        crawl_goalshot_data(soup, team[0], goalshot_data, ok)
        crawl_defensive_data(soup, team[0], defensive_data, ok)
        crawl_possess_data(soup, team[0], possess_data, ok)
        crawl_playtime_data(soup, team[0], playtime_data, ok)
        crawl_miscell_data(soup, team[0], miscell_data, ok)
        
        print(f'Đã cào xong đội {team[0]}...')
        ok += 1
        time.sleep(4)
    #Tạo 1 list chứa tất cả các df 
    all_df=[]
    #Chuyển đổi list thành Dataframe và loại bộ những hàng không cần thiết
    base_data_df=pd.DataFrame(base_data[1:],columns=base_data[0])
    base_data_df=base_data_df.drop(['90s','Gls','G+A','PK','npxG+xAG','Matches'],axis=1)
    all_df.append(base_data_df.drop_duplicates(subset='Player'))

    goalkeep_data_df=pd.DataFrame(goalkeep_data[1:],columns=goalkeep_data[0])
    goalkeep_data_df=goalkeep_data_df.drop(['Nation','Pos','Age','MP','Starts','Min','90s','Matches'],axis=1)
    all_df.append(goalkeep_data_df.drop_duplicates(subset='Player'))

    shooting_data_df=pd.DataFrame(shooting_data[1:],columns=shooting_data[0])
    shooting_data_df=shooting_data_df.drop(['Nation','Pos','Age','90s','Matches'],axis=1)
    all_df.append(shooting_data_df.drop_duplicates(subset='Player'))
    
    passing_data_df=pd.DataFrame(passing_data[1:],columns=passing_data[0])
    passing_data_df=passing_data_df.drop(['Nation','Pos','Age','90s','Matches'],axis=1)
    all_df.append(passing_data_df.drop_duplicates(subset='Player'))

    passtype_data_df=pd.DataFrame(passtype_data[1:],columns=passtype_data[0])
    passtype_data_df=passtype_data_df.drop(['Nation','Pos','Age','90s','Att','Matches'],axis=1)
    all_df.append(passtype_data_df.drop_duplicates(subset='Player'))

    goalshot_data_df=pd.DataFrame(goalshot_data[1:],columns=goalshot_data[0])
    goalshot_data_df=goalshot_data_df.drop(['Nation','Pos','Age','90s','Matches'],axis=1)
    all_df.append(goalshot_data_df.drop_duplicates(subset='Player'))

    defensive_data_df=pd.DataFrame(defensive_data[1:],columns=defensive_data[0])
    defensive_data_df=defensive_data_df.drop(['Nation','Pos','Age','90s','Matches'],axis=1)
    all_df.append(defensive_data_df.drop_duplicates(subset='Player'))
    
    possess_data_df=pd.DataFrame(possess_data[1:],columns=possess_data[0])
    possess_data_df=possess_data_df.drop(['Nation','Pos','Age','90s','Matches'],axis=1)
    all_df.append(possess_data_df.drop_duplicates(subset='Player'))

    playtime_data_df=pd.DataFrame(playtime_data[1:],columns=playtime_data[0])
    playtime_data_df=playtime_data_df.drop(['Nation','Pos','Age','90s','Matches','MP','Min','Mn/MP','Min%','+/-','+/-90','On-Off','xG+/-','xG+/-90','On-Off'],axis=1)
    all_df.append(playtime_data_df.drop_duplicates(subset='Player'))

    miscell_data_df=pd.DataFrame(miscell_data[1:],columns=miscell_data[0])
    miscell_data_df=miscell_data_df.drop(['Nation','Pos','Age','90s','Matches','CrdY','CrdR','2CrdY','Int','TklW','PKwon','PKcon'],axis=1)
    all_df.append(miscell_data_df.drop_duplicates(subset='Player'))

    #Outer join hết tất cả các df trong list all_df
    result = reduce(lambda left, right: pd.merge(left, right, on=['Player'], how='outer'),all_df)
    #Loại bỏ trùng lặp
    result=result.drop_duplicates()
    result = result.groupby('Player').first().reset_index()
    result=result.T.drop_duplicates().T
    #Loại các cầu thủ có chỉ số Min bé hơn 90 hoặc N/a
    def ch(a:str):
        if a=='N/a' :
            return 0
        return int(a.replace(',',''))
    a=list(result['Min'].values)
    b=[x for x in a if ch(x)>90]
    result=result[result['Min'].isin(b)].reset_index(drop=True)
    print(result)
    #Ghi thông tin vào file csv
    # result.to_csv("results.csv",index=False)
