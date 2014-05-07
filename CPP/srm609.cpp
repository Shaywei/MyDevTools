#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

class MagicalStringDiv1 {
public:
    int getLongest(std::string);
};

int MagicalStringDiv1::getLongest(std::string S) {
    int n = S.length();
    int ret = 0;
    for(int i=0;i<n;i++)
    {
        int left=0;
        int right = 0;
        for(int j=0;j<=i;j++)
        {
            if(S[j]=='>')
                left++;
        }
        for(int j=i+1;j<n;j++)
        {
            if(S[j]=='<')
                right++;
        }
        ret = std::max(ret,std::min(left,right));
    }
    return ret*2;
}

int main()
{
    std::cout << "Hello World!" << std::endl;
    MagicalStringDiv1* msd = new MagicalStringDiv1();
    std::cout << msd->getLongest("<><><<>") << std::endl;
}

//Powered by [KawigiEdit] 2.0!