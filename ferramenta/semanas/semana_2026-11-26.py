import json,sys
# Semana 26/11 a 02/12/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
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



# ===================== QUI 26/11 =====================
D='2026-11-26'
S1='Fonte: Exame (28/10/2026)'
add(D,'0800',J('novidade-mercado-livre-24x-e-100-mi-em-cupons',[
 {'k':'Novidade: Mercado Livre','t':'Mercado Livre promete ^24x sem juros^ e mais de R$ 100 mi em cupons','b':'Condições da Black Friday 2026, segundo a empresa'},
 {'l':'list','k':'Os números','t':'O que a empresa *anunciou*','items':[{'a':'R$ 100 mi+','t':'Em cupons, acima do valor do ano passado'},{'a':'37 mi','t':'De produtos em promoção'},{'a':'24x','t':'Sem juros no Mercado Pago, para compras elegíveis'}],'src':S1},
 {'k':'O consumidor','t':'^71%^ pretendem comprar no 11.11 e na Black Friday','b':'Eram 23% em 2025, segundo o Panorama de Consumo 2026 do Mercado Livre, com 3.345 usuários ouvidos.','src':S1},
 {'k':'Para você','t':'O cliente chega *comparando*','b':'Com cupom e parcelamento por todo lado, deixe preço, prazo e frete claros no seu anúncio.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'O Mercado Livre promete mais de R$ 100 milhões em cupons e até 24x sem juros no Mercado Pago na Black Friday 2026, segundo a empresa. Fonte: Exame (28/10/2026). Comente BLACK.',av=True))
add(D,'1100',steps('live-black-friday-em-4-blocos','Passo a passo de live','Sua live de Black Friday em ^4 blocos^','Para não se perder quando o chat acelerar',
 [('Abertura curta','Cumprimente, diga o que vai ofertar e até que horas a live fica no ar.'),
  ('Uma oferta por vez','Mostre o produto, o preço e o que acompanha. Só passe para o próximo depois de responder as dúvidas.'),
  ('Repita o essencial','A cada 10 minutos, repita as ofertas e o prazo para quem acabou de chegar.')],
 'Estrutura simples para uma live de Black Friday: abertura, uma oferta por vez e repetição do essencial. Salve e use.','Salve para ^usar^ na live','E me conta como foi.'))
add(D,'1400',steps('ia-resposta-para-pedido-de-desconto','IA para vendedor','Responda quem pede ^desconto^ com educação','Sem perder a venda e sem queimar a margem',
 [('Defina o seu limite','Anote o menor preço que você aceita. Não envie dados pessoais do cliente para a IA.'),
  ('Use este prompt','Escreva 3 respostas curtas e educadas para um cliente que pede desconto. Explique o valor do produto e ofereça uma alternativa, como frete ou brinde, sem ir abaixo do meu preço mínimo.'),
  ('Escolha e personalize','Fique com a resposta que soa como você. Troque o que parecer genérico.')],
 'Como usar IA para responder pedidos de desconto com educação, sem queimar a margem, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',enq('enquete-quantos-produtos-na-oferta','Quantos produtos você vai ofertar?',['1 a 3','4 a 6','7 a 10','Mais de 10'],'Enquete: quantos produtos você vai ofertar? Comente a letra: A 1 a 3, B 4 a 6, C 7 a 10 ou D mais de 10.'))
add(D,'2100',lst('amanha-e-black-friday-5-conferencias','Para guardar','Amanhã é Black Friday: ^5 conferências^',
 ['Estoque dos produtos de oferta','Preço mínimo anotado','Internet, som e luz testados','Prazo de envio que você consegue cumprir','Aviso ao público: dia, hora e ofertas'],
 'A Black Friday é amanhã, 27/11. Cinco conferências rápidas para esta noite. Salve a lista.','Salve e ^confira^ agora','E me conta o que já está pronto.',cb='A Black Friday é em 27/11',tip=('Dica','Durma *cedo*','Voz e energia descansadas ajudam mais que mais uma oferta.')))

# ===================== SEX 27/11 =====================
D='2026-11-27'
S2='Fonte: E-Commerce Brasil (27/10/2026)'
add(D,'0800',J('novidade-shopee-86-por-cento-black-friday',[
 {'k':'Hoje é Black Friday','t':'Shopee: ^86%^ dos consumidores ouvidos pretendem comprar','b':'No 11.11, na Black Friday ou nas duas datas'},
 {'l':'list','k':'O que a Shopee diz','t':'Os números da *empresa*','items':[{'a':'86%','t':'Pretendem comprar no 11.11, na Black Friday ou nos dois'},{'a':'Até 2x','t':'As vendas de um dia comum em datas duplas'},{'a':'R$ 10','t':'Compra mínima para os cupons de frete grátis'}],'src':S2},
 {'k':'Atenção','t':'Os dados são da *própria Shopee*','b':'Pesquisa e projeções apresentadas pela empresa, sem verificação independente. Use como referência, não como promessa.','src':S2},
 {'k':'Para você','t':'Hoje, *responda rápido*','b':'Em dia de muita procura, resposta rápida e prazo claro ajudam o cliente a decidir.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Hoje é Black Friday. Segundo dados da própria Shopee, 86% dos consumidores ouvidos pretendem comprar no 11.11, na Black Friday ou nos dois. Fonte: E-Commerce Brasil (27/10/2026). Comente LIVE.',av=True))
add(D,'1100',steps('live-ajustes-durante-a-black-friday','Passo a passo de live','3 ajustes ao ^vivo^ na Black Friday','Para aproveitar o que o chat mostra',
 [('Olhe o estoque','Se um produto está acabando, avise na hora. Não venda o que você não tem.'),
  ('Leia as perguntas repetidas','Se três pessoas perguntam a mesma coisa, responda para todos e repita depois.'),
  ('Troque a ordem','Se um produto chama mais atenção, mostre ele de novo em vez de seguir o roteiro à risca.')],
 'Na Black Friday, ajuste a live conforme o chat: estoque, perguntas repetidas e ordem dos produtos. Salve e use hoje.','Salve para ^usar hoje^','E me conta o que você ajustou.'))
add(D,'1400',steps('ia-lista-de-reposicao-de-estoque','IA para vendedor','Lista de ^reposição^ de estoque com IA','Para saber o que repor depois da campanha',
 [('Junte os seus números','Liste os produtos, quantas unidades vendeu e quanto ainda tem. Use só dados seus, sem dados de clientes.'),
  ('Use este prompt','Com esta lista, organize os produtos do que mais vendeu para o que menos vendeu e sugira o que repor primeiro, explicando o raciocínio.'),
  ('Decida você','A IA organiza. Confira o prazo do fornecedor e o dinheiro disponível antes de comprar.')],
 'Como usar IA para organizar uma lista de reposição de estoque depois da campanha, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',quiz('quiz-quando-e-a-cyber-monday','Quando é a ^Cyber Monday^ de 2026?','A Black Friday é hoje, 27/11.',
 ['26/11','28/11','30/11','02/12'],'É dia *30/11*','A Cyber Monday cai na segunda-feira depois da Black Friday. Fonte: Central do Varejo (11/08/2026).',
 'Planeje *a segunda* também','Quem ainda tem estoque pode manter uma oferta para quem deixou a compra para depois.',
 'Quiz: quando é a Cyber Monday de 2026? Resposta: 30/11. Fonte: Central do Varejo (11/08/2026). Comente a letra.'))
add(D,'2100',lst('3-numeros-para-anotar-na-black-friday','Para guardar','3 números para ^anotar hoje^',
 ['Quantos pedidos entraram e em que horários','Quais produtos mais geraram perguntas','Quanto sobrou depois de custo, taxas e frete'],
 'Hoje é Black Friday. Anote três números para decidir melhor nas próximas semanas. Salve a lista.','Salve e ^anote^ hoje','E me conta qual você vai medir.',cb='Hoje é Black Friday',tip=('Por quê','O que não é *anotado* se perde','Amanhã você já não lembra dos detalhes. Os números orientam a próxima oferta.')))

# ===================== SAB 28/11 =====================
D='2026-11-28'
S3='Fonte: E-Commerce Brasil (21/09/2026), pesquisa LWSA'
add(D,'0800',J('novidade-lwsa-so-20-por-cento-na-sexta',[
 {'k':'Novidade: pesquisa','t':'A Black Friday passou, mas a ^compra continua^','b':'Segundo a LWSA, poucos concentram tudo na sexta'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'20%','t':'Planejam concentrar as compras só na Black Friday'},{'a':'54%','t':'Pretendem aproveitar ofertas ao longo do mês'},{'a':'55%','t':'Sempre buscam frete grátis, mesmo com entrega mais lenta'}],'src':S3},
 {'k':'Como ler','t':'É *intenção*, não resultado','b':'A pesquisa mostra o que os consumidores planejavam fazer. Não garante que sua venda vai acontecer.','src':S3},
 {'k':'Para você','t':'A vitrine *continua aberta*','b':'Quem ainda tem estoque pode manter ofertas, kits e lives nos próximos dias, sempre com margem.'},
 end('Quer uma ^live^ pós-Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Segundo a pesquisa da LWSA, 20% dos consumidores planejavam concentrar as compras só na Black Friday e 54% pretendiam aproveitar ofertas ao longo do mês. Fonte: E-Commerce Brasil (21/09/2026). Comente LIVE.',av=True))
add(D,'1100',steps('shopee-pedidos-e-chat-depois-da-black-friday','Shopee','Shopee: ^pedidos e chat^ depois da campanha','Organize antes de a fila crescer',
 [('Responda o chat','Comece pelas dúvidas de quem já comprou: prazo, rastreio e produto. Cliente atendido reclama menos.'),
  ('Confira os envios','Veja o que precisa ser postado e o prazo de postagem informado na plataforma.'),
  ('Anote o que repetiu','Se a mesma dúvida apareceu várias vezes, melhore a descrição do produto.')],
 'Depois da campanha, organize os pedidos e o chat na Shopee: responda, confira os envios e melhore a descrição. Confira sempre as regras atuais da plataforma.','Salve para ^organizar^ o dia','E me conta o que você vai ajustar.'))
add(D,'1400',steps('ia-explicar-o-produto-em-linguagem-simples','IA para vendedor','Explique seu produto em ^linguagem simples^','Para o cliente entender em segundos',
 [('Cole a ficha técnica','Copie as características do produto. Se houver termos técnicos, deixe-os aí.'),
  ('Use este prompt','Explique este produto em 3 frases simples, como se fosse para alguém que nunca viu, com para que serve e como usar. Sem exagero e sem prometer o que ele não faz.'),
  ('Confira com o produto','Veja se tudo bate com o produto real. Use a explicação na live e no anúncio.')],
 'Como usar IA para explicar seu produto em linguagem simples, em 3 passos. Confira os fatos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',J('mito-depois-da-black-friday-ninguem-compra',[
 {'k':'Mito','t':'"Depois da Black Friday, ^ninguém compra^"','b':'Os calendários das plataformas mostram o contrário'},
 {'k':'No calendário','t':'TikTok Shop segue com *campanha*','b':'A Black Friday vai de 12/11 a 03/12 e o Double 12 de 04/12 a 09/12. Confira as datas oficiais no app.','src':'Fonte: Brasil Inovador (20/10/2026)'},
 {'k':'Na prática','t':'O fluxo *muda*, não acaba','b':'Depois das grandes ofertas, muita gente compra presente de Natal. Ajuste produtos, kits e prazos.'},
 end('Qual é a sua ^próxima oferta^?','Comente o produto que você vai ofertar em dezembro.')],
 'Mito: depois da Black Friday ninguém compra. O calendário do TikTok Shop segue até 03/12, com Double 12 de 04/12 a 09/12. Fonte: Brasil Inovador (20/10/2026). Confira as datas no app. Qual produto você vai ofertar em dezembro? Comente.'))
add(D,'2100',lst('cyber-monday-o-que-priorizar','Para guardar','Cyber Monday (30/11): o que ^priorizar^',
 ['Escolha 1 ou 2 produtos, não todos','Confira o estoque que sobrou','Defina o preço mínimo de novo','Avise o público hoje: dia, hora e oferta'],
 'A Cyber Monday é em 30/11. Veja o que priorizar com o estoque que sobrou. Fonte da data: Central do Varejo (11/08/2026). Salve a lista.','Salve e ^prepare^ hoje','E me conta o que você vai ofertar.',cb='Segunda-feira, 30/11',tip=('Foco','Menos ofertas, *mais atenção*','Uma oferta bem explicada vale mais que dez mal apresentadas.')))

# ===================== DOM 29/11 =====================
D='2026-11-29'
S4='Fonte: Guairá News (01/11/2026), pesquisa CNDL/SPC Brasil (jul/2026)'
add(D,'0800',J('novidade-cndl-spc-54-por-cento-compram-nas-redes',[
 {'k':'Novidade: pesquisa','t':'Mais da metade já comprou pelas ^redes sociais^','b':'Pesquisa CNDL/SPC Brasil com a Offerwise'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'54%','t':'Compraram por redes sociais em 12 meses'},{'a':'49%','t':'Compraram direto na plataforma nos 6 meses antes da pesquisa'},{'a':'29%','t':'Citam poder falar com o vendedor como motivo'}],'src':S4},
 {'k':'Antes de comprar','t':'^64%^ pesquisam preços nas redes','b':'As redes sociais também são lugar de comparar, não só de comprar.','src':S4},
 {'k':'Para você','t':'Conversar *vende*','b':'Quem responde dúvidas na live e nos comentários dá ao cliente o que ele diz valorizar.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'Pesquisa CNDL/SPC Brasil: 54% dos consumidores digitais compraram por redes sociais em 12 meses e 29% valorizam poder falar com o vendedor. Fonte: Guairá News (01/11/2026). Comente COMECAR.',av=True))
add(D,'1100',steps('tiktok-video-que-nao-vendeu-o-que-ajustar','TikTok Shop','Vídeo que ^não vendeu^: o que ajustar','Antes de desistir do produto',
 [('Revise o começo','Os primeiros segundos mostram o problema ou o benefício? Se não, troque o gancho.'),
  ('Revise a oferta','Preço, frete e prazo estão claros? Dúvida demais afasta o cliente.'),
  ('Teste uma mudança','Mude só uma coisa por vez e compare. Assim você sabe o que funcionou.')],
 'Um vídeo que não vendeu não é o fim. Revise o começo, a oferta e teste uma mudança por vez. Salve e use.','Salve para ^testar^','E conta qual ajuste você vai fazer.'))
add(D,'1400',steps('ia-3-erros-ao-usar-ia-para-vender','IA para vendedor','3 erros ao usar ^IA^ para vender','E como evitar cada um',
 [('Copiar sem revisar','A IA pode errar medidas, prazos e características. Confira cada dado antes de publicar.'),
  ('Enviar dados pessoais','Não cole nomes, endereços ou conversas com dados de clientes na IA.'),
  ('Prometer o que não existe','Se o texto promete resultado que o produto não entrega, corte. A responsabilidade é sua.')],
 'Três erros ao usar IA para vender e como evitar: copiar sem revisar, enviar dados pessoais e prometer demais. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',enq('enquete-como-foi-sua-black-friday','Como foi a sua Black Friday?',['Vendi mais que esperava','Dentro do esperado','Abaixo do esperado','Não participei'],'Enquete: como foi a sua Black Friday? Comente a letra: A vendi mais que esperava, B dentro do esperado, C abaixo do esperado ou D não participei.'))
add(D,'2100',J('resumo-da-semana-26-a-29-11',[
 {'k':'Resumo da semana','t':'^4 novidades^ para não perder','b':'Do que saiu de 26 a 29/11 aqui no perfil'},
 {'l':'list','k':'Salve este resumo','t':'O que *aconteceu*','items':[{'a':'Mercado Livre','t':'Mais de R$ 100 mi em cupons e até 24x sem juros'},{'a':'Shopee','t':'86% dos ouvidos pretendem comprar no 11.11 ou na Black Friday'},{'a':'LWSA','t':'20% concentram a compra só na Black Friday'},{'a':'CNDL/SPC','t':'54% compraram por redes sociais em 12 meses'}],'src':'Fontes: Exame, E-Commerce Brasil, Guairá News (set a nov/2026)'},
 {'k':'Para esta semana','t':'*Um passo* para cada novidade','b':'Deixe preço e frete claros, responda rápido, mantenha uma oferta ativa e converse mais com quem compra.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: novidades de Mercado Livre, Shopee, LWSA e CNDL/SPC. Salve e envie para um amigo que vende online.'))

# ===================== SEG 30/11 =====================
D='2026-11-30'
S5='Fonte: Brain_ing (04/11/2026)'
add(D,'0800',J('novidade-instagram-facebook-series-no-brasil',[
 {'k':'Novidade: Instagram','t':'Instagram e Facebook lançam ^Séries^ no Brasil','b':'Recurso para organizar vídeos em episódios'},
 {'l':'list','k':'Como funciona','t':'O que a matéria *conta*','items':[{'a':'Aba','t':'Os episódios ficam reunidos em uma aba do perfil'},{'a':'Feed','t':'Também podem aparecer no feed e na aba Reels'},{'a':'4/11','t':'A liberação começou nesta data, aos poucos'}],'src':S5},
 {'k':'Atenção','t':'Nem *todo mundo* tem ainda','b':'A matéria não informa regras de elegibilidade. O recurso chega gradualmente às contas.','src':S5},
 {'k':'Para você','t':'Série serve para *mostrar processo*','b':'Exemplo: "7 dias de live". Quando chegar na sua conta, teste um formato curto.'},
 end('Quer ideias de ^série^?','Comente a palavra abaixo e eu te chamo no direct.','QUERO')],
 'Instagram e Facebook começaram a liberar o recurso Séries no Brasil, para organizar vídeos em episódios. A liberação é gradual. Fonte: Brain_ing (04/11/2026). Comente QUERO.'))
add(D,'1100',steps('live-cyber-monday-uma-oferta-por-vez','Passo a passo de live','Live de Cyber Monday: ^uma oferta^ por vez','Hoje é 30/11, dia de Cyber Monday',
 [('Escolha 1 ou 2 produtos','Foque no que ainda tem estoque e margem boa. Menos é mais.'),
  ('Conte o motivo da oferta','Diga por que o preço está assim e até quando vale. Seja verdadeiro.'),
  ('Feche com o próximo passo','Mostre como o cliente compra e quando será o próximo encontro.')],
 'Para a Cyber Monday (30/11), faça uma live com 1 ou 2 produtos, motivo claro da oferta e próximo passo. Salve e use.','Salve para ^usar hoje^','E conta como foi.'))
add(D,'1400',steps('ia-fala-de-ultimas-horas-da-oferta','IA para vendedor','Fala de ^últimas horas^ da oferta com IA','Urgência real, sem pressão falsa',
 [('Conte os fatos','Informe o produto, o preço, o estoque que sobrou e a hora real em que a oferta termina.'),
  ('Use este prompt','Escreva uma fala de 30 segundos para a live avisando que a oferta termina em poucas horas. Use só os fatos que informei, sem exagero e sem inventar escassez.'),
  ('Cumpra o que disse','Quando acabar, acabou. Isso constrói confiança para a próxima.')],
 'Como usar IA para escrever uma fala de últimas horas da oferta, com urgência real e sem pressão falsa. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',quiz('quiz-lucro-do-kit','Kit de 3 itens a R$ 90. Quanto ^sobrou^?','Exemplo: o custo dos 3 itens soma R$ 45, e taxas com frete somam R$ 25.',
 ['R$ 20','R$ 45','R$ 65','R$ 90'],'Sobraram *R$ 20*','R$ 90 menos R$ 45 de custo e R$ 25 de taxas e frete dá R$ 20 por kit.',
 'Kit também *exige conta*','Vender mais itens por pedido ajuda, mas só se a conta fechar. Calcule antes de ofertar.',
 'Quiz: kit de 3 itens a R$ 90, custo de R$ 45 e taxas com frete de R$ 25. Quanto sobrou? Os números são um exemplo. Comente a letra.'))
add(D,'2100',lst('dezembro-comeca-amanha-3-decisoes','Para guardar','Dezembro começa amanhã: ^3 decisões^',
 ['Qual produto você vai priorizar','Em quais dias e horários vai fazer live','Qual meta simples você quer bater'],
 'Dezembro começa amanhã. Três decisões para tomar hoje à noite. Salve a lista.','Salve e ^decida^ hoje','E me conta qual é a sua meta.',cb='Amanhã é 1º de dezembro',tip=('Dica','Meta *pequena* e clara','Uma meta que cabe na sua rotina é mais fácil de cumprir.')))

# ===================== TER 01/12 =====================
D='2026-12-01'
S6='Fonte: E-Commerce Brasil (26/10/2026)'
add(D,'0800',J('novidade-tiktok-shop-calendario-de-dezembro',[
 {'k':'Novidade: TikTok Shop','t':'O calendário de ^dezembro^ do TikTok Shop','b':'Categorias em destaque em cada data'},
 {'l':'list','k':'Datas','t':'Marque no *calendário*','items':[{'a':'18/11 a 3/12','t':'Descontos gerais em várias categorias'},{'a':'4 e 5/12','t':'Casa e preparação para o Natal'},{'a':'6 e 7/12','t':'Moda verão'},{'a':'8 e 9/12','t':'Eletrônicos, bebidas e itens de festa'}],'src':S6},
 {'k':'Importante','t':'Datas podem *mudar*','b':'Confira o calendário oficial no app antes de planejar. A matéria foi publicada em 26/10.','src':S6},
 {'k':'Para você','t':'Escolha a categoria *da data*','b':'Veja qual dia combina com o seu produto e planeje a live e os vídeos antes.'},
 end('Quer o ^plano^ de dezembro?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Calendário do TikTok Shop para dezembro: 4 e 5/12 casa e Natal, 6 e 7/12 moda verão, 8 e 9/12 eletrônicos, bebidas e itens de festa. Confira as datas no app. Fonte: E-Commerce Brasil (26/10/2026). Comente LIVE.',av=True))
add(D,'1100',steps('live-pergunta-que-voce-nao-sabe-responder','Passo a passo de live','E se perguntarem o que você ^não sabe^?','Honestidade vale mais que improviso',
 [('Admita com calma','Diga: "Não tenho certeza, vou confirmar". Isso passa confiança.'),
  ('Anote a pergunta','Escreva em um papel ou no bloco de notas para não esquecer.'),
  ('Volte com a resposta','Responda ainda na live ou nos comentários. Quem perguntou lembra.')],
 'Não sabe responder uma pergunta na live? Admita com calma, anote e volte com a resposta. Salve e use.','Salve para ^usar^ na live','E conta qual pergunta você já recebeu.'))
add(D,'1400',steps('ia-metas-de-dezembro-em-3-cenarios','IA para vendedor','Metas de dezembro em ^3 cenários^','Com os seus números, não com palpite',
 [('Junte seus números','Anote o que vendeu em novembro, o ticket médio e as horas por semana que você tem. Sem dados de clientes.'),
  ('Use este prompt','Com estes números, monte 3 metas para dezembro: cuidadosa, realista e ambiciosa. Explique o que preciso fazer em cada uma.'),
  ('Escolha a realista','Pegue a meta que cabe na sua rotina. A IA sugere cenários; não garante resultado.')],
 'Como usar IA para montar três cenários de meta para dezembro com os seus números, em 3 passos. Sem garantia de resultado. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',enq('enquete-meta-de-dezembro','Qual é a sua meta para dezembro?',['Vender mais','Fazer mais lives','Aprender a usar IA','Organizar estoque e conta'],'Enquete: qual é a sua meta para dezembro? Comente a letra: A vender mais, B fazer mais lives, C aprender a usar IA ou D organizar estoque e conta.'))
add(D,'2100',J('o-que-eu-testaria-em-dezembro',[
 {'k':'Opinião','t':'3 coisas que eu ^testaria^ em dezembro','b':'Para quem vende online'},
 {'l':'list','k':'Teste','t':'Simples e *possíveis*','items':[{'a':'1','t':'Um kit de presente com preço fechado'},{'a':'2','t':'Uma live curta em horário fixo'},{'a':'3','t':'Um vídeo respondendo a pergunta mais comum'}]},
 {'k':'Regra','t':'Teste *uma coisa* por vez','badge':'+20 MIL|ALUNOS','b':'Mude pouco, observe e repita o que funcionar. Resultados variam de pessoa para pessoa.'},
 end('Qual você vai ^testar^?','Comente o número.')],
 'Três coisas que eu testaria em dezembro: kit de presente, live curta em horário fixo e vídeo respondendo a pergunta mais comum. Comente o número que você vai testar.'))

# ===================== QUA 02/12 =====================
D='2026-12-02'
S7='Fonte: E-Commerce Brasil (21/09/2026), pesquisa LWSA'
add(D,'0800',J('novidade-lwsa-13-por-cento-comecam-na-ia',[
 {'k':'Novidade: pesquisa','t':'^13%^ já começam a pesquisa de compra em ferramentas de IA','b':'Dado da pesquisa da LWSA sobre a Black Friday'},
 {'l':'list','k':'Onde a busca começa','t':'O que a pesquisa *mostrou*','items':[{'a':'56%','t':'Usam marketplaces como ponto de partida'},{'a':'13%','t':'Usam ferramentas de IA como ponto de partida'}],'src':S7},
 {'k':'Como ler','t':'Ainda é uma *minoria*','b':'A maioria começa nos marketplaces, mas o hábito de perguntar à IA aparece. É um sinal, não uma regra.','src':S7},
 {'k':'Para você','t':'Informação *clara* ajuda em qualquer busca','b':'Título, descrição, medidas e uso do produto bem escritos ajudam o cliente a decidir, onde quer que ele comece.'},
 end('Quer ^prompts^ prontos de IA?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Na pesquisa da LWSA, 56% usam marketplaces como ponto de partida para pesquisar produtos e 13% usam ferramentas de IA. Fonte: E-Commerce Brasil (21/09/2026). Comente PROMPT.',HIA,av=True))
add(D,'1100',steps('tiktok-3-ideias-de-video-de-natal','TikTok Shop','3 ideias de ^vídeo de Natal^ para vender','Simples, sem equipamento caro',
 [('Presente por faixa de preço','Mostre 3 opções de presente em faixas de preço diferentes.'),
  ('Antes e depois da embalagem','Mostre o produto chegando e como fica embalado para presente.'),
  ('Responda a dúvida mais comum','Pegue a pergunta que mais chega e responda em um vídeo curto.')],
 'Três ideias de vídeo de Natal para vender no TikTok Shop: presente por faixa de preço, embalagem e resposta à dúvida mais comum. Salve e teste.','Salve para ^gravar^ hoje','E conta qual ideia você vai testar.'))
add(D,'1400',steps('ia-melhorar-o-seu-proprio-texto','IA para vendedor','Melhore seu próprio texto com ^IA^','Sem perder a sua voz',
 [('Escreva primeiro','Faça a sua versão do texto do anúncio ou da legenda, do seu jeito.'),
  ('Use este prompt','Melhore este texto: deixe mais claro e curto, corrija erros de português e mantenha o meu jeito de falar. Não acrescente promessas nem dados novos.'),
  ('Compare e escolha','Leia as duas versões e fique com o melhor de cada. A última palavra é sua.')],
 'Como usar IA para melhorar o seu próprio texto sem perder a sua voz, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',J('mito-preciso-fazer-live-todo-dia',[
 {'k':'Mito','t':'"Preciso fazer live ^todo dia^ para dar certo"','b':'Nem sempre. Constância não é o mesmo que excesso'},
 {'k':'Na prática','t':'Escolha uma *frequência* que cabe','b':'Duas ou três lives por semana, em horário fixo, podem ser mais sustentáveis que uma maratona que você abandona.'},
 {'k':'O que importa','t':'Melhorar a cada *live*','b':'Anote o que funcionou, ajuste uma coisa e repita. Os resultados variam de pessoa para pessoa.'},
 end('Quantas lives ^você faz^ por semana?','Comente o número.')],
 'Mito: preciso fazer live todo dia. Uma frequência que cabe na sua rotina, em horário fixo, pode ser mais sustentável. Quantas lives você faz por semana? Comente o número.'))
add(D,'2100',lst('novembro-em-5-aprendizados','Para guardar','Novembro em ^5 aprendizados^',
 ['Calcule a margem antes de ofertar','Estoque e prazo vêm antes de enfeite','Prazo de oferta real gera confiança','Responder rápido ajuda a vender','Anote os números, eles orientam o próximo mês'],
 'Cinco aprendizados de novembro para levar para dezembro. Salve a lista.','Salve e ^releia^ no domingo','E me conta o seu maior aprendizado.',cb='De 1 a 30 de novembro',tip=('Para dezembro','Leve *um* aprendizado','Escolha um e aplique já na primeira live do mês.')))

for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
