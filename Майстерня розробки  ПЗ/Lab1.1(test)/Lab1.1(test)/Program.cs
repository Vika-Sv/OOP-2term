using System;

Console.WriteLine("Sviastyn V.I");

Random random = new Random();

int[,] A = new int[3, 3];
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
    {
        A[i, j] = random.Next(1, 21);
        Console.Write(A[i, j] + " ");
    }
    Console.WriteLine();
}
Console.WriteLine("Matrix A before changes ");

int[] D = new int[3];
for (int i = 0; i < 3; i++)
{
    D[i] = random.Next(1, 6);
    Console.Write(D[i] + " ");
}
Console.WriteLine("Array/Matrix D");

for (int i = 0; i < 3; i++)
{
    if ((i + 1) % 2 != 0)
    {
        for (int j = 0; j < 3; j++)
        {
            A[i, j] = D[j];
            Console.Write(A[i, j] + " ");
        }
    }
    else
    {
        for (int j = 0; j < 3; j++)
        {
            Console.Write(A[i, j] + " ");
        }
    }
    Console.WriteLine();
}
Console.WriteLine("Matrix A after changes");

int sum = 0;
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
    {
        sum += A[i, j];
    }
}
Console.WriteLine("Sum of all elements in Matrix A: " + sum);

