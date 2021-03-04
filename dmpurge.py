import discord
import asyncio

class Client(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.token = "" #token goes there in between the speech marks

    async def on_connect(self):
        for friend in self.user.friends:
            if friend.id != 1:
                channel = await self.fetch_user(friend.id)
                print(channel)
                async for msg in channel.history(limit=None):
                    if msg.author == self.user:
                        try:
                            await msg.delete()
                            await asyncio.sleep(1)
                        except:
                            pass

        print("Finished")

if __name__ == "__main__":
    client = Client()
    client.run(client.token, bot=False)
