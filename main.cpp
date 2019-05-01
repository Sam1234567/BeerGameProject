#include <iostream>
using namespace std;

class state {
public:
	double FL;
	double FPD2;
	double FPD1;
	double FPR;
	double FB;
	double FED;
	
	state() {}
};

state nextState(state in) {
	return in;
}

int main(int argc, char** argv) {
	
}