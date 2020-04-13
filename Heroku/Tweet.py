# authenticerings koder för twitter api
c_k = '2qQAPzxJxFlQ8B0POiF86yseM'
c_s = '6Bk3tQj6JLrP0obr5czAgqxvT0myk8LIRQwpCyp5hfkDCokzpu'
a_k = '1220610611664560130-miL6QjqLiAMdh9wrQc3RrzsKw8a0Rp'
a_s = 'S2pb9Plgbq93DURNCuRkivBLJwfnCKzmAeCclGgKMLr00'


import gpt_2_simple as gpt2
import tweepy
import time
import random
import tarfile
import requests
import os
from datetime import datetime, timedelta
import cv2
image_path = "/minion.png"namnet på filen som kommer skapas
dir_path = os.getcwd() #detta hämtar file directorien som filen körs i
filepath="checkpoint_runtwitter.tar"# paths till vikterna i min gDrive
filepath_stylegan = "start.pkl"
googefileid_stylegan = "1-qg1whOjTQvSovKR55m03n4LBxAz5ER2"# id till de filerna
googefileid= "1jyTBUmZ9EZaSG_TwopmHvCLnYGnSqZq7"

def extract():#extarherar tar filer
    with tarfile.open(filepath, 'r') as tar:
        tar.extractall()
    os.remove(filepath)
    print("File",filepath, "Removed!")

#authenticerar twitter api 
auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_k,a_s)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    
except:
    print("Error during authentication")



def download_file_from_google_drive(id, destination):# laddar ned filer från gDrive baserat på deras id och file path
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)
print("downloading")#laddar ned filerna
download_file_from_google_drive(googefileid_stylegan,filepath_stylegan)
download_file_from_google_drive(googefileid,filepath)
print("extracting")
extract()# extraherar dem
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='runtwitter')#laddar in vikterna för att skapa text

# ett par prefixer som Ai ska basera texten på
prefixes= ["Dogs","", "Climate","Bless", "Climate", "Sweden","Spets","Chuck Norris","","","#Winning","","","#Champ","","","Losing","#Memes"]

def createImage():#skapar en bild baserat på den tränade vikten och returerar sant om det går bra
  # idealt så skulle pip kunna hämta repositories men nu fungerar inte detta på min dator >:(
  #os.system('python '+dir_path+'/stylegan/invoke.py --model_file "'+dir_path+'/start.pkl" --output_file "'+dir_path+'/minion.png"')# kör filen som genererar bilder
  try:
    os.system('python "C:/Users/s8oliwit/Documents/stylegan-pokemon-master/stylegan-pokemon-master/stylegan/invoke.py" --model_file "./start.pkl" --output_file '+image_path)
    return True
  except:
      print("image failed")
      return False
def createtweet():#genererar text av vikter
    temp= random.randint(7,9)/10
    print(temp)
    prefix= prefixes[ random.randint(0,len(prefixes))]# hämtar en random prefix från listan ovan
    textlength=  random.randint(35,280-len(prefix))# bestämmer textens längd
    print(textlength)
    text= gpt2.generate(sess,# skapar en lista av genererade texter
            run_name='runtwitter',
            length= textlength,
            temperature=temp,
            # top_k=40,
            prefix=prefix,
            # nsamples=1,
            # batch_size=1,
            return_as_list=True
            )
            
    text= text[0]#tar första texten
    print(len(text),text)
    text= text[0:280-len(prefix)]# förkortarden
    text =text.split("\n \n")# delar den så att endast ett citat blir i text[0]
    # \n \n fungerar eftersom i tränings datan så delas alla citat upp av två rad byten och det har då det neutrala nätverket upptäck och återskapat
    print("  ")
    print(text[0])
    space = 0
    newtext=""
    font_index = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ \n"# opencv fonten fungerar endast på dessa figurer
    for letter in text[0]:# for loopen sätter in ny rad för vart tredje ord så att texten inte hamnar utanför
        if letter == " ":
            space+=1
        if space == 3:
            space =0
            newtext+="\n"
        elif letter in font_index:# checkar att symbolern är tillåten
            newtext+=letter
    return newtext,prefix

def createMedia():#skapar bild med text och returerar prefixen för texten 
    pic = createImage()
    text = createtweet()
    while pic ==False:# om bilden misslyckas så försöker den igen
        pic= createImage()
    while len(text)<10:# om texten blir för kort så försöker den igen
        text,prefix = createtweet()
    image = cv2.imread(image_path)
    y0, dy = 100, 60
    for i, line in enumerate(text.split('\n')):#opencv kan inte hantera \n så for loopen spiltar stringen och fixar det ändå
        y = y0 + i*dy
        cv2.putText(image, line, (100, y ), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
    cv2.imwrite('quote.png',image)#sparar bilden med text
    media = api.media_upload("quote.png")skapar media formatet som kan laddas upp i twitter apin
    return media, prefix
    
def post_tweet(now):
    try:
        media,tweet= createMedia()# skapar bilden
        post_result = api.update_status(status=tweet, media_ids=[media.media_id])#laddar uppden med bild textens prefix
        print('Completed posting tweet at ', now)
    except:
        print('tweet failed')

while True: # while loopen väntar i en viss tid mellen 50min till 120min   
    now = datetime.now()
    post_tweet(now)
    sleeptime= random.randint(3000,7200)
    now_plus = now + timedelta(seconds=sleeptime)
    print("Next tweet will be in ",str(timedelta(seconds=sleeptime)), " at " ,now_plus )
    time.sleep(sleeptime)
