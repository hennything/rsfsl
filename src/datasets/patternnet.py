from datasets.dataset_utils import load_dataset_from_pkl, load_dataset_from_from_folder 
from datasets.dataset_template import ColorDatasetInMemory, ColorDatasetOnDisk
import os

def get_Patternnet(args_per_set, setnames=["train", "val", "test"]):
    """
    Returns patternnet datasets.
    """
    datasets = {}
    for setname in setnames:
        args = args_per_set[setname]    
        data_path = os.path.abspath(args.data_path)
        filepath = os.path.join(data_path, "patternnet", "patternnet-cache-{0}.pkl".format(setname))
        data = load_dataset_from_pkl(filepath)
        dataset_class = ColorDatasetInMemory
            
        datasets[setname] = [data['image_data'], data['class_dict'], args, dataset_class]
        
    return datasets
