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
getquotes('https://www.goodreads.com/quotes/tag/inspirational?page=88')

console.log(quotes.length)
