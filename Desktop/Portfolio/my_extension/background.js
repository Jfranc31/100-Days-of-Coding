// background.js
chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension Installed');
  });
  
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log('Message received:', request);
    if (request.action === 'sendInfo') {
      const extractedInfo = request.data;
      console.log('Extracted Info:', extractedInfo);
  
      chrome.tabs.create({ url: chrome.runtime.getURL('another_page.html') }, (tab) => {
        console.log('New tab created:', tab);
  
        chrome.scripting.executeScript({
          target: { tabId: tab.id },
          function: (info) => {
            console.log('Script executed in the new tab:', info);
            chrome.runtime.sendMessage({ action: 'displayInfo', data: info });
          },
          args: [extractedInfo],
          // Handle errors
          onError: (error) => {
            console.error('Script execution error:', error);
            // Handle the error gracefully, maybe inform the user
          },
        });
      });
    }
  });