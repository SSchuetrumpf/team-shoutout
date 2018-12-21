import os

ScriptName = "Team Shoutout"
Website = "https://www.twitch.tv/blackholedevice"
Description = "Shout out other broadcasters based on their teams"
Creator = "BlackholeDevice"
Version = "1.1.0"
DefaultSettings = os.path.join(os.path.dirname(__file__), "../config.json")
DefaultTeams = os.path.join(os.path.dirname(__file__), "../teams.json")
