import json
import calendar
import time
from functools import wraps

EMPTY_RESULT = {
    "teams": []
}

API = {
    "teams": "https://api.twitch.tv/kraken/channels/{}/teams",
    "channelInfo": "https://api.twitch.tv/kraken/channels/{}"
}


def ttl_cache(time_to_live_seconds):
    def cache(func):
        memo = {}

        @wraps(func)
        def wrapper(*args):
            current_time = calendar.timegm(time.gmtime())

            def execute_and_cache():
                rv = func(*args)
                memo[args] = {
                    'returnVal': rv,
                    'time': current_time
                }
                return memo[args]

            try:
                cache_val = memo[args]
                if current_time - cache_val['time'] >= time_to_live_seconds:
                    cache_val = execute_and_cache()
                return cache_val['returnVal']
            except KeyError:
                return execute_and_cache()['returnVal']

        return wrapper
    return cache


class Twitch(object):
    def __init__(self, settings, parent):
        self.parent = parent
        self.settings = settings

    # 1 day
    @ttl_cache(time_to_live_seconds=60 * 60 * 24)
    def get_teams(self, username):
        self.parent.Log("API", "Fetching team info for {}".format(username))
        response = json.loads(self.parent.GetRequest(API.get("teams").format(username), self.get_headers())).get('response',
                                                                                                      json.dumps(
                                                                                                          EMPTY_RESULT))
        return json.loads(response)

    # 3 hours
    @ttl_cache(time_to_live_seconds=60 * 60 * 3)
    def get_channel_info(self, username):
        self.parent.Log("API", "Fetching channel info for {}".format(username))
        return json.loads(json.loads(self.parent.GetRequest(API.get("channelInfo").format(username), self.get_headers())).get('response', json.dumps(EMPTY_RESULT)))

    def get_headers(self):
        return {
            "Authorization": 'Bearer {}'.format(self.settings.get('ClientId')),
            "Client-Id": self.settings.get('ClientId')
        }
