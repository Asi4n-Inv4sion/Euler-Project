#include <stdio.h>

int even_fib_sum(int fib_1, int fib_2, int n, int sum)
{
    if ((fib_1 + fib_2 > 4000000))
    {
        return sum + 2;
    }
    else if ((fib_1 + fib_2) % 2 == 0)
    {
        return even_fib_sum(fib_2, fib_1 + fib_2, n + 1, sum + fib_1 + fib_2);
    }
    else
    {
        return even_fib_sum(fib_2, fib_1 + fib_2, n + 1, sum);
    }
}

int main()
{
    int sum = even_fib_sum(1, 2, 0, 0);
    printf("%d\n", sum);
}
