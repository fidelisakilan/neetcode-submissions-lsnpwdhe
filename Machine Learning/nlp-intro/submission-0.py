import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        combined = positive + negative
        words = set()
        for sentence in combined:
            for word in sentence.split():
                words.add(word)
        
        sorted_list = sorted(list(words))
        word_to_int = {}
        for i, c in enumerate(sorted_list):
            word_to_int[c] = i + 1
        
        unpadded = []
        for sentence in combined:
            encoded = []
            for word in sentence.split():
                encoded.append(word_to_int[word])
            unpadded.append(torch.tensor(encoded))
        return pad_sequence(unpadded, batch_first=True)
                
            

