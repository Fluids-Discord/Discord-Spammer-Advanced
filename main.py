import os, random, string, keep_alive
from discord.ext import commands, tasks

version = 'v2.7.4'

user_token = os.environ['user_token']
spam_id = os.environ['spam_id']

client = commands.Bot(command_prefix="&")
intervals = [2.0, 2.1, 2.2, 2.3, 2.4]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(string.ascii_letters+string.digits,50)*20))

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()
@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')

keep_alive.keep_alive()
client.run(f"{user_token}")