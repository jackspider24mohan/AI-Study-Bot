
import torch


def test_torch_import():
    """Verify that PyTorch is installed and can be imported."""
    assert torch is not None
    assert isinstance(torch.__version__, str)

    print(f"PyTorch version: {torch.__version__}")
    print("Torch imported successfully!")


if __name__ == "__main__":
    test_torch_import()
