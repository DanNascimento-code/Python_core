
# se trata de um loop que dividirá sempre os indíces da lista pelo meio a cada interação, lado esquerdo e direito
# sempre conterão os índices dos valores da lista, e não necessariamente o valor do índice
# o return da função também será o índice onde o valor foi encontrado (caso tenha sido encontrado)
# e não o valor em sí, e retornará - 1 caso não tenha sido encontrado


def binary_search(nums, target):
    # Lista de entrada:
    # nums = [1, 3, 5, 7, 9, 11, 13]
    # target = 11

    # Inicializamos os ponteiros
    left = 0                      # aponta para o início da lista (índice 0)
    right = len(nums) - 1         # aponta para o final da lista (índice 6)

    # -------------------------
    # ITERAÇÃO 1
    # Intervalo atual:
    # [1, 3, 5, 7, 9, 11, 13]
    #  ↑                   ↑
    # left=0            right=6
    # -------------------------

    while left <= right:

        # Calculamos o meio
        mid = (left + right) // 2

        # ITERAÇÃO 1:
        # mid = (0 + 6) // 2 = 3  (índice 3)
        # nums[mid] = nums[3] = 7  (número 7 se encontra no índice 3 da lista)

        # Comparação:
        if nums[mid] == target:
            # O meio não equivale ao target (7 != 11)
            return mid

        elif nums[mid] < target:
            # 7 < 11 → target está à direita

            # Descartamos toda a metade esquerda (incluindo o meio)
            # Novo intervalo começa após o mid
            left = mid + 1

            # Agora:
            # left = 4
            # right = 6

            # -------------------------
            # ITERAÇÃO 2
            # Intervalo atual:
            # [9, 11, 13]
            #  ↑       ↑
            # left=4 right=6
            # -------------------------

        else:
            # Não entra aqui
            right = mid - 1

        # Próxima iteração do loop...

        # ITERAÇÃO 2 (continuação do loop):
        # mid = (4 + 6) // 2 = 5
        # nums[mid] = nums[5] = 11

        if nums[mid] == target:
            # 11 == 11 → encontramos o valor

            # Retornamos o índice
            return mid

    # Se sair do loop, significa que não encontrou
    return -1


search = binary_search([1, 3, 5, 7, 9, 11, 13], 11)
print(search)

# a saída no console seria: 
# 5 (índice onde o int 11 (target) foi encontrado)