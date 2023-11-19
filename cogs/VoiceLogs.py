import discord, os
from discord.ext import commands


class VoiceLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_voice_state_update')
    async def voiceUpdate(self, member, before, after):
        voiceLogChannel = self.bot.get_channel(int(os.environ.get('VoiceLogChannel')))
        if before.channel == None and after.channel != None:
            embed = discord.Embed(title="Member Joined Channel", color=discord.Colour.green())
            embed.set_author(name=member, icon_url=member.display_avatar)
            embed.description = f"**{member}** tritt **{after.channel}** bei"
            await voiceLogChannel.send(embed=embed)
        elif before.channel != None and after.channel == None:
            embed = discord.Embed(title="Member Joined Channel", color=discord.Colour.red())
            embed.set_author(name=member, icon_url=member.display_avatar)
            embed.description = f"**{member}** verlässt **{before.channel}**"
            await voiceLogChannel.send(embed=embed)
        elif before.channel != None and after.channel != None:
            embed = discord.Embed(title="Member Switched Channel", color=discord.Colour.blue())
            embed.set_author(name=member, icon_url=member.display_avatar)
            embed.add_field(name="**Before:**", value=before.channel, inline=False)
            embed.add_field(name="**After:**", value=after.channel, inline=False)
            await voiceLogChannel.send(embed=embed)

    

async def setup(bot):
    await bot.add_cog(VoiceLogs(bot))
