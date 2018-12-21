import json
import codecs
# noinspection PyUnresolvedReferences
from .. import Constants


class Teams(object):
    def __init__(self, teams_config=None, default_message=None, parent=None):
        self.parent = parent
        self.teams = {'default': default_message}
        self.parent.Log(Constants.ScriptName, 'Loading teams')
        try:
            with codecs.open(teams_config, encoding="utf-8-sig", mode="r") as f:
                teams = json.load(f, encoding="utf-8")
                for team in teams:
                    self.parent.Log(Constants.ScriptName,
                                    'Team ID "{}", Shout message "{}"'.format(team.get("id"), team.get("message")))
                    self.teams[team.get("id").lower()] = team.get("message")
        except Exception as e:
            self.parent.Log(Constants.ScriptName, str(e))

    def find_matching_team(self, teams):
        return self.teams[next(iter(set(teams).intersection(self.teams.keys())), 'default')]
