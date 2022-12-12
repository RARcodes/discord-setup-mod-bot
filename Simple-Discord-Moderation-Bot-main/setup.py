import discord
from discord.ext import commands
from colorama import Fore, Style

r = Fore.MAGENTA
w = Fore.WHITE

print(f"""{r}
███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗\n████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗\n██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝\n██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗\n██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║\n╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      
{r}-------------------------------------------\n{r}| {r}.rar#0001 {r}|{r}\n{r}-------------------------------------------\n
{r}""")

#config
TOKEN = input("Input Bot Token: ")
SERVER = input("Input New Server name: ")
CAT1 = "welcome"
CHANNEL1 = "👋│joins"
CHANNEL2 = "📘│rules"
CAT2 = "info"
CHANNEL4 = "📢│announcements"
CHANNEL5 = "🎉│giveaways"
CHANNEL6 = "👥│feedback"
CHANNEL7 = "🌐│links"
CAT3 = "Main"
CHANNEL8 = "💬│chat"
CHANNEL9 = "📁│help"
CHANNEL10 = "🌼│off-topic"
CHANNEL11 = "🔥│your-work"
CAT4 = "other"
CHANNEL13 = "📨│ticket"

#prefix-settings
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#online-statement
@bot.event
async def on_ready():
  print(f"\n{w}ready! │ !setup")

#script
@bot.command()
async def setup(ctx):
  guild = ctx.message.guild
  await ctx.send("Setting Up...")
  channels = await ctx.guild.fetch_channels()
  for text_channel in channels:
        await text_channel.delete()
  await ctx.guild.edit(name=SERVER)
  category = await guild.create_category(CAT1)
  await category.create_text_channel(CHANNEL1)
  await category.create_text_channel(CHANNEL2)
  category = await guild.create_category(CAT2)
  await category.create_text_channel(CHANNEL4)
  await category.create_text_channel(CHANNEL5)
  await category.create_text_channel(CHANNEL6)
  await category.create_text_channel(CHANNEL7)
  category = await guild.create_category(CAT3)
  await category.create_text_channel(CHANNEL8)
  await category.create_text_channel(CHANNEL9)
  await category.create_text_channel(CHANNEL10)
  await category.create_text_channel(CHANNEL11)
  category = await guild.create_category(CAT4)
  await category.create_text_channel(CHANNEL13)
  
#run-bot
bot.run(TOKEN)