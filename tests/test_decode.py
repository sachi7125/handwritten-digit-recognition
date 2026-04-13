from src.decode import ctc_greedy_decode
import torch

def test_decode_basic():
    T, C = 5, 11
    logits = torch.full((T, 1, C), -10.0)

    logits[0, 0, 1] = 5
    logits[1, 0, 1] = 5
    logits[2, 0, 10] = 5
    logits[3, 0, 2] = 5
    logits[4, 0, 3] = 5

    assert ctc_greedy_decode(logits) == "123"