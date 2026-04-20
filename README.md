# Twitch Watchdog

Simple app that checks if the streamer is live on Twitch and notifies the VK chat if so

> Curruntly in a POC phase. Probes twitch -> send a VK message + has a UI for that.
> Looking forward to implement celery workers and impove UI that app become a social media management kind of tool and stuff 

## Description

This app could help streamer to lead their social media.
They have just one place to make a post to all platforms that their wants at once.

This app could also be extended to an event subscription tool.
User adds an event and receives a ping from the intended platform when this event occurs.

### User story

As a follower, I want to be notified by my streamer. So I add the bot that will ping me if the stream is live.

As a streamer, I want to make a post directly to my audience from one place.

### Use case

User adds a bot to the chat, when the stream goes live, the bot send a message to the chat.

### POC

For the streamer it is much easier to hold every social media account in one place.

## Launch

```bash
cd src
docker build -t twitch-watchdog-bot .
docker run --env-file ../.env twitch-watchdog-bot
```

## Info

Black - formatter \
Pylint - linter (try ruff next time) \

pre-commit to launch them locally \
github actions to launch them in the cloud

> with zsh you need to use `noglob`

```bash
pip install .               # For production
pip install -e .[dev]       # For development
pip install -e .[test]      # For testing

pre-commit run --all-files # Formatter + Linter
pre-commit install --install-hooks # Add .git/hooks

npm --prefix=frontend run pretty # Frontend formatter
```
