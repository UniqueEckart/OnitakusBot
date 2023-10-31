import discord
import os
from discord.ext import commands


class MemberLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_member_remove")
    async def member_leave(self, member: discord.Member):
        leave = self.bot.get_channel(int(os.environ.get("LeaveChannel")))
        await leave.send(f"<@{member.id}> hat uns leider verlassen!")
        
    @commands.Cog.listener("on_member_update")
    async def member_update(self, before: discord.Member, after: discord.Member):
        log = self.bot.get_channel(int(os.environ.get('UserLogChannel')))
        base_embed = discord.Embed(color=discord.Colour.red())
        if before.nick != after.nick:
            base_embed.title = "Nickname Änderung"
            base_embed.set_author(name=before.global_name, icon_url=before.avatar.url)
            base_embed.add_field(name="Before", value=before.nick, inline=False)
            base_embed.add_field(name="After", value=after.nick, inline=False)
            base_embed.set_footer(text=f"ID: {before.id}")
        else:
            base_embed.title = "Avatar Änderung"
            base_embed.set_author(name=before.global_name, icon_url=before.avatar.url)
            base_embed.set_thumbnail(url=after.avatar.url)
            base_embed.add_field(name="User", value=before.global_name)
            base_embed.set_footer(text=f"ID: {before.id}")
        await log.send(embed=base_embed)

    

async def setup(bot):
    await bot.add_cog(MemberLogs(bot))
