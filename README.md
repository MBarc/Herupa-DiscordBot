![alt text](https://github.com/MBarc/Herupa-DiscordBot/blob/master/herupaprofilepic.png)

# Herupa-DiscordBot
Open source discord bot that executes a collection of miscellaneous commands. 

Initializer: $

### Commands:

- [ ] Birthday:
  - Usage: $birthday MMDD 
  - [ ] Sends the birthday person a private message saying "Happy birthday <birthday person's name>, from <array of administrators' names> 
  - [ ] Message includes birthday meme. 

- [X] Herupa:
  - Usage: $herupa
  - [X] Herupa Bot joins the voice channel plays the 'Google Translate Audio of Herupa', then leaves.
  
- [x] Member of the week:
  - Usage: This command is automatic, cannot be called upon.
  - [X] Herupa picks a member of the week and sends them a congratulations message in the appropriate channel.
  
- [X] Join:
  - Usage: $join
  - [X] Joins voice channel.
  
- [X] Leave:
  - Usage: $leave
  - [X] Leaves voice channel.
  
- [ ] Play:
  - Usage: $play <link>
  - [X] Plays YouTube links.
  - [ ] Plays Spotify links. 
  - [X] Audio files are automatically added to a queue.
  
- [X] Pause:
  - Usage: $pause
  - [X] Pauses whatever audio file is playing.
  
- [X] Resume:
  - Usage: $resume
  - [X] Resumes whatever audio file is paused.
  
- [X] Stop:
  - Usage: $stop
  - [X] Completely cancels/stops whatever audio file is playing.
  
- [X] Queue:
  - Usage: $queue
  - [X] Adds audio files to queue.
  
- [ ] Leaderboards:
  - Usage: $leaderboards
  - [ ] Sends of list of top members in every category.
    Example: 
    
            Most messages: <username> with X messages sent!
            Voice chat: <username> joined X voice chats!
            AFK: <username> went away X times!
            Online: <username> came online X times!
            Offline: <username> only came online X times!
  
- [ ] ASMR:
  - Usage: $asmr
  - [ ] Plays cringey asmr videos in voice chat.
  
- [ ] Dank Airhorn:
  - Usage: $dank
  - [ ] Goes in every voice chat, one by one, and plays the Dank Airhorn audio file.
  
- [ ] Clear:
  - Usage: $clear <int>
  - [ ] Deletes the latest <int> messages in the channel that the command was sent in.
  
- [ ] Copy Cat:
  - Usage: $copy <username>
  - **Parts of this function are currently not possible. This function will be complete as much as possible and marked finished.**
  - [ ] Bot will repeat after target/<username> 
  - [ ] Follows target to voice channel to play their own voice back at them.
  
- [ ] Record:
  - Usage: $record
  - **This function is currently not possible with the current version of the Discord API but it is a planned for development.**
  - [ ] Records all audio in a voice channel.
  - [ ] Stops recording once author leaves voice channel.
  
- [ ] What To Watch:
  - Usage: $w2w <source> <genre>
  - [ ] Sends random link from the user's choice of either Netflix, Hulu, or Crunchy Roll.
  
- [ ] Survery:
  - Usage: $survey <prompt> <option 1> <option 2> . . . <option n>
  - [ ] Sends a survey monkey link.
  
- [ ] Help:
  - Usage: $help
  - [ ] Sends relevant info for every command in the channel prompted.
