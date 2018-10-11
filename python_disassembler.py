# ECE 366 GROUP 10
# Python Disassembler
# processBin explains what a MIPS instruction (in binary) is doing
# parameters: addr = (integer form) current instruction address (=PC)
#        binary = a MIPS instruction in machine code binary
# output: 
#       Print out each instruction's functionality, current PC, next PC
# Supported instructions:
#   ADD,ADDI,SUB,LOAD,OR,SLT,STORE,SLL,BEQ,BNE,ANDI,SRL,XOR,J,JR,JAL

def processBin(addr,binary):
    cur_PC = addr
    next_PC= 0
    binary = binary.replace(' ','')
    if(binary[1:4] == "0000"):    # ADD Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "add"
        next_PC = cur_PC + 1
        #else:
         #   print("Instruction not yet supported")
          #  exit()
        print("Instruction: "+op +" $"+ra+",$"+rb)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0001"):  # ADDI Instruction
        ra = str(int(binary[4:5],2))
        imm = int(binary[6:7],2)
        op = "addi"
        next_PC = cur_PC + 1
        imm = str(imm)
        
        print("Instruction: "+op + " $"+ra+","+imm)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0010"):    # SUB Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "sub"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+rb)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0011"):    # LOAD Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "load"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",($"+rb+")")
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0100"):    # OR Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "or"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+rb)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0101"):    # SLT Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "slt"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+rb)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0110"):    # STORE Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "sub"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",($"+rb+")")
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "0111"):    # SLL Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        imm = int(binary[6:7],2)
        imm = str(imm)
        op = "sll"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+imm)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "1000"): # BEQ Instruction
        ra = str(int(binary[4:5],2))
        imm = int(binary[6:7],2)
        imm = str(imm)

        op = "beq"

        zero = 0
        
        print("Instruction: "+op + " $"+ra+","+imm)
        print("If $"+ra+" == $"+zero+", then next_PC = 0x"+ format(cur_PC+(int(imm)<<2)+1,'02x'))
        print("Else next_PC = 0x", format(cur_PC + 1,'02x'))

    elif(binary[1:4] == "1001"): # BNE Instruction
        ra = str(int(binary[4:5],2))
        imm = int(binary[6:7],2)
        imm = str(imm)
       
        op = "bne"

        zero = 0
        
        print("Instruction: "+op + " $" + rs +",$"+rt+","+ imm)
        print("If $"+ra+" != $"+zero+", then next_PC = 0x"+ format(cur_PC+(int(imm)<<2)+1,'02x'))
        print("Else next_PC = 0x", format(cur_PC + 1,'02x'))

    elif(binary[1:4] == "1010"):    # ANDI Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        imm = int(binary[6:7],2)
        imm = str(imm)
        op = "andi"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+imm)
        print("next_PC = 0x"+ format(next_PC,'02x'))

     elif(binary[1:4] == "1011"):    # SRL Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,imm
        imm = int(binary[6:7],2)
        imm = str(imm)
        op = "srl"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+imm)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "1100"):    # XOR Instruction
        ra = str(int(binary[4:5],2))   # slice the ra,rb
        rb = str(int(binary[6:7],2))
        op = "xor"
        next_PC = cur_PC + 1
        
        print("Instruction: "+op +" $"+ra+",$"+rb)
        print("next_PC = 0x"+ format(next_PC,'02x'))

    elif(binary[1:4] == "1101"): # J Instruction
        offset = str(int(binary[5:7],2))

        op = "j"

        print("Instruction: "+op +" " + offset)
        print("next_PC = 0x"+ format((int(offset)<<2),'02x'))

    elif(binary[1:4] == "1110"): # JR Instruction
        ra = str(int(binary[5:7],2))   # slice the ra
        
        op = "jr"

        print("Instruction: "+op +" $" + ra)
        print("Replaces current PC with R5")
        print("next_PC = R5")

    elif(binary[1:4] == "1101"): # JAL Instruction
        offset = str(int(binary[5:7],2))

        op = "jal"
        PC = cur_PC + 1
        
        print("Instruction: "+op +" " + offset)
        print("Save current PC: 0x"+ format((int(PC)<<2),'02x') +" to R5")
        print("next_PC = 0x"+ format((int(offset)<<2),'02x'))
        
    else:
        print("Instruction not yet supported")
        exit()
          
    print()




input_file = open("machine_code.txt", "r")
output_file = open("assembly.txt","w")
print("ISA Python Disassembler")
print("----------")

addr = 0
for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue
    
        line = line.replace("\n","")    
        print("Machine code:", line)          
        line = line.replace(" ","")
    
        processBin(addr,binary)
        addr = addr + 1
    

input_file.close()
output_file.close()
