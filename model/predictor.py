import torch
from torchvision import transforms
from torchvision.models import resnet18


def get_model() -> torch.nn.Module:
    model = resnet18()
    last_layer_features_in = model.fc.in_features
    model.fc = torch.nn.Linear(last_layer_features_in, 10)
    return model


class MyModel:
    def __init__(self):
        self.model = get_model()
        input_size = 224
        self.transforms = transforms.Compose([
            transforms.Resize(input_size),
            transforms.CenterCrop(input_size),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def load_model(self):
        self.model.load_state_dict(torch.load("finetuned_model.pth"), strict=False)

    def __call__(self, data: torch.FloatTensor):
        print(data.shape, data[0, 0])
        with torch.no_grad():
            resized_data = self.transforms(data)
            prediction = self.model(resized_data)

            return prediction


model = MyModel()
model.load_model()
