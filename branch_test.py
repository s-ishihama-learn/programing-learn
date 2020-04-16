# 社器保険料率
social_rate = 0.15

# 所得税率
tax_rate = 0.1


# 10円単位四捨五入
def round10(v):
    r = int(v / 10 + 0.5) * 10
    return r


# 10円単位切り捨て
def trunc10(v):
    t = int(v / 10) * 10
    return t


# アルバイト
def calc_part(unit, time):
    salary = unit * time
    tax = salary * tax_rate
    bank = salary - tax
    return int(bank)


if __name__ == "__main__":
    bank_kiku = calc_part(1200, 90)
    bank_yama = calc_part(1000, 120)

    print(f'菊地章さんの振込額={bank_kiku}')
    print(f'山岸柑奈さんの振込額={bank_yama}')
