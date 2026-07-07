from dataclasses import dataclass
from enum import Enum, auto
import random

import pytest
from abc import ABC, abstractmethod

#using stack machine as baseline- most simply understandable machine

#there are accumulator machines/register machines but will be added later

"""실험 목표: given simple machine with (no type) simple class of instructions(ops)
주어진 목표를 수행하는 프로그램은 어떻게 자동으로 만들 수 있을까?

자동으로 만드는 방법은 
1. 랜덤으로 만들기(k**n)번 탐색
2. 적합도 함수를 바탕으로 유전 알고리즘 탐색
학습없이는 여기까지
학습 있게 데이터 준비한 뒤에는

인공신경망
강화학습
으로 할 수 있을 것이다 (will be covered)



"""

class Op(Enum): # a special type of class: enumerable class 
    INPUT = auto()
    CONST = auto()
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DUP = auto()
    RETURN = auto()


@dataclass(frozen=True)
class Instruction:
    op: Op
    arg: int | None = None


class VMError(Exception):
    pass

#runner- get 
def run(program: list[Instruction], x: int) -> int:
    stack: list[int] = []
    pc = 0

    while pc < len(program):
        instruction = program[pc]

        match instruction.op:
            case Op.INPUT:
                stack.append(x)

            case Op.CONST:
                if instruction.arg is None:
                    raise VMError("CONST requires an argument")
                stack.append(instruction.arg)

            case Op.ADD:
                if len(stack) < 2:
                    raise VMError("stack underflow")
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            case Op.SUB:
                if len(stack) < 2:
                    raise VMError("stack underflow")
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            case Op.MUL:
                if len(stack) < 2:
                    raise VMError("stack underflow")
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            case Op.DUP:
                if not stack:
                    raise VMError("stack underflow")
                stack.append(stack[-1])

            case Op.RETURN:
                if not stack:
                    raise VMError("empty return stack")
                return stack.pop()

        pc += 1

    raise VMError("program ended without RETURN")


#0707: 적합도 함수. 이론상 operation enumeration으로는 6+n1**2)**n2 의 시간 복잡도가 필요하다

examples = [
    (-2, -5),
    (0, 1),
    (1, 4),
    (5, 16),
    (10, 31),
]
#note: is not right instructions- only a machine that is fit with the examples


def fitness(program): #auto synthesize programs fitness check
    error = 0

    for x, expected in examples:
        try:
            actual = run(program, x)
            error += abs(actual - expected)
        except (IndexError, RuntimeError, ValueError,VMError):
            return float("inf")

    return error



def random_synthesizer(max_length): # 기본 합성기, without buffer hit ratio 1/7**6*20**7
    def random_instruction():
        op=random.choice(list(Op))

        if op == Op.CONST:
            return Instruction(
                op=op,
                arg=random.randint(-3,3),
            )

        return Instruction(op=op)
    return [random_instruction() for _ in range(max_length)]

    



#if fitting, return the program
def fitness_checker(seed:int,synthesizer, input=100000)->list:
    step=0
    while step<10000000:
        program=synthesizer(input)
        if fitness(program)==0:
            return program
        if step%100==0:
            print(f"SEARCH STEP:{step}, FITNESS:{fitness(program)}")
        
        step+=1

print(fitness_checker(42,random_synthesizer,6))

reference_program = [
    Instruction(Op.INPUT),
    Instruction(Op.CONST, 3),
    Instruction(Op.MUL),
    Instruction(Op.CONST, 1),
    Instruction(Op.ADD),
    Instruction(Op.RETURN),
]
proxy_program = [
    Instruction(op=Op.CONST, arg=1),
    Instruction(op=Op.INPUT, arg=None),
    Instruction(op=Op.CONST, arg=-3),
    Instruction(op=Op.MUL, arg=None),
    Instruction(op=Op.SUB, arg=None),
    Instruction(op=Op.RETURN, arg=None)
]

examples = [
    (-2, -5),
    (0, 1),
    (1, 4),
    (5, 16),
    (10, 31),
]

@pytest.mark.parametrize("program,examples",[(reference_program,examples)])

def test_vm(program,examples):
    for i in examples:
        assert run(program, i[0]) == i[1]


