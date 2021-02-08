
import torch
import torch.nn as nn


def nothing(*x) : return *x

class Trainer:

    def __init__(self, epochs, mini_batch_size, device=None):
        self.epochs = epochs
        self.mini_batch_size = mini_batch_size
        self.device = device or 'cuda' if torch.cuda.is_available() else 'cpu' # TODO: multi cpu or multi gpu options

    def set_epochs(epochs) : self.epochs = epochs
    def set_mini_batch_size(mini_batch_size) : self.mini_batch_size = mini_batch_size
    def set_device(device) : self.device = device

    def train(self, data_loader, model, loss_funct, optim_funct, pre_proc=None, post_proc=None):
        pre_proc  = pre_proc or nothing # nothing = lambda x : x
        post_proc = post_proc or nothing

       #TODO: definir un estandar de comportamiento para los datos sacados ell data loader, seguramente mirar el tutorial de pyTorch

