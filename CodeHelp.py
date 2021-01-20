import discord
import random 
from discord.ext import commands
from howdoi import howdoi
from dpymenus import Page, PaginatedMenu
import aiohttp
import typing 
import json

def remString(str, gap):
  index, arr = 0, list()
  while(index+gap<len(str)):
    arr.append(str[index:index+gap])
    index+=gap
  arr.append(str[index:])
  return arr
class CodeHelp(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name = 'ask',
        aliases = ['get', 'getcode'],
        help = 'Fetch code from CodeGrepper, Takes in No. of results (default 3) and the question.')
    async def ask(self,ctx, result_limit: typing.Optional[int] = 3, *, term: str=None):
        embedColour = random.randint(0, 0xffffff)
        if term!=None:
            googlequery=term
            q=googlequery.replace(" ","+")
            cq=googlequery.replace(" ","%20")
            searchurl='https://www.google.com/search?q='+q
            originurl='https://www.codegrepper.com/search.php?q='+cq
            # print(searchurl,q)


            startEmbed = discord.Embed(
                title ="You asked",
                description =f'{term} \n [source]({originurl})',
                colour=embedColour
            )       
            startEmbed.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
             # print(term)
            results=[]
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.codegrepper.com/api/search.php', params ={"q":term}) as r :
                    result = await r.json()
                results=result['answers']
                
                answerEmbed=discord.Embed(
                    title='Answers',
                    colour=embedColour
                )
            # print(len(results),'length')
            # embed.set_footer(text=f'{ctx.message}')
            print(len(results))
            if len(results)<1:
                notFoundEmbed=discord.Embed(
                    title="Answer Not Found",
                    description=f'''[Search yourself]({searchurl})
                    \nYou can also contribute to this by installing [codegrepper](https://www.codegrepper.com/) extension and marking an answer when you find it
                    ''',
                    colour=embedColour
                )
                await ctx.send(embed=startEmbed)
                await ctx.send(embed=notFoundEmbed)
                pass
            elif len(results)==1:
                print(len(results))
                await ctx.send(embed=startEmbed)
                data=results
                resultList = []
                for i in range(len(data)):
                    # print(i)
                    # print(i['answer'])
                    if i >= result_limit :
                        break
                    j=data[i]
                    ans = j['answer']
                    lang =j['language']
                    source=" "
                    source=j['source_url']
                    print(source,"source")
                    answer=f'```{lang}\n {ans}```'
                    answerEmbed=discord.Embed(
                        # name="name",
                        description=answer,
                        colour=embedColour
                    )
                notGotEmbed=discord.Embed(
                title=":frowning2: Did Not Find Your Answer?",
                description=f'''[Search yourself]({searchurl})
                \nYou can also contribute to this by installing [codegrepper](https://www.codegrepper.com/) extension and marking an answer when you find it
                ''',
                colour=embedColour
                )
                await ctx.send(embed=answerEmbed)
                await ctx.send(embed=notGotEmbed)                    
                
            elif len(results)>=2:
                await ctx.send(embed=startEmbed)
                data=results
                resultList = []
                for i in range(len(data)):
                    # print(i)
                    # print(i['answer'])
                    if i >= result_limit :
                        break
                    j=data[i]
                    ans = j['answer']
                    lang =j['language']
                    source=" "
                    source=j['source_url']
                    print(source,"source")
                    answer=f'```{lang}\n {ans}```'
                    answerEmbed=discord.Embed(
                        # name="name",
                        description=answer,
                        colour=embedColour
                    )
                    resultList.append(answerEmbed)
                    #await ctx.send(embed=answerEmbed)
                notGotEmbed=discord.Embed(
                title=":frowning2: Did Not Find Your Answer?",
                description=f'''[Search yourself]({searchurl})
                \nYou can also contribute to this by installing [codegrepper](https://www.codegrepper.com/) extension and marking an answer when you find it
                ''',
                colour=embedColour
                )
                menu = PaginatedMenu(ctx)
                menu.add_pages(resultList)
                menu.set_timeout(30)
                menu.show_command_message()
                menu.persist_on_close()
                menu.show_page_numbers()
                menu.show_skip_buttons()
                menu.allow_multisession()
                await menu.open()
                print('menu opened')
                await ctx.send(embed=notGotEmbed)
            else:
                pass
           
        else:  
            noargEmbed=discord.Embed(
                    title="Ask Something, it can't be blank",
                    description='''
                    something expected 
                    `?ask what you want to ask`
                    ''',
                    colour=embedColour
                )
            await ctx.send(embed=noargEmbed)
        # await ctx.send(answer)

    @commands.command(name = 'howdoi',
        help = 'Ask it anything programming related it returns an first answer for that (works well with python), answers for non programing are little unexpected be aware')
    async def howdoi(self,ctx, result_limit: typing.Optional[int] = 3, *, term: str=None):
        embedColour = random.randint(0, 0xffffff)
        if term!=None:
            answer=howdoi.howdoi(term)
            if len(answer)<2048:
                answerEmbed = discord.Embed(
                    title="Your Answer is :",
                    description=f'```{answer}```',
                    color=embedColour
                )
                await ctx.send(embed=answerEmbed)
            elif len(answer)>=2048:
                await ctx.send('Your answer is too Long')
                await ctx.send('**Your Answer is** :')

                resultList= remString(answer,2000)
                i=0
                for res in resultList:
                    print(f'{len(res)} len')
                    if i <1:
                        answerEmbed = discord.Embed(
                        title="Your Answer is :",
                        description=f'```{res}```',
                        color=embedColour
                        )
                    else:
                        answerEmbed = discord.Embed(
                        
                        description=f'```{res}```',
                        color=embedColour
                        )
                    i+=1
                    await ctx.send(embed=answerEmbed) 
                i =0
                # maxLen=2048
                # a = len(answer) /maxLen
                # a = int(a)+1
                # print(a)

                # times = 
        else:  
            noargEmbed=discord.Embed(
                    title="Ask Something, it can't be blank",
                    description='''
                    something expected 
                    `?ask what you want to ask`
                    ''',
                    colour=embedColour
                )
            await ctx.send(embed=noargEmbed)
        # await ctx.send(answer)


def setup(client):
    client.add_cog(CodeHelp(client))