const { chromium } = require('playwright');

const USERNAME = 'JonnyDigiArt';
const PASSWORD = process.env.REDDIT_PASSWORD;

async function dismissCookieBanner(page) {
  console.log('Checking for cookie banner...');
  try {
    const acceptBtn = await page.$('button:has-text("Accept All"), button:has-text("Accept")');
    if (acceptBtn) {
      console.log('Found cookie banner, accepting...');
      await acceptBtn.click();
      await page.waitForTimeout(1000);
    }
  } catch (e) {
    console.log('No cookie banner or already dismissed');
  }
}

async function login(page) {
  console.log('Navigating to Reddit login...');
  await page.goto('https://www.reddit.com/login', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(2000);
  
  // Dismiss cookie banner first
  await dismissCookieBanner(page);
  await page.waitForTimeout(500);
  
  console.log('Taking screenshot of login page...');
  await page.screenshot({ path: '/tmp/reddit-1-login.png' });
  console.log('Page URL:', page.url());
  
  // Wait for and fill username - use proper input simulation
  console.log('Filling username...');
  await page.waitForSelector('input[name="username"]', { timeout: 10000 });
  await page.click('input[name="username"]');
  await page.waitForTimeout(200);
  // Type character by character to trigger validation
  for (const char of USERNAME) {
    await page.keyboard.type(char);
    await page.waitForTimeout(50);
  }
  console.log('Username filled');
  
  await page.waitForTimeout(500);
  
  // Fill password with proper input simulation
  console.log('Filling password...');
  await page.click('input[name="password"]');
  await page.waitForTimeout(200);
  for (const char of PASSWORD) {
    await page.keyboard.type(char);
    await page.waitForTimeout(50);
  }
  console.log('Password filled');
  
  await page.waitForTimeout(1000);
  await page.screenshot({ path: '/tmp/reddit-2-filled.png' });
  
  // Try to find and click the login button with multiple selectors
  console.log('Looking for login button...');
  const buttonSelectors = [
    'button:has-text("Log In")',
    'button:has-text("Log in")',
    'button[type="submit"]',
    'form button',
    'button.login'
  ];
  
  let clicked = false;
  for (const sel of buttonSelectors) {
    try {
      const btn = await page.$(sel);
      if (btn) {
        // Check if button is enabled
        const isDisabled = await btn.getAttribute('disabled');
        console.log(`Found button with ${sel}, disabled=${isDisabled}`);
        
        // Force click even if disabled
        await btn.click({ force: true });
        console.log('Clicked login button');
        clicked = true;
        break;
      }
    } catch (e) {
      console.log(`Failed with ${sel}: ${e.message}`);
    }
  }
  
  if (!clicked) {
    // Try pressing Enter as fallback
    console.log('Trying Enter key as fallback...');
    await page.keyboard.press('Enter');
  }
  
  console.log('Waiting for login to complete...');
  await page.waitForTimeout(6000);
  await page.screenshot({ path: '/tmp/reddit-3-after-login.png' });
  
  console.log('Current URL:', page.url());
  
  // Check for 2FA or captcha
  const pageContent = await page.content();
  if (pageContent.includes('verification') || pageContent.includes('captcha')) {
    console.log('WARNING: 2FA or CAPTCHA detected!');
  }
  
  // Check if we're logged in by looking for user menu
  const userMenu = await page.$('button[id*="user"], a[href*="/user/"]');
  if (userMenu) {
    console.log('Login confirmed - found user menu!');
    return true;
  }
  
  if (page.url().includes('login') || page.url().includes('register')) {
    console.log('WARNING: May still be on login page');
    // Check for error messages
    const pageText = await page.textContent('body');
    if (pageText.includes('Incorrect') || pageText.includes('wrong')) {
      throw new Error('Login failed: incorrect credentials');
    }
  } else {
    console.log('Login appears successful!');
  }
  
  return true;
}

async function postComment(page, postUrl, commentText) {
  console.log(`Navigating to: ${postUrl}`);
  await page.goto(postUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await dismissCookieBanner(page);
  await page.screenshot({ path: '/tmp/reddit-post-page.png' });
  
  // Scroll down to find comment area
  await page.evaluate(() => window.scrollBy(0, 500));
  await page.waitForTimeout(1000);
  
  // Look for "Add a comment" and click it
  console.log('Looking for comment input...');
  
  try {
    // Try clicking on the placeholder text
    await page.click('text="Add a comment"', { timeout: 5000 });
    await page.waitForTimeout(1000);
  } catch (e) {
    console.log('Could not click "Add a comment", trying other selectors...');
  }
  
  // Now type the comment
  await page.keyboard.type(commentText);
  await page.waitForTimeout(500);
  
  await page.screenshot({ path: '/tmp/reddit-comment-filled.png' });
  
  // Find and click submit button
  const submitSelectors = [
    'button:has-text("Comment")',
    'button[type="submit"]'
  ];
  
  for (const sel of submitSelectors) {
    try {
      const btn = await page.$(sel);
      if (btn) {
        await btn.click();
        console.log('Comment submitted!');
        break;
      }
    } catch (e) {
      continue;
    }
  }
  
  await page.waitForTimeout(3000);
  await page.screenshot({ path: '/tmp/reddit-comment-done.png' });
  console.log('Final URL:', page.url());
}

async function createPost(page, subreddit, title, body, flair) {
  console.log(`Creating post in r/${subreddit}...`);
  
  // Use the text post submission URL
  const submitUrl = `https://www.reddit.com/r/${subreddit}/submit?type=TEXT`;
  await page.goto(submitUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await dismissCookieBanner(page);
  await page.screenshot({ path: '/tmp/reddit-submit-page.png' });
  
  // Fill title - look for title input
  console.log('Looking for title input...');
  const titleSelectors = [
    'textarea[placeholder*="Title"]',
    'input[placeholder*="Title"]',
    'textarea[name="title"]',
    '[data-testid="post-title"]'
  ];
  
  for (const sel of titleSelectors) {
    try {
      const input = await page.$(sel);
      if (input) {
        console.log('Found title input with:', sel);
        await input.click();
        await page.keyboard.type(title);
        console.log('Title filled');
        break;
      }
    } catch (e) {
      continue;
    }
  }
  
  await page.waitForTimeout(500);
  
  // Fill body
  console.log('Looking for body input...');
  const bodySelectors = [
    'div[contenteditable="true"]',
    'textarea[placeholder*="Text"]',
    '[data-testid="post-body"]'
  ];
  
  for (const sel of bodySelectors) {
    try {
      const input = await page.$(sel);
      if (input) {
        console.log('Found body input with:', sel);
        await input.click();
        await page.keyboard.type(body);
        console.log('Body filled');
        break;
      }
    } catch (e) {
      continue;
    }
  }
  
  await page.screenshot({ path: '/tmp/reddit-post-filled.png' });
  
  // Set flair if provided
  if (flair) {
    console.log('Setting flair:', flair);
    try {
      await page.click('button:has-text("Add flair"), button:has-text("Flair")', { timeout: 3000 });
      await page.waitForTimeout(1000);
      await page.click(`text="${flair}"`, { timeout: 3000 });
      console.log('Flair selected');
    } catch (e) {
      console.log('Could not set flair:', e.message);
    }
  }
  
  await page.screenshot({ path: '/tmp/reddit-post-ready.png' });
  
  // Submit
  console.log('Submitting post...');
  const postBtnSelectors = [
    'button:has-text("Post")',
    'button[type="submit"]'
  ];
  
  for (const sel of postBtnSelectors) {
    try {
      const btn = await page.$(sel);
      if (btn) {
        await btn.click({ force: true });
        console.log('Clicked submit button');
        break;
      }
    } catch (e) {
      continue;
    }
  }
  
  await page.waitForTimeout(5000);
  await page.screenshot({ path: '/tmp/reddit-post-done.png' });
  
  console.log('Final URL:', page.url());
}

async function main() {
  const action = process.argv[2]; // 'comment', 'post', or 'test'
  
  if (!PASSWORD) {
    console.error('ERROR: REDDIT_PASSWORD environment variable not set!');
    process.exit(1);
  }
  
  console.log('Action:', action);
  console.log('Starting browser...');
  
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
  });
  
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    viewport: { width: 1280, height: 800 }
  });
  
  const page = await context.newPage();
  
  try {
    await login(page);
    
    if (action === 'comment') {
      const postUrl = process.argv[3];
      const comment = process.argv[4];
      if (!postUrl || !comment) {
        console.error('Usage: node post.js comment <url> <comment>');
        process.exit(1);
      }
      await postComment(page, postUrl, comment);
    } else if (action === 'post') {
      const subreddit = process.argv[3];
      const title = process.argv[4];
      const body = process.argv[5];
      const flair = process.argv[6];
      if (!subreddit || !title || !body) {
        console.error('Usage: node post.js post <subreddit> <title> <body> [flair]');
        process.exit(1);
      }
      await createPost(page, subreddit, title, body, flair);
    } else {
      console.log('Test mode - login only');
    }
    
    console.log('Done!');
  } catch (err) {
    console.error('Error:', err.message);
    await page.screenshot({ path: '/tmp/reddit-error.png' });
  } finally {
    await browser.close();
  }
}

main();
