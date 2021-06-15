# urlshortener

a pretty bad easy to use url shortener

## Running

For max convenience, and to have everything setup easily, deploy on railway \/

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fzeromomentum121%2Furlshortener&plugins=redis&envs=PASSWORD&optionalEnvs=PASSWORD&PASSWORDDesc=your+custom+password+for+the+url+shortener)

If you want to do stuff manually, you are kinda on your own tbh, I have mine on railway, but it might be something like this

- Install Python3 / Redis
- `python3 -m pip install -r requirements.txt`
- Set environment variables for redis (the names should be self explanatory)
  - REDISHOST 
  - REDISPORT
  - REDISPASSWORD
- start it
- profit???

my instance is https://s.zeromomentum.me
