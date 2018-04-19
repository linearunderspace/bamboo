#!/usr/bin/env python

import sys

sys.path.append('/home/marco')
import bamboo

class Collection(object):
    """
    Set of FCS experiments

    Attributes
    ----------
    """
    def __init__(self, file_input = None):
        """
        Parameters
        ----------
        file_input: None / str
            Name of the input file with the list of FCS experiments
            Format of the file:
                file_name, condition_1, condition_2, ...
        """
        # LEGGI DATI DA FILE E CREA STRUTTURA DATI INTERNA
        pass
#    def add_experiment_from_file(self, file_name):
#        """
#        """
#    def add_experiment_from_data(self, experiment):
#        """
#        Parameters
#        ----------
#        experiment: Experiment
#        """
#    def get_index_experiment(self, name_experiment):
#        """
#        Parameters
#        ----------
#        name_experiment: str
#            Name of the experiment
#        """
#        # ...
#        return ind_start, ind_end
#    def get_array_experiment(self, name_experiment, array):
#        """
#        From an array select only the elements of experiment name_experiment
#
#        Parameters
#        ----------
#        name_experiment: str
#            Name of the experiment
#        array: np.array
#            Input array
#
#        Return
#        ------
#        np.array
#            Array of the selected elements
#        """
#        ind_start, ind_end = self.get_index_experiment(name_experiment)
#        return array[ind_start:ind_end]
#    def n_experiments(self):
#        """
#        Return
#        ------
#        int
#            Number of experiments
#        """
#    def delete_samples(self, samples_2_delete):
#        """
#        Parameters
#        ----------
#        samples_2_delete: np.array
#            size: <number of samples>
#            values: bool
#                True: delete
#                False: keep
#
#        Return
#        ------
#        Experiment
#            New Collection object with some samples deleted
#        """
#        new_collection = bamboo.data.Collection()
#        # for experiment in  [Experiment in self]:
#            samples_2_delete_experiment = self.get_array_experiment(name_experiment, samples_2_delete)
#            new_collection.add_experiment_from_data(experiment.delete_samples(samples_2_delete_experiment))
#        return new_collection
#    def get_np_array(self, conditions = None):
#        """
#        Parameters
#        ----------
#        conditions: None / list
#            If None return data of all experiments
#            If list return data from the conditions in the list
#        Return
#        ------
#        np.array
#            Data in the selected experiments
#        """
    def __str__(self):
        output = 'Collection of {0:d} experiments'.format(self.n_experiments())
        return output
#
#class Experiment(object):
#    def __init__(self, file_name = None):
#        """
#        Parameters
#        ----------
#        file_name: str
#            Name of FCS file
#        """
#    def n_samples(self):
#        """
#        Return
#        ------
#        int
#            Number of samples
#        """
#    def n_features(self):
#        """
#        Return
#        ------
#        int
#            Number of feautures
#        """
#    def get_np_array(self):
#        """
#        Return
#        ------
#        np.array
#            Data in the experiment
#        """
#    def delete_samples(self, samples_2_delete):
#        """
#        Parameters
#        ----------
#        samples_2_delete: np.array
#            size: <number of samples>
#            values: bool
#                True: delete
#                False: keep
#
#        Return
#        ------
#        Experiment
#            New experiment object with some samples deleted
#        """
#        if self.n_samples() != len(samples_2_delete):
#            raise ValueError('ERROR: wrong parameter in delete_samples')
#        #...
#        return new_experiment
#    def keep_samples(self, samples_2_keep):
#        """
#        Parameters
#        ----------
#        samples_2_keep: np.array
#            size: <number of samples>
#            values: bool
#                True: keep
#                False: Delete
#
#        Return
#        ------
#        Experiment
#            New experiment object with only the selected samples
#        """
#        return self.delete_samples(np.not(samples_2_keep))

if __name__ == '__main__':
    print 'Testing data.py...'
    # FAI UNA ROUTINE CHE LEGGE, CANCELLA DELLE RIGHE, ...
    C = bamboo.data.Collection('./data/input.txt')
    print C
