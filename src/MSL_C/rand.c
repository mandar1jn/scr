#include "rand.h"

static unsigned long random_next = 1;

//LCG (linear congruential generator) RNG algorithm
int rand()
{
    random_next = random_next * 1103515245 + 12345;
    return ((random_next >> 16) & 0x7fff);
}

void srand(unsigned long seed)
{
    random_next = seed;
}
