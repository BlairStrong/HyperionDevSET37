# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy
nlp = spacy.load('en_core_web_sm')


#1.) inputting GP sentences
gp_1 = "The old man the boat"
gp_2 = "The cotton clothing is made of grows in Mississippi"
gp_3 = "We painted the wall with cracks"
gp_4 = "Fat people eat accumulates"
gp_5 = "That Jill is never here hurts"
gp_6 = "I know the words to that song about the queen don’t rhyme"
gp_7 = "She told me a little white lie will come back to haunt me"
gp_8 = "Have the students who failed the exam take the supplementary"
gp_9 = "Until the police arrest the drug dealers control the street"
gp_10 = "The man who hunts ducks out on weekends"
gp_11 = "The prime number few"
gp_12 = "The horse raced past the barn fell"

#GP sentence list
gardenpathSentances = [gp_1, gp_2, gp_3, gp_4, gp_5, gp_7, gp_8, gp_8, gp_9, gp_10, gp_11, gp_12]
for sentence in gardenpathSentances:
    print(sentence)
    doc = nlp(sentence)

    #tokenising the NL input
    #[(token, token.orth_, token.orth) for token in doc]
    #to print the tokenised input, uncomment line below:
    #print([(token, token.orth_, token.orth) for token in doc])


    #ENTITY RECOGNITION and TOKENISATION
    print([(token, token.label_, token.label) for token in doc.ents])

#entity label GPE found in gp_2 - this means Geopolitical Entity after a online search. expected.
#entity label DATE found in gp_10 - this seems intuitive . expected