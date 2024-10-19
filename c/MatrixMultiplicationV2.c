#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define n 1024
double a[n][n];
double b[n][n];
double c[n][n];

struct timeval start, stop;

int main() {
    // Initialize matrices
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            a[i][j] = (double) rand() / RAND_MAX;
            b[i][j] = (double) rand() / RAND_MAX;
            c[i][j] = 0;
        }
    }
    
    gettimeofday(&start, NULL);
    
    // Matrix multiplication with loop unrolling
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            c[i][j] = 0; // Initialize result
            for (int k = 0; k < n; k += 2) {
                c[i][j] += a[i][k] * b[k][j];
                if (k + 1 < n) {
                    c[i][j] += a[i][k + 1] * b[k + 1][j];
                }
            }
        }
    }
    
    gettimeofday(&stop, NULL);
    double diff = stop.tv_sec - start.tv_sec
                + 1e-6 * (stop.tv_usec - start.tv_usec);
    printf("%0.6f\n", diff);
    
    return 0;
}
