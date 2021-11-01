from discord import FFmpegPCMAudio
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import asyncio
import time
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('log_in: ')
    print(bot.user.name)
    print('소환됐다 멍')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("짐니 생각"))

@bot.command()
async def copy(ctx, *, text):
  await ctx.send(text)

@bot.command()
async def summon(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send("크르릉멍멍!")
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("주인이 없다멍..")

@bot.command()
async def sleep(ctx):
        await vc.disconnect()
        await ctx.send("졸리다멍..")

@bot.command()
async def 멍(ctx):
    await ctx.send('멍?')

@bot.command()
async def 안녕(ctx):
    await ctx.reply('멍멍!')

@bot.command()
async def 잘가(ctx):
    await ctx.reply('멍..?멍....')

@bot.command()
async def 헤헹(ctx):
    await ctx.reply('푸항항 ꉂꉂ(ᵔᗜᵔ*) 푸항항 ꉂꉂ(ᵔᗜᵔ*) 푸항항 ꉂꉂ(ᵔᗜᵔ*)')

@bot.command()
async def p(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "Now Playing 멍멍", description = url, color = 0x00ff00))
    else:
        await ctx.send("재생중이다 멍!")
        
@bot.command()
async def t(ctx, *, msg):
    if not vc.is_playing():

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "C:\\Users\\박주성\\Downloads\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query="+msg)
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "Now Playing 멍멍", description = entireText, color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("재생중이다 멍!")

@bot.command()
async def pause(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "일시정지멍", description = entireText + "paused", color = 0x00ff00))
    else:
        await ctx.send("노래가 꺼져있다 멍")

@bot.command()
async def resume(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("노래가 꺼져있다 멍")
    else:
         await ctx.send(embed = discord.Embed(title= "다시재생멍", description = entireText  + "resumed", color = 0x00ff00))

@bot.command()
async def stop(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "노래끈다멍", description = entireText  + "stopped", color = 0x00ff00))
    else:
        await ctx.send("노래가 꺼져있다 멍")
        
bot.run('my token')
