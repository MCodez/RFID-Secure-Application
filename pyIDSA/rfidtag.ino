// VARIABLE DECLARATION

char input[12];				
int count = 0;				

// SETUP FUNCTION

void setup()
{
	Serial.begin(9600);   // START SERIAL AT BAUD RATE OF 9600 BITS/SEC		
	
}

// LOOP FUNCTION

void loop()
{      
     
	if(Serial.available())   // CHECK FOR AVAILABILITY OF SERIAL DATA
	{
		count = 0; 			// Reset the counter to zero
		/* Keep reading Byte by Byte from the Buffer till the RFID Reader Buffer is	empty 
		   or till 12 Bytes (the ID size of our Tag) is read */
		while(Serial.available() && count < 12) 
		{
			input[count] = Serial.read(); // Read 1 Byte of data and store it in the input[] variable
			count++; 					// increment counter
			delay(5);
		}
     // PRINTING RFID TAG           
    for(int i=0;i<12;i++)
    Serial.print(input[i]);
		Serial.println();
		
        }


}