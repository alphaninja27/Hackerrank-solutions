include <stdio.h>

void update(int *a,int *b) {
   int c,d;
   d=*a+*b;
   if(*a>*b)
   {
       c=*a-*b;
   }
   else
   {
       c=*b-*a;
   }
   *a=d;
   *b=c;
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}