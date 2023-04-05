#include <stdio.h>

int main()
{
    long long int b = 239809320265259;
    long int f = 2;
    long int g;

    while (b % f)
    {
        if (f <= b)
        {
            f++;
        }
        else {
            return (-1);
        }
    }

    g = b / f;
    printf("%lld = %ld * %ld\n", b, g, f);
    return (0);
}
