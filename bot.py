import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class Onitakus(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        application_id = os.environ.get("AppID")

        super().__init__(command_prefix="-", intents=intents, application_id=application_id)

    async def setup_hook(self) -> None:
       for file in os.listdir('cogs'):
           if file.endswith('.py'):
               await self.load_extension(f'cogs.{file[:-3]}')

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Onitakus"))
        #fmt = await self.tree.sync()
        #print(f"Synced {len(fmt)} Commands.")
        print(f"Logged in as {self.user}")

bot = Onitakus()
bot.run(os.environ.get("TOKEN"))