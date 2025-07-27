# Bro's streaming

Simple app that checks if the streamer is live on Twitch and notifies the VK chat if so

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

```bash
pip install .
pip install -e .[dev]
pre-commit run --all-files # Formatter + Linter
pre-commit install --install-hooks # Add .git/hooks

npm --prefix=frontend run pretty # Frontend formatter
```
