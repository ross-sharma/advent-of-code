package main

import (
	"strconv"
	"strings"
)

const input_0 = `
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
`
const input_1 = `
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
`

const input_3 = `
Register A: 47719761
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0
`

const (
	ADV = 0
	BXL = 1
	BST = 2
	JNZ = 3
	BXC = 4
	OUT = 5
	BDV = 6
	CDV = 7
)

const (
	OPTYPE_LITERAL = iota
	OPTYPE_COMBO
)

type Machine struct {
	Registers          map[string]int
	IsHalted           bool
	InstructionPointer int
	Instructions       []Instruction
	OutputFunc         func(string)
}

type Instruction struct {
	OpCode  int
	Operand int
}

func NewMachine() *Machine {
	return &Machine{
		Registers:          make(map[string]int),
		IsHalted:           false,
		InstructionPointer: 0,
		Instructions:       make([]Instruction, 0),
		OutputFunc:         func(s string) { println(s) },
	}
}

func (m *Machine) SetRegister(key string, value int) {
	m.Registers[key] = value
}

func parseRegisters(input string, m *Machine) {
	for _, line := range strings.Split(input, "\n") {
		line = strings.TrimSpace(line)
		spl := strings.Split(line, ": ")
		key := spl[0][len("Register "):]
		val, _ := strconv.Atoi(spl[1])
		m.SetRegister(key, val)
	}
}

func parseIntructions(input string, m *Machine) {
	input = input[len("Program: "):]
	spl := strings.Split(input, ",")
	for i := 0; i < len(spl); i += 2 {
		opcode, _ := strconv.Atoi(spl[i])
		operand, _ := strconv.Atoi(spl[i+1])
		inst := Instruction{
			OpCode:  opcode,
			Operand: operand,
		}
		m.Instructions = append(m.Instructions, inst)
	}
}

func parse(input string) *Machine {
	m := NewMachine()
	input = strings.TrimSpace(input)
	sections := strings.Split(input, "\n\n")
	parseRegisters(sections[0], m)
	parseIntructions(sections[1], m)
	return m
}

func (m *Machine) GetOperandValue(rawValue int, opType int) int {
	if opType == OPTYPE_LITERAL {
		return rawValue
	}

	switch rawValue {
	case 4:
		return m.Registers["A"]
	case 5:
		return m.Registers["B"]
	case 6:
		return m.Registers["C"]
	default:
		return rawValue
	}

}

func (m *Machine) ADV(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_COMBO)
	quotient := m.Registers["A"] / (1 << opVal)
	m.Registers["A"] = quotient
}

func (m *Machine) BDV(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_COMBO)
	quotient := m.Registers["A"] / (1 << opVal)
	m.Registers["B"] = quotient
}

func (m *Machine) CDV(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_COMBO)
	quotient := m.Registers["A"] / (1 << opVal)
	m.Registers["C"] = quotient
}

func (m *Machine) BXL(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_LITERAL)
	result := m.Registers["B"] ^ opVal
	m.Registers["B"] = result
}

func (m *Machine) BST(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_COMBO)
	result := opVal % 8
	m.Registers["B"] = result
}

func (m *Machine) JNZ(operand int) {
	opVal := m.GetOperandValue(operand, OPTYPE_LITERAL)
	if m.Registers["A"] != 0 {
		m.InstructionPointer = opVal / 2
	} else {
		m.InstructionPointer++
	}
	println("JNZ: " + strconv.Itoa(m.InstructionPointer))
}

func (m *Machine) BXC() {
	m.Registers["B"] = m.Registers["B"] ^ m.Registers["C"]
}

func (m *Machine) OUT(operand int) {
	val := m.GetOperandValue(operand, OPTYPE_COMBO) % 8
	m.OutputFunc(strconv.Itoa(val))
}

func (m *Machine) runNextInstruction() {
	needJump := true

	inst := m.Instructions[m.InstructionPointer]

	switch inst.OpCode {
	case ADV:
		m.ADV(inst.Operand)
	case BXL:
		m.BXL(inst.Operand)
	case BST:
		m.BST(inst.Operand)
	case JNZ:
		m.JNZ(inst.Operand)
		needJump = false
	case BXC:
		m.BXC()
	case OUT:
		m.OUT(inst.Operand)
	case BDV:
		m.BDV(inst.Operand)
	case CDV:
		m.CDV(inst.Operand)
	}

	if needJump {
		m.InstructionPointer++
	}

	if m.InstructionPointer >= len(m.Instructions) {
		m.IsHalted = true
	}
}

func (m *Machine) run() {
	for !m.IsHalted {
		m.runNextInstruction()
	}
}

func (m *Machine) ToString() string {
	var regStr = func(key string) string {
		return key + " = " + strconv.Itoa(m.Registers[key]) + "\n"
	}

	var sb strings.Builder
	sb.WriteString(regStr("A"))
	sb.WriteString(regStr("B"))
	sb.WriteString(regStr("C"))
	sb.WriteRune('\n')

	for index, inst := range m.Instructions {
		sb.WriteString(strconv.Itoa(index/2) + " " + strconv.Itoa(index) + " - ")
		sb.WriteString("OpCode: " + strconv.Itoa(inst.OpCode))
		sb.WriteString(" Operand: " + strconv.Itoa(inst.Operand) + "\n")
	}
	return sb.String()
}

func main() {
	output := make([]string, 0)
	var outputFunc = func(s string) {
		output = append(output, s)
	}
	mac := parse(input_3)
	mac.OutputFunc = outputFunc
	println(mac.ToString())
	mac.run()
	println(strings.Join(output, ","))
	println("Done\n")
	println(mac.ToString())
}
