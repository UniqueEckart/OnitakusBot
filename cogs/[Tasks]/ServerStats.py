from typing import Any, Coroutine
import discord, os
from utils.Logger import debugLog
from discord.ext import commands
from discord.ext.tasks import loop

class ServerStats(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.stats.start()

    def cog_unload(self):
        self.stats.cancel()

    @loop(minutes=30)
    async def stats(self):
        guild = self.bot.get_guild(int(os.environ.get("GUILD")))

        memberChannel = guild.get_channel(int(os.environ.get("MemberStats")))
        onisChannel = guild.get_channel(int(os.environ.get("OniStats")))
        botsChannel = guild.get_channel(int(os.environ.get("BotStats")))
        boosterChannel = guild.get_channel(int(os.environ.get("ServerBooster")))

        totalMembers = guild.member_count
        totalBoosters = guild.premium_subscription_count
        totalBots = "4"
        totalOnis = len(guild.get_role(1169216785782952018).members)

        memberName = "📊│all-members " + str(totalMembers)
        oniName = "🌸│onitakus " + str(totalOnis)
        botsName = "🤖│bots " + totalBots
        boosterName = "🚀│server-boosts " + str(totalBoosters)

        await memberChannel.edit(name=memberName)
        await onisChannel.edit(name=oniName)
        await botsChannel.edit(name=botsName)
        await boosterChannel.edit(name=boosterName)

    @stats.before_loop
    async def before_stats(self):
        debugLog("waiting for bot to be initialized")
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(ServerStats(bot))

    