#include <iostream>
#include <cstdlib>
#include <random>
#include <fstream>
#include <string>

using namespace std;

mt19937 mt;

int main(int argc, char *argv[]) {
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
	if (sameState == 1) {
		ifstream stateFile("stateFile.txt");
		stateFile >> mt;
	}
	else if (argc == 0) {
		cout << "No PRNG state given." << endl;
	}

	int n = 100000;
	double max_area = 0., max_a = 0.;
	for (int i = 0; i < n; i++) {
		double a = 100.0 * mt() / (mt.max() + 1.0);
		double b = 100.0 - a;
		double area = a * b;
		if (area > max_area) {
			max_area = area;
			max_a = a;
		}
	}
	cout << max_a << endl;
}