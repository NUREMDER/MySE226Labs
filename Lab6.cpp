#include <iostream>
using namespace std;

class Lab6 {
public:

    int myFunction(int n) {
        if (n == 0) {
            return 1; 
        }
        return n * myFunction(n - 1); 
    }

    int myFunction() {
        int n;
        cout << "Enter a number: ";
        cin >> n;
        return myFunction(n); 
    }
};

int main() {
    Lab6 obj; 

    int result = obj.myFunction();
    cout << "Result: " << result << endl;

    return 0;
}
