using System;

namespace DelegateExample
{
    // 1. Оголошення делегата
    delegate int CountLowerDelegate(string text);
    class Program
    {
        static void Main(string[] args)
        {
            string sample = "Hello World! Python Is FUN";

            // 2. Анонімний метод
            CountLowerDelegate anonMethod = delegate (string str)
            {
                int count = 0;
                foreach (char c in str)
                {
                    if (char.IsLower(c))
                        count++;
                }
                return count;
            };

            // 3. Лямбда-вираз
            CountLowerDelegate lambdaMethod = (text) =>
            {
                int count = 0;
                foreach (char c in text)
                {
                    if (char.IsLower(c))
                        count++;
                }
                return count;
            };

            // 4. Виклик делегатів
            Console.WriteLine('Count of symbols:' + anonMethod(sample));
            Console.WriteLine('Count of symbols:' + lambdaMethod(sample));

            Console.ReadKey();
        }
    }
}
