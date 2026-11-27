import json,sys
# Semana 17/12 a 23/12/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
HT='#tiktokshop #shopee #instagramshop #livesell #vendasonline #empreendedorismo'
HIA=HT+' #ia'
AV='Os resultados variam de pessoa para pessoa e dependem de constância, produto e execução. Confira sempre as regras atuais de cada plataforma.'
def J(slug,slides,cap,tags=HT,av=False):
    c=cap+('\n\n'+AV if av else '')
    return {'slug':slug,'slides':slides,'cap':c+'\n\nCurta, salve e siga @{H} para mais conteúdo de TikTok Shop, Shopee, Instagram Shop e IA.\n\n'+tags}
def end(t,b,cta=None):
    d={'t':t,'b':b,'follow':True}
    if cta:d['cta']=cta
    return d
jobs=[]
def add(day,slot,j):
    j['d']=day;j['slot']=slot;j['n']=slot;jobs.append(j)
def steps(slug,k,t,b,st,cap,et,eb,cta=None,tags=HT,av=False):
    s=[{'k':k,'t':t,'b':b}]
    for i,(a,c) in enumerate(st):s.append({'k':'Passo %d'%(i+1),'t':a,'b':c})
    s.append(end(et,eb,cta))
    return J(slug,s,cap,tags,av)
def lst(slug,k,t,items,cap,et,eb,cta=None,tags=HT,src=None,cb='',tip=None):
    s=[{'k':k,'t':t,'b':cb},{'l':'list','k':'Veja','t':'Em *poucos* passos','items':[{'a':str(i+1),'t':x} for i,x in enumerate(items)]}]
    if tip:s.append({'k':tip[0],'t':tip[1],'b':tip[2]})
    s.append(end(et,eb,cta))
    if src:s[1]['src']=src
    return J(slug,s,cap,tags)
def enq(slug,q,opts,cap):
    return J(slug,[{'k':'Enquete','t':q,'b':'Comente a letra'},{'l':'enquete','k':'Escolha','t':'Qual é a *sua*?','b':'\n'.join(opts)},{'k':'Próximo post','t':'Eu respondo a *mais votada*','b':'Conte nos comentários qual é a sua letra e por quê.'},end('Comente a sua ^letra^','Curta, salve e siga para ver a resposta.')],cap)
def quiz(slug,q,qb,opts,ans_t,ans_b,lic_t,lic_b,cap,et='Você ^acertou^?',eb='Comente a letra que você marcou.'):
    return J(slug,[{'k':'Quiz','t':q,'b':qb},{'l':'enquete','k':'Escolha','t':'Qual é a *resposta*?','b':'\n'.join(opts)},{'k':'Resposta','t':ans_t,'b':ans_b},{'k':'Lição','t':lic_t,'b':lic_b},end(et,eb)],cap)

def ia(slug,t,b,st,cap):
    return steps(slug,'IA para vendedor',t,b,st,cap,'Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA)
def news(slug,k,t,sub,items,src,ctx,para,cap,cta='LIVE',et='Quer aprender a ^vender em live^?'):
    return J(slug,[{'k':k,'t':t,'b':sub},
      {'l':'list','k':'Os números','t':'O que a matéria *mostrou*','items':[{'a':a,'t':x} for a,x in items],'src':src},
      {'k':'Como ler','t':ctx[0],'b':ctx[1],'src':src},
      {'k':'Para você','t':para[0],'b':para[1]},
      end(et,'Comente a palavra abaixo e eu te chamo no direct.',cta)],cap,HT,av=True)

# ===================== QUI 17/12 =====================
D='2026-12-17'
S='Fonte: E-Commerce Brasil (13/11/2026)'
add(D,'0800',news('novidade-shopee-11-11-dobrou-black-friday','Novidade: Shopee','Shopee diz que o 11.11 ^dobrou^ a Black Friday de 2025','Dados divulgados pela empresa',
 [('2x+','Vendas do 11.11 de 2026 sobre a Black Friday de 2025, segundo a matéria'),('95%+','Do volume vendido veio de vendedores locais'),('52%','Dos pedidos foram pagos com Pix')],S,
 ('Dados da *Shopee*','Os números foram divulgados pela empresa. A matéria não traz valores absolutos nem a metodologia.'),
 ('*Pix* e resposta rápida','Muita gente paga no Pix. Preço claro e atendimento rápido ajudam a não perder o pedido.'),
 'A Shopee diz que as vendas do 11.11 de 2026 mais que dobraram sobre a Black Friday de 2025, com mais de 95% do volume vindo de vendedores locais e 52% dos pedidos no Pix. Dados da empresa. Fonte: E-Commerce Brasil (13/11/2026). Comente LIVE.'))
add(D,'1100',steps('live-contar-a-historia-do-produto','Passo a passo de live','Conte a ^história^ do produto na live','Em vez de só ler a ficha técnica',
 [('Comece pelo problema','Diga que situação do dia a dia o produto resolve. Seja específico.'),
  ('Mostre o uso real','Use o produto na câmera, do começo ao fim, sem cortes.'),
  ('Fale do cuidado','Explique material, medidas e cuidados com o que está escrito no anúncio.')],
 'Como contar a história do produto na live em 3 passos: problema, uso real e cuidado. Salve e teste na próxima.','Salve para ^testar^','E me conta qual produto você vai mostrar.'))
add(D,'1400',ia('ia-resposta-para-duvida-de-tamanho','Resposta para dúvida de ^tamanho^','Com ajuda da IA, sem chute',
 [('Reúna as medidas','Tenha a tabela de medidas do fornecedor à mão. Meça o produto.'),
  ('Use este prompt','Escreva uma resposta curta e educada para um cliente com dúvida de tamanho, usando esta tabela de medidas. Peça a medida dele.'),
  ('Revise os dados','Confira se cada medida está igual à tabela. Não invente número.')],
 'Como usar IA para responder dúvidas de tamanho com educação e sem inventar medidas, em 3 passos. Comente PROMPT.'))
add(D,'1900',enq('enquete-ultima-live-do-ano','Quando será a sua última live do ano?',['Antes do Natal','Entre Natal e Ano-Novo','Só em janeiro','Ainda não sei'],'Enquete: quando será a sua última live do ano? Comente a letra: A antes do Natal, B entre Natal e Ano-Novo, C só em janeiro ou D ainda não sei.'))
add(D,'2100',lst('manter-cortar-testar','Para refletir','^Manter^, cortar e testar',
 ['Manter: uma rotina que funcionou em 2026','Cortar: uma tarefa que só tomou tempo','Testar: uma ideia pequena para janeiro'],
 'Três perguntas simples para fechar o ano: o que manter, o que cortar e o que testar. Salve e responda no papel.','Salve e ^responda^ hoje','E me conta o que você vai manter.',cb='Um exercício de 10 minutos',tip=('Por quê','Decidir *pouco* ajuda','Poucas escolhas bem feitas valem mais do que uma lista enorme que ninguém cumpre.')))

# ===================== SEX 18/12 =====================
D='2026-12-18'
S='Fonte: BPMoney (26/11/2026), relatório do BTG Pactual'
add(D,'0800',news('novidade-tiktok-shop-1-58-bi-por-mes','Novidade: TikTok Shop','TikTok Shop teria vendido ^R$ 1,58 bi^ em junho','Estimativa do BTG Pactual para o Brasil',
 [('R$ 1,58 bi','Vendas estimadas em junho de 2026 (valor bruto, o GMV)'),('R$ 19 bi','Projeção anualizada a partir de junho, não é o valor já vendido'),('~20%','Das vendas no Brasil vêm de lives, ante cerca de 10% nos EUA')],S,
 ('São *estimativas*','O BTG usa dados da Momentum Works e da Tabcut. A própria matéria pede cautela com o valor anual.'),
 ('A live pesa *mais* aqui','Pelo relatório, a live ocupa uma fatia maior das vendas no Brasil do que nos EUA. Vale treinar.'),
 'Segundo o BTG Pactual, o TikTok Shop teria vendido R$ 1,58 bilhão em junho de 2026 (GMV estimado). O valor de R$ 19 bi por ano é projeção, não venda realizada. Fonte: BPMoney (26/11/2026). Comente LIVE.'))
add(D,'1100',steps('tiktok-3-ganchos-para-abrir-o-video','TikTok Shop','3 ganchos para ^abrir o vídeo^','Os primeiros segundos pedem clareza',
 [('A pergunta','Comece com uma pergunta que o seu cliente faria. Ex.: como guardar isso sem ocupar espaço?'),
  ('O resultado','Mostre o produto funcionando já no primeiro quadro.'),
  ('O erro comum','Fale de um erro que as pessoas cometem e como evitar.')],
 'Três ganchos para abrir um vídeo de produto: pergunta, resultado e erro comum. Salve e teste um hoje.','Salve para ^gravar^ hoje','E me conta qual gancho você vai testar.'))
add(D,'1400',ia('ia-ler-relatorio-de-vendas','Entenda o seu ^relatório^ de vendas com IA','Sem se perder nos números',
 [('Copie os números','Cole a tabela de vendas da semana, sem dados pessoais de clientes.'),
  ('Use este prompt','Resuma estes números em 5 pontos simples: o que subiu, o que caiu e uma ação para a próxima semana.'),
  ('Confira no painel','A IA pode errar conta. Compare com o painel da plataforma antes de decidir.')],
 'Como usar IA para resumir o relatório de vendas da semana e conferir os números no painel, em 3 passos. Comente PROMPT.'))
add(D,'1900',J('mito-seguidor-nao-e-venda',[
 {'k':'Mito ou verdade','t':'"Preciso de ^muitos seguidores^ para vender"','b':'Vamos separar as coisas'},
 {'k':'O que pesa','t':'Seguidor *ajuda*, mas não decide','b':'Oferta clara, produto certo, prova do uso e resposta rápida também contam muito.'},
 {'k':'Na prática','t':'Comece com o *público que tem*','b':'Mostre o produto, responda as dúvidas e peça para quem já comprou contar como foi.'},
 {'k':'Atenção','t':'Resultado *varia*','b':'Não há garantia de venda. Teste, meça e melhore um ponto de cada vez.'},
 end('Qual é o seu ^maior bloqueio^?','Comente aqui embaixo.')],
 'Mito: preciso de muitos seguidores para vender. Seguidor ajuda, mas oferta clara, produto certo e atendimento também contam. Comente o seu maior bloqueio.'))
add(D,'2100',lst('um-passo-pequeno-por-dia','Para refletir','Um ^passo pequeno^ por dia',
 ['Responder uma dúvida de cliente','Gravar um vídeo curto do produto','Anotar um aprendizado do dia'],
 'Um passo pequeno por dia: responder uma dúvida, gravar um vídeo curto e anotar um aprendizado. Qual você faz hoje?','Qual passo você ^faz hoje^?','Comente 1, 2 ou 3.',cb='Constância sem exagero',tip=('Por quê','Rotina *leve* se mantém','Metas pequenas são mais fáceis de repetir, e repetir é o que melhora o resultado.')))

# ===================== SAB 19/12 =====================
D='2026-12-19'
S='Fonte: Exame (04/11/2026), estudo da BR Media'
add(D,'0800',news('novidade-black-friday-dos-influenciadores','Novidade: Black Friday','Black Friday 2025: influenciadores lideraram a ^conversa^','Estudo da BR Media citado pela Exame',
 [('74,8%','Das interações sobre a Black Friday nas redes em 2025 foram de influenciadores'),('18,6%','Foram de marcas'),('20 mil+','Creators publicaram sobre a data no período')],S,
 ('Dado de *2025*','O estudo olhou conversas em seis redes entre 1/11 e 10/12/2025. Mostra conversa, não venda.'),
 ('Recomendação *conta*','Quem mostra o produto em uso ajuda o público a decidir. Comece com o que você já vende.'),
 'Na Black Friday de 2025, influenciadores foram responsáveis por 74,8% das interações sobre a data nas redes, contra 18,6% das marcas, segundo estudo da BR Media citado pela Exame. É dado de 2025 e de conversa, não de vendas. Fonte: Exame (04/11/2026). Comente QUERO.',cta='QUERO',et='Quer ^falar comigo^?'))
add(D,'1100',steps('live-presentes-de-ultima-hora','Passo a passo de live','Presentes de ^última hora^ na live','Sem prometer o que você não controla',
 [('Mostre opções por preço','Separe 3 faixas de preço e apresente uma de cada vez.'),
  ('Confirme o prazo','Antes da live, confira o prazo de postagem e entrega na plataforma. Fale só o que for confirmado.'),
  ('Ofereça um plano B','Sugira vale-presente ou item que chegue depois, se o prazo apertar.')],
 'Como vender presentes de última hora na live em 3 passos, falando só de prazos confirmados. Salve para usar nesta semana.','Salve para ^usar^ nesta semana','E me conta o que você vai ofertar.'))
add(D,'1400',ia('ia-roteiro-de-story-de-natal','Roteiro de story de ^Natal^ com IA','Para a semana inteira',
 [('Defina o foco','Escolha o tema: prazo, presente, bastidor ou agradecimento.'),
  ('Use este prompt','Crie um roteiro de 3 stories curtos de Natal para uma loja pequena, com tom caloroso e uma chamada para ação clara.'),
  ('Coloque a sua cara','Troque o que soar genérico por algo seu e grave com o produto na mão.')],
 'Como usar IA para criar um roteiro de 3 stories de Natal para a sua loja, em 3 passos. Comente PROMPT.'))
add(D,'1900',quiz('quiz-o-que-e-margem','O que é ^margem^?','Palavra que decide se sobra dinheiro.',
 ['O preço do frete','O que sobra do preço após os custos','O desconto da oferta','O número de vendas'],'É a *letra B*','Margem é o que sobra do preço depois de descontar custo do produto, taxas, frete e embalagem. Normalmente se mostra em porcentagem.',
 'Calcule *antes* da oferta','Antes de dar desconto, confira se a margem ainda cobre os custos.',
 'Quiz: o que é margem? Resposta: B, a parte do preço que sobra depois dos custos. Comente a letra que você marcou.'))
add(D,'2100',lst('presente-para-o-seu-eu-de-janeiro','Para refletir','Deixe um ^presente^ para janeiro',
 ['Organize o estoque que sobrou','Anote as perguntas que mais chegaram','Escolha um produto para testar em 2027'],
 'Três tarefas pequenas que ajudam você em janeiro: organizar o estoque, anotar perguntas e escolher um produto para testar. Salve.','Salve e ^faça uma^ hoje','E me conta qual você escolheu.',cb='Facilite a volta ao trabalho',tip=('Por quê','Futuro *agradece*','Quem deixa tudo anotado volta ao trabalho sem começar do zero.')))

# ===================== DOM 20/12 =====================
D='2026-12-20'
S='Fonte: E-Commerce Brasil (13/11/2026)'
add(D,'0800',news('novidade-shopee-turbo-pet','Novidade: Shopee','No Shopee Turbo, ^pet^ liderou os pedidos','Dados do 11.11 de 2026, divulgados pela empresa',
 [('4 de 5','Itens mais pedidos no Turbo eram da categoria pet, como ração e areia'),('Recorde','Maior volume de pedidos do Turbo desde o lançamento'),('3x+','Vendas pelo fulfillment ante a Black Friday de 2025')],S,
 ('O Turbo é *regional*','A entrega em até 4 horas vale para a Grande São Paulo. Os dados são da Shopee.'),
 ('Pense em *recompra*','Ração e areia são itens de uso contínuo. Pense em produtos que o cliente precisa repor.'),
 'No 11.11 de 2026, quatro dos cinco itens mais pedidos no Shopee Turbo eram de pet, segundo a Shopee. O Turbo entrega em até 4 horas na Grande São Paulo. Fonte: E-Commerce Brasil (13/11/2026). Comente COMECAR.',cta='COMECAR',et='Quer ^começar a vender^?'))
add(D,'1100',steps('live-arrumar-o-estoque-antes-de-ligar','Passo a passo de live','Arrume o ^estoque^ antes de ligar','Para não prometer o que acabou',
 [('Conte o que tem','Confira a quantidade de cada produto que você vai mostrar.'),
  ('Separe e identifique','Deixe os itens da live à mão, com etiqueta de nome e preço.'),
  ('Atualize o anúncio','Se algo acabar durante a live, pause o anúncio e avise o público.')],
 'Como arrumar o estoque antes de ligar a live, em 3 passos: contar, separar e atualizar o anúncio. Salve.','Salve para ^conferir^ antes da live','E me conta se já tem o seu método.'))
add(D,'1400',ia('ia-checklist-de-envio-de-natal','Checklist de ^envio^ com IA','Para a semana do Natal',
 [('Descreva o seu fluxo','Conte como você separa, embala e posta os pedidos.'),
  ('Use este prompt','Monte um checklist de envio para pedidos de Natal com etapas, horários limite e pontos de conferência.'),
  ('Ajuste aos prazos reais','Troque os horários pelos prazos de postagem da sua plataforma e transportadora.')],
 'Como usar IA para montar um checklist de envio para a semana do Natal e ajustar aos prazos reais, em 3 passos. Comente PROMPT.'))
add(D,'1900',enq('enquete-maior-aprendizado-de-2026','Qual foi o seu maior aprendizado de 2026?',['Constância','Fazer live','Usar IA','Cuidar do cliente'],'Enquete: qual foi o seu maior aprendizado de 2026? Comente a letra: A constância, B fazer live, C usar IA ou D cuidar do cliente.'))
add(D,'2100',lst('semana-do-natal-3-prioridades','Para começar a semana','Semana do Natal: ^3 prioridades^',
 ['Responder todos os pedidos e dúvidas','Conferir o prazo de postagem','Cuidar do seu descanso'],
 'Semana do Natal: responder pedidos e dúvidas, conferir prazos de postagem e cuidar do descanso. Qual é a sua prioridade?','Qual é a sua ^prioridade^?','Comente 1, 2 ou 3.',cb='Foco no essencial',tip=('Por quê','Natal pede *organização*','Com pouco tempo, o essencial bem feito vale mais do que fazer tudo.')))

# ===================== SEG 21/12 =====================
D='2026-12-21'
S='Fonte: BPMoney (26/11/2026), relatório do BTG Pactual'
add(D,'0800',news('novidade-tiktok-shop-200-criadores-1-milhao','Novidade: TikTok Shop','Só cerca de ^200^ criadores passaram de R$ 1 mi','Estimativas do BTG Pactual para o 1º semestre de 2026',
 [('2,3 mi','Influenciadores ativos no TikTok Shop de janeiro a junho'),('~200','Passaram de R$ 1 milhão em vendas'),('~30%','Do GMV veio de moda feminina e beleza juntas')],S,
 ('Poucos chegam *ao topo*','São estimativas de terceiros. O resultado varia muito e depende de produto, constância e execução.'),
 ('Meta *realista*','Em vez de comparar com o topo, comece com uma meta pequena: a primeira venda, depois as dez primeiras.'),
 'Segundo estimativas do BTG Pactual, cerca de 200 criadores passaram de R$ 1 milhão em vendas no TikTok Shop entre 2,3 milhões de influenciadores ativos no 1º semestre de 2026. Resultados variam. Fonte: BPMoney (26/11/2026). Comente COMECAR.',cta='COMECAR',et='Quer ^começar do jeito certo^?'))
add(D,'1100',steps('tiktok-roteiro-de-video-de-5-quadros','TikTok Shop','Vídeo de produto em ^5 quadros^','Simples de gravar com o celular',
 [('Gancho','Quadro 1: mostre o resultado ou faça a pergunta.'),
  ('Produto','Quadros 2 e 3: mostre o produto de perto e em uso.'),
  ('Fechamento','Quadros 4 e 5: diga para quem serve e peça um comentário ou o clique.')],
 'Roteiro de vídeo de produto em 5 quadros: gancho, produto de perto, produto em uso, para quem serve e chamada. Salve.','Salve para ^gravar^','E me conta qual produto você vai gravar.'))
add(D,'1400',ia('ia-lista-de-tarefas-da-semana-do-natal','Lista de tarefas da semana do ^Natal^','Com IA, em 2 minutos',
 [('Liste tudo','Escreva todas as tarefas soltas: pedidos, envios, posts, lives.'),
  ('Use este prompt','Organize estas tarefas por prioridade e por dia, de segunda a quarta, com no máximo 5 tarefas por dia.'),
  ('Corte o resto','Escolha o que cabe no seu tempo. O que não cabe, fica para janeiro.')],
 'Como usar IA para organizar as tarefas da semana do Natal por prioridade, em 3 passos. Comente PROMPT.'))
add(D,'1900',quiz('quiz-o-que-e-gancho','O que é ^gancho^ em vídeo?','Os primeiros segundos importam.',
 ['O final do vídeo','O início que chama a atenção','A trilha sonora','A legenda'],'É a *letra B*','Gancho é o começo do vídeo, a frase ou imagem que faz a pessoa querer continuar assistindo.',
 'Comece *forte*','Pense na primeira frase antes de gravar o resto.',
 'Quiz: o que é gancho em vídeo? Resposta: B, o início que chama a atenção. Comente a letra que você marcou.'))
add(D,'2100',J('agradecimento-de-fim-de-ano',[
 {'k':'Antes do Natal','t':'Obrigado por ^2026^','b':'Por acompanhar, comentar e testar'},
 {'k':'O que eu desejo','t':'Mais *constância*, menos pressão','b':'Que a sua semana de Natal seja de vendas honestas e descanso de verdade.'},
 {'k':'Seu momento','t':'Você *chegou* até aqui','b':'Cada live, cada vídeo e cada resposta ao cliente foi um passo.'},
 end('Deixe um ^agradecimento^','Comente uma conquista de 2026, grande ou pequena.')],
 'Obrigado por acompanhar em 2026. Comente uma conquista sua deste ano, grande ou pequena.'))

# ===================== TER 22/12 =====================
D='2026-12-22'
S='Fonte: E-Commerce Brasil (18/11/2026), dados da Shopee'
add(D,'0800',news('novidade-shopee-video-280-milhoes','Novidade: Shopee','Shopee Vídeo tem mais de ^280 mi^ de reproduções','Dados da empresa citados pela matéria',
 [('280 mi+','Reproduções no Shopee Vídeo'),('140 mil+','Criadores ativos')],S,
 ('Dado da *empresa*','Os números são da Shopee. A matéria não detalha o período nem a metodologia.'),
 ('Vídeo curto *também* vende','Além da live, vídeos curtos mostram o produto. Poste vídeos simples e constantes.'),
 'A Shopee diz que o Shopee Vídeo tem mais de 280 milhões de reproduções e mais de 140 mil criadores ativos. Dados da empresa, sem detalhe de período. Fonte: E-Commerce Brasil (18/11/2026). Comente LIVE.'))
add(D,'1100',steps('shopee-video-mostrar-o-produto','Shopee','Vídeo de produto na ^Shopee^','Curto, claro e honesto',
 [('Mostre o produto inteiro','Comece com o produto completo, depois detalhes e tamanho.'),
  ('Use luz natural','Perto da janela, com fundo limpo. Evite filtros que mudem a cor.'),
  ('Confira as regras','Siga as regras atuais de conteúdo e de afiliados da plataforma.')],
 'Como gravar um vídeo de produto para a Shopee em 3 passos: produto inteiro, luz natural e conferir as regras. Salve.','Salve para ^gravar^','E me conta qual produto você vai mostrar.'))
add(D,'1400',ia('ia-legenda-para-video-de-produto','Legenda para vídeo de ^produto^ com IA','Curta e sem exagero',
 [('Conte o essencial','Informe o produto, para quem serve e um diferencial real.'),
  ('Use este prompt','Escreva 3 legendas curtas para este vídeo de produto, sem promessas exageradas, com uma chamada para ação.'),
  ('Revise os fatos','Confira se tudo o que a legenda diz está de acordo com o anúncio.')],
 'Como usar IA para criar legendas curtas para vídeos de produto, sem exagero, em 3 passos. Comente PROMPT.'))
add(D,'1900',enq('enquete-qual-formato-vende-mais-para-voce','Qual formato vende mais para você?',['Live','Vídeo curto','Story','Ainda estou testando'],'Enquete: qual formato vende mais para você? Comente a letra: A live, B vídeo curto, C story ou D ainda estou testando.'))
add(D,'2100',J('cartinha-para-o-eu-de-janeiro',[
 {'k':'Exercício de fim de ano','t':'Escreva uma ^carta^ para janeiro','b':'Leva 5 minutos'},
 {'l':'list','k':'Inclua','t':'Três *pontos*','items':[{'a':'1','t':'O que você aprendeu em 2026'},{'a':'2','t':'O que quer repetir'},{'a':'3','t':'O primeiro passo de janeiro'}]},
 {'k':'Por quê','t':'Você *vai agradecer*','b':'Em janeiro, o ritmo volta. Uma carta ajuda a retomar com clareza.'},
 end('Qual é o seu ^primeiro passo^?','Comente em uma frase.')],
 'Exercício de fim de ano: escreva uma carta para o seu eu de janeiro com o que aprendeu, o que quer repetir e o primeiro passo. Comente o seu primeiro passo.'))

# ===================== QUA 23/12 =====================
D='2026-12-23'
S='Fonte: YouPix (11/11/2026), Panorama de Consumo 2026'
add(D,'0800',news('novidade-mercado-livre-66-por-cento-confiam-em-creators','Novidade: Mercado Livre','^66%^ confiam em recomendação de creators','Pesquisa citada pela YouPix',
 [('66%','Dizem confiar em recomendações de creators e afiliados ao fechar uma compra'),('12 mi+','Participantes no programa de afiliados e creators do Mercado Livre na América Latina')],S,
 ('Pesquisa e *empresa*','A matéria não informa amostra nem período da pesquisa. O número de participantes é do Mercado Livre.'),
 ('Confiança *se constrói*','Mostre o produto de verdade, responda dúvidas e evite exagero.'),
 'Segundo o Panorama de Consumo 2026, 66% dizem confiar em recomendações de creators e afiliados ao fechar uma compra. A matéria não informa a amostra. Fonte: YouPix (11/11/2026). Comente QUERO.',cta='QUERO',et='Quer ^falar comigo^?'))
add(D,'1100',steps('live-ultima-live-antes-do-natal','Passo a passo de live','Última live antes do ^Natal^','Foco, clareza e carinho',
 [('Confirme prazos','Abra a live avisando até quando você consegue postar pedidos novos.'),
  ('Mostre o que ainda dá tempo','Foque em itens que você tem em estoque e consegue enviar.'),
  ('Agradeça e avise o retorno','Encerre agradecendo e diga quando volta a transmitir.')],
 'Como fazer a última live antes do Natal em 3 passos: confirmar prazos, mostrar o que dá tempo e agradecer. Salve.','Salve para ^usar^ hoje','E me conta se vai fazer live.'))
add(D,'1400',ia('ia-mensagem-de-ano-novo-para-clientes','Mensagem de ^Ano-Novo^ para clientes','Com IA e o seu jeito',
 [('Escolha o tom','Calmo, animado ou direto? Decida antes.'),
  ('Use este prompt','Escreva uma mensagem curta de Ano-Novo para clientes de uma loja online, em tom caloroso, sem prometer desconto.'),
  ('Personalize','Troque uma frase por algo seu e envie só por canais permitidos.')],
 'Como usar IA para escrever uma mensagem de Ano-Novo para clientes, em 3 passos. Comente PROMPT.'))
add(D,'1900',quiz('quiz-o-que-e-prova-social','Você sabe o que é ^prova social^?','Um motivo para confiar.',
 ['Um desconto grande','Avaliações de outros clientes','Um frete rápido','Um anúncio pago'],'É a *letra B*','Prova social é quando outras pessoas mostram que compraram e gostaram, com avaliações, depoimentos e fotos.',
 'Peça *com educação*','Peça avaliação depois da entrega. Nunca invente depoimento.',
 'Quiz: o que é prova social? Resposta: B, depoimentos e avaliações de outros clientes. Comente a letra que você marcou.'))
add(D,'2100',J('resumo-da-semana-17-a-23-12',[
 {'k':'Resumo da semana','t':'^17 a 23/12^ em poucos pontos','b':'O que vimos e o que fazer'},
 {'l':'list','k':'Novidades','t':'O que *saiu* nas notícias','items':[{'a':'Shopee','t':'11.11 de 2026 mais que dobrou a Black Friday de 2025, diz a empresa'},{'a':'TikTok Shop','t':'Estimativa de R$ 1,58 bi em junho; só cerca de 200 criadores passaram de R$ 1 mi'},{'a':'Creators','t':'Influenciadores lideraram a conversa da Black Friday de 2025'}]},
 {'k':'Para esta semana','t':'*Um passo* para cada novidade','b':'Mostre o produto em vídeo, cuide do prazo de envio, responda rápido e descanse no Natal.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: Shopee, TikTok Shop e creators. Salve e envie para um amigo que vende online.'))
for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
