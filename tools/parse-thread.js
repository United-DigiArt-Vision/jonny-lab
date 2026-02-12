#!/usr/bin/env node
/**
 * Parse X Thread Markdown → JSON tweets array
 * Supports multiple formats:
 * - ## Tweet 1 / ## CTA
 * - **1/10** / **CTA**
 * - --- separated blocks with numbering
 */
const fs = require('fs');
const path = process.argv[2];
if (!path) { console.error('Usage: node parse-thread.js <file.md>'); process.exit(1); }
const content = fs.readFileSync(path, 'utf8');

let tweets = [];

// Try format 1: ## Tweet N headers
const fmt1 = content.split(/^## (?:Tweet \d+|CTA.*)/m).slice(1);
if (fmt1.length >= 3) {
  tweets = fmt1.map(s => s.replace(/^[\s\n]+/, '').replace(/[\s\n]+$/, '').replace(/^---[\s\n]*/gm, '').trim()).filter(t => t.length > 0);
}

// Try format 2: **N/N** or **CTA** blocks separated by ---
if (tweets.length < 3) {
  tweets = [];
  // Find the thread content section
  const threadStart = content.indexOf('## Thread Content');
  const text = threadStart >= 0 ? content.slice(threadStart) : content;
  
  // Split by --- separators
  const blocks = text.split(/\n---\n/).map(b => b.trim()).filter(b => b.length > 0);
  
  for (const block of blocks) {
    // Match **N/N** or **CTA** patterns
    const match = block.match(/^\*\*(\d+\/\d+|CTA[^*]*)\*\*\s*\n([\s\S]*)/m);
    if (match) {
      const tweetText = match[2].trim();
      if (tweetText.length > 0) {
        // Prepend the numbering if it's N/N format
        const prefix = match[1].match(/\d+\/\d+/) ? match[1] + ' ' : '';
        tweets.push(prefix + tweetText);
      }
    }
  }
}

if (tweets.length === 0) {
  console.error('No tweets found in ' + path);
  process.exit(1);
}

console.log(JSON.stringify(tweets));
console.error('Parsed ' + tweets.length + ' tweets');
