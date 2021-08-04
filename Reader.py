from Mapper import getCentroids

#Check if distance of centroids and centroids1 is less than tolerance
def checkCentroidsDistance(centroids, centroids1):
    tol = 1e-4
    C1a = abs(centroids[0][0] - centroids1[0][0]) < tol
    C1b = abs(centroids[0][1] - centroids1[0][1]) < tol
    C1c = abs(centroids[0][2] - centroids1[0][2]) < tol
    C1d = abs(centroids[0][3] - centroids1[0][3]) < tol
    C1e = abs(centroids[0][4] - centroids1[0][4]) < tol
    C1f = abs(centroids[0][5] - centroids1[0][5]) < tol
    C1g = abs(centroids[0][6] - centroids1[0][6]) < tol

    C2a = abs(centroids[1][0] - centroids1[1][0]) < tol
    C2b = abs(centroids[1][1] - centroids1[1][1]) < tol
    C2c = abs(centroids[1][2] - centroids1[1][2]) < tol
    C2d = abs(centroids[1][3] - centroids1[1][3]) < tol
    C2e = abs(centroids[1][4] - centroids1[1][4]) < tol
    C2f = abs(centroids[1][5] - centroids1[1][5]) < tol
    C2g = abs(centroids[1][6] - centroids1[1][6]) < tol

    C3a = abs(centroids[2][0] - centroids1[2][0]) < tol
    C3b = abs(centroids[2][1] - centroids1[2][1]) < tol
    C3c = abs(centroids[2][2] - centroids1[2][2]) < tol
    C3d = abs(centroids[2][3] - centroids1[2][3]) < tol
    C3e = abs(centroids[2][4] - centroids1[2][4]) < tol
    C3f = abs(centroids[2][5] - centroids1[2][5]) < tol
    C3g = abs(centroids[2][6] - centroids1[2][6]) < tol

    C4a = abs(centroids[3][0] - centroids1[3][0]) < tol
    C4b = abs(centroids[3][1] - centroids1[3][1]) < tol
    C4c = abs(centroids[3][2] - centroids1[3][2]) < tol
    C4d = abs(centroids[3][3] - centroids1[3][3]) < tol
    C4e = abs(centroids[3][4] - centroids1[3][4]) < tol
    C4f = abs(centroids[3][5] - centroids1[3][5]) < tol
    C4g = abs(centroids[3][6] - centroids1[3][6]) < tol

    if C1a and C1b and C1c and C1d and C1e and C1f and C1g and C2a and C2b and C2c and C2d and C2e and C2f and C2g and C3a and C3b and C3c and C3d and C3e and C3f and C3g and C4a and C4b and C4c and C4d and C4e and C4f and C4g:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    checkCentroidsDistance(centroids, centroids1)
