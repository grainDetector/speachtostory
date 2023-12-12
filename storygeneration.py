import openai
# OpenAI API Key
API_key = "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"
openai.api_key = API_key

def storygen(prompt):
    print(prompt)
    query = openai.Completion.create(
		engine="text-davinci-003",
		prompt=f"create an acceptance criteria in Gherkins from the below requirements\n {prompt}",
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.7,
	)
    response = query.choices[0].text
    print(response)
    return response

