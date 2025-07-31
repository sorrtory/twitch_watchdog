# Twitch WatchDog. Software requirements specification

## Introduction

This document describes MVP of Streamer WatchDog app.
The main idea of the project is to help the content creator to connect to
their followers by integrating in the user-preffered social media platform.

## Description

The app appears to looks like a social media management tool.
User create a post in this app and these posts are sent on several platforms,
with the difference that these posts are distributed by chat bots, not the channels.

### Target audience

This product is anticipated to be used by streamers or their managers.
They access this app and register their bot
so that would work as their personal autoposting service.
As a result, a streamer's audience can add this bot to their environment to
keep in touch with a streamer.

### Idea

This idea is not new (see [existing products](#competitive-implementations)),
however this app stands out on its design as a "personal inchat channel"
and also solves additional issues like lack of VK integration.

#### Problem

Usually people do not really care about streaming platform notification and messages
unlike the social media chats they participate in.

#### Solution

Create a chat bot that will send content straight into chats.

#### Benefits

Followers will be closer to the streamer they like.
In addition, they will be able to discuss it with their friends only
without reposting.

### Dev plan

The first milestone of this app is to create an auto sending alert about Twitch
stream start straight to VK bot, which can be added to the one chat at least.

The second milestone is to allow streamer to take control of the bot's posts.
That it would be like a personal channel, but a posts would be
sent inside a chat. As a result user receives topics he shares and want to discuss
with his close friends. This type of bot becomes an inchat channel.

The third milestone is to implement multiple user support, user state maintanance
and finally test in production.

## System Features and Requirements

### Key features

- VK integration
- Open source
- One streamer one bot approach

### FURPS+

#### Functionality

- auth system for streamers (their managers)
- option to add a bot
- option to enable / disable notification messages

#### Usability

- many platforms integrated
- option to change a message
- statistics for each bot and overall

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
  The app can easily be enhanced to become it as a bot registration process looks
  pretty similar. So, streamer can grant tokens to their channel 
  and create cross platform posts just from one website.
- Add streamer statistics

### Use case

1.

- Follower adds a bot to their chat
- System acknowledges this chat
- Streamer goes live
- Bot sends an alert

2.

- Streamer signs up into WatchDog app
- Streamer sets Twitch nickname
- Streamer creates a VK bot
- Streamer sets bot's token
- Streamer turns on auto notification
- Streamer goes live
- Every chat that has this bot receive a notification message

3.

- Streamer logs in
- Streamer ensures to have a VK bot token set
- Streamer create a post on the app's panel
- Every chat that has this bot receive a post

## Competitive implementations

- [Telegram + Webhook](https://github.com/AleVersace/twitch-alert-telegram-bot)
- Discord [millionaire](https://streamcord.io/) and [another one](https://mee6.xyz/en)
- [General purpose ping](https://pingcord.xyz/)
