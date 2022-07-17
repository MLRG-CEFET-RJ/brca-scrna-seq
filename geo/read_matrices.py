from glob import glob
from scipy.sparse import vstack, save_npz
from scipy.io import mmread

DATA_FOLDER = 'data/GSE161529/RAW'

def read_gene_expression_matrices():
    mtx = None
    i = 1
    for filename in glob('*.mtx.gz', root_dir=DATA_FOLDER):
        print(f'Reading file {i} - {filename}')
        gene_data = mmread(f'{DATA_FOLDER}/{filename}')
        if mtx is not None:
            mtx = vstack((mtx, gene_data.transpose()))
        else:
            mtx = gene_data.transpose()
        i += 1
    print('Done reading!')
    return mtx


mtx = read_gene_expression_matrices()
save_npz('data.npz', mtx)