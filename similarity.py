from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distilbert-base-nli-mean-tokens')


def assign_interest(title: str, interests: list) -> int:

    interest_embeddings = model.encode(interests)
    title_embeddings = model.encode(title)

    max_similarity = 0
    max_similarity_index = 0

    for i in range(len(interest_embeddings)):
        curr_similarity = util.pytorch_cos_sim(interest_embeddings[i],title_embeddings)
        print(curr_similarity)
        if curr_similarity > max_similarity:
            max_similarity = curr_similarity
            max_similarity_index = i

    # print('Max similarity: ', max_similarity)
    # print('Max similarity Index: ', max_similarity_index)

    return max_similarity_index


interest = ['Generative AI','Trends','Llama','OpenAI']
title = 'Amazon to invest $2 billion into Anthropic to take on OpenAI'

print("Most relevant Interest:", interest[assign_interest(title,interest)])

