import numpy as np

def main(n, d):
    x = NeighborJoining(d,n)
    answer = {}
    for i, nodes in enumerate(x,start=0):
        temp = {}
        for j, w in nodes:
            v = w
            temp[j]=float(v)
        answer[i]=temp
    return answer


def NeighborJoining(d, n):
    DMat = np.array(d, dtype = float)
    TAdd = [Row for Row in range(n)]
    T = [[] for Row in range(n)]
    while True:
        if n == 2:
            T[len(T)-1].append((len(T)-2, DMat[0][1]))
            T[len(T)-2].append((len(T)-1, DMat[0][1]))
            return T

        TreeSize = len(T)
        TotalDistance = np.sum(DMat, axis = 0)
        
        #Variation from pseudocode
        #find elements i and j such that D'i,j is a minimum non-diagonal element of D'
        SD = (n-2)*DMat
        SD = SD - TotalDistance
        SD = SD - TotalDistance.reshape((n, 1))
        np.fill_diagonal(SD, 0.)
        Num = np.argmin(SD)
        Row = Num // n
        Col = Num % n
        
        Δ = (TotalDistance[Row] - TotalDistance[Col])/(n-2)
        LimbLengthi = (DMat[Row,Col]+Δ)/2
        LimbLengthj = (DMat[Row,Col]-Δ)/2
        TempD = (DMat[Row,:]+DMat[Col,:]-DMat[Row,Col])/2
        DMat = np.insert(DMat,n,TempD,axis=0)
        TempD = np.insert(TempD,n,0.,axis=0)
        DMat = np.insert(DMat,n,TempD,axis=1)
        DMat = np.delete(DMat,[Row,Col],0)
        DMat = np.delete(DMat,[Row,Col],1)

        #Done with calcs, modify tree
        #add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j)
        T.append([])
        T[TreeSize].append((TAdd[Row],LimbLengthi))
        T[TAdd[Row]].append((TreeSize,LimbLengthi))
        T[TreeSize].append((TAdd[Col],LimbLengthj))
        T[TAdd[Col]].append((TreeSize,LimbLengthj))

        #remove rows i and j from D
        #remove columns i and j from D
        if Row < Col:
            del TAdd[Col]
            del TAdd[Row]
        else:
            del TAdd[Row]
            del TAdd[Col]
        TAdd.append(TreeSize)
        n -= 1
    return T