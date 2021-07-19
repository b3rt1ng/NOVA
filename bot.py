import discord, timeit, random, datetime, caca, graph, os, time, json, re
version="2.4.1"
patchnote="**patchnote "+version+"**\n"+"- verouillage des entrées utilisateurs"+"\n"+"- foutre xd"
crew=caca.user()
try:
    crew.load()
except:
    print('no database found !')
def get_index(name):
    return crew.names.index(name)

def beg_msg(nom):
    n=random.randint(0,8)
    #-----------------------------------hugo spécial
    if nom=="Neokys#0755":
        if n==0:
            vanne = ["https://media.discordapp.net/attachments/558752088318803968/844997180536127518/evenement_paranormal.gif","ferme ta gueule ptn c'est un truc de ouf ça","mais tg on t'as dit !","envie de te dire ferme ta gueule mais je t'aime trop..."]
            n=random.randint(0,len(vanne)-1)
            return vanne[n]
    #-----------------------------------adrien spécial
    if nom=="Hazgaro#1362":
        if n==0:
            vanne = ["Attention, Adrien va chier un obélisque","adrien va oublier ses problèmes aux toilettes","Adrien part chialer dans les toilettes :sunglasses:"]
            n=random.randint(0,len(vanne)-1)
            return vanne[n]
    #-----------------------------------robin spécial
    if nom=="Roleb#4533":
        if n==0:
            vanne = ["y'a robin qui va chier un marathon là hein","met tes pieds par terre si tu va chier ou jsp quoi, j'ai jamais bu..."]
            n=random.randint(0,len(vanne)-1)
            return vanne[n]
    #-----------------------------------charly spécial
    if nom=="Charly#4408":
        if n==0:
            vanne = ["regardez le qui se trimbale avec sa petite calvoche pour aller faire un petit caca :heart_eyes:","dac vas-y petit cochon avec tes gros pecs là :yum: *petite claque au cul*"]
            n=random.randint(0,len(vanne)-1)
            return vanne[n]

    nom=nom[:-5]
    phrases = ["https://tenor.com/view/asain-throwing-up-em-gang-signs-gif-18505010","https://tenor.com/view/dog-puppy-cute-pet-gif-16224465","https://media.discordapp.net/attachments/456347479282286605/855212867111616533/image0.gif","https://tenor.com/view/hype-dance-excited-lets-go-oh-yeah-gif-17953674","https://tenor.com/view/okay-smile-ok-happy-gif-14150032","https://tenor.com/view/poggers-anime-poggers-pogger-kiss-poggers-kiss-gif-20187862","https://tenor.com/view/bruh-bruh-triggered-bruh-bttv-meme-gif-16887494","https://cdn.discordapp.com/emojis/823645762821947393.gif?v=1","https://tenor.com/view/notes-what-gif-11132970","https://tenor.com/view/family-guy-peter-griffin-bathroom-run-hurry-gif-15063908","ok lezgoo","dépèche toi j'ai pas ton temps...","top chrono "+nom+" dépèche toi, on à tous confiance en toi, tu peux le faire !","ahhhhh c'est cool, ça fait aux moins deux heures que t'es pas allé chié "+nom,nom+" tente le perfect ?","moi pisseur ? haha on me l'a pas faite depuis looooongtemps celle là. demande à mes potes si je cague pas, tu vas voir les réponses que tu vas te prendre, rien que la semaine passée, j'ai cagué donc chut ferme la pisseur de merde.","it's caca time for "+nom,"ce mec est un prédateur sexuel hein","c'est parti ma gazelle","bah lezgo en fait","c'est pas drôle mais je voudrais juste dire qu'adrien est une grosse salope à jouer à Death Stranding","je veux que ce soit hiroshima dans tes chiottes t'as compris ou bien","Chie sur la cuvette comme un vrai mec","Deux merdes au même endroit, une première","Cette fois ci, tu tentes le perfect !","J'en connait un qui va dunker avec son cul",nom+" n'a pas que des j**fs à déporter aujourd'hui","j'en connais un qui a le bobsleigh dans le dernier virage","Houlà, "+nom+" a un renoi qui tape au carreau","Alors, on a l'airbus en bout de piste ? (prhase proposée par charly)","mon srab "+nom+" fait ses bails dans les cabinets :sunglasses:","bah ou mais je m'en bas les couilles en fait, c'est pas pour être méchant "+nom+"...","c'est la porte du fond, cours "+nom,"vas-y "+nom+" dead moi ça","les mecs, y'a "+nom+" qui est parti cacater :note:",nom+" est parti chier", "devinez qui est-ce qui va chier ? bah c'est "+nom, "haha regardez ce sac a merde de "+nom+" qui part lacher sa cague de grosse victime","eh bah voilà il va encore chier",nom+" est encore parti **CAGUER** dans ses **TOILETTES**","oui oui allez casse toi faire tes trucs aux chiottes...","il va juste se branler hein...","je m'y attendais pas","gênant",nom+" pue la merde"]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

def end_msg_p1():
    phrases = ["bah dit donc, t'a mis", "eh beh,","ça va, t'as pris","sah,","**EUUUUU**","t'es un rapide toi,","bon du coup","oue bref","alors,","petit débrief champion:","ça c'est mon chieur,","wow,"]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

def random_compliment():
    phrases = ["il a pas le temps en fait","il est très fort","ma grand-mère ferait pas mieux","t'es juste un boss en fait","quel king haha chui mort :rofl:","je fais l'embrasser sur la bouche je crois..."]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

def random_pas_compliment():
    phrases = ["c'est nul","ça pue la merde","éclaté","bruh","tu passe ta vie là dedans ?","trouve un travail ptn...","c'est chaud","pas ouf"]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

def cancel_msg():
    phrases = ["quoi il a fait demis-tour le caca ?","comment t'as pu te tromper ? sans déconner !","t'es le plus gros boulet du serveur, je pèse mes mots...","mais je te déteste en fait ?","allez nique ta mère...","mais quel abruti tu fais..."]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

def con_msg(nom):
    phrases = ["bwaaaaaaaaaahahahah","wesh c'est quoi ça ?",":person_doing_cartwheel: "+str(nom)[:-5]+"\n"+":motorized_wheelchair: :woman_golfing: *l'intelligence*",":brain: = :poop:"]
    n=random.randint(0,len(phrases)-1)
    return phrases[n]

class saver:
    def __init__(self):
        self.last=[]
        self.name=''
        self.name2=''
        self.msg=''
    def save(self,msg):
        self.last.append(msg)
        if len(self.last)>2:
            self.last=self.last[1:]
    def save_name(self,nom):
        self.name=nom
    def save_name_2(self,nom):
        self.name2=nom
    def save_msg_location(self,message):
        self.msg=message
memory=saver()

class caguebot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        await client.change_presence(activity=discord.Game(name="cacabot v"+version))

    async def on_raw_reaction_add(self, payload):
        reactor=str(payload.member.name)
        message_reagit = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        cible=str((await client.get_channel(payload.channel_id).fetch_message(payload.message_id)).author)[:-5]
        if str(payload.emoji) == '🤝':
            premier,second='Null','Null_base'
            if reactor == 'Berting':
                premier = 'Antoine'
            if cible == 'Berting':
                second = 'Antoine'
            if reactor == 'Neokys':
                premier = 'Hugo'
            if cible == 'Neokys':
                second = 'Hugo'
            if reactor == 'Charly':
                premier = 'Charly'
            if cible == 'Charly':
                second = 'Charly'
            if reactor == 'Roleb':
                premier = 'Robin'
            if cible == 'Roleb':
                second = 'Robin'
            if reactor == 'Hazgaro':
                premier = 'Adrien'
            if cible == 'Hazgaro':
                second = 'Adrien'
            if cible == reactor:
                second = 'Null'
            if second == "Null":
                await message_reagit.reply(premier+" a dabé Ñ̵̛̥͠ư̶͎̻͌l̴͉̫͊̐̏l̵̙̒ (il s'est dabé tout seul)",file=discord.File("./dab/"+premier+"_"+second+".jpg"))
            elif second == "Null_base":
                False
            else:
                await client.get_channel(payload.channel_id).send(premier+" a dabé "+second,file=discord.File("./dab/"+premier+"_"+second+".jpg"))

    async def on_message(self, message):
        memory.save(message)
        if message.author.id == self.user.id:
            if "69" in message.content:
                await message.add_reaction('<:sourireencoin:864904077372424192>')
            return True

        if str(message.author) in crew.names:
            True
        # response----------------------------------------------------------------
        p=random.randint(0,1)
        if p == 0:
            if "quoi" in message.content:
                if message.content.startswith('!c vote') == True:
                    True
                else:
                    i=random.randint(0,3)
                    if i == 0:
                        avariable_sounds=[]
                        for subdir, dirs, files in os.walk('./feur'):
                            for file in files:
                              avariable_sounds.append(file)
                        n=random.randint(0,len(avariable_sounds)-1)
                        await message.channel.send(file=discord.File("./feur/"+avariable_sounds[n]))
                    else:
                        await message.channel.send("feur")
            if "Quoi" in message.content:
                if message.content.startswith('!c vote') == True:
                    True
                else:
                    i=random.randint(0,3)
                    if i == 0:
                        avariable_sounds=[]
                        for subdir, dirs, files in os.walk('./feur'):
                            for file in files:
                              avariable_sounds.append(file)
                        n=random.randint(0,len(avariable_sounds)-1)
                        await message.channel.send(file=discord.File("./feur/"+avariable_sounds[n]))
                    else:
                        await message.channel.send("feur")
            if "kwa" in message.content:
                if message.content.startswith('!c vote') == True:
                    True
                else:
                    await message.channel.send("feuw")
        if "fou" in message.content:
            if message.content.startswith('!c vote') == True:
                True
            else:
                await message.channel.send("tre")
        if "bougnoul" in message.content:
            await message.reply('comment ça "'+message.content+'" ?',file=discord.File('./spetial/racismo.mp4'))
        if "arabe" in message.content:
            await message.reply('comment ça "'+message.content+'" ?',file=discord.File('./spetial/racismo.mp4'))
        if "nigga" in message.content:
            await message.add_reaction('😬')
        if "negro" in message.content:
            await message.add_reaction('😬')
        if "negre" in message.content:
            await message.add_reaction('😬')
        if "noir" in message.content:
            await message.add_reaction('😬')
        if "69" in message.content:
            await message.add_reaction('<:sourireencoin:864904077372424192>')
        phrase=message.content.split()
        result=[]
        for i in range(len(phrase)):
            x = re.search('di', phrase[i])
            if(x!=None):
                if len(phrase[i][2:])>3:
                    if phrase[i][:2]=="di":
                        result.append(phrase[i][2:])
            else:
            	False
        if len(result)>0:
            string=''
            for i in range(len(result)):
                if i==0:
                    string=string+result[i]
                elif i==len(result)-1:
                    string=string+' et '+result[i]
                else:
                    string=string+", "+result[i]
            await message.reply(string)

        # response----------------------------------------------------------------
        if message.content.startswith('!c'):
            if message.content == ('!c'):
                index = get_index(str(message.author))
                if crew.status[index]==False:
                    crew.status[index]=True
                    crew.start[index] = timeit.default_timer()
                    print(message.author, "débute sa cague")
                    crew.save()
                    await message.reply(beg_msg(str(message.author)), mention_author=True)
                else:
                    crew.status[index]=False
                    crew.stop[index] = timeit.default_timer()
                    print(message.author, "fini sa cague")
                    crew.amount[index]=crew.amount[index]+1
                    if 67 <= round(crew.stop[index] - crew.start[index]) <= 71:
                        print(message.author,"a fait",round(crew.stop[index] - crew.start[index]),"on arrondi a 69")
                        temps=69
                    else:
                        temps=round(crew.stop[index] - crew.start[index])
                    info = []
                    info.append(temps) #temps de cague
                    info.append(datetime.datetime.now().strftime('%A')) #jour de cague
                    info.append(datetime.date.today().month) #mois de cague
                    crew.cague_data[index].append(info)
                    crew.save()
                    await message.reply(end_msg_p1()+' '+str(temps)+" secondes pour caguer, ça fait "+str(crew.amount[index])+" cacas", mention_author=True)
            if message.content == ('!c stats nul'):
                print(message.author, "demande ses stats moches")
                index = get_index(str(message.author))
                graph.render_weeks(crew.cague_data,str(message.author),index)
                await message.channel.purge(limit=1)
                await message.channel.send(file=discord.File('temp.png'))
                os.remove("temp.png")
            if message.content == ('!c stats time'):
                print(message.author, "demande ses stats de temps")
                index = get_index(str(message.author))
                graph.render_moy(crew.cague_data,str(message.author),index)
                await message.channel.purge(limit=1)
                await message.channel.send(file=discord.File('temp.png'))
                os.remove("temp.png")
            if message.content == ('!c stats'):
                index = get_index(str(message.author))
                print(message.author, "demande ses stats")
                graph.render_round_weeks(crew.get_data(no_string=True),index)
                await message.channel.purge(limit=1)
                await message.channel.send(file=discord.File('temp.png'))
            if message.content == ('!c stats all'):
                index = get_index(str(message.author))
                print(message.author, "veux voir les stats globales")
                graph.render_round_weeks_everyone(crew.get_data(no_string=True))
                await message.channel.purge(limit=1)
                await message.channel.send(file=discord.File('temp.png'))
                os.remove("temp.png")
            if message.content == ('!c save'):
                await message.channel.purge(limit=1)
                await message.channel.send("envoi du fichier data.txt dans "+str(message.channel))
                await message.channel.send(file=discord.File('data.txt'))
            if message.content == ('!c save_bot'):
                await message.channel.purge(limit=1)
                await message.channel.send("envoi du fichier bot.py dans "+str(message.channel))
                await message.channel.send(file=discord.File('bot.py'))
            if message.content == ('!c moyenne'):
                print(message.author, "veux sa moyenne")
                if round(crew.get_cague_moy(get_index(str(message.author)))) <= 90:
                    await message.reply("tu met en moyenne "+str(round(crew.get_cague_moy(get_index(str(message.author)))))+" secondes à chier, "+random_compliment(), mention_author=True)
                else:
                    await message.reply("tu met en moyenne "+str(round(crew.get_cague_moy(get_index(str(message.author)))))+" secondes à chier, "+random_pas_compliment(), mention_author=True)
            if message.content == ('!c shutdown'):
                if str(message.author) == "Berting#6337":
                    print('shuting down system')
                    await message.channel.send("c'est l'heure de nehess !")
                    os.system('sudo shutdown now')
                else:
                    await message.channel.send("t'as pas le droit de faire ça.")
            if message.content == ('!c oops'):
                print(message.author, "s'est trompé")
                crew.del_last(get_index(str(message.author)))
                crew.save()
                await message.reply(cancel_msg(), mention_author=True)
            if message.content == ('!c help'):
                print(message.author, "veux de l'aide")
                embed=discord.Embed(title="Voilà la liste de toutes les commandes disponibles:", color=0x00ff33)
                embed.set_thumbnail(url="https://www.pngkey.com/png/full/190-1909373_poop-poop-emoji-emoji-movie.png")
                embed.add_field(name="!c", value="Préfixe de base, débute/termine votre session cague.", inline=False)
                embed.add_field(name="stats", value="Affiche le graphique de tes cacas (par semaine), et d'ailleur stats à l'envers ça fait kayak haha", inline=False)
                embed.add_field(name="stats time", value="Affiche le graphique des temps par cacas", inline=False)
                embed.add_field(name="stats all", value="Affiche le graphique des cacas de tout le monde", inline=False)
                embed.add_field(name="top", value="Affiche le podium des cagueurs", inline=False)
                embed.add_field(name="oops", value="Ça arrive à tout le monde d'aller chier puis en fait, ça sort pas... vraiment à tout le monde... sac à merde", inline=False)
                embed.add_field(name="moyenne", value="Envoie le temps moyen de la totalité de tes caca petit bg va", inline=False)
                embed.add_field(name="time *nombre*", value="Te permet de changer le temps de ta dernière cague", inline=False)
                embed.add_field(name="vote *question*", value="Envoie une question avec deux options de réaction (oui ou non)", inline=False)
                embed.add_field(name="status *phrase* (option)", value="permet de changer le status du bot les options sonts a mettre entre parenthèses et sont 'play','watch','listen'", inline=False)
                embed.add_field(name="rappel", value="la commande existe pas, j'ai trop la flamme de la faire", inline=False)
                embed.add_field(name="règle", value="si tu connais pas les règles, tu tape ça...", inline=False)
                embed.add_field(name="nul", value="zebi des fois y'a plein de message de merde qui sont envoyés sur ce discord... bah go le dire !", inline=False)
                embed.add_field(name="vibe *id*", value="montre moi que je tu vibre ! (envoie une message de vibe par défaut, tu peux mettre l'id d'un message dans ton message pour que le bot réponde à celui-ci)", inline=False)
                embed.add_field(name="gay *id*", value="pareil des fois y'a des trucs super gay qui passent par là... ça se remarque.", inline=False)
                embed.add_field(name="pogger", value="WOOOOOOOOOOOOOO WAAAAAAAAAAAA WOUUUUUUUUUUUUUUU", inline=False)
                embed.add_field(name="ool 🤔", value="c'est cool ce que tu viens de dire dit donc ! (non)", inline=False)
                embed.add_field(name="patchnote", value="comme ça on peux savoir ce qui est nouveau dans la version "+version+" c'est pas super ?", inline=False)
                embed.add_field(name="on 🤔", value="ça arrive à tout le monde de dire un truc con, mais parfois c'est important de le faire remarquer. De manière construite et intelligente bien évidement...", inline=False)
                embed.add_field(name="playlist", value="la superbe playlist d'antoine qui est trop bien", inline=False)
                embed.set_footer(text="version "+version)
                await message.reply(embed=embed)
            if message.content == ('!c top'):
                print(message.author, "veux le top")
                noms=crew.names
                nombre=crew.amount
                sorted_nombre=sorted(nombre)[::-1]
                build=[]
                for j in range(len(sorted_nombre)):
                    for i in range(len(nombre)):
                        temp=[]
                        if nombre[i] == sorted_nombre[j]:
                            temp.append(sorted_nombre[j])
                            temp.append(noms[i])
                            build.append(temp)
                embed=discord.Embed(title="poduim du cul:", color=0x00ff33)
                for i in range(len(build)):
                    if i == 0:
                        embed.add_field(name="⠀", value=":first_place: "+build[i][1][:-5]+" avec "+str(build[i][0])+" cagues", inline=False)
                    elif i == 1:
                        embed.add_field(name="⠀", value=":second_place: "+build[i][1][:-5]+" avec "+str(build[i][0])+" cagues", inline=False)
                    elif i == 2:
                        embed.add_field(name="⠀", value=":third_place: "+build[i][1][:-5]+" avec "+str(build[i][0])+" cagues", inline=False)
                await message.reply(embed=embed)
            if message.content.startswith('!c time') == True:
                n=[int(s) for s in message.content.split() if s.isdigit()]
                n=n[0]
                index = get_index(str(message.author))
                old=crew.cague_data[index][len(crew.cague_data[index])-1][0]
                crew.cague_data[index][len(crew.cague_data[index])-1][0]=n
                new=crew.cague_data[index][len(crew.cague_data[index])-1][0]
                crew.save()
                await message.channel.send("ok "+str(message.author)[:-5]+" ta dernière cague passe de "+str(old)+" à "+str(new)+".")
            if message.content.startswith('!c vote') == True:
                await message.channel.purge(limit=1)
                msg = await message.channel.send(message.content[7:])
                await msg.add_reaction('☑️')
                await msg.add_reaction('❌')
            if message.content.startswith('!c status') == True:
                msg=message.content[9:]
                argument = re.findall(re.compile(".*?\((.*?)\)"), message.content[9:])
                print(argument)
                if message.content==('!c status'):
                    await message.add_reaction('⚠️')
                    await client.change_presence(activity=discord.Game(name="cacabot v"+version))
                else:
                    await message.channel.purge(limit=1)
                if argument == []:
                    argument = 'play'
                elif len(argument)>1:
                    argument = 'play'
                else:
                    argument=argument[0]
                if argument=='play':
                    await client.change_presence(activity=discord.Game(name=re.sub(r"\([^()]*\)", "", msg)))
                if argument=='listen':
                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=re.sub(r"\([^()]*\)", "", msg)))
                if argument=='watch':
                    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=re.sub(r"\([^()]*\)", "", msg)))
            if message.content == ('!con'):
                cible=memory.last[0]
                print(message.author, "trouve que",cible.author,"a dit une connerie")
                await message.channel.purge(limit=1)
                avariable_sounds=[]
                for subdir, dirs, files in os.walk('./con_sound'):
                    for file in files:
                      avariable_sounds.append(file)
                emojis=['🤦🏻','🤦🏼','🤦🏽','🤦🏾','🤦🏿','🤦🏻‍♂️','🤦🏼‍♂️','🤦🏽‍♂️','🤦🏾‍♂️','🤦🏿‍♂️','🤦‍♀️','🤦🏻‍♀️','🤦🏼‍♀️','🤦🏽‍♀️','🤦🏾‍♀️','🤦🏿‍♀️']
                n=random.randint(0,len(avariable_sounds)-1)
                await cible.reply(con_msg(cible.author), file=discord.File("con_sound/"+avariable_sounds[n]), mention_author=True)
                for i in range(len(emojis)):
                    await cible.add_reaction(emojis[i])
            if message.content == ('!c rappel'):
                await message.reply("trop trop trop la flemme", mention_author=True)
            if message.content == ('!c regle'):
                await message.reply("les règles sont simples: le caca débute une fois les fesses posées sur la cuvette et se termine une fois la chasse tirée.\n *remarque: ne pas s'essuyer les fesses et quand même tirer la chasse est autorisé mais fait de toi un très mauvais être humain.*", mention_author=True)
            if message.content == ('!c règle'):
                await message.reply("les règles sont simples: le caca débute une fois les fesses posées sur la cuvette et se termine une fois la chasse tirée.\n *remarque: ne pas s'essuyer les fesses et quand même tirer la chasse est autorisé mais fait de toi un très mauvais être humain.*", mention_author=True)
            if message.content == ('!c nul'):
                cible=memory.last[0]
                print(message.author, "trouve que",cible.author,"a mit un message nul")
                await message.channel.purge(limit=1)
                avariable_sounds=[]
                for subdir, dirs, files in os.walk('./not_funny'):
                    for file in files:
                      avariable_sounds.append(file)
                n=random.randint(0,len(avariable_sounds)-1)
                await cible.reply("😐😐😐😐😐",file=discord.File("not_funny/"+avariable_sounds[n]), mention_author=True)
            if message.content == ('!c pogger'):
                print(message.author, "est en etat de pog")
                await message.channel.purge(limit=1)
                avariable_sounds=[]
                for subdir, dirs, files in os.walk('./poggers'):
                    for file in files:
                      avariable_sounds.append(file)
                n=random.randint(0,len(avariable_sounds)-1)
                await message.channel.send("**POGGERS**",file=discord.File("poggers/"+avariable_sounds[n]), mention_author=True)
            if message.content.startswith('!c gay') == True:
                try:
                    message_id = int(re.search(r'\d+', message.content[7:]).group())
                    cible=message.channel.get_partial_message(message_id)
                    await message.channel.purge(limit=1)
                    await cible.add_reaction('😬')
                    avariable_sounds=[]
                    for subdir, dirs, files in os.walk('./gay'):
                        for file in files:
                          avariable_sounds.append(file)
                    n=random.randint(0,len(avariable_sounds)-1)
                    await cible.reply(file=discord.File("gay/"+avariable_sounds[n]), mention_author=True)
                except:
                    await message.channel.purge(limit=1)
                    avariable_sounds=[]
                    for subdir, dirs, files in os.walk('./gay'):
                        for file in files:
                          avariable_sounds.append(file)
                    n=random.randint(0,len(avariable_sounds)-1)
                    await message.channel.send(file=discord.File("gay/"+avariable_sounds[n]), mention_author=True)
            if message.content.startswith('!c vibe') == True:
                try:
                    message_id = int(re.search(r'\d+', message.content[8:]).group())
                    cible=message.channel.get_partial_message(message_id)
                    await message.channel.purge(limit=1)
                    await cible.reply(":star::star2::sparkles::star::star2::sparkles::star::star2:",file=discord.File("spetial/vibe.mp4"), mention_author=True)
                except:
                    await message.channel.purge(limit=1)
                    await message.channel.send(":star::star2::sparkles::star::star2::sparkles::star::star2:",file=discord.File("spetial/vibe.mp4"), mention_author=True)
            if message.content == ('!c patchnote'):
                print(message.author, "veux les nouveautés")
                await message.channel.purge(limit=1)
                await message.channel.send(patchnote)
            if message.content == ('!cool'):
                await message.channel.purge(limit=1)
                await memory.last[0].reply(file=discord.File("./spetial/cool.mp4"), mention_author=True)
            if message.content == ('!c playlist'):
                await message.reply("https://open.spotify.com/playlist/446BkBZpDg5VOOLtAriWiq?si=41ab4d67a1bc4ca1", mention_author=True)

client = caguebot()
client.run("ODQ2MzI0MDgxNjgzMjAyMDY4.YKt2uQ.10KYXgH7QP6Oj16nhOUGv2s01kc")
