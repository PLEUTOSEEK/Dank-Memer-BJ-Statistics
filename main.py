from lib import *

bot = commands.Bot(command_prefix="_")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    embeds = message.embeds
#===========================Embed Handle==============================  
    if len(embeds) != 0:
      for embed in embeds:
        embed.to_dict()

      print(embed.to_dict())
      #print(embed.fields[0].name)
#===========================Message Handle==============================  
    elif len(embeds) == 0:
      msg = message.content

bot.run(os.getenv("TOKEN"))
