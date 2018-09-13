using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;




namespace homework_two
{
    class Program
    {
        /* define global variables in a public, static class because C# does not allow
         * for global variable definitions */
        public static class Globals
        {
            public const double G = 1; // Unmodifiable
            public const double PI = 3.1415926;  // Unmodifiable
            public static double M1 = -1;  // Modifiable
            public static double M2 = -1;  // Modifiable
            public static double M = -1;
            public static double sep = -1; // Modifiable

            // search range for iterative methods
            public static double min = -700;
            public static double max = 700;

            // position of m1 and m2, respectively
            // current code written st x1 = 0 and x2 = sep
            internal static double x1;
            internal static double x2;
        }


        /* Main program defines grid size and asks for user to input values for M1, M2,
         * and seperation distance */
        static void Main(string[] args)
        {

            Console.WriteLine("Homework two, Sarah Roberts.");

            Console.WriteLine("Part (1)");

            // get Globals.{M1, M2, sep} from the user & ensure values are valid
            Console.WriteLine("To generate plots for part 2a, set M1 = 3, M2 = 1, and sep = 1");
            Console.WriteLine("To generate plots for part 2b, set M1 = 100, M2 = 1, and sep = 1");
            getInput();

            // initalize grid
            int minx = -2;
            int maxx = 2;
            int miny = -2;
            int maxy = 2;
            double step = 0.1;

            // dimensions used to construct array to hold grid
            int dimx = Math.Abs(minx) + Math.Abs(maxx);
            dimx *= 10; // 1/step = 10
            int dimy = Math.Abs(miny) + Math.Abs(maxy);
            dimy *= 10;

            // three dimensional array grid will hold grid points and function values
            double[,,] grid = new double[dimx, dimy, 5];

            Console.WriteLine("instantiated grid");

            
            // define x,y grid and evaluate gravity and potential for each (x,y)
            for (int i = 0; i < dimx; i++)
            {
                for (int j = 0; j < dimy; j++)
                {
                    grid[i, j, 0] = minx + i*step;  // x coordinate
                    grid[i, j, 1] = miny + j*step;  // y coodrinate

                    // Funct will calculate the effective gravity for a point
                    grid[i, j, 2] = FunctX(grid[i, j, 0], grid[i, j, 1]);  // g_x(x,y)
                    grid[i, j, 3] = FunctY(grid[i, j, 0], grid[i, j, 1]);  // g_y(x,y)

                    grid[i, j, 4] = Potential(grid[i, j, 1], grid[i, j, 0]); // potential(x,y)

                }
            }

            // output the x component of the acceleration at each grid point
            Console.WriteLine("printing acceleration at each grid point");
            using (StreamWriter ax = new StreamWriter("C:\\Users\\srobe\\Desktop\\ax.txt", true))
            {
                for (int i = 0; i < dimx; i++)
                    {
                        for (int j = 0; j < dimy; j++)
                        {
                            // print the effective gravity in the format (a_x, a_y)
                            //Console.Write("( {0} , {1} ) \t", grid[i, j, 2], grid[i, j, 3]);

                            ax.Write("{0}\t", grid[i, j, 2]);

                            if (j == dimy - 1)
                            {
                                ax.WriteLine();
                            }
                        }   // loop on j
                    }   // loop on i
                }   // close ay
          
            // output the y component of the acceleration at each grid point
            using (StreamWriter ay = new StreamWriter("C:\\Users\\srobe\\Desktop\\ay.txt", true))
            {
                for (int i = 0; i < dimx; i++)
                {
                    for (int j = 0; j < dimy; j++)
                    {

                        ay.Write("{0}\t", grid[i, j, 3]);

                        if (j == dimy - 1)
                        {
                            ay.WriteLine();
                        }
                    }   // loop on j
                }   // loop on i
            }   // close ay


            // output the potential for each grid point
            Console.WriteLine("printing potential for each grid point");
            using (StreamWriter writetext = new StreamWriter("C:\\Users\\srobe\\Desktop\\potential.txt", true))
            {
                for (int i = 0; i < dimx; i++)
                {
                    for (int j = 0; j < dimy; j++)
                    {
                        writetext.Write("{0} \t", grid[i, j, 4]);

                        if (j == dimy-1)
                        {
                            writetext.WriteLine();
                        }
                    }
                }
            }

            // part 2
            Console.WriteLine();
            Console.WriteLine("Part (2)");

            Console.WriteLine("This section is implemented using the script makePlots.py, ");
            Console.WriteLine("which looks for the text files generated in Part (1). ");


            // part 3
            Console.WriteLine();
            Console.WriteLine("Part (3)");

            // need to use coordinate system w/ origin at center of mass

            // part A
            Console.WriteLine("Part A");
            Console.WriteLine("M1 = 3, M2 = 1, sep = 1"); 

            Globals.M1 = 3;
            Globals.M2 = 1;
            Globals.M = Globals.M1 + Globals.M2;
            Globals.sep = 1;

            Globals.x1 = -1 * Globals.M1 * Globals.sep / Globals.M;
            Globals.x2 = Globals.M1 * Globals.sep / Globals.M;


            /*     // output the effective for each point on the x axis ( used for debugging)
                 Console.WriteLine("printing g for each grid point on x");
                 using (StreamWriter writetext = new StreamWriter("C:\\Users\\srobe\\Desktop\\gvals.txt", true))
                 {
                     for (int i = -100; i <= 100; i++)
                     {
                         writetext.WriteLine("{0} \t", L( (double) i * 0.10) );  
                     }
                 }       */

            Console.WriteLine("L1 = " + DoSecant(0.1, 0.2, 0));        // L1 = 0.165055535250554
            Console.WriteLine("L2 = " + DoSecant(1.2, 1.3, 0));        // L2 = 1.23828349344855
            Console.WriteLine("L3 = " + DoSecant(-1.6, -1.4, 0));      // L3 = -1.47547642755739 
            Console.WriteLine("L4 = " + DoSecant(0.8, 1.2, 1));        // L4 = 1.00
            Console.WriteLine("L5 = " + DoSecant(-1.2, -0.8, 1));      // L5 = -1.00


            // part B
            Console.WriteLine("Part B");
            Console.WriteLine("M1 = 100, M2 = 1, sep = 1"); 

            Globals.M1 = 100;
            Globals.M2 = 1;
            Globals.M = Globals.M1 + Globals.M2;
            Globals.sep = 1;

            Globals.x1 = -1 * Globals.M1 * Globals.sep / Globals.M;
            Globals.x2 = Globals.M1 * Globals.sep / Globals.M;

            /*   // output the effective for each point on the x axis ( used for debugging)
               Console.WriteLine("printing g for each grid point on x");
               using (StreamWriter writetext = new StreamWriter("C:\\Users\\srobe\\Desktop\\gvals.txt", true))
               {
                   double i = -2;
                   while ( i < 2 )
                   {
                       writetext.WriteLine("{0} \t {1}",i, L2( (double) i ) ); 
                       //writetext.WriteLine("{0} \t {1}",i, L( (double) i ) ); 
                       i += 0.1; 
                   }
               }       */

            
            Console.WriteLine("L1 = " + DoSecant(0.4, 0.5, 0));     // L1 = 0.446352519
            Console.WriteLine("L2 = " + DoBisection(1.06, 2));      // L2 = 1.0985546875
            Console.WriteLine("L3 = " + DoSecant(-10, -5, 0));      // L3 = -1.743881191
            Console.WriteLine("L4 = " + DoSecant(0.8, 1.2, 1));     // L4 = 1.00
            Console.WriteLine("L5 = " + DoSecant(-1.2, -0.8, 1));   // L5 = -1.00



            // keep window open
            Console.WriteLine();
            Console.WriteLine("\n Press any key to exit.");
            Console.ReadKey();

        }

        private static void getInput()
        {
            while (Globals.M1 < 0)
            {
                Console.WriteLine("enter a value for mass 1");
                Globals.M1 = Convert.ToDouble(Console.ReadLine());
            }

            while (Globals.M2 < 0)
            {
                Console.WriteLine("enter a value for mass 2");
                Globals.M2 = Convert.ToDouble(Console.ReadLine());
            }

            Console.WriteLine("enter a value for seperation between M1 and M2");
            Globals.sep = Convert.ToDouble(Console.ReadLine());
            

            if (Globals.M1 <= Globals.M2)
            {
                double temp = Globals.M1;
                Globals.M1 = Globals.M2;
                Globals.M2 = temp;
            }

            // M1 >= M2, assign locations
            Globals.x1 = 0;
            Globals.x2 = Globals.sep;

        }

        private static double Potential(double x, double y)
        {
            double U1 = (-1 * Globals.G * Globals.M1 * Globals.M2) / Math.Sqrt(x * x + y * y); 
            double U2 = (-1 * Globals.G * Globals.M1 * Globals.M2) / Math.Sqrt(((x - Globals.sep) * (x - Globals.sep) + y * y));

            return U1 + U2;
        }

        private static double FunctX(double x, double y)
        {
            double F1 = (Globals.G * Globals.M1) / (x * x + y * y);
            double F2 = (Globals.G * Globals.M2) / ( (x - Globals.sep) * (x - Globals.sep) + y * y);

            F1 *= (x / Math.Sqrt(x * x + y * y));
            F2 *= ((x - Globals.sep) / Math.Sqrt((x - Globals.sep) * (x - Globals.sep) + y * y));

            return F1 + F2;

        }

        private static double FunctY(double x, double y)
        {
            double F1 = (Globals.G * Globals.M1) / (x * x + y * y);
            double F2 = (Globals.G * Globals.M2) / ((x - Globals.sep) * (x - Globals.sep) + y * y);

            F1 *= (y / Math.Sqrt(x * x + y * y));
            F2 *= (y / Math.Sqrt(x * x + y * y));

            return F1 + F2;
        }

        private static double Funct(double v1, double v2)
        {
            throw new NotImplementedException();
        }

        private static double L(double x)
        {
            double temp = 0;
            temp = -1 * Globals.M1 * (x - Globals.x1) / Math.Pow(Math.Abs(x - Globals.x1), 3);
            temp -= Globals.M2 * (x - Globals.x2) / Math.Pow(Math.Abs(x - Globals.x2), 3);
            temp += Globals.M * x / Math.Pow(Globals.sep, 3);

            return temp;
        }

        private static double L2( double y)
        {
            double temp = 0;
            double x = (Globals.x1 + Globals.x2) / 2;


            temp = -1 * Globals.M1 * (y) / Math.Pow(Math.Abs(y), 3);
            temp -= Globals.M2 * y / Math.Pow(Math.Abs(y), 3);
            temp += Globals.M * y / Math.Pow(Globals.sep, 3); 



            return temp;
        }


        private static double Secant(double pm1, double pm2, int flag)
        {

            if (flag == 0)
            {
                return pm1 - (L(pm1) * (pm1 - pm2)) / (L(pm1) - L(pm2));
            }
            else
            {
                return pm1 - (L2(pm1) * (pm1 - pm2)) / (L2(pm1) - L2(pm2));
            }
            
        }

        private static double DoSecant(double min, double max, int flag)
        {

            double p = min + (max - min) / 2;
            double f = L(p);
            double tol = 0.0001;
            int maxIt = 50;

            // code for debugging
            //Console.WriteLine();
            //Console.WriteLine("( {0} , {1} )", min, max);
            //Console.WriteLine("( {0} , {1} )", L(min), L(max));
            

            //double[] pValuesS = new double[maxIt];
            double[] fpValuesS = new double[maxIt];

            // initial conditions
            if (flag == 0)
            {
                fpValuesS[0] = L(min);
            } else
            {
                fpValuesS[0] = L2(min);
            }

            fpValuesS[1] = Secant(min + (max - min) / 2, fpValuesS[0], flag);

            // initialize step counter to two b/c we do first two iterations outside the loop
            int i = 2;

            do
            {

                fpValuesS[i] = Secant(fpValuesS[i - 1], fpValuesS[i - 2], flag);

                //optional output
                // Console.WriteLine(i + "\t" + fpValuesS[i]);

                i++;

            } while (Math.Abs(fpValuesS[i - 1] - fpValuesS[i - 2]) > tol && i < maxIt - 1);

            return fpValuesS[i-1];
        }

        // Newton's method, not fully implemented (no derivative function)
        private static double DoNewtons()
        {
            int i = 0;
            int maxIt = 50;
            double tol = 0.0001;
            double min = Globals.min;
            double max = Globals.max;
            
            // function outputs
            double[] fpValuesN = new double[maxIt];
            // function inputs
            double[] pValuesN = new double[maxIt];
            // vals of function derivative
            double[] fprimeValuesN = new double[maxIt];

            // initial conditions
            pValuesN[0] = min + (max - min) / 2;
            fpValuesN[0] = L(min + (max - min) / 2);
            //fprimeValuesN[0] = Lderiv(min + (max - min) / 2);

            // optional output
            //Console.WriteLine("0" + "\t" + pValuesN[0]);

            i++;

            do
            {
                pValuesN[i] = pValuesN[i - 1]
                  - (fpValuesN[i - 1] / fprimeValuesN[i - 1]);
                fpValuesN[i] = L(pValuesN[i]);
            //    fprimeValuesN[i] = Lderiv(pValuesN[i]);

                // optional output
                //Console.WriteLine(i + "\t" + pValuesN[i]);

                i++;

            } while (Math.Abs(pValuesN[i - 1] - pValuesN[i - 2]) > tol
              && i < maxIt - 1);

            return 0;
        }

        // bisection method, used for third Lagrange point when M1 = 100 because
        // it was convering to a different point, even when interval was small
        private static double DoBisection(double a, double b)
        {

            double p = 0;
            int i = 0;
            double f = 0;
            int maxIt = 200;
            double tol = 0.001;

            bool increasing = true;

            double min = Globals.min;
            double max = Globals.max;

            // function outputs
            double[] fpValuesBi = new double[maxIt];
            // function inputs
            double[] pValuesBi = new double[maxIt];

            do { 
                // find p and store it in the array
                p = a + (0.5 * (b - a));
                pValuesBi[i] = p;

                // evaluate f(p) and store it
                f = L(p);
                fpValuesBi[i] = f;

                /*
                 * // break if f(p) is within the tolerance if (f == 0.0 || (f <=
                 * 0.01 && f >= 0) || (f >= -0.01 && f <= 0)) break;
                 */

                if (!increasing)
                {
                    // if f > 0 make p upper
                    if (f < 0)
                        b = p;

                    // if f < 0 make p lower
                    if (f > 0)
                        a = p;
                }
                else
                {
                    if (f > 0)
                        b = p;

                    // if f < 0 make p lower
                    if (f < 0)
                        a = p;
                }

                i++;

            } while (i <= maxIt && 0.5 * (b - a) > tol);

            // display the roots
            //Console.WriteLine("Bisection method gives a root at " + "(" + p + ", " + f + ")."); 

            return p;

        }


    }
}


