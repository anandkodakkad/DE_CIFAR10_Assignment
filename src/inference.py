from .model import getModel
from pathlib import Path
import PIL
import torch
from torchvision import  transforms


class Inference:
    def __init__(self, save_model_filename="saved_weights.pt"):
        self.classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship','truck']
        self.model = getModel(training=False,num_classes=len(self.classes))
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.load_state_dict(torch.load(f"./src/saved_weights/{save_model_filename}",map_location=device))
        return None 

    def __call__(self,image):
        if isinstance(image,(Path,str)):
            image = PIL.Image.open(image).convert("RGB")
        elif not isinstance(image,PIL.JpegImagePlugin.JpegImageFile): 
            raise Exception("must be PIL image or path ")
            #transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
        #image_input = transforms.ToTensor()(image).unsqueeze(0)
        image_input = transforms.ToTensor()(image)
        image_input = transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))(image_input)
        image_input = image_input.unsqueeze(0)

        with torch.no_grad():
            out = self.model(image_input).squeeze(0)
            print('Label-----------',torch.argmax(out).item)
            prob = torch.argmax(out).item()
            return self.classes[prob]
