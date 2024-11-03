import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import time

# Thiết lập mã hóa UTF-8 cho đầu ra
sys.stdout.reconfigure(encoding='utf-8')

# Hàm lấy danh sách tên đội và đường dẫn đến trang đội
def fetch_teams(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    teams_data = []

    # Tìm bảng các đội trong trang và lấy liên kết đến các trang đội
    league_table = soup.find('table', 
        {'class': 'table table-striped table-hover leaguetable mvp-table ranking-table mb-0'}
    )
    if league_table:
        team_rows = league_table.find('tbody')
        teams = team_rows.find_all('a', href=True)
        for team in teams:
            team_name = team.text.strip()
            team_url = team['href']
            teams_data.append((team_name, team_url))

    return teams_data

# Hàm lấy thông tin cầu thủ từ trang của từng đội
def fetch_players(team_name, team_url):
    player_data = []
    response = requests.get(team_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm bảng thông tin cầu thủ
    player_table = soup.find('table', {'class': 'table table-striped-rowspan ft-table mb-0'})
    if player_table:
        player_rows = player_table.find('tbody')
        players = player_rows.find_all('tr')
        
        for player in players:
            if "odd" in player.get('class', []) or "even" in player.get('class', []):
                player_name = player.find('th', class_='td-player').find('span').text.strip()
                transfer_cost = player.find_all('td')[-1].text.strip()
                player_data.append((player_name, team_name, transfer_cost))

    return player_data

# Hàm chính để thu thập và xử lý dữ liệu
def main():
    url = 'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/2023-2024'
    teams = fetch_teams(url)
    all_players_data = []

    for team_name, team_url in teams:
        players = fetch_players(team_name, team_url)
        all_players_data.extend(players)
        print(f"Hoàn thành đội: {team_name}")
        time.sleep(3)  # Dừng 3 giây để tránh bị chặn truy cập

    # Tạo DataFrame từ dữ liệu cầu thủ thu thập được
    df = pd.DataFrame(all_players_data, columns=['Player', 'Team', 'Cost'])
    # df.to_csv("results4.csv", index=False, encoding='utf-8-sig')  # Lưu dữ liệu ra file CSV nếu cần
    print(df)

if __name__ == "__main__":
    main()