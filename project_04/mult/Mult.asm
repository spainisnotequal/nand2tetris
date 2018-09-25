// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	@R2
	M=0	// R2 = 0

(LOOP)
	@R1	
	D=M	// D = R1, number of times we have to sum R0
	@END
	D;JEQ	// if R1 = 0, then go to END

	@R0
	D=M	// D = R0, we'll have to sum R0 "R1-times"
	@R2
	M=D+M	// R2 = R0 + R2

	@R1
	M=M-1	// R1 = R1 - 1, we decrement R1 by one
	
	@LOOP
	0;JMP	// go to LOOP

(END)
	@END
	0;JMP	// infinit loop
