/*Epsilon.cpp

Program to find and print the percision of the double primitive
type.

Adam Anthony
CS340 SP15
2/3/15
*/

#include <iostream>

using namespace std;

void main()
{
	double epsilon = 1;
	double number = 1;

	//loop until epsilon is too small to signifigantly change number
	while (epsilon + number != number)
	{
		epsilon /= 10;
	}

	//print epsilon
	cout << "Epsilon: " << epsilon << endl;

	system("pause");		
}