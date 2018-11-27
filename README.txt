How to configure teams

Make a file anywhere on your computer. The file should be a json file and have the following structure


[
    {
        "id": "team id 1",
        "message": "Message to shout when this team is found"
    },
    }
        "id": "team id 2",
        "message": "Second message to shout"
    }
]

Team ID is the twitch ID of the team to use. The ID should be pulled from the Team's URL. So, for example,
for Total Chaos, the link is "https://www.twitch.tv/team/totalchaos/", so the Team ID would be "totalchaos".
This must match exactly.

Parameters available

$targetid: Display Name of the caster to shout
$displayName: Identical to $targetid
$game: Last game being played by the caster
$url: Url to visit this casters channel
$title: Title of the last broadcast
$mature: "True" if the channel is listed as mature. "False" otherwise
$partner: "True" if the channel is listed a Twitch Partner. "False" otherwise
$views: Number of views this channel has
$followers: Number of followers this channel has

If for some reason the channel does not exist, only $targetid and $displayName will be available.

Check out $targetid! They were last seen playing $game. This is a default shoutout.