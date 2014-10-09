#include "stdio.h"

int fact(int value) {

    if ( value == 1 ) {
        return 1;
        } else {
        return value * fact(value - 1);
    }
}


main(int argc, char *argv) {

    printf("Factorielle % d\n",fact(5));
    }
