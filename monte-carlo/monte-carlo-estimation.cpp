/* C++ program for estimation of Pi using Monte
Carlo Simulation */
#include <string>
#include <random>
#include <iostream>
#include <fstream>

// Defines precision for x and y values. More the
// interval, more the number of significant digits
#define INTERVAL 10000
using namespace std;

mt19937 mt;

int main(int argc, char *argv[])
{
	int interval, i;
	double rand_x, rand_y, origin_dist, pi;
	int circle_points = 0, square_points = 0;

	unsigned int seed;
	// Get PRNG seed
	ifstream seedFile;
	seedFile.open("seedFile.txt");
	if (seedFile.fail()) {  // If no file exists, create one
		// Generate seed from datetime function
		seed = time(NULL);

		// Open a file to store seed
		ofstream seedFile;
		seedFile.open("seedFile.txt");

		// Write seed value to file
		string SeedString = to_string(seed);
		seedFile << SeedString;

		seedFile.close();  // Close seed file
	}
	else {  // If a file exists, set the seed to the stored seed
		string seedLine;
		getline(seedFile, seedLine);
		seed = stoi(seedLine);
	}
	mt.seed(seed); // Set seed

	int sameState = atoi(argv[1]);
	ofstream outFile;
	if (sameState == 1) {
		cout << "New state given." << endl;
		ifstream stateFile("stateFile.txt");
		stateFile >> mt;
		outFile = ofstream("out-estimate-cpp-sameState.txt");
	}
	else if (sameState == 0) {
		cout << "No PRNG state given." << endl;
		outFile = ofstream("out-estimate-cpp-sameSeed.txt");
	}
	


	// Total Random numbers generated = possible x
	// values * possible y values
	for (i = 0; i < (INTERVAL * INTERVAL); i++) {

		// Randomly generated x and y values
		rand_x = double(mt() % (INTERVAL + 1)) / INTERVAL;
		rand_y = double(mt() % (INTERVAL + 1)) / INTERVAL;
		/*if (i <= 5) {
			cout << mt() << endl;
			cout << rand_x << " " << rand_y << endl;
		}*/

		// Distance between (x, y) from the origin
		origin_dist = rand_x * rand_x + rand_y * rand_y;

		// Checking if (x, y) lies inside the define
		// circle with R=1
		if (origin_dist <= 1)
			circle_points++;

		// Total number of points generated
		square_points++;

		// estimated pi after this iteration
		pi = double(4 * circle_points) / square_points;
	}

	// Final Estimated Value
	cout << "Final Estimation of Pi = " << pi;

	string ansStr = to_string(pi);
	outFile << ansStr;
	outFile.close();
}
