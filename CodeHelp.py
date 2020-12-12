import discord
import random 
from discord.ext import commands
import aiohttp
import typing 
import json

class CodeHelp(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command('ask', help='ask a questions ')
    async def ask(self,ctx, result_limit: typing.Optional[int] = 1, *, term: str=None):
        if term!=None:
            googlequery=term
            q=googlequery.replace(" ","+")
            cq=googlequery.replace(" ","%20")
            searchurl='https://www.google.com/search?q='+q
            originurl='https://www.codegrepper.com/search.php?q='+cq
            # print(searchurl,q)

            embedColour = random.randint(0, 0xffffff)

            embed = discord.Embed(
                title ="You asked",
                description =f'{term} \n [source]({originurl})',
                colour=embedColour
            )           
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
            
            if len(results)<1:
                notFoundEmbed=discord.Embed(
                    title="Answer Not Found",
                    description=f''' You can also contribute to this answers by intalling [codegrepper](https://www.codegrepper.com/) Extensions and marking answer when you find it
                    \n[Search yourself]({searchurl})''',
                    colour=embedColour
                )
                await ctx.send(embed=embed)
                await ctx.send(embed=notFoundEmbed)
                pass
            elif len(results)>0:
                await ctx.send(embed=embed)
                data=results
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
                    answer=f'{i+1}\n```{lang}\n {ans}```'
                    answerEmbed=discord.Embed(
                        # name="name",
                        description=answer,
                        colour=embedColour
                    )
                    await ctx.send(embed=answerEmbed)
                notGotEmbed=discord.Embed(
                title=":frowning2: Did Not Find Your Answer?",
                description=f'''[Search yourself]({searchurl})
                \nYou can also contribute to this by installing [codegrepper](https://www.codegrepper.com/) extension and marking an answer when you find it
                ''',
                colour=embedColour
                )
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


def setup(client):
    client.add_cog(CodeHelp(client))