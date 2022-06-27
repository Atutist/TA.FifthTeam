package com.company;

import com.company.FillUp.InOrder;
import com.company.FillUp.Randomize;
import com.company.Tree.Three.BalancedBinaryTree;
import com.company.Tree.Three.UnbalancedBinaryTree;

public class Main {

    public static void main(String[] args) {
        Randomize randomize = new Randomize();
        InOrder inOrder = new InOrder();

        BalancedBinaryTree avlRandomize = new BalancedBinaryTree();
        BalancedBinaryTree avlInOrder = new BalancedBinaryTree();
        double start = System.nanoTime();
        randomize.Randomize(avlRandomize);
        double end = System.nanoTime();
        double res = end-start;
        System.out.println("Balanced avl: ");
        System.out.print("Random insertion: " + res + "\n");
        start = System.nanoTime();
        inOrder.InOrder(avlInOrder);
        end = System.nanoTime();
        res = end - start;
        System.out.print("Ordered insertion: " + res+ "\n");
        start = System.nanoTime();
        avlRandomize.search(300);
        end = System.nanoTime();
        res = end-start;
        System.out.print("Searching: " + res+ "\n");
        start = System.nanoTime();
        avlRandomize.delete(300);
        end = System.nanoTime();
        res = end-start;
        System.out.println("Deleting: " + res+ "\n");


        UnbalancedBinaryTree bstRandomize = new UnbalancedBinaryTree();
        UnbalancedBinaryTree bstOrdered = new UnbalancedBinaryTree();
        start = System.nanoTime();
        randomize.Randomize(bstRandomize);
        end = System.nanoTime();
        res = end-start;
        System.out.println("Unbalanced bst: ");
        System.out.print("Random insertion: " + res + "\n");
        start = System.nanoTime();
        inOrder.InOrder(bstOrdered);
        end = System.nanoTime();
        res = end - start;
        System.out.print("Ordered insertion: " + res+ "\n");
        start = System.nanoTime();
        bstRandomize.search(300);
        end = System.nanoTime();
        res = end-start;
        System.out.print("Searching: " + res+ "\n");
        start = System.nanoTime();
        bstOrdered.delete(300);
        end = System.nanoTime();
        res = end-start;
        System.out.print("Deleting: " + res+ "\n");
        start = System.nanoTime();
        bstOrdered.balance();
        end = System.nanoTime();
        res = end-start;
        System.out.print("Balancing order: " + res+ "\n");
        start = System.nanoTime();
        bstRandomize.balance();
        end = System.nanoTime();
        res = end-start;
        System.out.print("Balancing randomize: " + res+ "\n");


    }
}
