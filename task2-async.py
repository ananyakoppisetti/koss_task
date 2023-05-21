import time
import asyncio
import aiohttp

async def json(comic_id):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://xkcd.com/{comic_id}/info.0.json') as response:
            html= await response.text()
            with open(f'./asynchro_json/{comic_id}.json', 'w') as f:
                f.write(html)


# async def To_download(file,text):
#      async with aiofiles.open(file,'w') as f:
#           await f.write(text)
     



async def main():
        start= time.time() 

        tasks=[]
        for i in range(1,201):
            tasks.append(json(i))
            
        await asyncio.gather(*tasks) 

        time_taken = time.time() - start
        print('Time Taken {0}'.format( time_taken))

asyncio.run(main())


      

