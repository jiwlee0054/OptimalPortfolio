from lib.parameters import ProbOptions, LoadInputFile


options = ProbOptions()

inputs = LoadInputFile(options=options)


"""
1. 발전패턴 가공 365x24
2. 수요패턴 가공 365x24
3. 불확실성이 반영된 발전패턴 생성
4. penalty amount 계산
5. 계약 가격 산정
"""
