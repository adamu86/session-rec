import torch
print(f"Czy GPU jest dostępne? -> {torch.cuda.is_available()}")

print(f"Nazwa GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Brak GPU'}")
