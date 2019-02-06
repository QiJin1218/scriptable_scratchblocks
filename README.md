# Scriptable Scratchblocks
Generate Scratch Blocks png with Puppeteer.

## The Srcipt

The script will save the ScratchBlocks code as a png and save to the Downloads folder.

1. Specify your Scratchblocks code
```javascript
const block_code = '';
```
2. Run script
```javascript
node script.js
```

3. Scratchblocks output will be saved in the Downloads folder.

--

## Changing Download Directory

Change the download directory by un-commenting line 15
```javascript
await page._client.send('Page.setDownloadBehavior', 
{ behavior: 'allow', downloadPath: './scratchblocks_png/' });
```
Currently, changing the download directory sometimes causes the pictures to not save correctly.

--

## Dependencies

[Puppeteer](https://github.com/GoogleChrome/puppeteer)
[npm](https://github.com/npm/cli)

--
