# Quote-bot
Qoute bot är en AI som genererar citat baserad på på data från andra inspirerande citat. Men den skapar även bilder baserade på Minioner som den sedan lägger ihop och postar på [twitter](https://twitter.com/Jesusdaddy6). Citaten generas av en NLP(natural language processor) som läser av ordföljd menings byggnad och mer språkbaserade strukturer. Algoritmen skapar egna strukturer baserade på de citat som redan har hämtas in. Dessutom så skapas en bild baserat på minioner med hjälp av stylegan. Den har tränats upp genom att försöka skapa egna bilder som bedöms på likheten.Därefter så ändras vikterna inför nästa iteration. SLutligen så genereras ett citat och en bild som sedan läggs samman för att sedan bli postade på twitter. 
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
* [Skapa Minioner](https://colab.research.google.com/drive/1V1pZKiRDDPM_ITLF7Xuhh-qQa_fSpwBt?usp=sharing)- Här tränar vi vikterna för att skapa Minioner
* [Skapa citat](https://colab.research.google.com/drive/1JbndjII3nfG2BGXTWXOailEvpzqeEkl9?usp=sharing) - här tränas vikterna som skapar citaten

# Krav
gpt_2_simple ```pip install gpt_2_simple==0.7.1 ```

tensorflow 1.14.0 ```pip install tensorflow==1.14.0```

# Användning 
För att använda denna bot på ditt twitterkonto, så behövs ett [devkonto](https://developer.twitter.com/en/apply-for-access). Sedan byter man ut mina Client id och client secret mot ens egna i Twitter.py.Efter det är det bra att köra Twitter.py

# Problem och lösningar
## Heroku
Just Nu måste man manuellt köra filen på datorn för att generera bilder. Men det kan ändras genom att ladda upp och köra koden på Heroku.Tyvärr så är de nödvändiga filerna för stylegan allderes för stora och jag har ännu inte lyckats arbeta runt det problemet.
## Längd 
I början så vart lägden av citaten alldeles för långa och för många, de forstatte långt utan för bilden. Men jag löste detta genom att dela upp alla citat.Detta lyckades jag med då tränings filen jag skapade bestod hade två nya rader  mellan citaten, när programmet letade efter mönster så kopierade den då detta vilket resulterade i att de generaerade citaten vart separerade med två rader. Vilket var enkelt att identifiera via kod. Därefter för så delades varje rad upp i tre ord så att texten förblev inom bilden.

# Framtida framsteg
Jag skulle kunna försöka minimera storleken på style-GAN filen så att man kan automatisera processen genom att ladda upp all kod till heroku. Dessutom behöver vikten för att skapa minioner tränas mer så att bilderna blir bättre.
