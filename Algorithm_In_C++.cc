#include <iostream>
using namespace std;
#include <string>


int main()
{
  int time;
  string timeunit;
  string verb;
  string item;
  string noun;
  string nounthesecond;
  string emotion;

  string timeunitarray[6]={"seconds","minutes","hours","days","weeks","months"};

  cout << "You have " << time << timeunit << " to  " << verb << " a " << item << ". Your keywords are " << noun << nounthesecond << emotion << ". Good Luck!";
}
