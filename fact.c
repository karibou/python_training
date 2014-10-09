#include "stdio.h"

unsigned long fact(unsigned long value) {

    if ( value == 1 ) {
        return 1;
        } else {
        return value * fact(value - 1);
    }
}


main(int argc, char *argv[]) {

    unsigned long value = atoi(argv[1]);
    printf("Factorielle %li\n",fact(value));
    }
