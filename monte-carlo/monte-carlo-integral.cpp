#include <iostream>
#include <random>
#include <fstream>
#include <string>
#include <cmath>
#include <stdio.h>
#include <math.h>
#include <ostream>

using namespace std;

mt19937 mt;

double f(double x) {
	return exp(-pow(x, 2));
}

int main(int argc, char* argv[]) {

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
		seed = stol(seedLine);
	}
	mt.seed(seed); // Set seed


	int sameState = atoi(argv[1]);
	ofstream outFile;
	if (sameState == 1) {
		cout << "New state given." << endl;
		ifstream stateFile("stateFile.txt");
		stateFile >> mt;
		outFile = ofstream("out-integral-cpp-sameState.txt");
	}
	else if (sameState == 0) {
		cout << "No PRNG state given." << endl;
		outFile = ofstream("out-integral-cpp-sameSeed.txt");
	}
	

	int a = 0;
	double b = 1;
	int N = 1000;

	vector<double> ar(N);
	double integral = 0.0;
	double result;


	long int randInt;
	string randIntStr;
	size_t lenRand;
	double rand2;
	// Set all elements of ar to 0
	for (size_t i = 0; i < N; ++i) {
		// Get length of
		/*randIntStr = to_string(mt() * 2);
		lenRand = randIntStr.length();
		randInt = stol(randIntStr);

		ar[i] = double(randInt) / pow(10.0, lenRand);*/

		uniform_real_distribution<float> float_dist(a,b);
		ar[i] = float_dist(mt);
		if (sameState == 1){
			rand2 = float_dist(mt);
		}
		//ar[i] = double(mt()) / mt.max();

		result = f(ar[i]);
		integral += result;
	}

	double ans = (b - a) / double(N) * integral;

	cout << "The value calculated by monte carlo integration is " << ans << endl;

	string ansStr = to_string(ans);
	outFile << ansStr;
	outFile.close();
}
