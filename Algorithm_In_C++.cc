#include <iostream>
using namespace std;
#include <string>
#include <ctime>
#include <cstdlib>


int main()
{
    int ln = 1;
    int un = 60;

    srand((unsigned int)time(NULL));

//Time Unit
    int vari1 = 6;
    int RandIndex1 = rand() % vari1; //generates a random number between 0 and 5
    string timeunitarray[vari1]={"seconds","minutes","hours","days","weeks","months"};
//Verb
    int vari2 = 6;
    int RandIndex2 = rand() % vari2; //generates a random number between 0 and 5
    string verbage[vari2]={"paint","film","draw","write","photo","record"};
//Item
    int vari3 = 6;
    int RandIndex3 = rand() % vari3; //generates a random number between 0 and 5
    string itemarray[vari3]={"seconds","minutes","hours","days","weeks","months"};
//Nouns
    int vari4 = 6;
    int RandIndex4 = rand() % vari4; //generates a random number between 0 and 5
    string nounarray[vari4]={"paint","film","draw","write","photo","record"};
//Emotion
    int vari5 = 6;
    int RandIndex6 = rand() % vari5; //generates a random number between 0 and 5
    string emotionarray[vari5]={"paint","film","draw","write","photo","record"};

//Print
    cout<<"You have " << ln+rand() % static_cast<int>(un-ln+1) << " " << timeunitarray[RandIndex1] << " to " << verbage[RandIndex2] << " a " << itemarray[RandIndex3] << ". Your keywords are " << nounarray[RandIndex4]  << " " << nounarray[RandIndex4]  << " " << "emotion" << ". Good Luck!";
    return 0;
}
