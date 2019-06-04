# Solution is available in the other "solution.py" tab
import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    exp_values = map(lambda yi: np.exp(yi), x)
    exp_values = list(exp_values)
    total = sum(exp_values)

    soft_max = map(lambda x: x / total, exp_values)

    return list(soft_max)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))
