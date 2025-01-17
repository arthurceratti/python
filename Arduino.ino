//
//    FILE: dht11_test.ino
//  AUTHOR: Rob Tillaart
// VERSION: 0.1.01
// PURPOSE: DHT library test sketch for DHT11 && Arduino
//     URL:
//
// Released to the public domain
//

#include <dht.h>

dht DHT;

#define DHT11_PIN 3

void setup()
{
  Serial.begin(115200);
  //Serial.println("DHT TEST PROGRAM ");
  //Serial.print("LIBRARY VERSION: ");
  //Serial.println(DHT_LIB_VERSION);
 // Serial.println();
  //Serial.println("Type,\tstatus,\tHumidity (%),\tTemperature (C)");
}

void loop()
{
  // READ DATA
  //Serial.print("DHT11, \t");
  
  int chk = DHT.read11(DHT11_PIN);
  switch (chk)
  {
    case DHTLIB_OK:  
    //Serial.print("OK"); 
    break;
    case DHTLIB_ERROR_CHECKSUM: 
    //Serial.print("Checksum error"); 
    break;
    case DHTLIB_ERROR_TIMEOUT: 
   // Serial.print("Time out error"); 
    break;
  }
  // DISPLAY DATA
  Serial.print(DHT.humidity, 1);
  Serial.print(",");
  Serial.println(DHT.temperature, 1);
  Serial.print("\n");
  delay(2000);
}
//
// END OF FILE
//
