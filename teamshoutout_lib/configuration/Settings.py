import codecs
import json

from ..model.Teams import Teams
from .. import Constants


class Settings(object):
    def __init__(self, **kwargs):
        """
        :keyword config Path to config file
        :type config str
        :keyword parent parent object
        :type parent parent
        """
        self.settingsFile = kwargs.get('config')
        self.teamsFile = None
        self.parent = kwargs.get('parent')
        self.settings = {}
        self.teams = None
        self.load()

    def load(self):
        try:
            self.settings = self.load_json(self.settingsFile)
        except IOError:
            self.settings = {
                "Command": "!so",
                "DefaultMessage": "Check out $targetid! They were last seen playing $game",
                "Cooldown": 4,
                "Permission": "moderator"
            }
        self.teamsFile = self.settings.get('TeamConfig', Constants.DefaultTeams)
        self.teams = Teams(self.teamsFile, self.settings.get('DefaultMessage'), self.parent)

    def reload(self, json_data):
        self.settings = json.loads(json_data, encoding="utf-8")
        self.teams = Teams(self.teamsFile, self.settings.get('DefaultMessage'), self.parent)
        self.parent.Log(Constants.ScriptName, str(dir(self.settings)))
        return

    def save(self):
        try:
            with codecs.open(self.settingsFile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.settings, f, encoding="utf-8")
            self.parent.Log(Constants.ScriptName, "WRITING")
        except IOError:
            self.parent.Log(Constants.ScriptName, "Failed to save settings to file.")
        return

    def get(self, setting, default=None):
        return self.settings.get(setting, default)

    @staticmethod
    def load_json(file):
        with codecs.open(file, encoding="utf-8-sig", mode="r") as f:
            return json.load(f, encoding="utf-8")