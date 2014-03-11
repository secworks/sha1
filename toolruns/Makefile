#===================================================================
#
# Makefile
# --------
# Makefile for building sha1 core and top simulation.
#
#
# (c) 2013 Joachim Strombergson
#
#===================================================================

WMEM_SRC=../src/rtl/sha1_w_mem.v
WMEM_TB_SRC=../src/tb/tb_sha1_w_mem.v

CORE_SRC=../src/rtl/sha1_core.v ../src/rtl/sha1_w_mem.v
CORE_TB_SRC=../src/tb/tb_sha1_core.v

TOP_SRC=../src/rtl/sha1.v $(CORE_SRC)
TOP_TB_SRC=../src/tb/tb_sha1.v

SINGLE_SHOT_TOP_SRC=../src/rtl/sha1_single_shot.v $(CORE_SRC)

CC=iverilog


all: single_shot_top top core wmem


single_shot_top: $(TOP_TB_SRC) $(SINGLE_SHOT_TOP_SRC)
	$(CC) -o single_shot_top.sim $(TOP_TB_SRC) $(SINGLE_SHOT_TOP_SRC)


top: $(TOP_TB_SRC) $(TOP_SRC) $(CORE_SRC)
	$(CC) -o top.sim $(TOP_TB_SRC) $(TOP_SRC)


core: $(CORE_TB_SRC) $(CORE_SRC)
	$(CC) -o core.sim $(CORE_SRC) $(CORE_TB_SRC)


wmem: $(WMEM_SRC) $(WMEM_TB_SRC)
	$(CC) -o wmem.sim $(WMEM_SRC) $(WMEM_TB_SRC)


sim-single_shot_top: single_shot_top.sim
	./single_shot_top.sim


sim-top: top.sim
	./top.sim


sim-core: core.sim
	./core.sim


sim-wmem: wmem.sim
	./wmem.sim


debug:
	@echo "No debug available."


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
	@echo "debug:           Print the internal varibles."
	@echo "clean:           Delete all built files."

#===================================================================
# EOF Makefile
#===================================================================

