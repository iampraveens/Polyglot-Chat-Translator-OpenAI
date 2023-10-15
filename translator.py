import openai

def hinglish_translator(api_key, user_imput):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Translate the following English text to Hinglish: \"{user_imput}\"",
        max_tokens = 50,
        api_key = api_key
    )
    hinglish_text = response.choices[0].text.strip()
    return hinglish_text

def telugish_translator(api_key, user_imput):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Translate the following English text to Teluglish: \"{user_imput}\"",
        max_tokens = 50,
        api_key = api_key
    )
    telugish_text = response.choices[0].text.strip()
    return telugish_text

def thanglish_translator(api_key, user_imput):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Translate the following English text to Thanglish: \"{user_imput}\"",
        max_tokens = 50,
        api_key = api_key
    )
    thanglish_text = response.choices[0].text.strip()
    return thanglish_text
