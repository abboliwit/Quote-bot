const puppeteer = require('puppeteer');
var fs = require('fs');
var quotes =""

async function getquotes(url) {
  const browser = await puppeteer.launch({headless : false,defaultViewport: null});
  const page = await browser.newPage();
  await page.goto(url);
  await page.waitFor('.quoteText')
  quotes += await page.$$eval('.quoteText',rows =>{
    return rows.map(row => {
      return row.outerText+"\n \n";
    });
  })  
  
  const nexturl = await page.$$eval('.next_page',url =>{
    return url.map(string => {
      return string.getAttribute('href')
    }); 
  })
  console.log(nexturl)
  await browser.close();
  fs.appendFile('quotes.txt',quotes,function(err){if(err){throw err;}})
  console.log(quotes)
  quotes=""
  if(nexturl[0] != null){
  getquotes('https://www.goodreads.com'+nexturl[0])
}
 
  
  

};
async function getminion(url){
  const browser = await puppeteer.launch({defaultViewport: null});
  console.log('väntar på sidan')
  const page = await browser.newPage();
  await page.goto(url);
  await page.waitFor('body > div:nth-child(4) > div > ul > li:nth-child(1) > div.png_png.png_imgs > a > img')
  let imageHref = await page.$$eval('.png_png.png_imgs > a > img',sel => {
      return sel.map(string => {
        return string.getAttribute('src')
      }); ;
  });
  imageHref.forEach((link,index)=>{
    fs.appendFile('Link.txt',link+'\n',function(err){if(err){throw err;}})
  })

  await browser.close();
  console.log('Hämtade '+imageHref.length.toString()+' länkar')
}
getminion('http://pngimg.com/imgs/heroes/minions/')

