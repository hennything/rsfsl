from datasets.dataset_utils import load_dataset_from_pkl, load_dataset_from_from_folder 
from datasets.dataset_template import ColorDatasetInMemory, ColorDatasetOnDisk
from datasets.ucmerced import get_Ucm
from datasets.aid import get_Aid
from datasets.whurs19 import get_Whurs19
from datasets.patternnet import get_Patternnet
from datasets.resisc45 import get_Resisc45
import os

def get_Resisc45_to_Ucm(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Resisc45(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Ucm(args_per_set, setnames=["test"]))
    return datasets

def get_Resisc45_to_Aid(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Resisc45(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Aid(args_per_set, setnames=["test"]))
    return datasets

def get_Resisc45_to_Whurs19(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Resisc45(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Whurs19(args_per_set, setnames=["test"]))
    return datasets

def get_Resisc45_to_Patternnet(args_per_set):
    """
    Returns whurs19 datasets.
    """
    datasets = {}
    datasets.update(get_Resisc45(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Patternnet(args_per_set, setnames=["test"]))
    return datasets

def get_Ucm_to_Resisc45(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Ucm(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Resisc45(args_per_set, setnames=["test"]))
    return datasets

def get_Ucm_to_Aid(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Ucm(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Aid(args_per_set, setnames=["test"]))
    return datasets

def get_Ucm_to_Whurs19(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Ucm(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Whurs19(args_per_set, setnames=["test"]))
    return datasets

def get_Ucm_to_Patternnet(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Ucm(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Patternnet(args_per_set, setnames=["test"]))
    return datasets

def get_Aid_to_Resisc45(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Aid(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Resisc45(args_per_set, setnames=["test"]))
    return datasets

def get_Aid_to_Ucm(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Aid(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Ucm(args_per_set, setnames=["test"]))
    return datasets

def get_Aid_to_Whurs19(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Aid(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Whurs19(args_per_set, setnames=["test"]))
    return datasets

def get_Aid_to_Patternnet(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Aid(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Patternnet(args_per_set, setnames=["test"]))
    return datasets

def get_Whurs19_to_Resisc45(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Whurs19(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Resisc45(args_per_set, setnames=["test"]))
    return datasets

def get_Whurs19_to_Ucm(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Whurs19(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Ucm(args_per_set, setnames=["test"]))
    return datasets

def get_Whurs19_to_Aid(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Whurs19(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Aid(args_per_set, setnames=["test"]))
    return datasets

def get_Whurs19_to_Patternnet(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Whurs19(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Patternnet(args_per_set, setnames=["test"]))
    return datasets

def get_Patternnet_to_Resisc45(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Patternnet(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Resisc45(args_per_set, setnames=["test"]))
    return datasets

def get_Patternnet_to_Ucm(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Patternnet(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Ucm(args_per_set, setnames=["test"]))
    return datasets

def get_Patternnet_to_Aid(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Patternnet(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Aid(args_per_set, setnames=["test"]))
    return datasets

def get_Patternnet_to_Whurs19(args_per_set):
    """
    """
    datasets = {}
    datasets.update(get_Patternnet(args_per_set, setnames=["train", "val"]))
    datasets.update(get_Whurs19(args_per_set, setnames=["test"]))
    return datasets
