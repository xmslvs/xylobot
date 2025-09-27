from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess

import time
from pygame import mixer
from pygame import mixer, _sdl2 as devicer

import asyncio


# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="my-dev-profile")
polly = session.client("polly")
current_dir = os.getcwd()

mixer.init(devicename = 'CABLE-C Input (VB-Audio Cable C)') # Initialize audio output with the correct device


async def speak_polly_response(gemini_response):
    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=gemini_response, OutputFormat="mp3",
                                            VoiceId="Ivy")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(current_dir, "polly_output.mp3")

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # # Play the audio using the platform's default player
    # if sys.platform == "win32":
    #     os.startfile(output)
    # else:
    #     # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
    #     opener = "open" if sys.platform == "darwin" else "xdg-open"
    #     subprocess.call([opener, output])


    # mixer.init() # Initialize the mixer, this will allow the next command to work

    # # Returns playback devices, Boolean value determines whether they are Input or Output devices.
    # print("Inputs:", devicer.audio.get_audio_device_names(True))
    # print("Outputs:", devicer.audio.get_audio_device_names(False))

    # mixer.quit() # Quit the mixer as it's initialized on your main playback device

    # # Moved to top of file
    # mixer.init(devicename = 'CABLE-C Input (VB-Audio Cable C)') # Initialize it with the correct device

    mixer.music.load("polly_output.mp3") # Load the mp3
    mixer.music.play() # Play it

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    mixer.music.unload() # Unload the mp3
    os.remove(output)
    return