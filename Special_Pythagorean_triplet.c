#include <stdio.h>

int isTriplet (int a, int b, int c ) {
    if (a*a + b*b == c*c) {
        return 0;
    }
    return -1;
}

int main(int argc, char *argv[])
{
    int count = 1000;
    int i = 1;
    int j = 1;
    int k = 1;

    for(i = 1; i < count; i++) {
        for(j = 1; j < count; j++) {
            for(k = 1; k < count; k++) {
                if (isTriplet(i,j,k) == 0) {
                    if ((i+j+k) == count) {
                        printf("%d\n", i*j*k);
                        return(0);
                    }
                }
            }
        }
    }
}

