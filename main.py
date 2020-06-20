import discord
from discord.ext import commands
import time
import requests

bot = commands.Bot(command_prefix="/", status=discord.Status.online, activity=discord.Game("Booting ..."))
bot.remove_command('help')
bot.remove_command('nick')
members = 0
@bot.event
async def on_ready():
    print("Booting....")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Ryo is online| Wake me with '/'"))
    print("Logged in as:" + bot.user.name + "\n")

@bot.event
async def on_member_join(member: discord.Member):
    WelcomeChannel = bot.get_channel(695299156222279802)
    Community = discord.utils.get(member.guild.roles, id=int("695268457217917100"))
    await WelcomeChannel.send(f"{member.mention}! Welcome To {member.guild.name}! Please don't be a 𝒟𝐼𝒞𝒦 🤬 🙃 ")
    # await WelcomeChannel.send(f"{member.mention}! Welcome To {member.guild.name}! Please don't be a 𝒟𝐼𝒞𝒦 🤬 🙃 ")
    await member.add_roles(Community)
    # for guild in bot.guilds:
    #     for member in guild.members:
    #         MembersChannel = bot.get_channel(722574979639803924)
    #         await discord.VoiceChannel.edit(MembersChannel, name = f"✅All Members: {member}✅")



@bot.event
async def on_member_remove(member: discord.Member):
    ByeChannel = bot.get_channel(701890864103817276)
    await ByeChannel.send(f"{member.mention} Left 😰! Have a good time in heaven 😇!!Fucker 🤬")
    # for guild in bot.guilds:
    #     for member in guild.members:
    #         MembersChannel = bot.get_channel(722574979639803924)
    #         await discord.VoiceChannel.edit(MembersChannel, name = f"✅All Members: {member}✅")    

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member = None, reason = None):
    if member == ctx.message.author or member == None:
        await ctx.channel.send("``You can not ban YOURSELF``")
    if reason == None:
        reason = "no reason"
    discordManager = discord.utils.get(member.guild.roles, id=int("695300277540225054"))
    owners = discord.utils.get(member.guild.roles, id=int("695268462422917240"))
    DMBan = f"You have been banned from {ctx.guild.name} for {reason}"
    ChannelBan = f"{member} has been banned. For more details please contact a {discordManager} or {owners}"
    await member.ban()
    await member.send(DMBan)
    await ctx.channel.send(ChannelBan)
    return 

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member:discord.Member = None):
    if member == ctx.message.author or member == None:
        await ctx.channel.send("``You can not unban YOURSELF``")
    banned_users = await ctx.guild.bans()
    # member_name , member.discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member.name, member.discriminator):
          await ctx.guild.unban(user)
          discordManager = discord.utils.get(member.guild.roles, id=int("695300277540225054"))
          owners = discord.utils.get(member.guild.roles, id=int("695268462422917240"))
          DMUnban = f"You have been unbanned from {ctx.guild.name} please try be more carefull from now!"
          Channelunban = f"{user.mention} has been unbanned. For more details please contact a {discordManager.mention} or {owners.mention}"
          await member.send(DMUnban)
          await ctx.channel.send(Channelunban)
          return
        else:
            await ctx.channel.send("This user is not banned sorry 🙁 ")
    


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None, reason = None):
    if member == ctx.message.author or member == None:
        await ctx.channel.send("Error 404")
    if reason == None:
        reason = "no reason"
    ChannelKick = f"Thank you for being a great mod. You kicked {member} for {reason}" 
    DMKick = f"Dear {member}, You were kicked from {ctx.guild.name} for {reason}. Please DM a mod or a owner form the server"
    await member.kick()
    await ctx.channel.send(ChannelKick)
    await member.send(DMKick)
    return


@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild
    roles = member.roles
    # Gay = discord.utils.get(member.guild.roles, id=int("700790533177475164"))
    Community = discord.utils.get(member.guild.roles, id=int("695268457217917100"))
    DiscordManager = discord.utils.get(member.guild.roles, id=int("695300277540225054"))
    helper = discord.utils.get(member.guild.roles, id=int("695650378804363367"))
    mod = discord.utils.get(member.guild.roles, id=int("702261449535520938"))
    VALORANT = discord.utils.get(member.guild.roles, id=int("700636020101742714"))
    csgo5 = discord.utils.get(member.guild.roles, id=int("695300284326346763"))
    Partners = discord.utils.get(member.guild.roles, id=int("695341762557771846"))
    BotsRole = discord.utils.get(member.guild.roles, id=int("695269826507178026"))
    frietouchers = discord.utils.get(member.guild.roles, id=int("696648897417707560"))
    if Community in roles:
        await member.remove_roles(Community)
    if DiscordManager in roles:
        await member.remove_roles(DiscordManager)
    if helper in roles:
        await member.remove_roles(helper)
    if mod in roles:
        await member.remove_roles(mod)
    if VALORANT in roles:
        await member.remove_roles(VALORANT)
    if csgo5 in roles:
        await member.remove_roles(csgo5)
    if Partners in roles:
        await member.remove_roles(Partners)
    if BotsRole in roles:
        await member.remove_roles(BotsRole)
    if frietouchers in roles:
        await member.remove_roles(frietouchers)
    for role in guild.roles:
         if role.name == "Muted":
             await member.add_roles(role)
             Community2 = discord.utils.get(member.guild.roles, id=int("695268457217917100"))
             await member.remove_roles(Community2)
             await ctx.send(f"{member} has been muted")
             return



@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild
    Community = discord.utils.get(member.guild.roles, id=int("695268457217917100"))
    for role in guild.roles:
         if role.name == "Muted":
             await member.remove_roles(role)
             await ctx.send(f"{member} has been unmuted")
             await member.add_roles(Community)
             return


#@bot.command(pass_context=True)
#async def help(ctx):
#    author = ctx.message.author

@bot.command()
async def user(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(
        #title = f'User Details for {member}',
        #description = f'This is {member} details. Such as: When thay joined, What role they have and their profile picture',
        color = discord.Colour.purple(),
        timestap = ctx.message.created_at
    )
    embed.set_footer(text='This is a footer.')
    #embed.set_image(url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=f'{member.name}', icon_url=member.avatar_url)
    embed.add_field(name="Username:", value=f'{member.name}', inline=True)
    embed.add_field(name="ID:", value=f'{member.id}', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name="Created At", value=f'{member.created_at.strftime("%A, %B %d %Y")}.', inline=True)
    embed.add_field(name='Joined At', value=f'{member.joined_at.strftime("%A, %B %d %Y")}.', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name='Roles:', value=" ".join(role.mention for role in roles), inline=False)
    embed.add_field(name="Top Role:", value=f"{member.top_role.mention}")
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    #embed.add_field(name="Custom Status:", value=f"{member.Custom.status}", inline=True)
    #embed.add_field(name='Field', value='Field Value', inline=True)
    await ctx.channel.send(embed=embed)
    return


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = f'Commands And Rules For @Ryo#9425',
        description = f'This is a complete list for @Ryo#9425 commands and rules as of {ctx.message.created_at}. For more info or details please consult #𝓡𝔂𝓸-𝓽𝓱𝓮-𝓰𝓸𝓭-𝖀𝖕𝖉𝖆𝖙𝖊𝖘 ',
        colour = discord.Colour.gold()
    )
    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1213978854584463362/SumAINHm_400x400.jpg')       
    embed.add_field(name='/user', value='You can use this for you user credits or more information about you!', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name='/ban', value='This is a special command for mods and admins so normal people like the Community role cant use this', inline=True)
    embed.add_field(name='/unban', value='The clear opposite of ban!', inline=True)
    embed.add_field(name='/kick', value='Also a mod command you can oviously understand what it can do', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name='/mute', value='This is for people that are annoying and cant keep their mouth closed', inline=True)
    embed.add_field(name='/unmute', value='This is the opposite of mute', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name='!play', value='Music🎧(Currently using Rythm🎵!)', inline=True)
    embed.add_field(name='!disconnect', value='Disconnect Rythm🎵 from the voice channel', inline=True)
    embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎ ‎', inline=False)
    embed.add_field(name='!!!𝐍𝐄𝐖 𝐂𝐎𝐌𝐌𝐀𝐍𝐃!!!', value='/𝐦𝐨𝐝 it is a new command for you to get mod and admin powers to the server and it is for all roles to enjoy!!!', inline=True)

    await ctx.channel.send(embed=embed)
    return


@bot.command()
async def mod(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    roles = member.roles
    Gay = discord.utils.get(member.guild.roles, id=int("700790533177475164"))
    Community = discord.utils.get(member.guild.roles, id=int("695268457217917100"))
    DiscordManager = discord.utils.get(member.guild.roles, id=int("695300277540225054"))
    helper = discord.utils.get(member.guild.roles, id=int("695650378804363367"))
    mod = discord.utils.get(member.guild.roles, id=int("702261449535520938"))
    VALORANT = discord.utils.get(member.guild.roles, id=int("700636020101742714"))
    csgo5 = discord.utils.get(member.guild.roles, id=int("695300284326346763"))
    Partners = discord.utils.get(member.guild.roles, id=int("695341762557771846"))
    BotsRole = discord.utils.get(member.guild.roles, id=int("695269826507178026"))
    frietouchers = discord.utils.get(member.guild.roles, id=int("696648897417707560"))
    if Community in roles:
        await member.remove_roles(Community)
    if DiscordManager in roles:
        await member.remove_roles(DiscordManager)
    if helper in roles:
        await member.remove_roles(helper)
    if mod in roles:
        await member.remove_roles(mod)
    if VALORANT in roles:
        await member.remove_roles(VALORANT)
    if csgo5 in roles:
        await member.remove_roles(csgo5)
    if Partners in roles:
        await member.remove_roles(Partners)
    if BotsRole in roles:
        await member.remove_roles(BotsRole)
    if frietouchers in roles:
        await member.remove_roles(frietouchers)
    await ctx.channel.send("{} you thought you where funny ha. You stupid ass dickhead will now suck cock for eternity".format(member.mention))
    await member.add_roles(Gay)

@bot.event
async def on_message(message):
    HeyRyo = ['hey ryo', 'Hey Ryo', 'HEY RYO', 'Hey ryo', 'hey Ryo']
    BadWords = ['nigga', 'NIGGA', 'Nigga', 'Retard', 'retard', 'Retard', 'autistic', 'Autistic', 'AUTISTIC']


    if message.content.lower() in BadWords:
        await message.delete()
        await message.channel.send("Please do not say that here as we are a respectfull community and do not enforce those kind of messages😣🥰!")
        embed = discord.Embed(
            color = discord.Color.dark_blue(),
            title = f"Hey!"
        )    
        embed.set_thumbnail(url="https://i.imgur.com/3YmKdIu.png")
        await message.channel.send(embed=embed)
        return
    for  word in HeyRyo:
        if message.content.count(word):
            embed = discord.Embed(
            title = f"Hey!",
            color = discord.Color.dark_blue()     
            ) 
            embed.set_thumbnail(url="https://i.imgur.com/AcoMCmN.png")
            embed.add_field(name="‎‏‏‎ ‎", value='‏‏‎Hello there i saw that you talked about me in your messages. If you need me to help you type /help in chat and that you are gay :)', inline=False)
            await message.channel.send(embed=embed)
            return
    await bot.process_commands(message)
    
@bot.command()
async def warn(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    if member == ctx.message.author  or member == None:
       await ctx.channel.send("You can not warn yourself!") 
    else:
        embed = discord.Embed(
        color = discord.Color.dark_blue(),
        title = f"WARN BAN"
        )  
        embed.set_thumbnail(url="https://i.imgur.com/3YmKdIu.png")
        embed.add_field(name='Warn Ban', value="You have been warned for beeing a asshole or a retard and if you get 3 warning you get perm banned from the server", inline=True)
        await member.send(embed=embed)   
        await bot.get_all_members

 





@bot.command()
@commands.has_permissions(ban_members=True)
async def clear(ctx, amount: int):

    await ctx.channel.purge(limit=amount + 1)
    await ctx.channel.send(f"You deleted {amount} messages")
    time.sleep(3)
    await ctx.channel.purge(limit = 1)
    return




bot.run('YOUR TOKEN HERE)