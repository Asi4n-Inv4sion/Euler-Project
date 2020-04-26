/*
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
*/
#include <iostream>

long long int sequence(long long int n)
{
    if (n % 2 == 0)
    {
        n = n/2;
    }
    else
    {
        n = 3*n + 1;
    }
    return n;
}

int main()
{
    long long int chain_num;
    long long int i;
    int longest_counter = 1;
    for (i = 999999; i > 1; i--)
    {
        long long int current_chain = i;
        int counter = 1;

        while (current_chain != 1)
        {
            current_chain = sequence(current_chain);
            counter++;
        }

        if (counter > longest_counter)
        {
            longest_counter = counter;
            chain_num = i;
        }
    }

    std::cout << chain_num;
}
