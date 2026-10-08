# Máquina de carrosséis (@diegoreisads)

Gera carrosséis 1080x1350 no estilo "tweet" branco e publica via Metricool.

Uso:
  python3 ferramenta/render.py diegoreisads jobs.json SAIDA [slug1,slug2]
  (jobs.json = lista de {d, slot, n, slug, slides, cap}; veja exemplos/jobs_exemplo.py)
Saída: SAIDA/<d>/<n>-<slug>/slide-XX.jpg + legenda.txt. Copiar para postagens/AAAA-MM-DD/HHMM-slug/.

Chaves de slide: k (kicker), t (título, *negrito* ^destaque dourado^), b (texto), src (fonte),
l ('list','chart','enquete'), items, data, cta, follow, badge ('+20 MIL|ALUNOS').
Slugs com prefixo tiktok/shopee/ia- ganham logo.

Regras fixas: dizer "IA", nunca citar Claude; não cortar fotos; só fotos solo do Diego;
nunca repetir tema já publicado/agendado; todo número com fonte e data.
Horários (BRT): 08h, 11h, 14h, 19h, 21h; 5 posts/dia.
Fotos: fotos/ (pool). Não usar fotos de palco com texto cortado (80bd0a6c, 56f1beea já excluídas das capas).
