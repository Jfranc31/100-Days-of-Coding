// content.js
console.log('Content script executed!');
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'extractInfo') {
      const pageInfo = {
        title: document.title,
        url: window.location.href,
        // Add more properties as needed
      };
  
      chrome.runtime.sendMessage({ action: 'sendInfo', data: pageInfo });
    }
  });