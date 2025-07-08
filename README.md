# Bro's streaming

Simple app that checks if streamer is alive on twitch, in that case notify VK chat.

## Launch

```bash
cd src
docker build -t twitch-watchdog-bot
docker run --env-file ../.env twitch-watchdog-bot
```
