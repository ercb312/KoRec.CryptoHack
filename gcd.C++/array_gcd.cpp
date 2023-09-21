//revised attempt
#include <iostream>
using namespace std;

void gcd();

int main() {
	gcd();
}

void gcd() {
	int a[10], b[10], q[10], r[10];
	
// a:dividend, b:divisor, q:quotient, r:remainder
	cout << "정수 두개를 입력하세요(dividend divisor) >> ";
	cin >> a[0] >> b[0];
	for (int n = 0; r[n] <= 0; n++) {
		r[n] = a[n] % b[n];
		q[n] = (a[n] - r[n]) / b[n];
		a[n + 1] = b[n];
		b[n + 1] = r[n];
		cout << "a:" << a[n] << ", b:" << b[n] << ", q:" << q[n] << ", r:" << r[n] << endl;
	}
}