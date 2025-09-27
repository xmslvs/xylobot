from gemini_llm import system_prompt, gen_gemini_response
from polly_tts import speak_polly_response
from comment_reader import init_comment_loader, read_new_comment
import asyncio
numberOfComments = 0

async def main():
    driver = init_comment_loader()
    while True:
        prompt = read_new_comment(driver)
        gemini_input = system_prompt(prompt)
        response = gen_gemini_response(gemini_input)
        await speak_polly_response(response)

asyncio.run(main())