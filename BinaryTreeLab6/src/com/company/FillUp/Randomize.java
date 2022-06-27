package com.company.FillUp;

import com.company.Tree.BinarySearchTree;

import java.util.Random;

public class Randomize {
    Random rand = new Random();
    public BinarySearchTree Randomize(BinarySearchTree tree){
        for (int i = 0; i < 2000; i++) {
            int int_random = rand.nextInt(100000);
            tree.insert(int_random);
        }
        return tree;
    }
}
