from RealtimeSTT import AudioToTextRecorder
from pygame import mixer, _sdl2 as devicer

from gemini_llm import system_prompt, independent_prompt, gen_gemini_response
from polly_tts import speak_polly_response
from comment_reader import init_comment_loader, read_new_comment
from vtube_studio import trigger_hotkey
from screen_capture import update_screen_history


import json
import asyncio

numberOfComments = 0
past_conversation_log = []

async def process_text(text):
    new_comment = text
    past_conversation_log.append(new_comment)
    gemini_input = system_prompt(past_conversation_log, numberOfComments)

    response = await gen_gemini_response(gemini_input)
    response_elem = json.loads(response)
    past_conversation_log.append(response_elem)
    await trigger_hotkey(response_elem)
    await speak_polly_response(response_elem["response"])
    print(past_conversation_log)
    print(text)

async def mainloop():
    while True:
        text = recorder.text()
        formatted_text = {
            "user": "User",
            "response": text
        }
        await process_text(formatted_text)


if __name__ == '__main__':
    mixer.init()
    input_device_list =  devicer.audio.get_audio_device_names(True)
    recorder = AudioToTextRecorder(input_device_index=input_device_list.index('マイク (ZOOM H and F Series Async Audio)'))
    asyncio.run(mainloop())