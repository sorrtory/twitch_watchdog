# Bro's streaming

Simple app that checks if the streamer is live on Twitch and notifies the VK chat if so

## Launch

```bash
cd src
docker build -t twitch-watchdog-bot .
docker run --env-file ../.env twitch-watchdog-bot
```
