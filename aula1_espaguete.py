import os
import pandas as pd

# buscar_csvs
todos_arquivos = []
pastas_para_verificar = ["dados"]
while pastas_para_verificar:
    pasta = pastas_para_verificar.pop()
    for item in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, item)
        if os.path.isdir(caminho_completo):
            pastas_para_verificar.append(caminho_completo)
        elif item.endswith(".csv") and not item.startswith("resumo_"):
            todos_arquivos.append(caminho_completo)

# carregar_vendas + limpar_dados
todos_dfs = []
for caminho in todos_arquivos:
    df_temp = pd.read_csv(caminho)
    df_temp = df_temp.dropna(subset=["regiao", "quantidade"])
    df_temp["quantidade"] = df_temp["quantidade"].astype(int)
    df_temp = df_temp[df_temp["quantidade"] > 0]
    todos_dfs.append(df_temp)

# calcular_totais_por_regiao
df_tudo = pd.concat(todos_dfs, ignore_index=True)
df_tudo["total"] = df_tudo["quantidade"] * df_tudo["valor_unitario"]
resumo = df_tudo.groupby("regiao")["total"].agg(["sum", "count"]).reset_index()
resumo.columns = ["regiao", "faturamento", "num_vendas"]
resumo = resumo.sort_values("faturamento", ascending=False)

# salvar_resumo
resumo.to_csv("dados/resumo_consolidado.csv", index=False)

print("=== Relatorio consolidado ===")
print(resumo.to_string(index=False))
