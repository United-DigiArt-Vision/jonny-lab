/**
 * X Thread Poster — Paste-basiert
 * 
 * Dieses Script wird als EINE evaluate-Aktion im Browser ausgeführt.
 * Es fügt alle Tweets in den X Compose-Dialog ein und postet sie.
 * 
 * USAGE: 
 * 1. Browser auf https://x.com/compose/post öffnen
 * 2. Dieses Script als evaluate() ausführen mit tweets-Array
 * 3. Wartet automatisch und klickt "Post all"
 * 
 * Der Aufrufer (Balerion) muss:
 * - Die Thread-Datei parsen
 * - tweets[] Array bauen  
 * - Dieses Script mit den Tweets als evaluate() ausführen
 */

// This function is called inside browser evaluate()
// tweets is injected by the caller
function postThread(tweets) {
  return new Promise((resolve, reject) => {
    let currentIndex = 0;
    
    function getLastEditor() {
      const editors = document.querySelectorAll('div.DraftEditor-editorContainer [contenteditable="true"]');
      return editors[editors.length - 1];
    }
    
    function pasteText(element, text) {
      element.focus();
      const dt = new DataTransfer();
      dt.setData('text/plain', text);
      element.dispatchEvent(new ClipboardEvent('paste', {
        clipboardData: dt,
        bubbles: true,
        cancelable: true
      }));
    }
    
    function addNextTweet() {
      if (currentIndex >= tweets.length) {
        // All tweets inserted, click "Post all"
        setTimeout(() => {
          const postAllBtn = Array.from(document.querySelectorAll('button[data-testid="tweetButton"], button'))
            .find(b => b.textContent.trim() === 'Post all');
          if (postAllBtn && !postAllBtn.disabled) {
            postAllBtn.click();
            resolve('Posted ' + tweets.length + ' tweets');
          } else {
            resolve('All ' + tweets.length + ' tweets inserted. Post all button not found or disabled — check manually.');
          }
        }, 1000);
        return;
      }
      
      if (currentIndex === 0) {
        // First tweet — just paste into existing editor
        const editor = getLastEditor();
        if (!editor) {
          reject('No editor found');
          return;
        }
        pasteText(editor, tweets[currentIndex]);
        currentIndex++;
        setTimeout(addNextTweet, 600);
      } else {
        // Click "Add post" then paste
        const addBtn = document.querySelector('[data-testid="addButton"]');
        if (!addBtn) {
          // Try finding by aria-label
          const altBtn = document.querySelector('button[aria-label="Add post"]');
          if (!altBtn) {
            resolve('Inserted ' + currentIndex + '/' + tweets.length + ' tweets. Add button not found.');
            return;
          }
          altBtn.click();
        } else {
          addBtn.click();
        }
        
        setTimeout(() => {
          const editor = getLastEditor();
          if (editor) {
            pasteText(editor, tweets[currentIndex]);
            currentIndex++;
            setTimeout(addNextTweet, 600);
          } else {
            resolve('Inserted ' + currentIndex + '/' + tweets.length + ' tweets. Editor not found after add.');
          }
        }, 800);
      }
    }
    
    addNextTweet();
  });
}
