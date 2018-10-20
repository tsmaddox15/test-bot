import os
import random

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import praw
import urllib.request
import requests

bot = commands.Bot(command_prefix='!')

lastChoice = ""


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='!help'))


@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("testing")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed1 = discord.Embed(title="{}'s info".format(user.name), description="Here is what I found.", color=0x00ff00)
    embed1.add_field(name="Name:", value=user.name, inline=True)
    embed1.add_field(name="ID:", value=user.id, inline=True)
    embed1.add_field(name="Status:", value=user.status, inline=True)
    embed1.add_field(name="Highest Role:", value=user.top_role, inline=True)
    embed1.add_field(name="Joined at:", value=user.joined_at, inline=True)
    embed1.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed1)
    # Bot says information.
    '''
    await bot.say("The user's name is: {}".format(user.name))
    await bot.say("This user's Id is: {}" .format(user.id))
    await bot.say("This user's Status is: {}" .format(user.status))
    await bot.say("This user's highest role is: {}".format(user.top_role))
    await bot.say("This user joined at: {}" .format(user.joined_at))
    '''


@bot.command(pass_context=True)
async def serverInfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server), description="Server info")
    embed.set_author(name="Author", value=ctx.message.server.author)
    embed.add_field(name="Server name:", value=ctx.message.server, inline=True)
    embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles:", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members:", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def embed(ctx):
    embed1 = discord.Embed(title="test", description="Howdy!", color=0x00ff00)
    embed1.set_footer(text="this is our footer")
    embed1.set_author(name="Taylor Maddox")
    embed1.add_field(name="Our field", value=":]", inline=True)
    await bot.say(embed=embed1)


@bot.command(pass_context=True)
async def dm(ctx):
    await bot.send_message(ctx.message.author, "testing dm.")


@bot.command(pass_context=True)
async def img(ctx):
    path = r"C:\Users\tsmad_000\Desktop\PycharmProjects\TestingBots\imgs"
    global lastChoice
    imgList = os.listdir(path)
    imgString = random.choice(imgList)
    while imgString == lastChoice:
        imgString = random.choice(imgList)
    imgPath = path + "\\" + imgString
    lastChoice = imgString
    await bot.send_file(ctx.message.channel, imgPath)


# @bot.command(pass_context=True)
# async def saveI(ctx):
#     path = r"C:\Users\tsmad_000\Desktop\PycharmProjects\TestingBots\imgs"
#     # img = urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
#     img_data = requests.get(
#         "https://vignette.wikia.nocookie.net/logopedia/images/a/af/Super_Smash_Bros_4_merged_logo%2C_no_subtitle.png/revision/latest?cb=20180316052816").content
#     with open(path + 'image_name.jpg', 'wb') as handler:
#         handler.write(img_data)
#     # link = str(ctx.message.attachments)
#     # # test2 = str(image)
#     # # await bot.say(": )")
#     # print(link)
#     # img = urllib.request(link)
#     # output = open("file01.jpg", "wb")
#     # output.write(img.read())
#     # output.close()


@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    role_channel_id = '501117904918413312'
    print(reaction.emoji)
    role1 = discord.utils.get(reaction.message.server.roles, name="Role 1")
    print("This is the emote:" + str(reaction.emoji))
    if reaction.message.channel.id != role_channel_id:
        return  # So it only happens in the specified channel
        print("not in right channel")
    if str(reaction.emoji) == "😃":
        print("in add role")
        await bot.add_roles(user, role1)


@bot.event
async def on_reaction_remove(reaction, user):
    role_channel_id = '501117904918413312'
    role1 = discord.utils.get(reaction.message.server.roles, name="Role 1")
    message = bot.get_message(501117904918413312)
    # print("This is the emote:" + str(reaction.emoji))
    if reaction.message.channel.id != role_channel_id:
        print("not in right channel")
        return  # So it only happens in the specified channel
    if str(reaction.emoji) == "😃":
        print("in remove role")
        await bot.remove_roles(user, role1)


@bot.event
async def on_member_join(member):
    await bot.send_message(member, "testing joining server message.")


@bot.command(pass_context=True)
async def split(ctx, gp):
    server = ctx.message.server.id
    channel = ctx.message.channel.id
    messageID = ctx.message.id
    userMessage = str(ctx.message)

    link = "https://discordapp.com/channels/" + str(server) + "/" + str(channel) + "/" + str(messageID) + "/"
    # print(link)
    if channel != "501141126636371978":
        await bot.delete_message(ctx.message)
        await bot.send_message(ctx.message.author, "All Splits should be confirmed in #loot-and-splits")

    # elif not (userMessage.startswith()) && channel == 501141126636371978:
    #     await bot.delete_message(ctx.message)
    #     await bot.send_message(ctx.message.author, "All Splits should be confirmed in #loot-and-splits")

    else:
        embed1 = discord.Embed(title="{}'s Split".format(ctx.message.author), description="",
                               color=0x00ff00)
        embed1.add_field(name="Name:", value=ctx.message.author, inline=True)
        embed1.add_field(name="ID:", value=ctx.message.author.id, inline=True)
        embed1.add_field(name="Rank:", value=ctx.message.author.top_role, inline=True)
        embed1.add_field(name="Split Amount:", value=gp, inline=True)
        embed1.add_field(name="Link:", value=link, inline=True)
        embed1.set_thumbnail(url=ctx.message.author.avatar_url)
        # embed1.set_thumbnail(url=image)
        await bot.send_message(bot.get_channel(id='502538741785821184'), embed=embed1)
        # await bot.say(502538741785821184,embed=embed1)


# @bot.event
# async def on_message(message):
#     channel = message.channel.id
#     message1 = str(message)
#     print(message1)
#     if channel == "501141126636371978" and not message1.startswith("!split"):
#         await bot.delete_message(message)
#         await bot.send_message(message.author, "Please only type !split or confirm on #loot-and-splits")


bot.run('NDgwMzk5NDAzODM2NzY4MjU3.DlnQig.OoChZ4ZKIyXqJdsiDs1fmbPq1FY')
