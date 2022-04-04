#? Note: Ensure conda environment is activated with rdkit. For example:
# conda create -c conda-forge -n yogimass_env rdkit
# conda init
# conda activate yogimass_env

# RDKit can be used to draw SMILES:
def draw_compound_from_smiles(smiles):
    '''
    Uses rdkit to draw a molfile compound from smiles.

    '''
    import rdkit
    from rdkit import Chem
    from rdkit.Chem import Draw
    mol_file = Chem.MolFromSmiles(smiles)
    return Draw.MolToFile(mol_file, f'{smiles}.png')

# RDKit can be used to draw SMILES from matchms scores object:
def molecules_from_scores(scores_query):
    '''
    Export chemical structures of top 10 best matches to png files from matchms scores object
    '''
    from rdkit import Chem
    from rdkit.Chem import Draw
    for i, smiles in enumerate([x[0].get('smiles') for x in scores_query]):
        m = Chem.MolFromSmiles(smiles)
        return Draw.MolToFile(m, f'match_compound_{i}.png')
