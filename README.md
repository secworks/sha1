sha1
====

## Introduction ##
Verilog implementation of the SHA-1 cryptgraphic hash function.
The implementaion follows the specification in NIST FIPS 180-4.


## Implementation details ##

### Altera Cyclone IV GX ###
Implementation results using Altera Quartus-II 13.1.

Altera Cyclone IV E - EP4CE6F17C6
* 2913 LEs
* 1527 regs
* 107 MHz

Altera Cyclone IV GX - EP4CGX22CF19C6
* 2814 LEs
* 1527 regs
* 105 MHz

Altera Cyclone V - 5CGXFC7C7F23C8
* 1124 ALMs
* 1527 regs
* 104 MHz


## TODO ##
* Extensive functional verification in real HW.
* Add Wishbone interface.
* Documentation


## Status ##
**(2014-02-23):***

Added reset of W-memory registers. This reduce the size of the
implementation with 16 LEs - one for each register.

**(2014-02-23):***

Changed the W-memory into a sliding window with 16 32-bit registers. A
massive improvement in resource utilization. The old results:

* 10718 LEs
* 3575 Regs
* 103 MHz

The new results:

* 2829 LEs
* 1527 regs
* 105 MHz


***(2014-02-21):***

The core is basically done and should be ready to use. But the
functional verification should be more thorough.

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
