int LED1 = 43;
int LED2 = 44;
int LED3 = 45;
int LED4 = 46;

int BTN1 = 30;
int BTN2 = 31;
int BTN3 = 32;
int BTN4 = 33;

bool state1 = false;
bool state2 = false;
bool state3 = false;
bool state4 = false;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);

  pinMode(BTN1, INPUT_PULLUP);
  pinMode(BTN2, INPUT_PULLUP);
  pinMode(BTN3, INPUT_PULLUP);
  pinMode(BTN4, INPUT_PULLUP);
}

void loop() {
  
  digitalWrite(LED1, HIGH);
  delay(1000);
  digitalWrite(LED1, LOW);
  delay(1000);

  
  digitalWrite(LED1, HIGH);
  delay(1000);
  digitalWrite(LED2, HIGH);
  delay(1000);
  digitalWrite(LED3, HIGH);
  delay(1000);
  digitalWrite(LED4, HIGH);
  delay(1000);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);

  
  if (digitalRead(BTN1) == LOW) {
    state1 = !state1;
    digitalWrite(LED1, state1);
    delay(250);
  }
  if (digitalRead(BTN2) == LOW) {
    state2 = !state2;
    digitalWrite(LED2, state2);
    delay(250);
  }
  if (digitalRead(BTN3) == LOW) {
    state3 = !state3;
    digitalWrite(LED3, state3);
    delay(250);
  }
  if (digitalRead(BTN4) == LOW) {
    state4 = !state4;
    digitalWrite(LED4, state4);
    delay(250);
  }
}
