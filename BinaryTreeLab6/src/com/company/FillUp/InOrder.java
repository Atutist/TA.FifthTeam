package com.company.FillUp;


import com.company.Tree.BinarySearchTree;

public class InOrder {
    public BinarySearchTree InOrder(BinarySearchTree tree){
        for (int i = 0; i < 2000; i++){
            tree.insert(i);
        }
        return tree;
    }
}
