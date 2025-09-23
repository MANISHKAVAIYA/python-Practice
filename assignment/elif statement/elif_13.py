# TODO 13. Check the size of a T-shirt (S, M, L, XL) based on input. 

# t-shirt size source = https://www.jockey.in/pages/jockey-t-shirt-size-chart?srsltid=AfmBOoqRfe_2_X2Kv0rzbMAm1w-HJ5Bqj9a-vh7Yr93uRuILVPG3h4np

print("size is measured in inches(in)")

size = int(input("Enter your t-shirt size : "))

if 31 <= size <= 33:
    print(f"your t-shirt size {size} is S")

elif 35 <= size <=37:
    print(f"your t-shirt size {size} is M")

elif 39 <= size <= 41:
    print(f"your t-shirt size {size} is L")

elif 43 <= size <= 45:
    print(f"your t-shirt size {size} is XL")

else:
    print("unavailable stock")