from ..api.TwitchApi import Twitch

PARAMETER_CONFIG = {
    "targetid": "display_name",
    "displayName": "display_name",
    "game": "game",
    "url": "url",
    "title": "status",
    "mature": "mature",
    "partner": "partner",
    "views": "views",
    "followers": "followers"
}


class ShoutoutCommand(object):
    def __init__(self, **kwargs):
        """
        Wrapper for command processing
        :param kwargs: Keyword arguments
        :type kwargs dict
        :keyword settings: Settings object
        :type settings: Settings
        :keyword parent: parent object
        :type parent: parent
        """
        self.parent = kwargs.get("parent")
        self.settings = kwargs.get("settings")
        self.teams = self.settings.teams
        self.twitch = Twitch(self.settings, self.parent)

    def handle_command(self, data):
        if self.should_execute_command(data):
            shouted_user = data.GetParam(1)
            api = self.twitch
            team_json = api.get_teams(shouted_user).get('teams', [])
            channel_info = api.get_channel_info(shouted_user)
            self.parent.SendStreamMessage(
                self.parse_parameters(self.teams.find_matching_team([t.get('name').lower() for t in team_json]),
                                      data,
                                      channel_info))
            self.parent.AddCooldown(self.settings.get('Command'), self.settings.get('Command'),
                                    self.settings.get('Cooldown'))

    def should_execute_command(self, data):
        return data.IsChatMessage() \
           and data.GetParam(0).lower() == self.settings.get('Command') \
           and not self.parent.IsOnCooldown(self.settings.get('Command'), self.settings.get('Command')) \
           and self.parent.HasPermission(data.User, self.settings.get('Permission'), '') \
           and data.IsFromTwitch()

    @staticmethod
    def parse_parameters(message, data, channel_info):
        if channel_info.get('display_name') is None:
            channel_info = {
                "display_name": data.GetParam(1),
            }
        for key in PARAMETER_CONFIG.keys():
            message = message.replace("${}".format(key), str(channel_info.get(PARAMETER_CONFIG[key], "<No such channel>")))
        return message
