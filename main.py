
import asyncpixel
import asyncio

thefile = open(r'C:\Users\carso\.lunarclient\logs\launcher\renderer.log')

apikey = '9cbaf94e-acd1-4b21-96bf-cfc4cdc7a541'

#You may notice i put big ugly code into functions
def star(player):
  return str(str(player.raw).split( "'skywars_you_re_a_star': ",1)[1]).split(',',1)[0] 
  


fstats = open('./stats.txt','w')


async def main(player):
  hypixel = asyncpixel.Hypixel(apikey)
  ign = await hypixel.uuid_from_name(player)
  _player = await hypixel.player(ign)
  swstats = str('Kills: '+ str(_player.stats.skywars.kills)+', Wins: ' + str(_player.stats.skywars.wins) + ', KD: ' + str(round(_player.stats.skywars.kills_per_death,2))+ ', WL: ' + str(round(_player.stats.skywars.wins_per_lose,2)))
  fstats = open('stats.txt','w')
  stats_ = str(_player.playername+': '+star(_player)+' star, '+str(swstats))
  print(stats_)
  
  
  fstats.write(str(stats_))
  fstats.close
  await hypixel.close()




while True:
    thefile.seek(0,2)
    line = thefile.readline()
    if "!sw " in line:
        asyncio.run(main(line.split('!sw ',1)[1]))

    

