# Brain Criticality  

This package is a minimal version of the MATLAB code. It plots the power-law fit of avalanche size and lifetime, given continuous size and discrete lifetime data. The input must be an `(n, 2)` matrix, where the first column represents the size and the second column represents the lifetime.  

You can provide the path to this matrix as an argument to the program, and it will generate the plot:  

```bash
python main.py path_to_matrix
```  