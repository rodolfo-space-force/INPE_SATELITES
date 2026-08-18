import matplotlib.pyplot as plt

# ============================================================
# HISTÓRICO DE LANÇAMENTOS DE SATÉLITES BRASILEIROS
#
# Fonte:
# Elaborado pelo autor com base em dados do INPE (2025)
# ============================================================

# Dados dos satélites
satelites = [
    ("SCD-1",      1993, "Sucesso - operacional"),
    ("SCD-2A",     1997, "Falha do lançador"),
    ("SCD-2",      1998, "Sucesso - operacional"),
    ("CBERS-1",    1999, "Sucesso - missão encerrada"),
    ("SACI-1",     1999, "Falha do satélite"),
    ("SACI-2",     1999, "Falha do lançador"),
    ("CBERS-2",    2003, "Sucesso - missão encerrada"),
    ("CBERS-2B",   2007, "Sucesso - missão encerrada"),
    ("CBERS-3",    2013, "Falha do lançador"),
    ("CBERS-4",    2014, "Sucesso - operacional"),
    ("CBERS-4A",   2019, "Sucesso - operacional"),
    ("AMAZONIA-1", 2021, "Sucesso - operacional"),
]

# ============================================================
# Categorias no eixo Y
# ============================================================

categorias = {
    "Falha do lançador": 0,
    "Falha do satélite": 1,
    "Sucesso - missão encerrada": 2,
    "Sucesso - operacional": 3
}

# ============================================================
# Cores
# ============================================================

cores = {
    "Falha do lançador": "red",
    "Falha do satélite": "orange",
    "Sucesso - missão encerrada": "blue",
    "Sucesso - operacional": "green"
}

# ============================================================
# Criando a figura
# ============================================================

fig, ax = plt.subplots(figsize=(16, 8))

# ============================================================
# Plotagem
# ============================================================

for nome, ano, status in satelites:

    y = categorias[status]

    # Ponto referente ao satélite
    ax.scatter(
        ano,
        y,
        s=300,
        color=cores[status],
        edgecolor="black",
        linewidth=1.1,
        zorder=3
    )

    # --------------------------------------------------------
    # Posição padrão do texto
    # --------------------------------------------------------

    deslocamento_x = 0

    if status in [
        "Sucesso - operacional",
        "Sucesso - missão encerrada"
    ]:
        deslocamento_y = -0.15
    else:
        deslocamento_y = 0.16

    # --------------------------------------------------------
    # Ajustes manuais para evitar sobreposição de rótulos
    # --------------------------------------------------------

    if nome == "CBERS-4A":
        deslocamento_x = -0.55
        deslocamento_y = -0.17

    elif nome == "AMAZONIA-1":
        deslocamento_x = 0.65
        deslocamento_y = -0.17

    # --------------------------------------------------------
    # Inserção do nome do satélite
    # --------------------------------------------------------

    ax.text(
        ano + deslocamento_x,
        y + deslocamento_y,
        nome,
        ha="center",
        va="center",
        fontsize=10.5
    )

# ============================================================
# Configuração do eixo Y
# ============================================================

ax.set_yticks([0, 1, 2, 3])

ax.set_yticklabels([
    "Falha do lançador",
    "Falha do satélite",
    "Sucesso – missão encerrada",
    "Sucesso – ainda operacional"
], fontsize=11)

# ============================================================
# Configuração do eixo X
# ============================================================

anos = [
    1993,
    1997,
    1998,
    1999,
    2003,
    2007,
    2013,
    2014,
    2019,
    2021
]

ax.set_xticks(anos)

ax.tick_params(
    axis="x",
    labelrotation=45,
    labelsize=10
)

# Limites
ax.set_xlim(1991.5, 2023.5)
ax.set_ylim(-0.25, 3.25)

# ============================================================
# Grade
# ============================================================

ax.grid(
    True,
    linestyle="--",
    linewidth=0.7,
    alpha=0.4
)

ax.set_axisbelow(True)

# ============================================================
# Título e eixos
# ============================================================

ax.set_title(
    "Histórico de Lançamentos de Satélites Brasileiros",
    fontsize=15,
    pad=15
)

ax.set_xlabel(
    "Ano de lançamento",
    fontsize=12
)

# ============================================================
# Fonte
# ============================================================

fig.text(
    0.125,
    0.015,
    "Fonte: Elaborado com base em dados do INPE (2025).",
    fontsize=9,
    ha="left"
)

# ============================================================
# Ajuste do layout
# ============================================================

plt.tight_layout(
    rect=[0, 0.05, 1, 1]
)

# ============================================================
# Salvar imagem em alta resolução
# ============================================================

plt.savefig(
    "historico_lancamentos_satelites_brasileiros_INPE.png",
    dpi=300,
    bbox_inches="tight"
)

# ============================================================
# Exibir
# ============================================================

plt.show()
