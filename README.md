# I'm streaming

Simple app that checks if user is alive on twitch and notify VK chat in that case.

## Launch

```bash
docker build -t vk-twitch-bot .
docker run --env-file .env vk-twitch-bot
```

