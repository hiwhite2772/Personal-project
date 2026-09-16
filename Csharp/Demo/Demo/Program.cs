using System.Security.Cryptography;

namespace Demo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string s1 = Console.ReadLine();
            string s2 = Console.ReadLine();
            string s3 = s1.ToLower();
            string s4 = s2.ToLower();

            Console.WriteLine(s3.IndexOf(s4));
        }
    }
}
