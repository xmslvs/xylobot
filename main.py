from gemini_llm import system_prompt, independent_prompt, gen_gemini_response
from polly_tts import speak_polly_response
from comment_reader import init_comment_loader, read_new_comment
import asyncio
numberOfComments = 0
userdata = []
async def main():
    driver = init_comment_loader()
    while True:
        new_comment = read_new_comment(driver)

        if new_comment[0] != "":
            userdata.append(new_comment)
            gemini_input = system_prompt(userdata, numberOfComments)
        else:
            gemini_input = independent_prompt(userdata)

        response = await gen_gemini_response(gemini_input)
        response_elem = ["Xylo", response]
        userdata.append(response_elem)
        await speak_polly_response(response)

asyncio.run(main())