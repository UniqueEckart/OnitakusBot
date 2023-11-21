import discord
from discord import app_commands
from discord.ext import commands

class CogAdmin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="reload", description="Hot reload a Cog. Only for Debug!")
    @app_commands.checks.has_permissions(administrator=True)
    async def reload(self, interaction: discord.Interaction, cog: str):
        for name, cogObject in self.bot.cogs.items():
            if cog == name:
                co = str(cogObject.__class__).replace("<class '", "")
                co = co.replace("'>", '').split(".")
                co = co[0] + "." + co[1] + "." + co[2]
                await self.bot.reload_extension(co)
                await interaction.response.send_message(f"Reloaded Cog {cogObject.__class__}", ephemeral=True)
                return
        await interaction.response.send_message("Failed to reload cog!", ephemeral=True)

    @app_commands.command(name="unload", description="Unload a Cog. Only for Debug!")
    @app_commands.checks.has_permissions(administrator=True)
    async def unload(self, interaction: discord.Interaction, cog: str):
        for name, cogObject in self.bot.cogs.items():
            if cog == name:
                co = str(cogObject.__class__).replace("<class '", "")
                co = co.replace("'>", '').split(".")
                co = co[0] + "." + co[1] + "." + co[2]
                await self.bot.unload_extension(co)
                await interaction.response.send_message(f"Unloaded Cog {cogObject.__class__}", ephemeral=True)
                return
        await interaction.response.send_message("Failed to unload cog!", ephemeral=True)

    @app_commands.command(name="sync", description="Responsible for Syncing new Commands.")
    async def sync(self, interaction: discord.Interaction):
        if interaction.user.id != 275024450494136321:
            await interaction.response.send_message("Du hast keine Berechtigung diesen Command zu verwenden!", ephemeral=True)
            return
        fmt = await self.bot.tree.sync()
        await interaction.response.send_message(f"Ich habe insgesamt {len(fmt)} Commands gesynct!", ephemeral=True)
        
        


    

async def setup(bot):
    await bot.add_cog(CogAdmin(bot))
