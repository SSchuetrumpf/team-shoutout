# ---------------------------
#   Import Libraries
# ---------------------------
import clr
import sys
import os

sys.path.append(os.path.dirname(__file__))
# sys.path.append(os.path.join(os.path.dirname(__file__), "main", "api"))
# sys.path.append(os.path.join(os.path.dirname(__file__), "main", "command"))
# sys.path.append(os.path.join(os.path.dirname(__file__), "main", "configuration"))
# sys.path.append(os.path.join(os.path.dirname(__file__), "main", "model"))
# sys.path.append(os.path.join(os.path.dirname(__file__), "main", "exception"))

from teamshoutout_lib import Constants
from teamshoutout_lib.command.ShoutoutCommand import ShoutoutCommand
from teamshoutout_lib.configuration.Settings import Settings
from teamshoutout_lib.exception.ExceptionHandler import ExceptionHandler

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")


# ---------------------------
#   [Required] Script Information
# ---------------------------
ScriptName = Constants.ScriptName
Website = Constants.Website
Description = Constants.Description
Creator = Constants.Creator
Version = Constants.Version

# ---------------------------
#   Define Global Variables
# ---------------------------
commands = []
settings = None
exception_handler = None


# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    global commands, settings, exception_handler
    exception_handler = ExceptionHandler(Parent)
    try:
        settings = Settings(
            config=Constants.DefaultSettings,
            parent=Parent
        )
        commands.append(
            ShoutoutCommand(
                parent=Parent,
                settings=settings
            )
        )
    except Exception as e:
        exception_handler.handle_exception(e)
        raise e
    return


# ---------------------------
#   [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):
    try:
        [c.handle_command(data) for c in commands]
    except Exception as e:
        exception_handler.handle_exception(e, data)
        raise e


# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    return


# ---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters)
# ---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    return parseString


# ---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
# ---------------------------
def ReloadSettings(jsonData):
    settings.reload(jsonData)
    settings.save()
    return


# ---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
# ---------------------------
def Unload():
    return


# ---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
# ---------------------------
def ScriptToggled(state):
    return
