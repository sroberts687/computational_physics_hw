///*Bisection and FP Method.cpp
//Uses a function defined in f and the interval defined as constants
//to calculate the root of a function across the interval.
//
//Assumes f(A) and f(B) have different signs.
//
//Adam Anthony
//CS340 SP15
//2/9/15
//*/
//#include <iostream>
//#include <cmath>
//#include <iomanip>
//
////bounds of the interval
//#define A 2
//#define B 3
//#define TOL 1E-4
//using namespace std;
//
//double f(double);
//double g(double);
//
//void main()
//{
//	//expected value
//	double exp = pow(5, 2.0 / 3);
//	
//	//bounds of the interval
//	double a = A, b = B;
//
//	//point to evaluate at
//	double p = 0, fa = f(a),fp;
//
//	//max iterations, and current iteration
//	int iteration = 0, maxIterations = 100;
//	bool foundPoint = false;
//
//
//	cout << "Using the bisction method: " << endl;
//
//	//Loop for the bisection method
//	while (iteration < maxIterations)
//	{
//		p = a + (b - a) / 2;
//		fp = f(p);
//		iteration++;
//
//		cout << "Iteration: " << setw(3) << left << iteration;
//		cout << " a: " << setw(7) << left << a;
//		cout << " b: " << setw(7) << left << b;
//		cout << " p: " << setw(7) << left << p;
//		cout << " f(p) = " << setw(7) << left << f(p) << endl;
//
//		//check to see if we're done
//		//p-a = (b-a)/2
//		if (p - a <= TOL || fp == 0)
//		{
//			foundPoint = true;
//			break;
//		}
//		//else
//		
//		if (fa*fp > 0)
//		{
//			//shift the location of a
//			a = p;
//			fa = fp;
//		}
//		else
//		{
//			//shift location of b
//			b = p;
//		}
//	}
//
//	//print out error if it didn't converge
//	if (!foundPoint)
//	{
//		cout << endl << "Bisection method failed after " << iteration << " iterations." << endl << endl;
//	}
//	else
//	{
//		//Print results		
//		cout <<endl << "The root of the function on the interval [" << A 
//			<< ", " << B << "] is x = " << p << endl;
//		cout << "f(" << p << ") = " << fp << " after " << iteration << " iterations.";
//		cout << endl << endl;
//	}
//
//	//reset variables for FP iteration
//	iteration = 0; 	
//	a = A; b = B;
//	double prevP = (a+b)/2;
//	p = 0;
//
//	cout << "Using the fixed point iteration method: " << endl;
//
//	while(iteration < maxIterations)
//	{
//		p = g(prevP);
//		iteration++;
//
//		cout << "Iteration: " << setw(3) << left << iteration;
//		cout << " prevP: " << setw(7) << left << prevP;
//		cout << " p: " << setw(7) << left << p << endl;
//
//		//check cond
//		if(abs(p-prevP) <= TOL)
//		{
//			foundPoint = true;
//			break;
//		}
//
//		prevP =p;
//		
//	}
//	
//	if (!foundPoint)
//	{
//		cout << endl << "FP method failed after " << iteration << " iterations." << endl << endl;
//	}
//	else
//	{
//		//Print results		
//		cout << endl << "The root of the function on the interval [" << A
//			<< ", " << B << "] is x = " << p << endl;
//		cout << "f(" << p << ") = " << fp << " after " << iteration << " iterations.";
//		cout << endl << endl;
//	}
//
//	cout << "The expected value is " << exp << endl << endl;
//	system("pause");
//}
//
//double f(double x)
//{
//	//x^3-25
//	return pow(x, 3) - 25;
//}
//double g(double x)
//{
//	//x-x^3+25
//	return x-(x*x*x-25)/(3*x*x);
//}
