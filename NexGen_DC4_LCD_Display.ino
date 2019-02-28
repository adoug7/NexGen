#include <LiquidCrystal_I2C.h>

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x3F, 16, 2);
volatile unsigned long int countdown;
volatile unsigned long int counter;
int displaycount;
int ledger[100];


int i = 1;
int k = 0;
int fakepackage = 0;

void setup()
{
  // initialize the LCD
  lcd.init();

  // Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Next Package in:");
  Serial.begin(9600);

  for (int z = 0; z<100;z++)
  ledger[z] = 0;

  ledger[0]=42;
}

void loop()
{
   // Print test variable
  Serial.println(countdown);
  counter = int(millis());
  //displaycount= 30-(counter/1000);

  //Measure time
  delay (1000);
  fakepackage++;

 //if (counter % 1000 == 0)
 
  for (int j = 0; j <100; j++)
   {
    if (ledger[j] != 0)
    {
      ledger[j]--;
    }
   }


if (fakepackage % 9 == 0)
{
  ledger[i] = random(37,47);
  ++i;
}

if (ledger[k] == 0)
  ++k;

  // Clear LCD screen and print out angle
  lcd.clear();
  String TestData;
  TestData = "Next package in:";
  lcd.setCursor(0, 0);
  lcd.print(TestData);
  lcd.setCursor(0, 1);
  lcd.print(String(ledger[k]));

}
