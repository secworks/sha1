//======================================================================
//
// sha1_w_mem_reg.v
// -----------------
// The SHA-1 W memory. This memory includes functionality to 
// expand the block into 80 words.
//
//
// Copyright (c) 2013 Secworks Sweden AB
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or 
// without modification, are permitted provided that the following 
// conditions are met: 
// 
// 1. Redistributions of source code must retain the above copyright 
//    notice, this list of conditions and the following disclaimer. 
// 
// 2. Redistributions in binary form must reproduce the above copyright 
//    notice, this list of conditions and the following disclaimer in 
//    the documentation and/or other materials provided with the 
//    distribution. 
// 
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
// FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
// COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
// BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
// STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
// ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//======================================================================

module sha1_w_mem(
                  input wire           clk,
                  input wire           reset_n,

                  input wire           init,
                  input wire [511 : 0] block,

                  input wire [6 :   0] addr,
                  output wire [31 : 0] w
                 );

  
  //----------------------------------------------------------------
  // Registers including update variables and write enable.
  //----------------------------------------------------------------
  reg [31 : 0] w_mem [0 : 15];
  
  
  //----------------------------------------------------------------
  // Wires.
  //----------------------------------------------------------------
  reg [31 : 0] w_tmp;
  
  
  //----------------------------------------------------------------
  // Concurrent connectivity for ports etc.
  //----------------------------------------------------------------
  assign w = w_tmp;
  
  
  //----------------------------------------------------------------
  // reg_update
  // Update functionality for all registers in the core.
  // All registers are positive edge triggered with synchronous
  // active low reset. All registers have write enable.
  //----------------------------------------------------------------
  always @ (posedge clk)
    begin : reg_update
      if (!reset_n)
        begin
          w_mem[00] <= 32'h00000000;
          w_mem[01] <= 32'h00000000;
          w_mem[02] <= 32'h00000000;
          w_mem[03] <= 32'h00000000;
          w_mem[04] <= 32'h00000000;
          w_mem[05] <= 32'h00000000;
          w_mem[06] <= 32'h00000000;
          w_mem[07] <= 32'h00000000;
          w_mem[08] <= 32'h00000000;
          w_mem[09] <= 32'h00000000;
          w_mem[10] <= 32'h00000000;
          w_mem[11] <= 32'h00000000;
          w_mem[12] <= 32'h00000000;
          w_mem[13] <= 32'h00000000;
          w_mem[14] <= 32'h00000000;
          w_mem[15] <= 32'h00000000;
        end
      else
        begin
          if (init)
            begin
              w_mem[00] <= block[511 : 480];
              w_mem[01] <= block[479 : 448];
              w_mem[02] <= block[447 : 416];
              w_mem[03] <= block[415 : 384];
              w_mem[04] <= block[383 : 352];
              w_mem[05] <= block[351 : 320];
              w_mem[06] <= block[319 : 288];
              w_mem[07] <= block[287 : 256];
              w_mem[08] <= block[255 : 224];
              w_mem[09] <= block[223 : 192];
              w_mem[10] <= block[191 : 160];
              w_mem[11] <= block[159 : 128];
              w_mem[12] <= block[127 :  96];
              w_mem[13] <= block[95  :  64];
              w_mem[14] <= block[63  :  32];
              w_mem[15] <= block[31  :   0];
            end
        end
    end // reg_update

  
  //----------------------------------------------------------------
  // external_addr_mux
  //
  // Mux for the external read operation. This is where we extract
  // the W variable. This version implements the circular buffer
  // type of W scheduler for SHA-1.
  //----------------------------------------------------------------
  always @*
    begin : external_addr_mux
      reg [3  :  0] s13_addr;
      reg [3  :  0] s8_addr;
      reg [3  :  0] s2_addr;
      reg [31 :  0] pre_w;
      
      s13_addr = (addr + 13);
      s8_addr  = (addr +  8);
      s2_addr  = (addr +  2);
      pre_w = w_mem[s13_addr] ^ w_mem[s8_addr] ^ w_mem[s2_addr];
      
      if (addr < 16)
        begin
          w_tmp = w_mem[addr[3 : 0]];
        end
      else
        begin
          w_tmp = {pre_w[30 : 0], pre_w[31]};
        end
    end // external_addr_mux

endmodule // sha1_w_mem

//======================================================================
// sha1_w_mem.v
//======================================================================
