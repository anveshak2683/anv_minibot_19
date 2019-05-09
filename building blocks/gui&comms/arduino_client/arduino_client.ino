#include<SPI.h>
#include <Ethernet.h>

//IP of shield
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(10,42,0,5);

//Server
IPAddress server(10,42,0,3);
int port  = 3000;

EthernetClient client;

char c[2];
int right,left;

void setup() 
{
 Ethernet.begin(mac, ip);
 pinMode(13, OUTPUT);
 pinMode(4, OUTPUT);
 while(!client.connect(server, port))
 {}
 /*TCCR0A = _BV(COM0A0) | _BV(COM0B1) | _BV(WGM00)|_BV(WGM01);
 TCCR2B = _BV(CS02)| _BV(CS01)| _BV(CS00);
 OCR2A = 255;
 OCR2B = 12;*/
}

void loop() 
{
  if(!client.connected())
  {
    while(!client.connect(server,port))
    {}    
  }
  else if (client.available()) 
  {
    c = client.readStringUntil('\n');
    right = int(c[0]);
    left = int(c[1]);
    //OCR2B= map(d, 0, 1023, 12, 255);
  }
}
