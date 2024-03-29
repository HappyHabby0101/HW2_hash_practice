# Import Data
with open("hw2_data.txt", "r") as file:
    data = file.readlines() # data:list

# Put data in dictionary
hash = {}
for line in data:
    key = line.strip()
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1


num_keys = len(hash)
print("總共有多少個不重複的英文字：", num_keys )
print("每一個英文字出現次數為：\n", hash)
