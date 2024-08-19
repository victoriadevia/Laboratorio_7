// constants won't change. Used here to set a pin number:
const int ledPin = 12;  // the number of the LED pin

// Variables will change:
int ledState = LOW;  // ledState used to set the LED

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;  // will store last time LED was updated

// constants won't change:
const long interval = 1000;  // interval at which to blink (milliseconds)

void setup() {
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Iniciar comunicación serial
}

void loop() {
  // Leer el valor del sensor
  int sensorValue = analogRead(A0);

  // Imprimir el valor del sensor y el estado del LED
  Serial.print(sensorValue);
  Serial.print(",");
  Serial.print(ledState);
  Serial.println();

  // Actualizar el estado del LED
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    ledState = (ledState == LOW) ? HIGH : LOW; // Alternar estado del LED
    digitalWrite(ledPin, ledState);
  }

  delay(1);  // Espera entre lecturas para estabilidad 1 milisegundo
}

