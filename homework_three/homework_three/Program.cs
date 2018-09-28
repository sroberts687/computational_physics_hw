using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

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
            Console.WriteLine("Homework three, Sarah Roberts.");

           

            int i = 0;
            double[] input = new double[100];
            double[] output = new double[100];
            double[] error = new double[100];
            double[] alphaL = new double[30];
            double[] alphaG = new double[30];
 
            
            // open and process data file
            StreamReader data = File.OpenText("hw3-fitting.dat");
            string str = null;  // will hold line from data
            
            while ((str = data.ReadLine()) != null)
            {
                // split str into three values using Regex
                var ary = Regex.Split(str,@"[^0-9\.]+").Where(c => c != "." && c.Trim() != ""); 
                
                //store in the correct arrays
                input[i] = ary[0];   // TODO: get the first entry
                output[i] = ary[1];    // TODO: get the second entry
                error[i] = ary[2];     // TODO: get the last entry

                i += 1;
                
                //debug: display line that was just parsed
                Console.WriteLine(str);
            }
            data.Close();

            
           

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
