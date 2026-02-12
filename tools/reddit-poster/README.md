# Reddit Poster Tool

Automated Reddit posting via Playwright.

## Setup
```bash
cd ~/.openclaw/workspace/tools/reddit-poster
npm install
npx playwright install chromium
```

## Usage

### Test Login
```bash
REDDIT_PASSWORD="your_password" node post.js test
```

### Post Comment
```bash
REDDIT_PASSWORD="your_password" node post.js comment "https://reddit.com/r/sub/comments/xxx" "Your comment text"
```

### Create Post
```bash
REDDIT_PASSWORD="your_password" node post.js post "subreddit" "Post Title" "Post body text" "Optional Flair"
```

## Current Status
- ⚠️ Login blocked - "Something went wrong" error
- Possible causes: Wrong credentials, CAPTCHA, headless detection

## TODO
- [ ] Verify credentials
- [ ] Try with cookies/session storage instead of login
- [ ] Add proxy support to avoid rate limiting
- [ ] Consider Reddit API (OAuth) instead of scraping
