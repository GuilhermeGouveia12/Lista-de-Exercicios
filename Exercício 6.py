biblioteca = []

def adicionar_livro(titulo, autor, ano):
  novo_livro = [titulo, autor, ano]
  biblioteca.append(novo_livro)
  print("Livro adicionado com sucesso!")

def listar_livros():
  if not biblioteca:
    print("A biblioteca está vazia.")
  else:
    for livro in biblioteca:
      print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

def buscar_livro(titulo):
  resultados = [livro for livro in biblioteca if titulo.lower() in livro[0].lower()]
  if resultados:
    for livro in resultados:
      print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")
  else:
    print("Livro não encontrado.")


adicionar_livro("Revolução dos Bichos", "George Orwell", 1945)

listar_livros()

buscar_livro("pequeno")