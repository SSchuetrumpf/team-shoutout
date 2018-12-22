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
if the link is "https://www.twitch.tv/team/team123/", so the Team ID would be "team123".
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

Upgrade Instructions:
    1. Back up config.json and config.js
    2. Delete TeamShoutout script directory
    3. Reimport TeamShoutout.zip
    4. Replace config.json and config.js


Obtaining a client Id:

In order for this script to be able to automatically look up team information, you must generate a twitch app client id.

1. Navigate to https://dev.twitch.tv/
2. Log in
3. Navigate to "Your Dashboard" if needed
4. Go to "Apps" tab
5. Click "Register your Application" and fill out the form
6. Copy the string in the field labeled "Client ID"
7. Enter into the "Client Id" section of Team Shoutout and click Save.