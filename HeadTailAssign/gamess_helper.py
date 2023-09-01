class GamessHelper:
    '''
    Class related to Non-public methods which are GAMESS class helpers.

    Methods
        _generate_mol_with_atom_index(self, mol) = Non-public method. This function returns the atom indexes to be included in the
                                                   2D monomer representation to be saved as a png figure file.
        _generate_gamess_input_file(self, runtype, basis, filename) = Non-public method. This function returns the gamess input file.
    '''


    def _generate_mol_with_atom_index(self, mol):
        '''
        Non-public method. This function returns the atom indexes to be included in the
        2D monomer representation to be saved as a png figure file.

        Arguments:
            mol(Mol object) = Mol object generated by RDKit.
        '''
        atoms = mol.GetNumAtoms()
        for idx in range( atoms ):
            molecule = mol.GetAtomWithIdx( idx ).SetProp( 'molAtomMapNumber', str( mol.GetAtomWithIdx( idx ).GetIdx() ) )
        return molecule

    def _generate_gamess_input_file(self, name_dir, runtype, basis, filename):
        '''
        Non-public method. This function returns the gamess input file.

        Arguments:
            runtype(str) = GAMESS input.
            basis(str) = GAMESS input. 
            filename(str) = Name of the files that will be modified.
        '''   

        input_file = open(filename+".xyz", "r", encoding="utf-8")
        output_file = open(filename+".inp", "w", encoding="utf-8")

        if (runtype == 'scf' and basis == 'sto3g'):
            output_file.write('!   File created by MacMolPlt 7.7.2 \n')
            output_file.write(' $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 $END \n')
            output_file.write(' $SYSTEM TIMLIM=525600 MWORDS=50 MEMDDI=200 $END \n')
            output_file.write(' $BASIS GBASIS=STO NGAUSS=3 $END \n')
            output_file.write(' $SCF DIRSCF=.TRUE. $END')
            output_file.write('\n')

        if (runtype == 'scf' and basis == 'pm3'):
            output_file.write('!   File created by MacMolPlt 7.7.2 \n')
            output_file.write(' $CONTRL SCFTYP=RHF RUNTYP=ENERGY MAXIT=30 MULT=1 $END \n')
            output_file.write(' $SYSTEM TIMLIM=525600 MWORDS=50 MEMDDI=200  $END \n')
            output_file.write(' $BASIS GBASIS=PM3 $END \n')
            output_file.write(' $SCF DIRSCF=.TRUE. $END')
            output_file.write('\n')

        if (runtype == 'opt' and basis == 'sto3g'):
            output_file.write('!   File created by MacMolPlt 7.7.2 \n')
            output_file.write(' $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 $END \n')
            output_file.write(' $SYSTEM TIMLIM=525600 MWORDS=50 MEMDDI=200  $END \n')
            output_file.write(' $BASIS GBASIS=STO NGAUSS=3 $END \n')
            output_file.write(' $SCF DIRSCF=.TRUE. $END')
            output_file.write('\n')

        if (runtype == 'opt' and basis == 'pm3'):
            output_file.write('!   File created by MacMolPlt 7.7.2 \n')
            output_file.write(' $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE MAXIT=30 MULT=1 $END \n')
            output_file.write(' $SYSTEM TIMLIM=525600 MWORDS=50 MEMDDI=200  $END \n')
            output_file.write(' $BASIS GBASIS=PM3 $END \n')
            output_file.write(' $SCF DIRSCF=.TRUE. $END')
            output_file.write('\n')

        output_file.write(' $DATA\n')
        output_file.write('Title\n')
        output_file.write('C1\n')

        i = 0
        atomic_number_dictionary = {'H':1.0,'He':2.0,'B':5.0,'C':6.0,'N':7.0,'O':8.0,'F':9.0,'Na':11.0,'Al':13.0,'Si':14.0,'P':15.0,'S':16.0,'Cl':17.0,'K':19.0,'Ca':20.0,'Br':35.0, 'Li':3.0, 'Sn': 50.0, 'I': 53.0, 'Mg': 12.0, 'Ti': 22.0, 'Pr': 59.0, 'Nd': 60.0, 'Sb': 51.0, 'Ag': 47.0, 'Zn': 30.0, 'Ge': 32.0, 'Ni': 28.0, 'Pd': 46.0, 'Ba': 56.0, 'W': 74.0}
        for line in input_file:
            lin = line.split()
            i = i + 1
            if (i >= 3 and len(lin) == 4):
                atomic_number = atomic_number_dictionary[lin[0]]
                output_file.write(str(lin[0])+' '+str(atomic_number)+' '+str(lin[1])+' '+str(lin[2])+' '+str(lin[3])+'\n')

        output_file.write(' $END\n')
        output_file.close()
        input_file.close()
            
        return