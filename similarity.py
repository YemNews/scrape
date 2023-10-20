# from sentence_transformers import SentenceTransformer, util
# import logging

# model = SentenceTransformer("distilbert-base-nli-mean-tokens")


# def assign_interest(title: str, interests: list) -> int:

#     interest_embeddings = model.encode(interests)
#     title_embeddings = model.encode(title)

#     max_similarity = 0
#     max_similarity_index = 0

#     for i in range(len(interest_embeddings)):
#         curr_similarity = util.pytorch_cos_sim(interest_embeddings[i], title_embeddings)
#         if curr_similarity > max_similarity:
#             max_similarity = curr_similarity
#             max_similarity_index = i

#     if max_similarity < 0.6:
#         return ""
#     else:
#         return interests[max_similarity_index]
