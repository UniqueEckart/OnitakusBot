import discord
from discord.ext import commands
import os, utils.Logger
from dotenv import load_dotenv

load_dotenv()

class Onitakus(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        application_id = os.environ.get("AppID")

        super().__init__(command_prefix="-", intents=intents, application_id=application_id)

    async def setup_hook(self) -> None:
       for dirs in os.listdir('cogs'):
            if os.path.isdir("./cogs/" + dirs) and dirs.startswith("["):
               for cog in os.listdir("./cogs/" + dirs):
                    if cog.endswith(".py"):
                        cog = cog[:-3]
                        utils.Logger.debugLog(f"loading Cog: {cog} from Category {dirs}")
                        await self.load_extension(f'cogs.{dirs}.{cog}')
            else:
               utils.Logger.warning(f"The Directory {dirs} is not a valid Category!")

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Onitakus"))
        print(f"Logged in as {self.user}")

bot = Onitakus()
bot.run(os.environ.get("TOKEN"))