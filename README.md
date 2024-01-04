### Simple TTS Server Implementation ###


# Installation
Refer to [libraries.md](libraries.md) to install necesary libraries.

# Run demo

The repo provide an example client request to convert text to speech then save to an audio file.

Server receive the text request, create the audio file, save a copy in server side then return information to client.

(Please refer to [command.md](command.md) for more useful commands.)

In one termianl tab, run this line:
```
python tts_python_server.py
```

Open another terminal tab and run this line:
```
python tts_python_client.py -o voice_output_client -t <text input to convert to speech>
```
