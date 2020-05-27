import discord
from discord.ext import commands
import time

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 도움(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="도움말", description= "**EZ봇 1.0 \nPrefix: ``.``**", color=0xffffff)
        embed.add_field(name='**도움**', value='**이 메시지를 보여줍니다.**', inline = False)
        embed.add_field(name='**아바타**', value='**본인의 아바타 또는 멘션된 유저의 아바타를 보여줍니다.**', inline = False)
        embed.add_field(name='**말하기**', value='**봇이 말을하게 만들 수 있습니다.**', inline = False)
        embed.add_field(name='**지원 서버**', value='**[클릭!](https://discord.gg/HerTmj5)**', inline = False)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
