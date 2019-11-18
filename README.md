![alt text](https://github.com/MBarc/Herupa-DiscordBot/blob/master/herupaprofilepic.png)

# Herupa-DiscordBot
Open source discord bot that executes a collection of miscellaneous commands. 

This bot utlizies multiple APIs: Discord.py (rewrite), PRAW, Selenium, and 

Initializer: $

### Commands:

- [ ] Birthday:
  - Usage: $birthday MMDD 
  - [X] Sends the birthday person a private message saying "Happy birthday <birthday person's name>, from <array of administrators' names> 
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
  - Usage: $clear <int_number>
  - [ ] Deletes the latest <int_number> messages in the channel that the command was sent in.
  
- [ ] Copy Cat:
  - Usage: $copy <user_name>
  - **Parts of this function are currently not possible. This function will be completed as much as possible and marked finished.**
  - [ ] Bot will repeat after target/<username> 
  - [ ] Follows target to voice channel to play their own voice back at them.
  
- [ ] Record:
  - Usage: $record
  - **This function is currently not possible with the current version of the Discord API but it is planned for development.**
  - [ ] Records all audio in a voice channel.
  - [ ] Stops recording once author leaves voice channel.
  
- [ ] What To Watch:
  - Usage: $w2w <_source_> <_genre_>
  - [ ] Sends random link from the user's choice of either Netflix, Hulu, or Crunchy Roll.
  
- [ ] Survey:
  - Usage: $survey <_prompt_> <_option 1_> <_option 2_> . . . <_option n_>
  - [ ] Sends a survey monkey link.
  
- [ ] Reddit:
  - Usage: $reddit <_subreddit_> <text_channel>
  - [ ] Takes the given <_subreddit_> and will send every new post to the specified <text_channel>.
  
- [ ] Animal Facts:
  - Usage: $animalfact <optional_animal> <optional_nsfw>
  - [ ] Sends picture of animal.
  - [ ] Sends a random facts about any animal, could be specified. The facts could be nsfw if specified.
  - [ ] Will take either the scientific name or the common name as an argument.

- [ ] Rock, Paper, Scissors:
  - Usage: $rps <user's_choice>
  - [ ] Herupa will randomly pick between rock, paper, or scissors and send it in the channel prompted.
  
- [ ] Coin Flip:
  - Usage: $flip <user's_choice>
  - Herupa will randomly pick between heads and tails and let the user know if their <user's_choice> was correct.
  
- [ ] Assign:
  - Usage: $assign <server_role>
  - Herupa will assign the author the given <role>. 

- [ ] Help:
  - Usage: $help
  - [ ] Sends relevant info for every command in the channel prompted.
  
- [ ] Welcome Message:
  - Usage: This command is automatic, cannot be called upon. 
  - [ ] Sends a welcome message when member joins the server.
  
- [ ] Goodbye Message:
  - Usage: This command is automatic, cannot be called upon. 
  - [ ] Sends a message saying that the member has left the server.
  - [ ] Also sends a private message saying goodbye.
  
  - [ ] Watch Party:
  - Usage: $watchparty <_command_> **or** <_title_of_video_>
  - [ ] Bot will host a Netflix Party that users can join.
  - [ ] pause command will pause the video.
  - [ ] play command will resume the video.
  - [ ] rewind <_int_> will rewind the video by <_int_> seconds
  - [ ] fastforward <_int_> will fast forward the video by <_int_> seconds
