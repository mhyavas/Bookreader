import string
import discord
from discord.ext import commands
import config

token=config.token
client=commands.Bot(command_prefix= '.')

day=open('hour_cal.txt','r+')
day_count=day.read()
day.close()
saat=open('hour.txt','r+')
saat_str=saat.read()
saat_int=int(saat_str)
newsaat_int= saat_int+1
saat.close()
saat_w=open('hour.txt','w')
saat_w.write(str(newsaat_int))
saat_w.close()
if newsaat_int==24:
    newsaat_int=0
    saat_w=open('saat.txt','w')
    saat_w.write(str(newsaat_int))
    saat_w.close()
    h_w=open('hour_cal.txt','r+')
    h_w_str=h_w.read()
    h_w.close()
    int_hw=int(h_w_str)
    new_int_hw=int_hw + 1
    h_w2=open('hour_cal.txt','w')
    h_w2.write(str(new_int_hw))



def tt():
    filename='book.txt'

    f=open(filename,"r")
    strinng=f.read()
    split_sentences=[]
    without_n=[]
    quotes1=strinng.split("\"")
    char_num=[]
    for i in quotes1:
        a=i.replace('\n',"")
        without_n.append(a)
    #print(len(without_n))

    fileObj=open(r"char.txt","r+")
    b=fileObj.read()
    int_b=int(b)
    fileObj.close()
    if len(without_n[int_b])>280:
        lg=open('long_char.txt','r')
        str_pos=lg.read()
        lg.close()
        pos=int(str_pos)
        twet=without_n[int_b].split('. ')
        if pos==len(twet):
            new_b=0
            fl_wr=open("long_char.txt","w")
            fl_wr.write(str(new_b))
            fl_wr.close()

            new_int=int_b+1
            fl_wr=open("char.txt","w")
            fl_wr.write(str(new_int))
            fl_wr.close()

        else:
            msg=twet[pos]
            lg_add=open('long_char.txt','w')
            new_pos=pos +1
            lg_add.write(str(new_pos))
            lg_add.close()

            return msg
    elif len(without_n[int_b])<2:
        new_b=int_b+1
        fl_wr=open("char.txt","w")
        fl_wr.write(str(new_b))
        fl_wr.close()
        return "."
    else:
        msg=without_n[int_b]
        new_b=int_b+1
        fl_wr=open("char.txt","w")
        fl_wr.write(str(new_b))
        fl_wr.close()
        return msg


@client.event
async def on_ready():
    #print('bot ready')
    channel=client.get_channel(config.channelID)
    if False:
        pass
    else:
        try:
            await channel.send("Day: "+day_count+""+tt())
            await client.close()
        except Exception as e:
            print(e)
            await client.close()

client.run(token)
