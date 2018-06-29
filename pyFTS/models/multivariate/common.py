import numpy as np
import pandas as pd


def fuzzyfy_instance(data_point, var, alpha_cut=0.0):
    mv = np.array([var.partitioner.sets[key].membership(data_point) for key in var.partitioner.ordered_sets])
    ix = np.ravel(np.argwhere(mv > alpha_cut))
    sets = [(var.name, var.partitioner.ordered_sets[i]) for i in ix]
    return sets


