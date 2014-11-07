sha1
====

## Introduction ##
Verilog implementation of the SHA-1 cryptgraphic hash function. The
functionality follows the specification in NIST FIPS 180-4.

The implementation is iterative with one cycle/round. The initialization
takes one cycle. The W memory is based around a sliding window of 16
32-bit registers that are updated in sync with the round processing. The
total latency/message block is 82 cycles.

There are top level wrappers that provides interface for easy
integration into a System on Chip (SoC). This interface contains mesage
block and digest registers to allow a host to load the next block while
the current block is being processed.

The implementation also includes a functional model written in Python.


## Implementation details ##

The sha1 design is divided into the following sections.
- src/rtl - RTL source files
- src/tb  - Testbenches for the RTL files
- src/model/python - Functional model written in python
- doc - documentation (currently not done.)
- toolruns - Where tools are supposed to be run. Includes a Makefile for
building and simulating the design using [Icarus Verilog](http://iverilog.icarus.com/)

The actual core consists of the following files:
- sha1_core.v - The core itself with wide interfaces.
- sha1_w_mem.v - W message block memort and expansion logic.
- sha1_k_constants.v - K constants ROM memory.

The top level entity is called sha1_core. This entity has wide
interfaces (512 bit block input, 160 bit digest). In order to make it
usable you probably want to wrap the core with a bus interface.

Unless you want to provide your own interface you therefore also need to
select one top level wrapper. There are two wrappers provided:
- sha1.v - A wrapper with a 32-bit memory like interface.
- wb_sha1.v - A wrapper that implements a [Wishbone](http://opencores.org/opencores,wishbone) interface.

***Do not include both wrappers in the same project.***

The core (sha1_core) will sample all data inputs when given the init
or next signal. the wrappers provided contains additional data
registers. This allows you to load a new block while the core is
processing the previous block.


## FPGA-results ##

### Altera Cyclone FPGAs ###
Implementation results using Altera Quartus-II 13.1.

** Altera Cyclone IV E **
- EP4CE6F17C6
- 2913 LEs
- 1527 regs
- 107 MHz

** Altera Cyclone IV GX **
- EP4CGX22CF19C6
- 2814 LEs
- 1527 regs
- 105 MHz

** Altera Cyclone V **
- 5CGXFC7C7F23C8
- 1124 ALMs
- 1527 regs
- 104 MHz

### Xilinx FPGAs ###
Implementation results using ISE 14.7.

** Xilinx Spartan-6 **
- xc6slx45-3csg324
- 1589 LUTs
- 564 Slices
- 1592 regs
- 100 MHz


## TODO ##
* Documentation


## Status ##

***(2014-11-07):***

Core has been completed for quite a while. Added new implementation
results for Spartan-6.

***(2013-02-25)***

Updated README with some more information about the design.

***(2014-02-23):***

Added reset of W-memory registers. This reduce the size of the
implementation with 16 LEs - one for each register.

***(2014-02-23):***

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
