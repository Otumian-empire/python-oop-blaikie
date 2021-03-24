# Object serialization
# Serialization = persistent storage (to disk)
# Relational storage writes data to tables

import pickle

# data = [1, 2, 3, 4]

# with open("datafile.txt", 'w') as fp:
#     pickle.dump(data, fp)

# with open("datafile.txt") as fp:
#     print(pickle.load(fp))


# loads and dumps
pdump = pickle.dumps(['1', 2])
# print(pdump)

pload = pickle.loads(pdump)
# print(pload)
