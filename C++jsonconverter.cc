#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
int main()
{
    json no_init_list = json::array();
    json empty_init_list = json::array({});
    json nonempty_init_list = json::array({1, 2, 3, 4, 5, 6, 7, 8});
    json list_of_pairs = json::array({ {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5} });
    std::cout << no_init_list << '\n';
    std::cout << empty_init_list << '\n';
    std::cout << nonempty_init_list << '\n';
    std::cout << list_of_pairs << '\n';
}


/*
Output

[]
[]
[1,2,3,4,5,6,7,8]
[["one",1],["two",2],["three",3],["four",4],["five",5]]
*/