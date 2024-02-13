# 首先创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_user = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_user.append(current_user)

#显示所有已验证的用户

print("\nThe following users have been confirmed:")
for confirmed_user in unconfirmed_users:
	print(confirmed_user.title())