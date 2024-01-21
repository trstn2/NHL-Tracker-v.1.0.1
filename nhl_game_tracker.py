import requests
import json

print("Use abbreviations ex: (wpg) |winnipeg jets| or (WPG) |WINNIPEG JETS|.")
user_input_choice = input("(L)League Standings, (T)Team games, (A)All team schedules, (TS)Team Stats (RS)Roster "
                          "Season: ")

url_schedule = "https://api-web.nhle.com/v1/schedule/now"
league_standings_now = "https://api-web.nhle.com/v1/standings/now"

# Enter the abbreviation of your favorite NHL team. EX: wpg or WPG

if user_input_choice == "RS":
    roster_of_choice = input("Enter team for roster this season: ")
    roster_url = f"https://api-web.nhle.com/v1/roster/{roster_of_choice}/now"
else:
    roster_url = None

if user_input_choice == "T":
    team_of_choice = input("Enter Team ABBR: ")
    team_url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_of_choice}/now"
else:
    team_url = None

if user_input_choice == "TS":
    team_stats_of_choice = input("Enter Team ABBR: ")
    team_stats_url = f"https://api-web.nhle.com/v1/club-stats-season/{team_stats_of_choice}"
else:
    team_stats_url = None

# Make a GET request to the NHL API
response_roster = requests.get(roster_url) if roster_url else None
response_schedule = requests.get(url_schedule) if url_schedule else None
response_league = requests.get(league_standings_now) if league_standings_now else None
response_team = requests.get(team_url) if team_url else None
response_team_stats = requests.get(team_stats_url) if team_stats_url else None

if user_input_choice == "RS":
    if response_roster.status_code == 200:
        roster_this_season = response_roster.json()
        print("Current roster this season:\n", roster_this_season)
        with open('nhl_stats.json', 'w') as f:
            json.dump(roster_this_season, f)
    else:
        print(f"Roster error. Status code:\n {response_roster.status_code}")

if user_input_choice == "L":
    if response_league.status_code == 200:
        league_standings = response_league.json()
        print("Current NHL League Standings:\n", league_standings)
        with open('nhl_stats.json', 'w') as f:
            json.dump(league_standings, f)
    else:
        print(f"An error occurred. Status code: {response_league.status_code}")

if user_input_choice == "T":
    if response_team and response_team.status_code == 200:
        team_data = response_team.json()
        print("Current NHL team schedule:\n", team_data)
        with open('nhl_stats.json', 'w') as f:
            json.dump(team_data, f)
    else:
        print(f"An error occurred. Status code: {response_team.status_code}")

if user_input_choice == "A":
    if response_schedule.status_code == 200:
        schedule_data = response_schedule.json()
        print("Current NHL schedule:\n", schedule_data)
        with open('nhl_stats.json', 'w') as f:
            json.dump(schedule_data, f)
    else:
        print(f"An error occurred. Status code: {response_schedule.status_code}")

if user_input_choice == "TS":
    if response_team_stats and response_team_stats.status_code == 200:
        team_stats = response_team_stats.json()
        print("Current NHL Teams Stats:\n", team_stats)
        with open('nhl_stats.json', 'w') as f:
            json.dump(team_stats, f)
    else:
        print(f"An error occurred. Status code: {response_team_stats.status_code}")
