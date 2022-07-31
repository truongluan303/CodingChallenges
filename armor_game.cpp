/*
 * Given an array of integer where each index of the array represent a level in a game and the value at that index
 * represents the amount of damage the player needs to take.
 * The player then also given an armor that can block a certain amount of damage. But the user can only use the
 * armor once. So for example, if the player decides to use the armor of value 5 at a level where the damge is 3,
 * the player will loose all of his armor even though the armor is stronger than the damage. On the other hand, if
 * the damage is stronger than the armor, for example armor is 5 and damage is 8, the player will receive 3 damages.
 *
 * Calculate the minimum amount of health that the user needs to survive all levels.
 */

#include <iostream>
#include <cassert>


using namespace std;


int minimum_health(int* levels, size_t len, int armor)
{
    int max_dmg = 0;
    for (size_t i = 0; i < len; i++)
    {
        max_dmg = (levels[i] > max_dmg) ? levels[i] : max_dmg;
    }

    int total_dmg = (armor >= max_dmg) ? -max_dmg : -armor;
    for (size_t i = 0; i < len; i++)
    {
        total_dmg += levels[i];
    }

    return total_dmg + 1;
}


int main()
{
    int* levels1 = new int[5] { 1, 3, 5, 6, 8  };
    int* levels2 = new int[3] { 3, 3, 2 };
    int armor = 5;

    assert(minimum_health(levels1, 5, armor) == 19);
    assert(minimum_health(levels2, 3, armor) == 6);

    cout << "Passed!" << endl;

    delete [] levels1;
    delete [] levels2;

    return 0;
}
