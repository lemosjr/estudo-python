# 5. Login Simples
print("\n--- Exercício 5: Login Simples ---")
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin" and senha == "admin123":
    print("Login efetuado com sucesso!")
else:
    print("Usuário ou senha incorretos.")