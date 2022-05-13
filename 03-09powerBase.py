# 전기 사용량의 기본 요금 예산

elec = float(input('전기 사용량을 입력하세요(kWh) >> '))

less200 = elec <= 200
less400 = 201 <= elec <= 400
greater400 = 400 < elec

base = 730*less200 + 260*less400 + greater400*6060
# false=0, true=1
print('전기 사용량(kw): %d, 기본 요금(원): %d' % (elec, base))
