const puppeteer = require('puppeteer');
const block_code = 'When%20This%20Sprite%20Clicked%0AWait%20[9]%20Secs%0APlay%20Sound%20[]%20Until%20Done%0A';
const base = 'http://scratchblocks.github.io/#?style=scratch3&script=';
const link = base + block_code;

(async () => {
  const browser = await puppeteer.launch({
  	headless : false
  });
  const page = await browser.newPage();
  const PNG_SELECTOR = '#export-png';
  await page.goto(link);
  // Redirect Download
  // await page._client.send('Page.setDownloadBehavior', { behavior: 'allow', downloadPath: './scratchblocks_png/' });
  await page.click(PNG_SELECTOR);
  setTimeout(() => { browser.close(); }, 300);
})();