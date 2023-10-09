from similarity import assign_interest

interest = ['Generative AI','Trends','Llama','OpenAI']
title = 'Amazon to invest $2 billion into Anthropic to take on OpenAI'

print("Most relevant Interest:", interest[assign_interest(title,interest)])
