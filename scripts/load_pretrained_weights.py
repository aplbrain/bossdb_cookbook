#Loads the downloaded pretrained weights into the specified model.
import torch

# task specification 

def load_weights(model_name, task, model_object):
    """Load pre-trained weights into a given model object based on the model name and task.

    This function constructs the path to the pre-trained model weights based on the provided model name
    and task. It then loads the weights into the provided model object.

    Args:
        model_name (str): Name of the model ('unet' or other specific types).
        task (str): The specific task for which the model was trained.
        model_object (torch.nn.Module): The model object into which the weights will be loaded.

    Returns:
        torch.nn.Module: The model object with the loaded weights.

    Raises:
        FileNotFoundError: If the specified model weights file is not found.
    """
    
    # Base path to the pretrained models
    base_path = "../Notebooks/pretrained_model_weights/"
    
    # Construct the path to the model weights based on the model_name and task
    if model_name == 'unet':
        model_path = base_path + 'UNet_2D_' + str(task) + '.pt'
    else:
        model_path = base_path + 'UNet_2D_' + str(model_name) + '_' + str(task) + '.pt'
    
    # Load the model weights
    checkpoint = torch.load(model_path)
    model_object.load_state_dict(checkpoint)
    
    # Print a success message
    if model_name == 'unet':
        print(f'Successfully loaded pre-trained weights into the {model_name} Model')
    else:
        print(f'Successfully loaded pre-trained weights into the unet_{model_name} Model')
    
    return model_object
