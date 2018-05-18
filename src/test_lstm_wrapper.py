from algorithm.bac import LSTM
import numpy as np
from lample_lstm_tagger.lstm_wrapper import data_to_lstm_format
import pandas as pd
from sklearn.metrics import accuracy_score

savepath = '../../data/bayesian_annotator_combination/data/ner/'  # location to save our csv files to

text = pd.read_csv(savepath + '/task1_test_text.csv', skip_blank_lines=False, header=None)
text = text.fillna(' ').values

print('loading doc_starts for task1 test...')
doc_start = pd.read_csv(savepath + '/task1_test_doc_start.csv', skip_blank_lines=False, header=None).values

print('loading ground truth for task1 test...')
gt = pd.read_csv(savepath + '/task1_test_gt.csv', skip_blank_lines=False, header=None).values

N = len(text)
nclasses = len(np.unique(gt))

# N = 2
# text = ['octopus', 'mesmerise']
# doc_start = [1, 1]
# nclasses = 2

# dev_sentences, _, _ = data_to_lstm_format(3, np.array(['octopus', 'octopus', 'mesmerise']),
#                                     np.array([1, 1, 1]),
#                                     np.array([1, 1, 0]), 2)

dev_sentences, _, _ = data_to_lstm_format(N, text, doc_start, gt, nclasses, include_missing=False)

Et = np.zeros((N, nclasses))
Et[np.arange(N), gt.flatten()] = 1

lstm = LSTM()

lstm.init(None, N, text, doc_start, nclasses, dev_sentences)

n_epochs = 25
for n in range(n_epochs):
    prob = lstm.predict(Et)
    print('training set accuracy = %f' % accuracy_score(gt.flatten(), np.argmax(prob, 1)))

print(prob)