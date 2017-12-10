import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
 
    #for sentence in test_set.sentences_index:
    #    sent_dict = dict()
    #    for word_id in test_set.sentences_index[sentence]:
    #        word = test_set.wordlist[word_id]
    #        try:
    #            model = models[word]
    #            X,L = test_set.get_item_Xlengths(word_id)
    #            score = model.score(X,L)
    #            
    #        sent_dict[word] = score
    #    print(sent_dict)
    #    probabilities.append(sent_dict)
    #    print('\n')
    
    for word_id in [i for i,word in enumerate(test_set.wordlist)]:
        word_dict = dict()
        for key, model in models.items():
            try:
                X,L = test_set.get_item_Xlengths(word_id)
                score = model.score(X,L)
            except:
                score = float("-inf")
            
            word_dict[key] = score
            
        probabilities.append(word_dict)
        guesses.append(max(word_dict, key=word_dict.get))
    
    return (probabilities, guesses)
        
      