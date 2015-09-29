import pickle

algo_list = []


algo = {'name': 'MNI 152',
  'align_algo': 'noalign',
  'nfeature': '813',
  'kernel': None,
  'rand': False
}
algo_list.append(algo)

algo = {'name': 'HA (813)',
  'align_algo': 'ha',
  'nfeature': '813',
  'kernel': None,
  'rand': False
}
algo_list.append(algo)

algo = {
  'name': 'pHA 400',
  'align_algo': 'pha_em',
  'nfeature': '400',
  'kernel': None,
  'rand': True
}
algo_list.append(algo)

algo = {
  'name': 'PCA 400',
  'align_algo': 'ppca2',
  'nfeature': '400',
  'kernel': None,
  'rand': False
}
algo_list.append(algo)


algo = {
  'name': 'ICA 400',
  'align_algo': 'pica2',
  'nfeature': '400',
  'kernel': None,
  'rand': True
}
algo_list.append(algo)

# write python dict to a file
output = open('algo_list.pkl', 'wb')
pickle.dump(algo_list, output)
output.close()

# read python dict back from the file
pkl_file = open('algo_list.pkl', 'rb')
algo_list_out = pickle.load(pkl_file)
pkl_file.close()

print algo_list