using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;

public static class Solution_1197 {
    struct Edge {
        public Node other;
        public int weight;
    }

    class Node {
        public int value;
        public List<Edge> edges = new List<Edge>();
        public Node(int value) {
            this.value = value;
        }
    }

    public struct Edge2 {
        public int a, b, weight;
    }

    public static void Main() {
        var parsed = Console.ReadLine().Split(" ").Select(number => int.Parse(number));
        var V = parsed.ElementAt(0);
        var E = parsed.ElementAt(1);

        /*
        // initialize node array
        Node[] nodes = new Node[V + 1];
        for (int i = 1; i <= V; i++)
            nodes[i] = new Node(i);

        Action<int, int, int> connect = (int a, int b, int weight) => {
            Node node_a = nodes[a], node_b = nodes[b];
            
            node_a.edges.Add(new Edge() { weight = weight, other = node_b });
            node_b.edges.Add(new Edge() { weight = weight, other = node_a });
        };

        // read inputs
        for (int i = 0; i < E; i++) {
            var input = Console.ReadLine().Split(" ").Select(d => int.Parse(d)).ToArray();
            var a = input[0];
            var b = input[1];
            var weight = input[2];

            connect(a, b, weight);
        }
        */

        int[,] map = new int[V + 1, V + 1]; // 0, x 와 x, 0은 무시

        SortedList<int, Edge2> sortedList = new();

        for (int i = 0; i < E; i++) {
            var input = Console.ReadLine().Split(" ").Select(d => int.Parse(d)).ToArray();
            var a = input[0];
            var b = input[1];
            var weight = input[2];

            sortedList.Add(weight, new() { a = a, b = b, weight = weight });
        }

        bool checkConnected(int a, int b) {
            bool _FindWithDFS(int root, int target) {
                for ()
            }
            return false;
        }

        foreach(var edge in sortedList) {

        }
    }
}