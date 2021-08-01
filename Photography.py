import discord
from discord.ext.commands import errors
import Util
import random
from discord.ext import commands
import dpytools.checks

class Photography(commands.Cog):
    """
    Contains commands for making posts for Photography Club
    """

    def __init__(self, client):
        self.client = client
        self.RawChannel = 825054209338376194
        self.EditedChannel = 825054426925498389

    HangoutChannel = 825055154201821244

    @commands.command(name="postraw", help="Posts attachment to the Raw Clicks channel")
    @dpytools.checks.in_these_channels(HangoutChannel)
    async def postraw(self, ctx, *, description=None):
        #if ctx.channel.id == self.HangoutChannel:
        if not len(ctx.message.attachments) < 1:
            if not len(description) < 1:
                postembed = discord.Embed(title="{}".format(
                    description), colour=random.randint(0, 0xffffff))
                postembed.set_image(url=ctx.message.attachments[0])
                postembed.set_author(name="{}".format(
                ctx.message.author.display_name), icon_url=ctx.message.author.avatar_url)
                sent = await self.client.get_channel(self.RawChannel).send(embed=postembed)
                await ctx.message.delete()
                await sent.add_reaction("❤")
            else:
                await ctx.send("Make sure you provide a caption to your image. `?rawpost CAPTION`")
                await ctx.message.delete()
        else:
            await ctx.send("Please attatch a lovely image")
            await ctx.message.delete()
        #else:
        #    await ctx.send("You can't do that here. Please go to <#{}>".format(self.HangoutChannel))
        #    await ctx.message.delete()
    @postraw.error
    async def postrawerror(self, ctx, error):
        await Util.ErrorHandler(ctx, error)

    @commands.command(name="postedited", help="Posts attachment to the Edited Pictures channel")
    @dpytools.checks.in_these_channels(HangoutChannel)
    async def postedited(self, ctx, *, description=None):
        #if ctx.channel.id == self.HangoutChannel:
        if not len(ctx.message.attachments) < 1:
            if not len(description) < 1:
                postembed = discord.Embed(title="{}".format(
                    description), colour=random.randint(0, 0xffffff))
                postembed.set_image(url=ctx.message.attachments[0])
                postembed.set_author(name="{}".format(
                ctx.message.author.display_name), icon_url=ctx.message.author.avatar_url)
                sent = await self.client.get_channel(self.EditedChannel).send(embed=postembed)
                await ctx.message.delete()
                await sent.add_reaction("❤")
            else:
                await ctx.send("Make sure you provide a caption to your image. `?editedpost CAPTION`")
                await ctx.message.delete()
        else:
            await ctx.send("Please attatch a lovely image")
            await ctx.message.delete()
        #else:
        #    await ctx.send("You can't do that here. Please go to <#{}>".format(self.HangoutChannel))
        #    await ctx.message.delete()
    @postedited.error
    async def posteditederror(self, ctx, error):
        await Util.ErrorHandler(ctx, error)
    


def setup(client):
    client.add_cog(Photography(client))
