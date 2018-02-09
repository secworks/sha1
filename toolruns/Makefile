#===================================================================
#
# Makefile
# --------
# Makefile for building sha1 core and top simulation.
#
#
#
# Author: Joachim Strombergson
# Copyright (c) 2013, Secworks Sweden AB
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#===================================================================

WMEM_SRC=../src/rtl/sha1_w_mem.v
WMEM_TB_SRC=../src/tb/tb_sha1_w_mem.v

CORE_SRC=../src/rtl/sha1_core.v ../src/rtl/sha1_w_mem.v
CORE_TB_SRC=../src/tb/tb_sha1_core.v

TOP_SRC=../src/rtl/sha1.v $(CORE_SRC)
TOP_TB_SRC=../src/tb/tb_sha1.v

CC = iverilog
CC_FLAGS = -Wall

LINT = verilator
LINT_FLAGS = +1364-2001ext+ --lint-only  -Wall -Wno-fatal -Wno-DECLFILENAME


all: top core wmem


top: $(TB_TOP_SRC) $(TOP_SRC)
	$(CC) $(CC_FLAGS) -o top.sim $(TB_TOP_SRC) $(TOP_SRC)


core: $(CORE_TB_SRC) $(CORE_SRC)
	$(CC) $(CC_FLAGS) -o core.sim $(CORE_SRC) $(CORE_TB_SRC)


wmem: $(WMEM_SRC) $(WMEM_TB_SRC)
	$(CC) $(CC_FLAGS) -o wmem.sim $(WMEM_SRC) $(WMEM_TB_SRC)


lint: $(TOP_SRC)
	$(LINT) $(LINT_FLAGS) $(TOP_SRC)


sim-top: top.sim
	./top.sim


sim-core: core.sim
	./core.sim


sim-wmem: wmem.sim
	./wmem.sim


clean:
	rm -f single_shot_top.sim
	rm -f top.sim
	rm -f core.sim
	rm -f wmem.sim


help:
	@echo "Supported targets:"
	@echo "------------------"
	@echo "all:             Build all simulation targets."
	@echo "single_shot_top: Build the top simulation target."
	@echo "top:             Build the top simulation target."
	@echo "core:            Build the core simulation target."
	@echo "wmem:            Build the wmem simulation target."
	@echo "sim-single_shot: Run single shot top level simulation."
	@echo "sim-top:         Run top level simulation."
	@echo "sim-core:        Run core level simulation."
	@echo "sim-wmem:        Run wmem level simulation."
	@echo "clean:           Delete all built files."

#===================================================================
# EOF Makefile
#===================================================================
