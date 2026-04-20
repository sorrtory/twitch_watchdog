# Twitch WatchDog. Software requirements specification

## Introduction

This document describes MVP of the Streamer WatchDog app.
It sets the concept, development flow and
3 epics that are sufficient to launch the application.

## Description

The Streamer WatchDog project is intended to be a service that brings
content creator and their followers closer together.
It acts as an integration in the user-preffered
social media platform, which allows the content creator to focus on the
content itself but social networks.

### Concept

The main idea lies in the chat bot. Followers add this bot to their chats and
subscribe to content creator (or some other events). The creator posts using
the application web interface, then followers receive it directly inchat.

The app appears to look like a social media management tool.
However, the system operates as control panel of a bot instead of social media communities.

The bot is general and is led by multiple content creators, who are only allowed to
make posts and participate in the bot's subscribtion list. Thus followers only pick
from the mentioned list.

### Target audience

This product is anticipated to be used by streamers or their managers.
These users access the app and sign up in the system, therefore
the system adds streamer to the watch list allowing them to autopost on the new livestream.

As a result, streamer's audience can add this bot to their environment to
stay tuned for a streamer.

### Motivation

Idea of the Streamer WatchDog is not new (see [existing products](#competitive-implementations)),
but unlike others this app stands out on its design as a "personal inchat channel"
and also solves some issues like absence of VK integration.

#### Problem

Usually people do not really care about streaming platform notifications,
as against the social media chats they participate in.

#### Solution

Create a chat bot that will send content straight into chats.

#### Benefits

Followers will be able to discuss some topics they share with their friends only,
with no need of reposting. In addition, the bot can implement much more features
than the content feed platform.

### Dev plan

The first milestone of this app is the creation of a system that notifies about
stream start straight to VK bot. The system have to be scalable for multiple targets
and open for modification (as new features appear)

The second milestone is about web app creation. The web app have to feature a control
panel and a dashboard. It have to allow user to create a post

The third milestone is to implement multiple user support, user state maintanance.

After these steps been accomplished, the app should be launed into production.

## System Features and Requirements

### Key features

- VK integration
- Open source
- One bot, many creators

### Stack

- FastAPI
- MongoDB
- Celerry
- Docker
- Vite
- React + React Router
- Tailwind CSS

### FURPS+

#### Functionality

- auth system for content creators
- option to add to bot
- option to enable / disable notification messages

#### Usability

- vk integration
- editable stream alert message
- bot statistics

#### Reliablity

- less than 10 seconds on sending
- exactly one sending per sending request
- control over each watchdog process

#### Perfomance

- 100 rps on average
- less than 1 second to load the page

#### Suportability

- relevant documentation
- more than 80% unit testing coverage

### Additional

- Work not only with Twitch streaming, but other platforms and applications like blogs, YT videos, events

  That will require general purpose event. So, after it has been triggered, the notification been sent.
  This means this app become a service offerring the event subscription functionality.
  (For example, user claims to be pinged on Discord when this HTML page value is changed)

- Create a common bot, that user can sub to events their want to be notified of
- Support changing the notification text and other settings stuff
- Social media management tool.
- Add streamer statistics

### Use cases

1.

- Follower adds a bot to their chat
- Follower subscribe to the stremaer
- System acknowledges this chat
- Streamer goes live
- Bot sends an alert

2.

- Streamer signs up into WatchDog app
- Streamer configures the account with Twitch nickname, etc
- Streamer turns on auto notification
- Streamer goes live
- Every chat that has the bot and is also subscribed to this stremaer
  receive a notification message

3.

- Streamer logs in
- System ensures stramer to have a right configuration
- Streamer create a post in the app's control panel
- Every chat that has this bot receive a post

## Competitive implementations

- [Telegram + Webhook](https://github.com/AleVersace/twitch-alert-telegram-bot)
- Discord [millionaire](https://streamcord.io/) and [another one](https://mee6.xyz/en)
- [General purpose ping](https://pingcord.xyz/)
- [Zapier](https://zapier.com/)
