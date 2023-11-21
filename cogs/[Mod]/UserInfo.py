import discord
from discord import app_commands
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="info", description="Zeig dir Informationen über einen User an")
    @app_commands.checks.has_permissions(kick_members=True)
    async def info(self, interaction: discord.Interaction, target: discord.Member):
        embed = discord.Embed(title=f"User Informationen vom User {target}", color=discord.Colour.green())
        embed.set_author(name=target, icon_url=target.display_avatar)  
        embed.add_field(name="**Username**", value=target)
        embed.add_field(name="**User ID**", value=target.id)
        embed.add_field(name="**Account erstellt am**", value=target.created_at.strftime("%Y/%m/%d %H:%M"), inline=False)
        embed.add_field(name="**Server beigetreten am**", value=target.joined_at.strftime("%Y/%m/%d %H:%M"), inline=False)
        await interaction.response.send_message(embed=embed)

    

async def setup(bot):
    await bot.add_cog(UserInfo(bot))
