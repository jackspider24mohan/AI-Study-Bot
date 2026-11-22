import torch

def test_torch_import():
    assert torch is not None

if __name__ == "__main__":
    test_torch_import()
    print("Torch imported successfully!")