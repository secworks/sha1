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


## Implementation status ##

The core has been completed and been used in several designs. It is
considered mature. Minor changes are non-functional cleanups of code.


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

The top level entity is called sha1_core. This entity has wide
interfaces (512 bit block input, 160 bit digest). In order to make it
usable you probably want to wrap the core with a bus interface.

Unless you want to provide your own interface you therefore also need to
use a top level wrapper. There is one wrapper provided:
- sha1.v - A wrapper with a 32-bit memory like interface.

The core (sha1_core) will sample all data inputs when given the init
or next signal. the wrappers provided contains additional data
registers. This allows you to load a new block while the core is
processing the previous block.


## FPGA-results ##

### Altera Cyclone FPGAs ###
Implementation results using Altera Quartus-II 13.1.

**Altera Cyclone IV E**
- EP4CE6F17C6
- 2913 LEs
- 1527 regs
- 107 MHz

**Altera Cyclone IV GX**
- EP4CGX22CF19C6
- 2814 LEs
- 1527 regs
- 105 MHz

**Altera Cyclone V**
- 5CGXFC7C7F23C8
- 1124 ALMs
- 1527 regs
- 104 MHz


### Xilinx FPGAs ###
Implementation results using ISE 14.7.

**Xilinx Spartan-6**
- xc6slx45-3csg324
- 1589 LUTs
- 564 Slices
- 1592 regs
- 100 MHz


## TODO ##
* Documentation
