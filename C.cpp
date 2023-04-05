#include <iostream>

int main() {
int n;
std::cin >> n;

int prev = -1;
for (int i = 0; i < n; i++) {
    int new_num;
    std::cin >> new_num;

    if (i == 0 || new_num != prev) {
        std::cout << new_num << "\n";
    }

    prev = new_num;
}

return 0;
}

