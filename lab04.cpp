#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;
    int num;
    int capacity;

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num == capacity - 1) {
            increaseCapacity();
        }

        Node* Node1 = new Node();
        Node1->data = x;
        Node1->next = head;
        head = Node1;
        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }

        Node* current = head;
        int poppedValue = head->data;
        head = head->next;
        delete current;
        num--;
        return poppedValue;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
        cout << "Capacity is set. New capacity is " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }

        Node* current = head;
        Node* prev = nullptr;

        while (current != nullptr && current->data != val) {
            prev = current;
            current = current->next;
        }

        if (current == nullptr) {
            cout << "Element " << val << " not found!" << endl;
            return false;
        }

        if (prev == nullptr) {
            head = current->next;
        } else {
            prev->next = current->next;
        }

        delete current;
        num--;
        cout << "Deleted element: " << val << endl;
        return true;
    }
};

int main() {
    Stack myStack(5);

    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    myStack.push(40);
    myStack.push(50);

    cout << "Top element is: " << myStack.peek() << endl;

    
    int newValue;
    cout << "Enter a value to push into the stack: ";
    cin >> newValue;  
    myStack.push(newValue);  

    cout << "Top element after push " << newValue << " is: " << myStack.peek() << endl;

    cout << "Popped element: " << myStack.pop() << endl;

    cout << "Top element after pop is: " << myStack.peek() << endl;

    myStack.deleteElement(30);

    cout << "Top element after deleting 30 is: " << myStack.peek() << endl;

    return 0;
}
