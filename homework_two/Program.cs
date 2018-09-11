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

            
            for (int i = 0; i < dimx; i++)
            {
                for (int j = 0; j < dimy; j++)
                {
                    grid[i, j, 0] = minx + i*step;  // x coordinate
                    grid[i, j, 1] = miny + j*step;  // y coodrinate

                    // Funct will calculate the effective gravity for a point
                    grid[i, j, 2] = FunctX(grid[i, j, 0], grid[i, j, 1]);  // g_x(x,y)
                    grid[i, j, 3] = FunctY(grid[i, j, 0], grid[i, j, 1]);  // g_y(x,y)

                    grid[i, j, 4] = Potential(grid[i, j, 0], grid[i, j, 1]); // potential(x,y)

                }
            }

            // output the x,y component of the acceleration at each grid point
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

           //Console.Write("{0} \t", grid[i, j, 4]);
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

            // TODO: generate contour plots
            // TODO: generate vector plot


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

            Console.WriteLine(DoSecant(Globals.x2, 2)); 
            Console.WriteLine(DoSecant(0, Globals.x2));
            Console.WriteLine(DoSecant(-2, Globals.x1));


            // part B
            Console.WriteLine("Part B");
            Console.WriteLine("M1 = 100, M2 = 1, sep = 1"); 

            Globals.M1 = 100;
            Globals.M2 = 1;
            Globals.M = Globals.M1 + Globals.M2;
            Globals.sep = 1;

            Globals.x1 = -1 * Globals.M1 * Globals.sep / Globals.M;
            Globals.x2 = Globals.M1 * Globals.sep / Globals.M;

            Console.WriteLine(DoSecant(Globals.x2, 2));
            Console.WriteLine(DoSecant(0, Globals.x2));
            Console.WriteLine(DoSecant(-2, Globals.x1));

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
            temp = -1 * Globals.M1 * (x - Globals.x1) / Math.Pow((x - Globals.x1), 3);
            temp -= Globals.M2 * (x - Globals.x2) / Math.Pow((x - Globals.x2), 3);
            temp += Globals.M * x / Math.Pow(Globals.sep, 3);

            return temp;
        }


        private static double Secant(double pm1, double pm2)
        {
            return pm1 - (L(pm1) * (pm1 - pm2)) / (L(pm1) - L(pm2));
        }

        private static double DoSecant(double min, double max)
        {

            // initialize step counter to two b/c we do first two iterations outside the loop
            int i = 2;  

            double p = min + (max - min) / 2;
            double f = L(p);
            double tol = 0.0001;
            int maxIt = 50;


            double[] pValuesS = new double[maxIt];
            double[] fpValuesS = new double[maxIt];

            // initial conditions
            fpValuesS[0] = 1.5;
            fpValuesS[1] = Secant(min + (max - min) / 2, fpValuesS[0]);

            do
            {

                fpValuesS[i] = Secant(fpValuesS[i - 1], fpValuesS[i - 2]);

                //optional output
                // Console.WriteLine(i + "\t" + fpValuesS[i]);

                i++;

            } while (Math.Abs(fpValuesS[i - 1] - fpValuesS[i - 2]) > tol
              && i < maxIt - 1);

            return fpValuesS[i];
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
            // derivatives of function outputs
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

        }
}


