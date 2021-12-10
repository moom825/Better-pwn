# better-pwn

Tools for hacking better discord(BD). One a token grabber builder, one a malawre dropper builder. both in betterdiscord plugin form, both output payloads obfuscated.<br>

## **Disclaimer:**

This tool is for educational use only, the author will not be held responsible for any misuse of this tool.<br>

## **How to use:**
There are 2 files here, one generates a better discord plugin that is a token grabber, the other generates a better discord plugin that is a malware dropper.<br>

judging by the file names it should be pretty easy to identify which ones which.<br>

when running the token grabber builder a prompt will come up asking for the plugin's display name, the plugin version, the plugins description, the plugin author, and the webhook (thats where the token will be sent) (how to make a discord webhook: https://www.youtube.com/watch?v=fKksxz2Gdnc) url.<br>
Lastly it will ask for a output filename, thats what the filename will be called.<br>
it will save the plugin in the current directory.<br>
<br>
EXAMPLE BUILDING:
```
enter plugin's display name:

>>>message logger

enter plugin version:

>>>1.5.2

enter plugins description:

>>>logs all messages sent in servers

enter author:

>>>moom825

enter webhook: 

>>>https://discord.com/api/webhooks/channel-id/webhook-token

enter output filename: 

>>>message logger

complete, saved to "message logger.plugin.js"
```
<br>
<br>
<br>
<br>

when running the malware dropper builder a prompt will come up asking for the plugin's display name, the plugin version, the plugins description, the plugin author, a direct download link to the file you want dropped (One way to make a direct download link can be found on this website: https://sites.google.com/site/gdocs2direct/), and then it will ask what the dropped filename name should be.
Lastly it will ask for a output filename, thats what the filename will be called.
it will save the plugin in the current directory.<br>
<br>
<br>
EXAMPLE BUILDING:
```
enter plugin's display name: 

>>>message logger

enter plugin version: 

>>>1.2.7

enter plugins description: 

>>>logs messages

enter author: 

>>>moom825

enter dropped filename(ex: file.exe): 

>>>virus.exe

enter direct download link: 

>>>https://www.direct-download-to-link.com/filename.exe

enter output filename: 

>>>message logger

complete, saved to message logger.plugin.js
```
<br>
For the outputed files of each tool the payload itself will be obfuscated.

## **Install requirements** :
```
pip3 install requests or pip install requests
```
Then if the steps above were successful, you can launch the python file by executing ```python filename.py```.

**Requirements:**\
Python3, Windows(x64)

## **Contact:**
Feel free to contact me if you have any problems.
https://discord.gg/V589WeDmUr. ```moom825#0001```
