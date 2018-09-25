// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(START)
	@SCREEN
	D=A
	@word
	M=D	// word = first word of the screen's memory

	@KBD
	D=M	// input status of the keyboard
	@WHITE
	D;JEQ	// if D = 0, then go to WHITE
	@BLACK
	D;JNE	// if D != 0, then go to BLACK

(WHITE)
	@colour
	M=0	// set the colour variable to white("0" decimal in 16-bits binary is "0000000000000000")
	@DRAW
	0;JMP	// go to DRAW

(BLACK)
	@colour
	M=-1	// set the colour variable to black ("-1" decimal in 16-bits binary is "1111111111111111")
	@DRAW
	0;JMP	// go to DRAW

(DRAW)
	@word
	D=M	// current word address
	@KBD
	D=D-A	// D = current word address - keyboard address
	@START
	D;JEQ	// if D = 0  (current word address is equal to the keyboard address), go to START and start the program again
	
	@colour
	D=M
	@word
	A=M
	M=D	// set that word to zeros or ones depending on the colour variable

	@word
	M=M+1	// next word

	@DRAW
	0;JMP	// go to DRAW and continue drawing the next word
