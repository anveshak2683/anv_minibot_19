#include<SPI.h>
#include <Ethernet.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(10,42,0,5);
IPAddress server(10,42,0,3);
EthernetClient client;
char c;
int d;

void setup() 
{
 Ethernet.begin(mac, ip);
 pinMode(13, OUTPUT);
 pinMode(4, OUTPUT);
 while(!client.connect(server, 10005))
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
    while(!client.connect(server,10005))
    {}    
  }
  else if (client.available()) 
  {
    c=client.read();
    d=int(c);
    /*c = client.readStringUntil('\n');
    d = c.toInt();
    OCR2B= map(d, 0, 1023, 12, 255);*/
  }
}
