using System;
using System.Collections.Generic;

namespace C_
{
    class Solution
    {
        static int[] memo = new int[27];
        static void countChars(string s, int low, int high)
        {
            Array.Clear(memo, 0, memo.Length);
            for (int i = low; i <= high; i++)
                memo[s[i] - 'a']++;
        }

        static int countVariant()
        {
            int count = 0;
            for (int i = 0; i < memo.Length; i++)
                if (memo[i] != 0)
                    count++;

            return count;
        }

        // Complete the substrCount function below.
        static long substrCount(int n, string s)
        {
            int totalCount = 0;
            for (int i = 0; i < s.Length; i++)
            {
                int low = i, high = i;

                while (low >= 0 && high < s.Length)
                {
                    countChars(s, low, high);

                    int variant_count = countVariant();
                    bool shouldBreak = false;

                    switch (variant_count)
                    {
                        case 2:
                            {
                                int mid = (low + high) / 2;
                                if (memo[s[mid] - 'a'] == 1)
                                    totalCount++;
                            }
                            break;

                        case 1:
                            {
                                totalCount++;
                            }
                            break;

                        default:
                        shouldBreak = true;
                        break;
                    }

                    if (shouldBreak)
                        break;

                    // 짝수 검사
                    low--;
                    if (low >= 0)
                    {
                        countChars(s, low, high);
                        variant_count = countVariant();
                        if (variant_count == 1)
                            totalCount++;
                    }

                    high++;
                }
            }

            return totalCount;
        }

        static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        
        var C = int.Parse(Console.ReadLine());
        var input_stack = new Stack<int>();
        var output_stack = new Stack<int>();
        
        for (int i = 0; i < C; i++) {
            var input = Console.ReadLine().Split(' ');
            int opcode = int.Parse(input[0]);
            
            switch (opcode) {
                case 1: { // enqueue
                    int operand = int.Parse(input[1]);
                    input_stack.Push(operand);
                } break;
                
                case 2: { // dequeue
                    if (output_stack.Count == 0)
                        while (input_stack.Count > 0)
                            output_stack.Push(input_stack.Pop());
                            
                    output_stack.Pop();
                } break;
                
                case 3: { // print front
                    if (output_stack.Count == 0)
                        while (input_stack.Count > 0)
                            output_stack.Push(input_stack.Pop());

                    Console.WriteLine(output_stack.Peek());
                } break;
            }
        }
    }
    }
}
