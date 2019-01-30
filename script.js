const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://scratchblocks.github.io/#?style=scratch3&script=');
  await page.screenshot({path: 'google.png'});

  await browser.close();
})();