import discord
import os, datetime
from discord.ext import commands
from utils.Helpers import hasAttachments


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

    @commands.Cog.listener("on_message_edit")
    async def messageEdit(self, before, after):
        if before.channel.id == 943152490898153532 or 995768874660278362:
            return
        messageEditChannel = self.bot.get_channel(int(os.environ.get('MessageLogChannel')))
        currentTime = datetime.date.strftime(datetime.datetime.now(), "%H:%M")

        embed = discord.Embed(title=f"Nachricht bearbeitet in {before.channel}", color=discord.Colour.blue())
        embed.set_author(name=before.author, icon_url=before.author.display_avatar)
        embed.add_field(name="**Before:**", value=before.content, inline=False)
        embed.add_field(name="**After:**", value=after.content, inline=False)
        embed.set_footer(text=f"Message ID: {before.id} - Heute um {currentTime}")

        await messageEditChannel.send(embed=embed)

    @commands.Cog.listener("on_message_delete")
    async def messageDelete(self, message: discord.Message):
        if message.channel.id == 943152490898153532 or 995768874660278362:
            return
        messageDeleteChannel = self.bot.get_channel(int(os.environ.get('MessageLogChannel')))
        currentTime = datetime.date.strftime(datetime.datetime.now(), "%H:%M")

        embed = discord.Embed(title=f"Nachricht gelöscht in {message.channel}", color=discord.Colour.red())
        embed.set_author(name=message.author, icon_url=message.author.display_avatar)
        embed.description = message.content
        embed.set_footer(text=f"Message ID: {message.id} - Heute um {currentTime}")

        attachments = hasAttachments(message=message)
        if (attachments):
            embed.add_field(name="Attachments", value=attachments)
        await messageDeleteChannel.send(embed=embed)

    

async def setup(bot):
    await bot.add_cog(MemberLogs(bot))
