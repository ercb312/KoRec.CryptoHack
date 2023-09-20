//initial idea
#include <iostream>
using namespace std;

void gcd();

int main() {
	gcd();
}

void gcd() {
	int a1, b1, q1, r1;
	int a2, b2, q2, r2;
	int a3, b3, q3, r3;
	int a4, b4, q4, r4;
	cout << "정수 두개를 입력하세요(dividend divisor) >> ";
	cin >> a1 >> b1;
	r1 = a1 % b1;
	q1 = (a1 - r1) / b1;

	cout << a1 << b1 << q1 << r1 << endl;

	a2 = b1;
	b2 = r1;
	r2 = a2 % b2;
	q2 = (a2 - r2) / b2;

	cout << a2 << b2 << q2 << r2 << endl;
	

}