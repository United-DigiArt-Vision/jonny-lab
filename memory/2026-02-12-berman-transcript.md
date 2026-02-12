# Matthew Berman "OpenClaw is NUTS" — Vollständiges Transkript

**Quelle:** YouTube Video, von Dino manuell transkribiert/geliefert
**Datum:** 2026-02-12

---

I'm going to show you exactly how I'm using OpenClaw. I have spent countless hours over the last few weeks exploring every nook and cranny of what is possible with OpenClaw. I truly believe I am one of the most advanced users of OpenClaw on the planet. And I'm going to show you everything that I've learned.

And it all starts right here. This is a fresh MacBook Air. I wiped it clean and I installed OpenClaw on it. This thing lives right on my desk. I have it in clamshell mode. So when I close it, it does not shut off. It is running 24 hours a day, connected to the internet. And I make it easily available anywhere. I installed team viewer on it so that if I'm remote and something happens and I need to change something directly on the computer, I just team viewer into it and I can do that. I also set up tail scale so I can easily SSH into it. So if I want to code something with cursor on it, I can SSH in from any other computer and that one just sits on my desk.

## Overview

Here Overview is the high-level overview of everything going on in my system. And I know it looks complicated. I'm going to get into detail about all of it.

All right, so here is the overview. First, we have the interfaces. This is how I'm actually talking to my openclaw. I use Telegram as the primary one. And if you watched my previous video, you know I'm using Telegram groups. I have a bunch of different topics. I keep all of the topics very narrow, very niche, and I actually don't have it start new sessions anymore. Previously, a default setting in OpenClaw is to start a new session every day at like 4:00 a.m. That means it basically forgot everything in the chat prior, which would make sense if I had a single DM that spanned forever, but instead I have all of these individual channels, so I didn't want to do that anymore. And the solution, I simply had it set the expiration of a session to be one year. And so look at all these different sessions. I have my knowledge base, my food journal, cron updates, video research, self-improvement, business analysis, meeting prep, all of these different ones, and it allows me to stay on topic.

All right, so now back here, second, I have Slack, but I have it very narrowly implemented in Slack. It's only available in two channels, and it's only available to me. I am the only one who's able to invoke my open claw. If somebody else tries to invoke it, it just ignores it.

Then of course we have our command line interface. I sometimes SSH in and we also have scripts.

## Models

I'm using multiple models of course. So we have Anthropic, Opus, Sonnet and Haiku. I'm using Google Gemini for a bunch of stuff. We're using XAI Gro and XARCH. And of course we're using Open AI.

## Skills Overview

And it already has after just two plus weeks of using it a ton of different skills. I use it as a personal CRM. I use it as a knowledge base, a video idea pipeline, X and Twitter research, business meta analysis. That's a crazy one. Wait till I tell you about that. HubSpot Ops. I always apply the humanizer skill. I want all the text coming out of it to be humanlike, not AI like. No M dashes. I plugged it into my to-do list and I kind of use it as a task management system as well. I track all of the usage across everything I do. And of course, I use it for YouTube analytics.

## Data Storage

And I'm also storing a ton of data. I actually try to store all the data I possibly can. And I usually do that in a traditional database mixed with a vector column. So I want to be able to do traditional SQL searches, but I also want to be able to do natural language searches using the vector column. And so I created a standardized way of creating this hybrid database and I use it across a bunch of different skills. So I have my contacts in my CRM. Again, I'm going to go over all of these use cases. So I have my knowledge base, I have video pitches, my business meta analysis, views of my social channels, the cron log, everything is stored.

## External Services

Then I've plugged in a bunch of different external services. We have Google Workspace via GG. I have a sauna. I have HubSpot. I have to-doist, Fathom, Brave, and GitHub. I have X. I have YouTube's API. So much is happening right now.

## Personal CRM

All right. So, the first workflow I want to talk about is my personal CRM. It is incredible because it allows me to plug in all of this builtup knowledge into everything else I'm doing. Let me just explain. So, I basically have my OpenCloud download all of my emails and start to parse through them, understand who's the email from, filter out contacts that I don't want saved, like newsletters and cold outreach, cold pitches, and then it finds the highest quality contacts, and starts saving it to my CRM. It reads all of the downloaded emails, builds out a graph, builds out an understanding of all the conversations I've had with each contact, and starts to save that in the database. and I have it do that every single day. So, it's always up to date. It always knows who I'm talking to, what I'm talking about, and it's just super helpful because I can always ask questions like, "Who is the last person I talked to at Grapile and what did we talk about?" Or, "Who else do I know at, you know, this other company?"

And so, this is how it works. I have the daily ingestion trigger, which is a cron job. It downloads Gmail and my calendar, by the way, not just Gmail, also my calendar. It extracts people from the senders and participants. It deduplicates everything, merges contact records. It uses AI to classify the role in context and I use a very inexpensive very fast Gemini 2.5 flash model I believe to do that classification. Then we start to update the timeline in Last Touch. It does semantic indexing and it sends me updates via Telegram when I want it and I can also just query against it as I said earlier.

Now, where this is also very useful is in my meeting prep workflow. Every single day, first thing in the morning, it looks at my calendar for the day. It filters out events that don't have anybody or only have my internal team. And it basically gives me a meeting prep for the day. It says, "Hey, you're meeting with this person. Here's the last thing you talked about. Here's what they want to talk about in this meeting. Here's who they are." And it's just super helpful to keep me up to date going into these meetings.

## Knowledge Base

All right. Next is my knowledge base. I am constantly on X and searching the web and reading articles all about artificial intelligence. And I wanted a single place where I can just throw everything interesting that I find into a single repository and I'm able to use natural language to search against it. And again, all of the things that I'm building, I want to be able to use across different workflows. That's really important. And so when I get to the video ideation workflow later, you're going to see it actually references different articles that are that have been saved to this knowledge base.

And so the way this works is I take a file or URL, I drop it in Telegram, it detects the source type, extracts all the information from it, normalizes it, chunks it, puts it in the vector database, and then stores it. So then when I have a question like, find me all the articles about the Opus 4.6 model. And so I put that user question in, it embeds it, it grabs all of the candidate articles, and then it answers with sources. So now I'm building up this infinite knowledge base of everything that has interested me and it just stores it and I can always reference it.

## Video Idea Pipeline

Okay, next. And this is one of my favorite ones. This is the video idea pipeline. This was something that I spent a ton of time on. The way I was doing it previously is I would drop links, again, something that I'm now doing via the knowledge base into Slack to share with my team. We would talk about it and the ones that interested us the most, we would decide to make a video about. Then I would create an Asana card. I would do research, find all relevant articles, find relevant posts, and put it all together in that Asana card. And it would just, you know, take a lot of time.

But now I don't have to do any of that. So first remember the previous knowledge base? Well, part of that workflow is when I drop an article in Telegram and it gets all that information, it posts to the Slack channel for me and it says, "Hey, this is what Matt's looking at." And we can have that discussion there. Also, if somebody from my team drops a link in Slack, I can actually tag my open claw and say, "Hey, let's make a video idea about this." And so both of these ways work.

Let me show you what happens after that. So we have this idea trigger. It either comes from Slack or Telegram. We parse the video topic or intent. Then it does research on X and it also does research on the web. Then we query the knowledge-based context. So it looks for potential articles that might be relevant. It comes up with video pitches and make sure it hasn't pitched us something like that already. Then it starts to build hooks and an outline for the video. It links all sources, creates that Asana task, and then sends confirmation to wherever I invoked it. All of this happens in like 30 seconds.

## Twitter/X Search (Tiered)

Okay. Next, I built out an entire workflow just for searching on Twitter because I do so many searches on Twitter, whether it's getting the data from specific posts, and there are so many different ways to do it. I actually built an entire fallback daisy chain system that handles it for me and it's cost-optimized and yeah, it's amazing.

All right, so here's how it's actually working. So first tier one, it uses FX Twitter's API, which is apparently free. You can only grab individual tweets with it. Single tweet lookup only. There's no search. Then it goes to the low-cost tier 2 which is the twitterapi.io. It's 15 cents per thousand tweets. It does search profiles, user tweets, thread context. Then I use the expensive tier three as another fallback. The official X API v2. This is very expensive. So it's 0.005 cents per tweet, pay per use, but you get basically everything. Then as a fallback, we use the XAI API with the XARCH tool. Sometimes we use Grock to search against Twitter.

## Analytics Tracker

All right. Next, obviously, I use it to track my YouTube analytics and some of my competitors or the channels that I keep a close eye on. So, it hits the API daily, pulls down all of my stats for all of my videos, the channels growth, everything. It persists it and takes a snapshot and records it in a database locally. Then it does some computations on it and again stores all that locally. We scan our competitors, their uploads, their cadence to see what they're doing. We get PNG charts, and then it feeds all of those insights into the meta-analysis workflow.

## Business Meta-Analysis (Data Review / Council)

All right, this next one is absolutely insane. And I actually got this idea from Brian Armstrong, the CEO of Coinbase. He said they're using AI in a really novel way where they basically plug in all of their data and have AI review all of it and look for gaps in their understanding of their business, ways to improve. And I thought, hey, we can do that.

So, check this out. I basically ingest all the data from my business. I put together a council of AI experts, AI agents that all work together, collaborate, and then put together a daily report for me on things that I'm missing from the business, ways to improve the business, and more.

So, first, here are all the signals. We have YouTube metrics, CRM health, cron reliability, social growth, Slack, all the Slack messages, emails, Asana, X, Fathom meetings, that's one of the coolest ones. So, Fathom, which is an AI notetaker, joins all my meetings, records them, transcribes them, and then I ingest that. So, I have a record of all the meetings that I have, and then also my HubSpot pipeline.

Then, we compact it all down into the top 200 signals by confidence. And I have first a draft created. Then phase two, I have a **growth strategist, a revenue guardian, a skeptical operator, and a team dynamics architect** all review it, collaborate, go back and forth with each other. They come to a consensus. I have a council moderator again, Opus 4.6. They reconcile disagreements, put it all together, and finally rank everything and give me that report.

That runs once a day in the middle of the night. So, it's when I'm not using a lot of usage from Opus anyways. And then it provides me with that report and it gives me great actionable insights about the business.

## HubSpot

All right. Next, I plugged in HubSpot into my OpenClaw. And I'm not actually using this all that much, but I do allow OpenClaw to reference my deal pipeline. And of course, that's for sponsorships for this channel.

## Humanizer

All right, next. And this is something that I use across the board both in my direct messages with my open claw as well as any content it writes. It basically uses the humanizer skill against everything. And so that removes the AI smell from writing. And it's very easy. It is a skill. It's on Clawhub. You can download it, install it, and it's constantly being updated with AI smells.

## Image/Video Generation

All right. Next is image generation and also video generation. I plugged in Nano Banana and VO as APIs to OpenClaw and now it has the ability to create images and video anytime I want for any use case. All of this happens through Telegram. I have a separate Telegram topic for images and another one for video.

## To-Do List (Fathom + Todoist)

All right. Here's another one. I also have it managing my to-do list. And this one is crazy. There's a few ways that this can get started. One, I have a meeting. I mentioned earlier whenever I have a video conference, I have my Fathom notetaker join it and transcribe all the notes. Then rather than using Fathom's built-in takeaway generator, which was wonky and didn't really work all that well, I take the transcript and send it to Gemini 2.5 Flash and say, "Look through everything. Tell me what are key takeaways for me to do and takeaways that my attendee needs to do." And record them both. Again, all of this gets stored locally.

I can also just simply say, okay, add a task to follow up with X person by Friday. And all of it gets extracted, actions, owner, deadlines, cross referenced with the CRM, who is the person, what is the company, it looks at all of the context it has about them, shows me the task list, if I approve it, it puts it into my Todoist, which is the to-do list app that I use, and it just manages it.

## Usage Tracker (Saves Money)

All right. Next, I started to notice because I'm doing so much with it. Occasionally, I would get charged a lot of money for an API call or for a model, and I wanted to keep an eye on it. And, you know, I'm still paying per month. I pay a hundred bucks per month for the Cloud subscription. I pay for the Gemini API calls, the X API calls. It's not cheap. I'm probably paying about $150 per month in total for all of this, which relative to the value I'm getting from it is very cheap in my opinion.

So, I have something now that tracks all of my spend and my usage. Every single AI call, every single API call gets logged to a single place. And I can ask how much I spent this week, which workflows are costing a lot of money, show me the 30-day trend.

## Services Summary

All right, let me show you all of the services I'm using now. Telegram, Slack, Google Workspace via Gogg (calendar and email ingestion, drive backup), Asana, Todoist, HubSpot, YouTube APIs, X and Twitter search, Fathom, GitHub, Google Drive, Brave search, and Firecrawl.

## Automations (Cron Overview)

All right. So next, let me just show you the holistic view of all the automations I'm doing.
- Every hour: sync code repo, check for changes, back up to GitHub
- Databases: backed up to Google Drive (not GitHub)
- Detailed restore document in case of total loss
- Every day: ingesting emails, collecting YouTube analytics, performing health checks, nightly business briefing
- Every week: synthesize daily notes into long-term memory, housekeeping
- Pattern: cron executes tasks, notifies in Telegram

## Backup Strategy

It is all tracked in Git. Push all code including markdown files. Databases get backed up to Google Drive, timestamped. Restore procedure documented. Code updates about every hour.

## Memory

Using default memory built in (not QMD). During the day: conversations, tasks completed, mistakes made → daily notes. Weekly synthesis → distills patterns and preferences → long-term memory. Learnings folder: corrective patterns, mistakes not to make again. Gets better over time.

## Building OpenClaw (Development Setup)

I prefer developing in Cursor. I SSH into the MacBook Air from Mac Studio. Cursor SSH + direct SSH + TeamViewer. MacBook Air always on, never leaves home. Multiple gits: one for major projects (like CRM), one for OpenClaw as a whole. Write tests for everything. Commit and push to GitHub frequently.

## Updating/Maintaining Markdown Files

Multiple markdown files can drift. Everything in markdown depends on the model you're using. **Opus 4.6 really listens to every single word — you don't need bold, all caps, "don't ever forget this" etc.** Very different from Opus 4.5.

Created `workspace.md` specifying how everything works. Table of contents, very large file, used as reference.

**Daily maintenance cron:**
1. Had OpenClaw download best practices from openclaw.com and store locally
2. Daily cross-reference all markdown files against best practices
3. Also downloaded Opus 4.6 prompting guide, stored locally
4. Cross-references against Anthropic's prompting best practices
5. Constantly updating and cleaning itself
