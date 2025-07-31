# Twitch WatchDog software requirements specification

## Introduction

This document describes MVP of Streamer WatchDog app.
The main idea of the project is to help the content creator to connect with their followers
by integrating the "new content appeared" alerts to user-preffered social media platform.

### Target audience

This product is anticipated to be used by streamers or their managers.
They access this app and register their bot to work as a posting service.
As a result, a streamer's audience can add this bot to their environment to
keep in touch with a streamer.

## Description

### Problem

Usually people do not really care about streaming platform notification and messages
unlike the social media chats they participate in.

### Solution

Create a chat bot that will send content straight into chats.

### Benefits

Followers will be closer to the streamer they like

## System Features and Requirements

- 


### Additional

- Work not only with Twitch streaming, but other platforms and applications like blogs, YT videos, events

  That will require general purpose event. So, after it has been triggered, the notification been sent.
  This means this app become a service offerring the event subscription functionality.
  (For example, user claims to be pinged on Discord when this HTML page value is changed)

- Create a common bot, that user can sub to events their want to be notified of
- Support changing the notification text and other settings stuff
- Social media management tool.
  The app can easily be enhanced to become it as a bot registration process looks
  pretty similar. So, streamer can grant tokens and create posts just from one website.
- Add streamer statistics
- Allow streamer to take control of the bot posts. 
Then it will be like a channel but inside a chat with only user's own friends
So this bot will become a next-gen channels?

### Use case

- As a Follower, I want to be



## Competitive implementations
- [Telegram + Webhook](https://github.com/AleVersace/twitch-alert-telegram-bot)
- Discord [millionaire](https://streamcord.io/) and [another one](https://mee6.xyz/en)
- [General purpose ping](https://pingcord.xyz/)

### Excuse for creating this
- VK integration
- Open source
- One streamer one bot approach
