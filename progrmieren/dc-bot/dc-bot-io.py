import discord
from launchmod import launchapp as launch
class botclient(discord.Client):
    async def on_ready(self):#login
        print("loged in")
    async def on_message(self,message):#if event message sendhap pend:
        print("new message by",message.author,"wich contains",message.content)
        if message.author==client.user:
            return
        if message.content.startswith("bot"):
            command=message.content.split(" ")[1]
            content=str(message.content)[4:len(str(message.content))]
            await message.channel.send(":\n"+str(process.launchmodules(command,content)))
class process():
    def launchmodules(cmdinp:str,continp:str):
        print(cmdinp)
        if "help" in cmdinp[0:5]:
            return "random      |givees random\n test test"
        if cmdinp=="random":
            return launch("random",continp)
        return "unknown command: "+str(cmdinp)
client = botclient()
client.run("")
