from gemini_llm import system_prompt, independent_prompt, gen_gemini_response
from polly_tts import speak_polly_response
from comment_reader import init_comment_loader, read_new_comment
import json
import asyncio
numberOfComments = 0
past_conversation_log = []
async def main():
    driver = init_comment_loader()
    while True:
        new_comment = read_new_comment(driver)

        if new_comment["user"] != "":
            past_conversation_log.append(new_comment)
            gemini_input = system_prompt(past_conversation_log, numberOfComments)
        else:
            gemini_input = independent_prompt(past_conversation_log)

        response = await gen_gemini_response(gemini_input)
        response_elem = json.loads(response)
        past_conversation_log.append(response_elem)
        await speak_polly_response(response_elem["response"])
        print(past_conversation_log)

asyncio.run(main())