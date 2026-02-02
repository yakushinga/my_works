
int third_node (int matrix[][], int M, int a, int b){
    int c = 0, i;
    for (i = 0; i < M; i++)
        if (matrix[a][i] == 1 && matrix[b][i] == 1
            && i != a && i!= b)
            c++;
    return c;
}
