#UNet model. From: https://github.com/johschmidt42/PyTorch-2D-3D-UNet-Tutorial
import torch
import os
import sys                            

def load_model(network_config, device):
    """Load a specific U-Net model based on the provided configuration.

    This function dynamically imports and initializes a U-Net model based on the model type specified
    in the network configuration. Supported model types include attention, residual, depth, and the
    standard U-Net.

    Args:
        network_config (dict): Configuration dictionary specifying model type and other parameters.
        device (torch.device): The device (CPU or GPU) where the model will be loaded.

    Returns:
        UNet: An instance of the specified U-Net model initialized with the given parameters.

    Raises:
        ImportError: If the specified model type is not recognized.
    """

    # Dynamically import the appropriate UNet based on model_type
    if network_config["model_type"]  == "attention":
        from models.unet_attention import UNet
    elif network_config["model_type"] == "residual":
        from models.unet_residual import UNet
    elif network_config["model_type"] == "depth":
        from models.unet_depth import UNet
    else:  # default to the standard UNet
        from models.unet import UNet

    print(f'loading {network_config["model"]} model')
    model = UNet(in_channels=network_config['in_channels'],
                 out_channels=network_config['classes'],
                 n_blocks=network_config['n_blocks'],
                 start_filters=network_config['start_filters'],
                 activation=network_config['activation'],
                 normalization=network_config['normalization'],
                 conv_mode=network_config['conv_mode'],
                 dim=network_config['dim']).to(device)

    return model



    
