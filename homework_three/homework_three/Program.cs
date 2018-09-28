using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace homework_three
{
    class Program
    {


        public static class Globals
        {
            public const double PI = 3.14159265358979323846264338; // Unmodifiable
            public const double E =  2.71828182845904523536028747; // Unmodifiable
            public static double dummy = -1; // Modifiable

            // search range for iterative methods
            public static double min = -700;
            public static double max = 700;

        }


        static void Main(string[] args)
        {
            Console.WriteLine("Homework two, Sarah Roberts.");







            // keep window open
            Console.WriteLine();
            Console.WriteLine("\n Press any key to exit.");
            Console.ReadKey();
        }

        static double L( double v, double alpha)
        {
            double v0 = 1.2;    // TODO: DEFINE V0
            return alpha / (Globals.PI * Math.Pow(v - v0, 2) + Math.Pow(alpha, 2));
        }

        static double G( double v, double alpha)
        {
            double v0 = 1.2;    // TODO: DEFINE V0
            double temp = 1 / alpha;
            double exp = -Math.Log(2) * Math.Pow(v - v0, 2) / (alpha*alpha);
            temp *= Math.Sqrt(Math.Log(2) / Globals.PI);
            temp *= Math.Pow(Globals.E, exp);

            return temp;
        }



    }
}
