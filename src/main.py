from utils.utils import set_torch_seed, set_gpu, get_tasks, get_data, get_model, get_backbone, get_strategy
from utils.utils import compress_args, get_args, torch_summarize
from utils.builder import ExperimentBuilder
from utils.bunch import bunch
import sys
import pprint
import torch
import GPUtil

if __name__ == '__main__':

    def print_gpu_status():
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print(f"GPU ID: {gpu.id}, Name: {gpu.name}, Load: {gpu.load * 100:.1f}%, Free Memory: {gpu.memoryFree}MB, Used Memory: {gpu.memoryUsed}MB, Total Memory: {gpu.memoryTotal}MB, Temperature: {gpu.temperature}°C")

    # Print GPU status before clearing cache
    print("Before clearing cache:")
    print_gpu_status()

    # Clear GPU cache in PyTorch
    torch.cuda.empty_cache()

    # Print GPU status after clearing cache
    print("After clearing cache:")
    print_gpu_status()


    torch.cuda.empty_cache()
    
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print(f"GPU ID: {gpu.id}, Name: {gpu.name}, Memory Free: {gpu.memoryFree}MB, Memory Total: {gpu.memoryTotal}MB")

    # Select the GPU with the most free memory
    best_gpu = max(gpus, key=lambda gpu: gpu.memoryFree)

    # Set the device to the selected GPU
    device = torch.device(f"cuda:{best_gpu.id}")
    print(device)
    # Example usage
    # print("PyTorch version:", torch.__version__)
    # print("CUDA available:", torch.cuda.is_available())
    # print("CUDA version:", torch.version.cuda)
    # if torch.cuda.is_available():
    #     print("GPU name:", torch.cuda.get_device_name(0))

    # for i in range(torch.cuda.device_count()):
    #     print(torch.cuda.get_device_properties(i).name) 
    torch.cuda.empty_cache()   
    args, excluded_args, parser = get_args()
    args = bunch.bunchify(args)
    
    set_torch_seed(args.seed)
    # device = set_gpu(args.gpu)
    
    datasets = get_data(args)
    tasks    = get_tasks(args)
    backbone = get_backbone(args, device)
    strategy = get_strategy(args, device)
    model    = get_model(backbone, tasks, datasets, strategy, args, device)
    
    compressed_args = compress_args(bunch.unbunchify(args), parser)
    print(" ----------------- FULL ARGS (COMPACT) ----------------")
    pprint.pprint(compressed_args, indent=2)
    print(" ------------------------------------------------------")
    print(" ------------------ UNRECOGNISED ARGS -----------------")
    pprint.pprint(excluded_args, indent=2)
    print(" ------------------------------------------------------")
    
    system = ExperimentBuilder(model, tasks, datasets, device, args)
    system.load_pretrained()
    system.train_model()
    system.evaluate_model()
        
