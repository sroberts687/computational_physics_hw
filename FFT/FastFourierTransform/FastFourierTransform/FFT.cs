using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

/*FFT.cs
 * 
 * Recursive implimentation of a FFT algorithm from "Introduction to Algorithms" Thomas H. Cormen et al.
 * 
 * Sarah Roberts and Adam Anthony
 * 5/5/2015
 */


namespace FastFourierTransform
{
    class FFT
    {
        static void main(string[] args)
        {
            Complex[] fft;
            double[] a = { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            double[] b = { 0, 1, 2, 3, 4, 5, 6, 7 };

            try
            {
                fft = recusiveFFT(a);
                Console.Out.WriteLine("Input");
                Console.Out.WriteLine(string.Join(",", a), "\n");
                Console.WriteLine();

                Console.Out.WriteLine("Output");
                Console.Out.WriteLine(complexToString(fft));

                Console.Out.WriteLine("Power Spectrum");
                Console.Out.WriteLine(powerSpec(fft));

                Console.Out.WriteLine();
            }
            catch (Exception e)
            {
                Console.Out.WriteLine(e.Message);
                Console.Out.WriteLine();
            }

            //b
            fft = recusiveFFT(b);
            Console.Out.WriteLine("Input");
            Console.Out.WriteLine(string.Join(",", b));
            Console.WriteLine();

            Console.Out.WriteLine("Output");
            Console.Out.WriteLine(complexToString(fft));

            Console.Out.WriteLine("Power Spectrum");
            Console.Out.WriteLine(string.Join(", ", powerSpec(fft)));
            Console.WriteLine();
            Console.WriteLine();

            //b2
            b = new double[16];
            for (int i = 0; i < b.Length; i++ )
            {
                b[i] = Math.Cos(Math.PI * i);
            }
            
            fft = recusiveFFT(b);
            Console.Out.WriteLine("Input");
            Console.Out.WriteLine(string.Join(",", b));
            Console.WriteLine();

            Console.Out.WriteLine("Output");
            Console.Out.WriteLine(complexToString(fft));

            Console.Out.WriteLine("Power Spectrum");
            Console.Out.WriteLine(string.Join(", ", powerSpec(fft)));
            
            Console.In.ReadLine();
        }
        
        public static Complex[] recusiveFFT(double[] a)
        {
            return unNomrRecusiveFFT(a);
        }

        static Complex[] unNomrRecusiveFFT(double[] a)
        {
            //make sure the number of coeff is a power of 2
            if (!powerOfTwo(a.Length))
                throw new System.ArgumentException("Input size must be a power of 2", "a");

            //if a has a length of one, just return
            if (a.Length == 1)
                return toComplex(a);

            //split a into odd and even indices
            double[] evenA = new double[a.Length / 2];
            double[] oddA = new double[a.Length / 2];

            for (int i = 0; i < a.Length; i++)
            {
                //if even
                if (i % 2 == 0)
                {
                    //add to even array
                    evenA[i / 2] = a[i];
                }
                else
                {
                    //add to odd array if odd (int div)
                    oddA[i / 2] = a[i];
                }
            }

            //Continue to subdivide input array
            Complex[] oddY = unNomrRecusiveFFT(oddA);
            Complex[] evenY = unNomrRecusiveFFT(evenA);

            //Transform a -> y
            Complex omega = Complex.One;
            Complex[] y = new Complex[a.Length];

            for (int k = 0; k < a.Length / 2; k++)
            {
                y[k] = evenY[k] + omega * oddY[k];
                y[k + a.Length / 2] = evenY[k] - omega * oddY[k];
                omega *= Complex.Exp(new Complex(0, 2 * Math.PI / a.Length));
            }

            return y;
        }

        //Cast a double array into an array of complex numbers
        static Complex[] toComplex(double[] a)
        {
            Complex[] c = new Complex[a.Length];
            for(int i = 0; i < a.Length; ++i)
            {
                c[i] = a[i];
            }

            return c;
        }
        
        //Return true if n is a power of 2
        static bool powerOfTwo(int n)
        {
            return (n & (n - 1)) == 0;
        }
    
        //Normalize an array of complex numbers
        static Complex[] normalize(Complex[] a)
        {
            Complex[] norm = new Complex[a.Length];
            double normFactor = Math.Sqrt(a.Length);
            for (int i = 0; i < a.Length; i++ )
            {
                norm[i] = a[i] / normFactor;
            }
               
            return norm;
        }
    
        //Convert complex number to string
        static string complexToString(Complex c)
        {
            return string.Format("{0} + {1} * i", c.Real, c.Imaginary);
        }

        //Convert a complex array to string
        static string complexToString(Complex[] a)
        {
            string returnStr = "";
            foreach(Complex c in a)
            {
                returnStr += (complexToString(c) + "\n");
            }

            return returnStr;
        }
    
        static double[] powerSpec(Complex[] a)
        {
            double[] spec = new double[a.Length];
            for(int i = 0; i < a.Length; i++)
            {
                spec[i] = a[i].Magnitude;
            }

            return spec;
        }
    }
}
