#!/usr/bin/sage

from sage.all import *
from sboxU import *
import time



if __name__ == '__main__':
    S_boxes = [
        [6, 11, 14, 0, 15, 1, 4, 3, 10, 13, 2, 8, 12, 7, 5, 9],
        [4, 6, 3, 8, 12, 2, 0, 10, 13, 9, 14, 11, 5, 15, 7, 1],
        [13, 1, 8, 9, 6, 14, 11, 3, 12, 4, 15, 5, 7, 2, 0, 10],
        [6, 14, 4, 10, 15, 11, 5, 8, 2, 0, 1, 9, 13, 3, 7, 12]
    ]
    print(differential_spectrum(S_boxes[0]))
    for i, S in enumerate(S_boxes, start=1):
        DDT = ddt(S)
        LAT = lat(S)
        # Дифференциальная равномерность
        print(DDT)
        print(LAT)
        diff_uniformity = max(DDT[a][b] for a in range(1, len(S)) for b in range(len(S))) / (2 ** 4)

        # Линейная равномерность(не уврен: что правильно)
        lin_uniformity = max(abs(LAT[u][v]) for u in range(1, len(S)) for v in range(len(S))) / (2 ** 4)
        print("S[{}] Diff: {}, Lin: {}".format(i, diff_uniformity, lin_uniformity))
        for j, SS in enumerate(S_boxes, start=1):
            print("Affine equivalency S[{}] and S[{}]: {}".format(i, j, len(affine_equivalence(S, SS)) != 0))

"""
Результат
S[1] Diff: 0.375, Lin: 0.75
Affine equivalency S[1] and S[1]: True
Affine equivalency S[1] and S[2]: False
Affine equivalency S[1] and S[3]: True
Affine equivalency S[1] and S[4]: False
S[2] Diff: 0.375, Lin: 0.75
Affine equivalency S[2] and S[1]: False
Affine equivalency S[2] and S[2]: True
Affine equivalency S[2] and S[3]: False
Affine equivalency S[2] and S[4]: True
S[3] Diff: 0.375, Lin: 0.75
Affine equivalency S[3] and S[1]: True
Affine equivalency S[3] and S[2]: False
Affine equivalency S[3] and S[3]: True
Affine equivalency S[3] and S[4]: False
S[4] Diff: 0.375, Lin: 0.75
Affine equivalency S[4] and S[1]: False
Affine equivalency S[4] and S[2]: True
Affine equivalency S[4] and S[3]: False
Affine equivalency S[4] and S[4]: True
"""