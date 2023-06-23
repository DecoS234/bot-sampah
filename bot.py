


import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Halo ini bot untuk mengutamakan solusi sampah , silahkan pilih antara 1 , 2 ,3 !')
    elif  message.content.startswith('$1'):
        await message.channel.send(f'Jangan nyampah')
    elif message.content.startswith('$2'):
        await message.channel.send(f'Solusi pengurangan sampah kedua adalah mengurangi penggunaan plastik sekali pakai. Dengan menggunakan wadah makanan yang dapat digunakan berulang kali dan membawa tas belanja sendiri, kita dapat mengurangi limbah plastik yang dihasilkan')
    elif message.content.startswith('$3'):
        await message.channel.send(f'Solusi pengurangan sampah ketiga adalah kompos. Dengan mengomposkan sisa makanan dan bahan organik lainnya, kita dapat mengurangi jumlah sampah yang berakhir di tempat pembuangan akhir dan juga menghasilkan pupuk alami yang berguna untuk tanaman')

client.run("Your token discord okay")

