const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
  	headless: false,
  });
  const page = await browser.newPage();
  const PNG_SELECTOR = '#export-png';
  await page.goto('http://scratchblocks.github.io/#?style=scratch3&script=test');
  await page._client.send('Page.setDownloadBehavior', { behavior: 'allow', downloadPath: './scratchblocks_png/' });
  await page.click(PNG_SELECTOR);
  setTimeout(() => { browser.close(); }, 50);
  // await browser.close();
})();