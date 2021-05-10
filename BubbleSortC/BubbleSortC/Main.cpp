#include <iostream>
#include <algorithm>
#include <time.h>
#include <math.h>
using namespace std;
void CreateList(long long arr[], long long n)
{
	srand(time(0));
	for (int i = 0; i < n; i++)
	{
		arr[i] = rand();
	}
}
long long bubblesort(long long arr[], long long n)
{
	int i, j;
	long long count = 1; //i=0
	for (i = 0; i < n - 1; ++i)
	{
		count += 2; //i<n-1
		for (j = 0; j < n - i - 1; j++)
		{
			count += 3; //j<n-i-1
			if (arr[j] > arr[j + 1])
			{
				swap(arr[j], arr[j + 1]);
				count += 6;
			}
			else
				count += 2;
			count += 1; //j++
		}
		count += 1; //i++
		count += 3; //j<n-i-1
		count += 1; //j=0
	}
	count += 2; //i=n-1
	return count;
}
void PrintList()
{
	for (long long i = 800; i < 800000000000; i *= 1.1)
	{
		static long long* a = new long long[100000000];
		CreateList(a, i);
		long long count = bubblesort(a, i);
		cout << i << "," << count << endl;
		float size = trunc(log10(count)) + 1;
		if (size > 17)
			break;
	}
}
int main()
{
	PrintList();
}