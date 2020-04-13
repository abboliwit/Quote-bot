# Quote-bot
Qoute bot är en AI som genererar citat baserad på på data från andra inspirerande citat. Men den skapar även bilder baserade på Minioner som den sedan lägger ihop och postar på [twitter](https://twitter.com/Jesusdaddy6)
# Filer
## Heroku
* /Tweet.py- denna fil är själva boten som lägger upp tweets
## get_qoutes
* /raw- denna mapp innehåller alla bilder på Minioner som har hämtas
* Link.txt - all Länkar till minion bilderna
* img_download.py - hämtar bilderna baserat på innehållet från Link.txt
* index.js - Ett puppeter script som hämtar citat [här](https://www.goodreads.com) och Minioner [här](http://pngimg.com/imgs/heroes/minions/)
* quotes.txt - här sammals all citat som samlats från index.js alla citat delas upp av en "\n\n"
## Colab
* [Skapa Minioner](https://colab.research.google.com/drive/1V1pZKiRDDPM_ITLF7Xuhh-qQa_fSpwBt#scrollTo=094lgkW5rWOd)- Här tränar vi vikterna för att skapa Minioner
* [Skapa citat](https://colab.research.google.com/drive/1JbndjII3nfG2BGXTWXOailEvpzqeEkl9#scrollTo=2RJfgRriWIbT) - här tränas vikterna som skapar citaten

# Krav
gpt_2_simple ```pip install gpt_2_simple==0.7.1 ```

tensorflow 1.14.0 ```pip install tensorflow==1.14.0```

# Användning 
För att använda denna bot på ditt twitterkonto, så behövs ett [devkonto](https://developer.twitter.com/en/apply-for-access). Sedan byter man ut mina Client id och client secret mot ens egna i Twitter.py.Efter det är det bra att kör Twitter.py

# Problem och lösningar
## Heroku
Just Nu måste man manuellt köra filen på datorn för att generera bilder. Men det kan ändras genom att ladda upp och köra koden på Heroku.Tyvärr så är de nödvändiga filerna för stylegan allderes för stora och jag har ännu inte lyckats arbeta runt det problemet.
## Längd 
I början så vart lägden av citaten alldeles för långa och för många, de forstatte långt utan för bilden. Men jag löste detta genom att della upp alla citat för att sedan dela upp varje rad i tre ord. Så texten förblev inom bilden.

# Framtida framsteg
Jag skulle kunna klura ut ett sätt att få upp koden på heroku så att den postar bilder för alltid. Dessutom behöver vikten för att skapaminioner tränas mer.
