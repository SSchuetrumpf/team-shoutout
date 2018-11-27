from main.model.Teams import Teams

def main():
    teams = Teams("teams.json")
    team = teams.find_matching_team("asd")
    print(team)


if __name__ == '__main__':
    main()
