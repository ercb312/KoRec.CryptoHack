//only two variables w/ jh park
#include <iostream>
using namespace std;

int gcd(int a, int b);

int main() {
	int a, b;
	cout << "정수 두개를 입력하세요(dividend divisor) >> ";
	cin >> a >> b;
	]

	cout << gcd(a, b);
}

int gcd(int a, int b) {
	while (a >= b) {
		a = a - b;
		if (b == 0) {
			return a;
		}
	}
	//cout << "a:" << b << ", b:" << a << endl;
	return gcd(b, a);
}