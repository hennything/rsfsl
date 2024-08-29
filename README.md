# Few-Shot Learning in Remote Sensing

## Running Repository
### Dependecies

* numpy
* python 3.8+
* pytorch
* tqdm
* pillow
* scikit-learn
* gpytorch

To set up the specific conda environment run:
```
conda create -n ci_fsl python=3.8
conda activate ci_fsl
conda install pytorch torchvision -c pytorch
conda install gpytorch -c gpytorch
conda install -c conda-forge tqdm
conda install -c anaconda pillow scikit-learn
```

### Structure

The framework is structured as follows:

```
.
├── generator.py          # Experiment generator to reproduce settings from the paper
├── data/                 # Default data source
├── [experiments/]        # Default script, config and results destination
└── src
    ├── main.py           # Main program
    ├── datasets          # Code for loading datasets
    ├── models            # FSL methods, baselines, backbones
    ├── strategies        # Imbalance strategies
    ├── tasks             # Standard FSL, Imbalanced FSL tasks
    └── utils             # Utils, experiment builder, performance tracker, dataloader
```

### Data

See ```./data/README.md```

## Generating Main Experiments

To generate the experiment scripts and files for the main experiments in the paper:
```
python generator.py --imbalanced_supports
```
To generate the evaluation scripts for imbalanced support set:
```
python generator.py --imbalanced_supports --test
```

For ROS/ROS+ inference on imbalanced support sets run:
```
python generator.py --imbalanced_supports --inference
```

## Running main program

To run a specific experiment setting from a configuration file:
```
python src/main.py --args_file <CONFIGPATH> --gpu <GPU>
```
<!--
Arguments from the ```CONFIGPATH``` can be overwriten by arguments passed through the command line.

Run ```python src/main.py --help``` for general help

For sepecific model/task/stategy arguments substitute key words and run any of the following:

```
python src/main.py  --model <MODEL> --help_model
python src/main.py  --task <TASK> --help_task
python src/main.py  --strategy <STRATEGY> --help_stategy
python src/main.py  --model <MODEL>   --task <TASK>  --task <STRATEGY>   --help_all```
```
-->

____

### Contributions
This repository contains parts of code from the following GITHUB repositories:



____

### Attribution

We want to thank Eleni Triantafillou, Hae Beom Lee, Hayeon Lee, and the members of the Bayesian and Neural Systems group at the University of Edinburgh for valuable comments, suggestions, and discussions offered at various stages of this work. This work was supported by the EPSRC Centre for Doctoral Training in Robotics and Autonomous Systems, funded by the UK Engineering and Physical Sciences Research Council (Grant No. EP/S515061/1) and SeeByte Ltd, Edinburgh, UK.
