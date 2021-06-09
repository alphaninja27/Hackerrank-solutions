#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
string a,b,c;
int l1,l2;
cin>>a;
cin>>b;
l1=a.size();
l2=b.size();
c=a+b;
cout<<l1<<" "<<l2<<endl;
cout<<c<<endl;
a[0]=b[0];
b[0]=c[0];
cout<<a<<" "<<b;
return 0;
}