import discord.ext.commands
import json

import fireapi.config

class FireApiNotLoadedConfigError(Exception): pass

try:
    with open("fireapi.json") as config_file:
        fireapi.config.keys = json.load(config_file)
except FileNotFoundError:
    print("fireapi.json must be in running folder")
    raise FireApiNotLoadedConfigError()
except JSONDecodeError as e:
    print("fireapi.json not valid JSON format")
    print(str(e))
    raise FireApiNotLoadedConfigError()
except TypeError as e:
    print("I don't know how this works, lol")
    print(str(e))
    raise e
