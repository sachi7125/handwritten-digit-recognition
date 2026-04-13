DIGITS = "0123456789"

idx_to_char = {i: c for i, c in enumerate(DIGITS)}
blank_idx = len(DIGITS)

def ctc_greedy_decode(logits):
    preds = logits.argmax(-1).squeeze(1).tolist()
    
    output = []
    prev = -1
    
    for p in preds:
        if p != prev and p != blank_idx:
            output.append(idx_to_char[p])
        prev = p
    
    return "".join(output)