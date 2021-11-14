# mee6-level-bypasser
Uses a webhook to ping you when someone passes you on a mee6 leaderboard.


**DO NOT USE FOR BIG DISCORD SERVERS**
The "API" just grabs the top 100 people on the scoreboard and looks if your user is there. It won't work if you aren't in the top 100. There's not much that can be done about this without being rate limited. Maybe I'll work on a solution later...

<a href="https://repl.it/github/probablypablito/mee6-level-bypasser" title="Run on Repl.it"><img alt="Run on Repl.it" src="https://raw.githubusercontent.com/QuiteAFancyEmerald/HolyUnblockerPublic/master/views/assets/img/replit.svg?raw" width="140" height="30"><img></a>
&nbsp;

# HOW TO USE

1)  Press the run on repl.it button
2)  Open `config.txt`
3)  Follow [this guide](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) to copy your user ID and guild (server) ID
4)  Paste those values into the config
5)  Go to any Discord server in which you have owner permissions (eg. a diary server)
6)  Server Settings > Integrations > Webhooks > New Webhooks
7)  Change the name, profile picture, and channel to whatever you want
8)  Copy the Webhook URL into the config
9)  Run the program with the run button or `python main.py` if self-hosting.
10) Done! To check if it works change `rank.txt` to 0. Long as you aren't in first, the program should ping you!   
