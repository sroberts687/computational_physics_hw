/*
Uses an array filled with random numbers,
finds the mean, print each element,and each element
higher than the mean

Adam Anthony
CS340 SP15
1/29/15
*/
#include <cstdlib>
#include <iostream>

#define ARRAYSIZE 20

void main()
{
	double nums[ARRAYSIZE];
	double average = 0;

	std::cout << "Array: " << std::endl;
	for (int i = 0; i < ARRAYSIZE; i++)
	{
		nums[i] = std::rand();
		average += nums[i];
		std::cout << nums[i] << std::endl;
	}

	average /= ARRAYSIZE;
	std::cout << "Larger than " << average << ": " << std::endl;
	for (int i = 0; i < ARRAYSIZE; i++)
	{
		if (nums[i] > average)
		{
			std::cout << nums[i] << std::endl;
		}
	}

	system("pause");
}