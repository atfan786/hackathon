'''
This example implements the approach shown in slide "Provided Example" of the challenge_introduction.pdf" slides.
Feel free to modify this code and use it as a first basis for your own approach.
'''

# load the large language model file
import pandas as pd
from llama_cpp import Llama

LLM = Llama(model_path="llama-2-7b-chat.Q5_K_M.gguf", n_ctx=2048)

# Read issue Dataframe from Pickle file
df = pd.read_pickle('github_issues.pkl')

# Only take issues, no pull requests
df = df.loc[df['pr'] == 'issue']

# Get random issue from database
sample = df.sample()
subject = sample['title'].values[0]
request = sample['body'].values[0]

print(30*'-')
print('Selected issue:')
print(f"Subject: {subject}")
print(f"Request: {request}")
print(30*'-')

# create a text prompt
prompt = f'The following is a customer request. Estimate the urgency of this request and translate it in a number between 1 (not urgent) and 5 (very urgent):\n \
"Subject: {subject} \
Request: {request}"'

# Generate a response (takes several seconds to minutes)
output = LLM(prompt, max_tokens=0)

# Display the response
print('Model output:')
print(output["choices"][0]["text"])