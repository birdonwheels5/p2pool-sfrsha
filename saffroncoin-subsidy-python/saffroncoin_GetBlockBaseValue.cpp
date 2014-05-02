#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <math.h> 

static const int64_t COIN = 100000000;

int64_t static GetBlockBaseValue(int nBits, int nHeight)
{

 int64 nSubsidy = nStartSubsidy;

    std::string cseed_str = prevHash.ToString().substr(5,7);
    const char* cseed = cseed_str.c_str();
    long seed = hex2long(cseed);
    int rand = generateMTRandom(seed, 6000);

    //Random Superblock
    if(rand > 2075 && rand < 2099)  
    {
        nSubsidy *= 5;
    }

    // 1st 2 days bonus
    if(nHeight < 5761)     
    {
        nSubsidy *= 3;
    }


    // Mining phase: Subsidy is cut in half every SubsidyHalvingInterval
    nSubsidy >>= (nHeight / 524160);
    
    // Inflation phase: Subsidy reaches minimum subsidy
    // Network is rewarded for transaction processing with transaction fees and 
    // the inflationary subsidy
    if (nSubsidy < nMinSubsidy)
    {
        nSubsidy = nMinSubsidy;
    }

    return nSubsidy + nFees;

}


#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(saffroncoin_subsidy)
{
    def("GetBlockBaseValue", GetBlockBaseValue);
}

