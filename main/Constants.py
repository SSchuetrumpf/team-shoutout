import os

ScriptName = "Team Shoutout"
Website = "https://www.twitch.tv/blackholedevice"
Description = "!so <User>. Will automatically shout out <User> using your configured team shoutouts"
Creator = "BlackholeDevice"
Version = "1.0.0.1"
DefaultSettings = os.path.join(os.path.dirname(__file__), "../config.json")
DefaultTeams = os.path.join(os.path.dirname(__file__), "../teams.json")
