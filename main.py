import copy;
a=[[2,3],[4,5]];
b1=a.copy();
b2=copy.deepcopy(a);

b2[0][0]=999;
print(a);