# Heap-Sort

Heap sort relies on the properties of a heap data structure to sort a data set. A heap is a partially ordered binary tree where every node is greater than or equal to both of its children, hence the largest value in the tree is always in the root node. A binary tree is mapped onto an array so that the node in position i is parent of the nodes in positions 2*i and (2*i + 1), if of course they exist.

Heapsort sorts an array by first converting the array into a heap so that it has the relational property described above. It then sorts the data in reverse by repeatedly placing the largest unsorted element into its correct place. It does so by repeatedly (1) removing the maximum value in the heap (the value in the root node), (2) putting that value into the sorted array, and (3) rebuilding the heap with one fewer elements. Note that heapsort does not need two separate arrays; it can use use the same array for the heap and the sorted array.

