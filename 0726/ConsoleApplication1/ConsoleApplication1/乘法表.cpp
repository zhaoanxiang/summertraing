#include<iostream>
#include<math.h>
using namespace std;
int main()
{

	int a[9] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	for (int i = 0; i < 9; i++)
	{

		for (int j = 0; j < 9; j++)
		{
			if (a[j] <= a[i]){
				int result = a[j] * a[i];
				cout << a[j] << "*" << a[i] << "=" << result << "  ";
			}
		}
		cout << endl;
	}
	system("pause");
	return 0;
}