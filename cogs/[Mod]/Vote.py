from typing import Any, Coroutine
import discord, os, datetime
from utils.Logger import debugLog
from utils.Helpers import timeToUnix
from discord.ext import commands
from discord import app_commands
from discord.ext.commands.context import Context


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def cog_command_error(self, ctx, error: Exception):
        if error == discord.app_commands.MissingRole:
            debugLog("User missing Role")

    @app_commands.command(name="vote", description="Lässt die eine abstimmung machen!")
    @app_commands.checks.has_role(int(os.environ.get("TeamRole")))
    async def vote(self, interaction: discord.Interaction, topic: str, duration: str, answer1: str = "", answer2: str = ""):
        unix = timeToUnix(duration)

        voteEmbed = discord.Embed(title=f"Abstimmung über {topic}", color=discord.Colour.green())
        voteEmbed.add_field(name="Antwort 1", value=answer1, inline=False)
        voteEmbed.add_field(name="Antwort 2", value=answer2, inline=False)
        voteEmbed.set_footer(f"Die Abstimmung endet am: <t:{unix}:f>")

        await interaction.response.send_message(embed=voteEmbed)
        message = await interaction.original_response()
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        
async def setup(bot):
    await bot.add_cog(Vote(bot))
