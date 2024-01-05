// another_page.js
console.log('Content script executed!');
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'displayInfo') {
      const extractedInfo = request.data;
      // Display the extracted information on the page
      document.getElementById('info').innerText = JSON.stringify(extractedInfo, null, 2);
    }
});