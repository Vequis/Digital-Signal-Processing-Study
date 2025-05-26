# def split_signal(x, M, OL, w):
#     """
#     Split signal into blocks of size M with overlap OL and window w
#     """
#     N = len(x)
#     size_intersection = int(M*OL)

#     X_b = []
#     for i in range(0, N, M+size_intersection):
#         if (i + M > N):
#             break
#         frame = x[i:i+M].copy()
#         if (i + M + size_intersection < N and size_intersection > 0):
#             frame[-size_intersection:] += x[i+M:i+M+size_intersection]

#         X_b.append(frame * w)

#     return X_b
        
import numpy as np

def split_signal(x, M, OL, w):
    """
    Divide o sinal x em blocos de tamanho M com sobreposição OL e janela w
    """

    # k = (len(x) - M) // int(M * (1 - OL)) + 1
    step = int(M * (1 - OL))
    num_blocks = (len(x) - M) // step + 1
    blocks = np.zeros((num_blocks, M))
    
    for i in range(num_blocks):
        start = i * step + 1
        end = start + M
        blocks[i, :] = x[start:end] * w
    
    return blocks
