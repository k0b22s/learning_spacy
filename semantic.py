# import spacy
import spacy

#run example extracts from task file
# ex. 1
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word2.similarity(word3))
print(word3.similarity(word1))

print("\n")

# ex.2
tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
print("\n")

# ex. 3
sentence_to_compare = "Why is cat on the car?"

sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "I/'ve lost my car in my car",
    "I/'d like my boat back",
    "I will name my dof Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)

print("\n")
# What I found interesting about cat monkey and banana

# What I found interesting is that the similarity between cat and apple is just a bit less than the similarity between monkey and apple
# whereas (as pointed out, the similarity between monkey and bananas are high). which shows that the stereotipical way of thinking that
# that humas ar famous for is programmed into spacy. Furhermore, monkey and cat are only a little bit hugher than monkey and banana, 
# but still very close.

# my ex, on tis topic
nlp2 = spacy.load("en_core_web_sm")
my_tokens = nlp2("sugar rock music  guitar powder")

for token1 in my_tokens:
    for token2 in my_tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
print("\n")

## Comparison between (en_core_web_sm) and (en_core_web_md):

# After looking at example.py, the most immediate thing to be picked up in the numbers is how they drop from running en_core_web_md to running 
# en_core_web_sm. It is clear from the start that en_core_web_md is able to pick up a lot more similarities between the three lists than en_core_web_sm. 
# But this is of course to be expected, considering that en_core_web_sm is a smaller module. There are many similarities between these two models, 
# considering that they are both english language models. However, the one fundamental difference as mentioned previously is the size. That is
# why en_core_web_md is able to pick up more similarities, it has access to a larger vocabulary, as well as better semantics.
