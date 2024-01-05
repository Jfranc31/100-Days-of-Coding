// popup.js
console.log('Popup script executed!');
chrome.action.onClicked.addListener((tab) => {
    console.log('Button clicked!');
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: () => {
        chrome.runtime.sendMessage({ action: 'extractInfo' });
      },
    });
  });