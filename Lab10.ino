const int ledPins[4] = {43, 44, 45, 46};
const int buttonPins[4] = {38, 39, 40, 41};


bool ledStates[4] = {false, false, false, false};


bool lastButtonStates[4] = {false, false, false, false};

void setup() {
  
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Turn off all LEDs at start
  }


  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) {
    bool buttonState = digitalRead(buttonPins[i]);

    
    if (buttonState == HIGH && lastButtonStates[i] == LOW) {
    
      ledStates[i] = !ledStates[i];
      digitalWrite(ledPins[i], ledStates[i] ? HIGH : LOW);
    }

    
    lastButtonStates[i] = buttonState;
  }
}
