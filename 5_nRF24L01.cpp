
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <unistd.h>
#include <RF24/RF24.h>

using namespace std;

//here the raspberry pi will be the transmitter and the arduino will work as a receiver

RF24 radio(22,0);

// const uint8_t pipes[][6] = {"1Node", "2Node"};
const uint8_t address[6] = "00010";



int main(int argc, char**argv){
	
	
    // Setup and configure rf radio
    radio.begin();

    // optionally, increase the delay between retries & # of retries
    radio.setRetries(15, 15);
    // Dump the configuration of the rf unit for debugging
    radio.printDetails();


	radio.openWritingPipe(address[0]);
	radio.startListening();
    while (1) {
		radio.stopListening();
		printf("please enter the message");
		string string;
		getline (cin, string);
		printf("sending %s", string);
		bool ok = radio.write(string, string.size());

		if (!ok) {
			printf("failed.\n");
		}
		sleep(2);
	}

}


