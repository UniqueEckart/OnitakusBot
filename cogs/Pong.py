import discord
from discord import app_commands
from discord.ext import commands


class Pong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Returns th ping of the Bot in ms")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(interaction.client.latency * 1000)
        await interaction.response.send_message(f"Pong! With a Latency of {bot_latency}")

async def setup(bot):
    await bot.add_cog(Pong(bot))
