sha1
====

## Introduction ##
Verilog implementation of the SHA-1 cryptgraphic hash function.
The implementaion follows the specification in NIST FIPS 180-4.


## Implementation details ##

### Altera Cyclone IV GX ###
Implementation using Altera Quartus-II 13.1 with a EP4CGX22CF19C6 device
as target.
* 10718 LEs
* 3575 Regs
* 103 MHz


## TODO ##
* Implement the main round functionality.
* Functional verification
* HW implementation.


## Status ##
***(2014-02-21):***

Several minor updates to core RTL and TB after synthesis using Altera
Quartus II tool. The core now builds to a complete FPGA design without
any design warnings. And we have some performance results too. See
above.


***(2014-02-20):***

The core now generates the correct digest for single and double block
messages. We need to fix the top level wrapper and build for FPGA before
the core is somewhat completed.


***(2014-01-29):***

Completed the Python based functional model. It might need some
polishing, but works and can be used to drive the RTL implementation.

Updated the W memory scheduler to a version without circular buffer and
ahead-of-use processing similar to what is used in the SHA-256 core.

The W memory scheduler has been verified to be functionally correct and
has been synthesized using Altera Quartus-II 13.1 without errors and
design related warnings.


***(2014-01-29):***

Initial draft. Based on the SHA-256 core. 
