### set up decision variables ------------------------------------------------------------------------------------------
# binary choices for each supplier
var dcw binary;
var dnm binary;
var dafd binary;
var dlac binary;

# amount to purchase from each supplier
var cw;
var nm;
var afd;
var lac;

# set up objective ------------------------------------------------------------------------------------------
minimize cost: 10000*dcw + 2500*cw + 20000*dnm + 2450*nm + 0*dafd + 2510*afd + 13000*dlac + 2470*lac;

### set constraints ------------------------------------------------------------------------------------------
# total furniture requirement
subject to requirements: cw + nm + afd + lac >= 2000;

# bid/capacity limits (each producer can only send so much)
subject to cw_bid: cw <= 1000;
subject to nm_bid: nm <= 1200;
subject to afd_bid: afd <= 800;
subject to lac_bid: lac <= 1100;

# fixed charge problem - need to ensure that binary decision variable = 1 if that supplier is bought from 
subject to cw_dec: cw <= 1000000*dcw;
subject to nm_dec: nm <= 1000000*dnm;
subject to afd_dec: afd <= 1000000*dafd;
subject to lac_dec: lac <= 1000000*dlac;

# can't have negative purchasing!
subject to nn_cw: cw >= 0;
subject to nn_nm: nm >= 0;
subject to nn_afd: afd >= 0;
subject to nn_lac: lac >= 0; 

