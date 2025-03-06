#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int d, Node* n = nullptr) {
        data = d;
        next = n;
    }
};

class Queue {
private:
    Node* back;
    Node* front;

public:
    Queue() : back(nullptr), front(nullptr) {}

    bool isEmpty() {
        return back == nullptr && front == nullptr;
    }

    void enqueue(int input) {
        if (isEmpty()) {
            front = new Node(input);
            back = front;
        } else {
            back->next = new Node(input);
            back = back->next;
        }
    }

    void dequeue() {
        if (!isEmpty()) {
            Node* temp = front;
            if (front == back) {
                front = nullptr;
                back = nullptr;
            } else {
                front = front->next;
            }
            cout << "Top of the values is removing value : " << temp->data << endl;
            delete temp;
        }
    }

    void print(const string& message) {
        cout << message;
        for (Node* p = front; p != nullptr; p = p->next) {
            cout << p->data << " ";
        }
        cout << endl;
    }

    int size() {
        int counter = 0;
        for (Node* p = front; p != nullptr; p = p->next) {
            counter++;
        }
        return counter;
    }

    int top() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return front->data;
    }
};

int main() {
    Queue* q = new Queue();
    cout << "Adding Integer..." << endl;

    q->enqueue(1);
    q->enqueue(2);
    q->enqueue(3);
    q->enqueue(4);
    q->enqueue(5);
    q->enqueue(6);

    q->dequeue();

    q->print("Printing : ");
    cout << "Size : " << q->size() << endl;

    q->dequeue();

    q->print("New Printing : ");

    delete q;
    return 0;
}
