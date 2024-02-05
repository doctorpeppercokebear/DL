import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
manual_seed = 999
torch.manual_seed(manual_seed)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Define the generator
class Generator(nn.Module):
    def __init__(self, nz, ngf, nc):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(nz, 256),  # Input: noise vector (nz), Output: 256
            nn.ReLU(inplace=True),
            nn.Linear(256, 512),  # Input: 256, Output: 512
            nn.ReLU(inplace=True),
            nn.Linear(512, 784),  # Input: 512, Output: 28x28 image (784)
            nn.Tanh()  # Tanh activation to map values to [-1, 1] range
        )

    def forward(self, input):
        return self.main(input).view(-1, 1, 28, 28)


# Define the discriminator
class Discriminator(nn.Module):
    def __init__(self, nc, ndf):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(784, 512),  # Input: 28x28 image (784), Output: 512
            nn.ReLU(inplace=True),
            nn.Linear(512, 256),  # Input: 512, Output: 256
            nn.ReLU(inplace=True),
            nn.Linear(256, 1)  # Input: 256, Output: 1 (real/fake)
        )

    def forward(self, input):
        input = input.view(-1, 784)  # Flatten the input image
        return self.main(input)


# Set parameters
batch_size = 64
nz = 100  # Size of input noise vector
ngf = 64  # Number of generator features
ndf = 64  # Number of discriminator features
nc = 1  # Number of channels (grayscale)
lr = 0.0002  # Learning rate
epochs = 20  # Number of epochs

# Create the generator and discriminator
netG = Generator(nz, ngf, nc).to(device)
netD = Discriminator(nc, ndf).to(device)

# Initialize weights (custom function not provided here)
# netG.apply(weights_init)
# netD.apply(weights_init)

# Create optimizers
optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(0.5, 0.999))
optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(0.5, 0.999))

# Loss function
criterion = nn.MSELoss()

# Load data
transform = transforms.Compose([
    transforms.ToTensor(),  # Convert PIL Image to tensor
    transforms.Normalize((0.5,), (0.5,))  # Normalize to range [-1, 1]
])

dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=2)

# Training loop
for epoch in range(epochs):
    for i, data in enumerate(dataloader, 0):
        # Update discriminator
        netD.zero_grad()
        real_cpu = data[0].to(device)
        batch_size = real_cpu.size(0)
        label = torch.full((batch_size,), 1, dtype=torch.float, device=device)

        output = netD(real_cpu).view(-1)
        errD_real = criterion(output, label)
        errD_real.backward()
        D_x = output.mean().item()

        noise = torch.randn(batch_size, nz, device=device)
        fake = netG(noise)
        label.fill_(0)
        output = netD(fake.detach()).view(-1)
        errD_fake = criterion(output, label)
        errD_fake.backward()
        D_G_z1 = output.mean().item()
        errD = errD_real + errD_fake
        optimizerD.step()

        # Update generator
        netG.zero_grad()
        label.fill_(1)
        output = netD(fake).view(-1)
        errG = criterion(output, label)
        errG.backward()
        D_G_z2 = output.mean().item()
        optimizerG.step()

        # Print losses
        if i % 100 == 0:
            print('[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
                  % (epoch, epochs, i, len(dataloader),
                     errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

    # Save generated images (assuming img_list is defined)
    # if epoch % 10 == 0:
    #     with torch.no_grad():
    #         fake = netG(fixed_noise).detach().cpu()
    #     img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

# Show generated images
# plt.figure(figsize=(10,5))
# plt.title("Generated Images")
# plt.imshow(np.transpose(img_list[-1],(1,2,0)))
# plt.axis("off")
# plt.show()
