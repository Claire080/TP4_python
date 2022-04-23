import os
from dotenv import load_dotenv
from discord.ext import commands
from argparse import ArgumentParser, Namespace


load_dotenv(dotenv_path="config")

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur")

    async def on_message(self,message):
        if(message.content.lower()=="ping"):
            await message.channel.send("pong",delete_after=5)


    def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
        return parser.parse_args()

doc_bot=DocBot()
doc_bot.run(os.getenv("TOKEN"))        