import fireapi
import fireapi.config
import fireapi.commands

import sys

zipcode = sys.argv[1]

print(fireapi.commands.zipToLatLong(zipcode))

#import catbot
#import catbot.commands
#import catbot.config
#import catbot.events

#catbot.bot.run(catbot.config.keys["discord"])
