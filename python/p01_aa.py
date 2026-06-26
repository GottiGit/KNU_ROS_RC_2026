# ## 파이썬 코드 작성 프롬프트

# 상품의 이름, 가격, 할인율을 입력받아 할인 금액과 최종 가격을 계산하는 파이썬 프로그램을 작성하세요.

# 프로그램은 사용자에게 다음 정보를 입력받아야 합니다.

# 1. 상품명
# 2. 상품 가격
# 3. 할인율

# 상품 가격과 할인율은 숫자로 입력되어야 하며, 숫자가 아닌 값이 입력되면 `"가격과 할인율은 숫자로 입력해야 합니다."`라는 안내 문구를 출력해야 합니다.

# 정상적으로 숫자가 입력되면 다음 공식을 사용해 할인 금액과 최종 가격을 계산하세요.

# ```python
# 할인 금액 = 상품 가격 * 할인율 / 100
# 최종 가격 = 상품 가격 - 할인 금액
# ```

# 계산이 끝나면 상품명, 원래 가격, 할인율, 할인 금액, 최종 가격을 보기 좋게 f-string으로 출력하세요.

# 프로그램은 `main()` 함수 안에 작성하고, 파일이 직접 실행될 때만 `main()` 함수가 실행되도록 작성하세요.

# AI 활용해서 코드를 작성하세요.
def main():
    product = input("상품명을 입력하세요> ")
    price = input("상품 가격을 입력하세요> ")
    discount = input("할인율을 입력하세요. 예: 10> ")

    if price.isdigit() and discount.isdigit():
        price = int(price)
        discount = int(discount)

        discount_price = price * discount / 100
        final_price = price - discount_price

        print("========== 할인 계산 결과 ==========")
        print(f"상품명: {product}")
        print(f"원래 가격: {price}원")
        print(f"할인율: {discount}%")
        print(f"할인 금액: {discount_price}원")
        print(f"최종 가격: {final_price}원")
        print("===================================")
    else:
        print("가격과 할인율은 숫자로 입력해야 합니다.")


if __name__ == "__main__":
    main()