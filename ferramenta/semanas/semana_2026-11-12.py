import json,sys
# Semana 12/11 a 18/11/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
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
    j['d']='2026-11-'+day;j['slot']=slot;j['n']=slot;jobs.append(j)
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

# ===================== QUI 12/11 =====================
S1='Fonte: Brasil Inovador (20/10/2026)'
add('12','0800',J('novidade-tiktok-shop-calendario-black-friday-12-11',[
 {'k':'Novidade: TikTok Shop','t':'TikTok Shop marca a ^Black Friday^ de 12/11 a 03/12','b':'Calendário divulgado pela plataforma em 19/10'},
 {'l':'list','k':'Calendário','t':'As *três fases*','items':[{'a':'27/10 a 03/11','t':'Mega Oferta 11.11'},{'a':'12/11 a 03/12','t':'Black Friday'},{'a':'04/12 a 09/12','t':'Double 12 (12.12)'}],'src':S1},
 {'k':'O que está previsto','t':'Descontos de até *70%* e frete grátis','b':'Também há cupons de até R$ 200 para compradores recorrentes. Os benefícios dependem de cada lojista parceiro.','src':S1},
 {'k':'Para você','t':'Defina *o que ofertar* antes da fase','b':'Escolha 3 produtos, preço mínimo e prazo de envio. Confira o calendário oficial no seu app.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'O TikTok Shop divulgou o calendário de fim de ano: Mega Oferta 11.11 (27/10 a 03/11), Black Friday (12/11 a 03/12) e Double 12 (04/12 a 09/12). Confira as datas oficiais no seu app. Fonte: Brasil Inovador (20/10/2026). Comente BLACK.'))
add('12','1100',steps('live-ofertas-em-degraus','Passo a passo de live','Oferta em ^degraus^ durante a live','Para manter o público até o fim',
 [('Degrau 1: oferta de abertura','Algo simples nos primeiros minutos, para quem entrou cedo se sentir recompensado.'),
  ('Degrau 2: oferta principal','No meio da live, quando o público já entendeu o produto e a confiança cresceu.'),
  ('Degrau 3: oferta de encerramento','Última chance, com prazo claro. Sem pressão e sem prometer o que não existe.')],
 'Oferta em degraus: abertura, principal e encerramento. Uma forma simples de organizar a live e manter o público até o fim. Salve e teste.','Salve para ^testar^ na próxima live','E conta nos comentários qual degrau funcionou melhor.'))
add('12','1400',steps('ia-roteiro-de-oferta-relampago','IA para vendedor','Roteiro de oferta ^relâmpago^ com IA','Em poucos minutos',
 [('Conte os fatos','Produto, preço, prazo da oferta, estoque disponível e frete. Só o que é verdade.'),
  ('Use este prompt','Escreva um roteiro de 60 segundos para anunciar uma oferta relâmpago em live, com gancho, benefício, preço, prazo e chamada para comprar.'),
  ('Confira e fale do seu jeito','Revise preço e prazo, tire exageros e adapte para a sua voz. Quem responde pela oferta é você.')],
 'Como usar IA para escrever o roteiro de uma oferta relâmpago, em 3 passos. Revise sempre preço e prazo. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('12','1900',quiz('quiz-conta-do-desconto','Você vende por R$ 100 e dá ^20% de desconto^. Sobra lucro?','Exemplo: o produto custa R$ 60 para você. Taxas e frete somam R$ 25.',
 ['Lucro de R$ 15','Lucro de R$ 5','Zero a zero','Prejuízo de R$ 5'],'Prejuízo de *R$ 5*','R$ 100 menos 20% é R$ 80. Tirando o custo (R$ 60) e as taxas com frete (R$ 25), faltam R$ 5.',
 'Calcule *antes* de dar desconto','Defina o preço mínimo com custo, taxas e frete. Desconto bom é o que cabe na margem.',
 'Quiz: você vende por R$ 100, dá 20% de desconto, o custo é R$ 60 e taxas com frete somam R$ 25. Qual o resultado? Os números são um exemplo. Comente a letra.'))
add('12','2100',lst('pos-venda-depois-da-black-friday','Para guardar','Depois da venda vem o ^atendimento^',
 ['Responda dúvidas de entrega no mesmo dia','Explique a política de troca com clareza','Confira se o produto saiu certo e bem embalado','Peça avaliação só depois da entrega'],
 'Vender é só metade do trabalho. Atendimento rápido e troca clara reduzem reclamação e ajudam o cliente a voltar.','Salve para ^depois^ da Black Friday','E me conta qual item você já faz.',cb='O que fazer depois de vender',tip=('Por quê','Atendimento *constrói* confiança','Responder rápido e com clareza dá ao cliente um motivo para voltar a comprar.')))

# ===================== SEX 13/11 =====================
S2='Fonte: E-Commerce Brasil (21/10/2026)'
add('13','0800',J('novidade-abiacom-black-friday-16-6-bi',[
 {'k':'Novidade: Black Friday','t':'Abiacom projeta ^R$ 16,6 bi^ para a semana da Black Friday','b':'É uma projeção, não um resultado'},
 {'l':'list','k':'Projeção 2026','t':'Os *números* da Abiacom','items':[{'a':'16,6 bi','t':'Faturamento projetado, alta de 24,4%'},{'a':'21,66 mi','t':'Pedidos projetados (2025: 16,51 mi)'},{'a':'R$ 766,50','t':'Ticket médio projetado, queda de 5,2%'}],'src':S2},
 {'k':'Atenção','t':'Cada projeção usa um *período* diferente','b':'A da Neotrust (R$ 13,3 bi) cobre 26 a 29/11. Por isso, não dá para comparar direto.','src':S2},
 {'k':'Para você','t':'Mais pedidos, *ticket menor*','b':'Kits, combos e itens de impulso ajudam, desde que a margem pague taxas e frete.'},
 end('Quer a ^conta da margem^?','Comente a palavra abaixo e eu te chamo no direct.','MARGEM')],
 'A Abiacom projeta R$ 16,6 bilhões para a semana da Black Friday 2026 (27/11), com 21,66 milhões de pedidos e ticket médio de R$ 766,50. É uma projeção. Fonte: E-Commerce Brasil (21/10/2026). Comente MARGEM.'))
add('13','1100',steps('live-moderador-de-comentarios','Passo a passo de live','Chame um ^moderador^ para a sua live','Quem apresenta não precisa ler tudo',
 [('Quem apresenta foca no produto','Mostra, demonstra e responde as dúvidas principais olhando para a câmera.'),
  ('Quem modera cuida dos comentários','Separa as perguntas, avisa o que está repetido e destaca o que importa.'),
  ('Combinem sinais simples','Um aviso rápido para pergunta urgente e outro para pedir preço e prazo na tela.')],
 'Um moderador ajuda a live a fluir: um apresenta, outro cuida dos comentários. Salve e combine com alguém.','Salve para ^combinar^ com alguém','Pode ser um amigo, um familiar ou um parceiro.'))
add('13','1400',steps('ia-plano-de-conteudo-de-dezembro','IA para vendedor','Plano de conteúdo de ^dezembro^ com IA','Para chegar ao Natal com pauta pronta',
 [('Liste o que você vende','Categoria, 5 produtos, público e o que o cliente costuma perguntar.'),
  ('Use este prompt','Monte um calendário de conteúdo de 4 semanas para dezembro, com ideias de post, live e story para presente de Natal, sem promessas exageradas.'),
  ('Escolha o que cabe','Marque o que você consegue fazer de verdade. Pouca coisa feita vale mais que um plano enorme.')],
 'Como montar um plano de conteúdo de dezembro com ajuda da IA, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('13','1900',J('mito-vender-na-live-e-sorte',[
 {'k':'Mito','t':'"Vender em live é ^sorte^"','b':'Nem sempre. Tem preparação'},
 {'k':'Realidade','t':'A sorte ajuda, o *preparo sustenta*','b':'Produto bem escolhido, roteiro e horário fixo aumentam as chances.'},
 {'k':'O que você controla','t':'Preparação, *constância* e atendimento','b':'Clareza na oferta, rotina de lives e cuidado depois da venda.'},
 {'k':'O que não controla','t':'Algoritmo e *movimento do dia*','b':'Por isso a rotina importa mais que um único resultado.'},
 end('Qual é a sua ^dúvida^?','Comente abaixo e eu respondo.')],
 'Mito: vender em live é sorte. A sorte ajuda, mas preparo e constância sustentam. Qual é a sua dúvida? Comente abaixo.'))
add('13','2100',J('rotina-de-30-minutos-por-dia',[
 {'k':'Para refletir','t':'Rotina de ^30 minutos^ por dia','b':'Para quem tem pouco tempo'},
 {'l':'list','k':'Divida o tempo','t':'Três *blocos* de 10 minutos','items':[{'a':'10 min','t':'Responder comentários e mensagens'},{'a':'10 min','t':'Gravar ou planejar um vídeo'},{'a':'10 min','t':'Revisar o que funcionou ontem'}]},
 {'k':'Importante','t':'Pouco, mas *todo dia*','b':'Constância pequena vence esforço grande que acontece uma vez por mês.'},
 end('Você consegue ^começar hoje^?','Comente EU VOU se a resposta for sim.')],
 'Uma rotina de 30 minutos por dia: responder, gravar ou planejar e revisar. Comente EU VOU se você começa hoje.'))

# ===================== SAB 14/11 =====================
S3='Fonte: PHANT, republicando Exame (20/10/2026)'
add('14','0800',J('novidade-shopee-lives-e-afiliados-numeros',[
 {'k':'Novidade: Shopee','t':'Shopee diz reunir ^20 mil lives^ de vendas por dia','b':'Dados informados pela própria empresa'},
 {'l':'list','k':'Segundo a Shopee','t':'Os *números* da plataforma','items':[{'a':'20 mil','t':'Lives de vendas por dia'},{'a':'700 mil+','t':'Novos vídeos curtos por dia'},{'a':'10 mi+','t':'Afiliados registrados'}],'src':S3},
 {'k':'Afiliados','t':'Cerca de *1.800 pedidos por minuto*','b':'Gerados pela rede de afiliados, segundo a Shopee. O número de cadastrados não mostra quantos estão ativos.','src':S3},
 {'k':'Para você','t':'Live, vídeo e afiliado *se somam*','b':'Quem aprende a vender ao vivo e em vídeo tem mais de um caminho para ser descoberto.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'A Shopee diz reunir 20 mil lives de vendas por dia, mais de 700 mil novos vídeos curtos por dia e mais de 10 milhões de afiliados registrados. Dados da própria empresa. Fonte: PHANT, republicando Exame (20/10/2026). Comente LIVE.',av=True))
add('14','1100',steps('live-kit-presente-de-natal','Passo a passo de live','Monte um ^kit de presente^ para a live','Ideia para a época de Natal',
 [('Escolha produtos que combinam','Itens que o cliente usaria juntos ou daria de presente na mesma ocasião.'),
  ('Faça a conta antes','Some custo, taxas e frete. O preço do kit precisa fechar com margem.'),
  ('Mostre o kit completo ao vivo','Abra, mostre cada item e explique para quem serve esse presente.')],
 'Kit de presente é uma ideia simples para a live de fim de ano. Escolha itens que combinam e faça a conta da margem antes.','Salve para ^montar o seu^','E me conta qual kit você vai testar.'))
add('14','1400',steps('ia-politica-de-troca-clara','IA para vendedor','Política de troca ^clara^ com ajuda da IA','Menos dúvida e menos reclamação',
 [('Anote as regras reais','Prazo, estado do produto, quem paga o frete e como pedir. Use as regras da plataforma onde você vende.'),
  ('Use este prompt','Escreva um texto curto e educado explicando esta política de troca em linguagem simples, com passo a passo para o cliente.'),
  ('Revise com cuidado','Confira se o texto bate com as regras atuais da plataforma. Em dúvida, consulte a Central do Vendedor.')],
 'Como usar IA para escrever uma política de troca clara, sem inventar regra. Revise sempre. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('14','1900',enq('enquete-como-voce-paga-online','Como você mais paga compras online?',['Pix','Cartão à vista','Cartão parcelado','Boleto ou outro'],'Enquete: como você mais paga compras online? Comente a letra: A Pix, B cartão à vista, C cartão parcelado ou D boleto ou outro.'))
add('14','2100',lst('plano-do-fim-de-semana-black-friday','Para guardar','Fim de semana para ^organizar^ a Black Friday',
 ['Escolha 3 produtos de oferta','Calcule o preço mínimo de cada um','Grave 2 vídeos ou planeje 1 live','Confira estoque e prazo de envio'],
 'A Black Friday é em 27/11. Use o fim de semana para organizar produtos, preço mínimo, conteúdo e estoque.','Salve e ^faça hoje^','A Black Friday é em 27/11.',cb='Faltam poucos dias para 27/11',tip=('Prioridade','Faça primeiro o que *mais pesa*','Preço mínimo e estoque vêm antes. O conteúdo vem depois.')))

# ===================== DOM 15/11 =====================
S4='Fonte: Guairá News (21/10/2026), CNDL/SPC/Offerwise (mai-jun/2026)'
add('15','0800',J('novidade-cndl-spc-consumo-online-85-por-cento',[
 {'k':'Novidade: pesquisa','t':'^85%^ dos consumidores digitais compraram online em 12 meses','b':'Pesquisa CNDL/SPC Brasil com a Offerwise, nas capitais'},
 {'l':'list','k':'Os números','t':'Como o brasileiro *compra online*','items':[{'a':'66%','t':'Compraram no mês anterior (eram 54%)'},{'a':'5,1','t':'Pedidos por mês, em média (eram 4,6)'},{'a':'95%','t':'Voltaram a comprar no mesmo site ou app'}],'src':S4},
 {'l':'chart','k':'Escolha da loja','t':'O que pesa na *decisão*','data':[{'l':'Frete grátis','v':60,'d':'60%','hl':True},{'l':'Preço baixo','v':49,'d':'49%'},{'l':'Promoções','v':44,'d':'44%'}],'src':S4},
 {'k':'Para você','t':'Frete e *confiança* decidem','b':'Coloque o frete na conta do preço e cuide do atendimento: 27% tiveram problema na última compra.','src':S4},
 end('Quer o ^checklist^ de envio?','Comente a palavra abaixo e eu te chamo no direct.','ENVIO')],
 'Pesquisa CNDL/SPC Brasil com a Offerwise: 85% dos consumidores digitais das capitais compraram online em 12 meses; frete grátis (60%) é o principal critério na escolha da loja. Fonte: Guairá News (21/10/2026). Comente ENVIO.'))
add('15','1100',steps('shopee-estoque-e-prazo-de-postagem','Shopee','Estoque certo e prazo de ^postagem^','O básico que evita reclamação',
 [('Estoque atualizado todo dia','Vender o que não tem gera cancelamento e avaliação ruim.'),
  ('Cumpra o prazo de postagem','Poste dentro do prazo que você informou. Confira o prazo atual na Central do Vendedor.'),
  ('Embale para chegar inteiro','Produto danificado costuma virar reclamação. Proteja bem e confira antes de fechar.')],
 'Estoque atualizado, prazo de postagem cumprido e embalagem reforçada evitam boa parte das reclamações. Confira as regras atuais na Central do Vendedor.','Salve para ^revisar^ sua loja','E me conta o que você vai ajustar.'))
add('15','1400',steps('ia-boas-vindas-para-seguidor-novo','IA para vendedor','Mensagem de boas-vindas com ^IA^','Para quem chega no seu perfil',
 [('Defina o tom','Mais próximo ou mais profissional? Escolha como você fala no dia a dia.'),
  ('Use este prompt','Escreva uma mensagem curta de boas-vindas para novos seguidores de um perfil de vendas, convidando a conhecer os destaques e tirar dúvidas.'),
  ('Não copie e cole','Troque palavras, tire o que soar robótico e deixe a mensagem com a sua voz.')],
 'Como criar uma mensagem de boas-vindas para novos seguidores com ajuda da IA. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('15','1900',quiz('quiz-taxa-de-conversao','O que é ^taxa de conversão^?','Termo comum em vendas online',
 ['Quantos seguidores você tem','Quem comprou entre quem viu','Quanto você gasta em frete','Quantas lives você fez'],'Resposta: *letra B*','É a parte das pessoas que viram a oferta e compraram. Exemplo: 100 pessoas viram e 3 compraram, então a conversão é 3%.',
 'Meça por *oferta*','Compare lives, vídeos e horários para saber o que converte mais.',
 'Quiz: o que é taxa de conversão? Resposta: a parte das pessoas que viram a oferta e compraram. Comente a letra que você marcou.'))
add('15','2100',J('vender-e-resolver-um-problema',[
 {'k':'Para refletir','t':'Vender é resolver um ^problema^','b':'Em três passos'},
 {'k':'Primeiro','t':'Pergunte *primeiro*','b':'Antes de falar do produto, pergunte o que a pessoa quer resolver.'},
 {'k':'Depois','t':'Mostre a *solução*','b':'Mostre como o produto ajuda, sem exagerar e sem prometer o que não entrega.'},
 {'k':'Por fim','t':'Deixe a *decisão* com ela','b':'Cliente que decide com clareza compra com mais segurança.'},
 end('Qual problema o seu produto ^resolve^?','Escreva em uma frase nos comentários.')],
 'Vender é resolver um problema: descubra, mostre a solução e deixe a decisão com a pessoa. Qual problema o seu produto resolve? Conte nos comentários.'))

# ===================== SEG 16/11 =====================
S5='Fonte: Gazeta Web, blog Rapha Falcão (20/10/2026)'
add('16','0800',J('novidade-instagram-meta-one-assinatura',[
 {'k':'Novidade: Instagram','t':'Meta lança a assinatura ^Meta One^ para empresas e criadores','b':'Planos a partir de R$ 59 por mês, segundo a matéria'},
 {'l':'list','k':'Os planos','t':'*Quatro* níveis no Brasil','items':[{'a':'R$ 59','t':'Essencial: selo de verificação e proteção de identidade'},{'a':'R$ 199','t':'Avançado: links clicáveis em posts e Reels (4 por mês)'},{'a':'R$ 599','t':'Expert: até 8 links por mês e acesso para 8 pessoas'},{'a':'R$ 1.999','t':'Máximo: até 12 links por mês e acesso para 30 pessoas'}],'src':S5},
 {'k':'Atenção','t':'Valores e benefícios *podem variar*','b':'A matéria avisa que preços, benefícios e disponibilidade variam por conta, região e app.','src':S5},
 {'k':'Para você','t':'Só assine se *resolver* um problema','b':'Links clicáveis podem encurtar o caminho até a compra, mas não garantem vendas. Avalie o custo antes.'},
 end('Quer vender pelo ^Instagram^?','Comente a palavra abaixo e eu te chamo no direct.','QUERO')],
 'A Meta lançou a assinatura Meta One para empresas e criadores, com planos de R$ 59 a R$ 1.999 por mês, segundo matéria. Valores e disponibilidade podem variar. Fonte: Gazeta Web (20/10/2026). Comente QUERO.'))
add('16','1100',steps('live-quadro-fixo','Passo a passo de live','Crie um ^quadro fixo^ na sua live','Para o público saber o que esperar',
 [('Escolha um momento repetido','Por exemplo, "Dúvida da hora" ou "Produto surpresa" sempre no mesmo ponto da live.'),
  ('Dê um nome simples','Nome curto que o público repete nos comentários.'),
  ('Mantenha por várias lives','O hábito se forma com repetição. Observe se o público espera por aquele momento.')],
 'Um quadro fixo dá ritmo à live e cria hábito no público. Escolha um nome e repita. Salve e teste.','Salve para ^criar o seu^','E conta qual nome você vai usar.'))
add('16','1400',steps('ia-beneficio-em-frase-curta','IA para vendedor','Transforme característica em ^benefício^','Com ajuda da IA',
 [('Liste as características','Material, tamanho, voltagem, quantidade. O que o produto tem.'),
  ('Use este prompt','Transforme estas características em 5 benefícios curtos para o cliente, em linguagem simples e sem exagero.'),
  ('Escolha o mais forte','Use um benefício por vídeo ou por trecho da live. Uma mensagem por vez é mais fácil de lembrar.')],
 'Como transformar características de produto em benefícios com ajuda da IA, em 3 passos. Confira sempre os fatos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('16','1900',enq('enquete-maior-medo-de-vender-online','Qual é o seu maior medo ao vender online?',['Não vender nada','Aparecer na câmera','Errar na plataforma','Perder dinheiro'],'Enquete: qual é o seu maior medo ao vender online? Comente a letra: A não vender nada, B aparecer na câmera, C errar na plataforma ou D perder dinheiro.'))
add('16','2100',J('motivacao-acaba-rotina-fica',[
 {'k':'Para refletir','t':'^Motivação^ acaba. A rotina fica.','b':'Para começar a semana'},
 {'k':'Motivação','t':'Ela *oscila*','b':'Tem dia em que você acorda animado e tem dia em que não.'},
 {'k':'Rotina','t':'Ela *sustenta*','b':'Um horário fixo e uma tarefa pequena fazem você continuar mesmo sem vontade.'},
 {'k':'Comece pequeno','t':'Dez minutos hoje *valem mais*','b':'Mais que um plano perfeito que nunca sai do papel.'},
 end('Qual é a sua ^tarefa mínima^ de hoje?','Comente abaixo.')],
 'Motivação acaba, rotina fica. Qual é a sua tarefa mínima de hoje? Comente abaixo.'))

# ===================== TER 17/11 =====================
S6='Fonte: Portal G (20/10/2026)'
add('17','0800',J('novidade-shopee-sorteio-black-friday-30-mil',[
 {'k':'Novidade: Shopee','t':'Shopee sorteia ^R$ 30 mil^ em créditos na campanha da Black Friday','b':'Campanha para compradores, de 26/10 a 29/11'},
 {'l':'list','k':'A campanha','t':'Os *detalhes* do sorteio','items':[{'a':'3','t':'Ganhadores, com R$ 30 mil em créditos ShopeePay cada'},{'a':'26/10 a 29/11','t':'Período da campanha, até 23h59'},{'a':'R$ 100+','t':'Compra elegível dá 10 números da sorte'}],'src':S6},
 {'k':'Como participar','t':'Moedas Shopee e *compras elegíveis*','b':'A cada 2 moedas, 1 número da sorte. Pedidos a partir de R$ 100 em uma única compra dão 10 números.','src':S6},
 {'k':'Para você','t':'Campanha chama atenção. Prepare *preço e prazo*','b':'Se o movimento aumentar, quem tem anúncio claro, frete calculado e estoque certo aproveita melhor.'},
 end('Quer vender na ^Shopee^?','Comente a palavra abaixo e eu te chamo no direct.','SHOPEE')],
 'A Shopee lançou a campanha 1 Ano de Shopee Grátis Black Friday, que sorteia R$ 30 mil em créditos ShopeePay para 3 ganhadores, de 26/10 a 29/11. Fonte: Portal G (20/10/2026). Comente SHOPEE.'))
add('17','1100',steps('tiktok-responder-comentario-com-video','TikTok Shop','Responda comentário com ^vídeo^','Transforme dúvida em conteúdo',
 [('Pegue a pergunta que mais aparece','Se uma pessoa perguntou, outras provavelmente têm a mesma dúvida.'),
  ('Grave mostrando o produto','Mostre na prática, em 20 a 30 segundos, direto ao ponto.'),
  ('Chame para o próximo passo','Diga onde clicar ou o que fazer a seguir, sem pressão.')],
 'Responder dúvidas com vídeo é uma forma simples de criar conteúdo e tirar objeção. Salve e teste hoje.','Salve para ^usar hoje^','E conta qual dúvida você vai responder primeiro.'))
add('17','1400',steps('ia-ideias-de-live-tematica-de-natal','IA para vendedor','5 ideias de live de ^Natal^ com IA','Para sair do óbvio',
 [('Conte o seu nicho','Produto, público e faixa de preço dos presentes que você vende.'),
  ('Use este prompt','Sugira 5 ideias de lives temáticas de Natal para este nicho, com título, roteiro em 3 partes e uma chamada para comprar.'),
  ('Escolha uma e teste','Faça a live, observe os comentários e ajuste a próxima.')],
 'Como pedir à IA ideias de live temática de Natal, em 3 passos. Adapte sempre ao seu produto. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('17','1900',J('mito-postar-mais-sempre-ajuda',[
 {'k':'Mito','t':'"Postar mais sempre ^ajuda^"','b':'Qualidade e constância pesam mais'},
 {'k':'Realidade','t':'Quantidade sem cuidado *cansa*','b':'Se o conteúdo não resolve nada, postar mais só aumenta o cansaço.'},
 {'k':'Constância','t':'É diferente de *exagero*','b':'Defina uma frequência que você consegue manter por meses.'},
 {'k':'O que fazer','t':'Repita o que *funciona*','b':'Observe salvamentos, comentários e compartilhamentos e refaça os formatos que se destacam.'},
 end('Quantos posts você ^consegue manter^?','Comente o número.')],
 'Mito: postar mais sempre ajuda. Na prática, constância e qualidade pesam mais. Quantos posts por semana você consegue manter? Comente o número.'))
add('17','2100',J('o-cliente-diz-o-que-quer-comprar',[
 {'k':'Para refletir','t':'O cliente diz o que ^quer comprar^','b':'Se você ouvir'},
 {'k':'Leia com atenção','t':'Os *comentários* contam','b':'Dúvidas e pedidos mostram o que as pessoas procuram.'},
 {'k':'Anote','t':'As perguntas *repetidas*','b':'Elas viram vídeo, live e até ideia de produto.'},
 {'k':'Responda','t':'E volte ao *assunto*','b':'Quem sente que foi ouvido costuma confiar mais.'},
 end('Qual pergunta ^mais aparece^ para você?','Comente abaixo.')],
 'O cliente diz o que quer comprar nos comentários. Qual pergunta mais aparece para você? Comente abaixo.'))

# ===================== QUA 18/11 =====================
S7='Fonte: Propmark (21/10/2026)'
add('18','0800',J('novidade-adcos-live-12-horas-tiktok-shop',[
 {'k':'Novidade: TikTok Shop','t':'Adcos faz live de até ^12 horas^ na estreia no TikTok Shop','b':'Campanha "Beauty Glow", de 20 a 24/10'},
 {'l':'list','k':'A estreia','t':'O que a marca *fez*','items':[{'a':'12 h','t':'Live de até 12 horas, em 23/10'},{'a':'20 a 24/10','t':'Campanha Beauty Glow'},{'a':'10%','t':'Comissão para criadores do programa Dermo Squad'}],'src':S7},
 {'k':'O que dá para aprender','t':'Live, loja e *criadores* juntos','b':'A estreia combinou live, programação de abertura da loja e programa de criadores com comissão.','src':S7},
 {'k':'Para você','t':'Você *não precisa* de 12 horas','b':'Comece com 30 minutos, um roteiro simples e um horário fixo. Aumente com o tempo.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'A Adcos estreou no TikTok Shop com a campanha Beauty Glow (20 a 24/10), live de até 12 horas e programa de criadores com 10% de comissão. Fonte: Propmark (21/10/2026). Comente LIVE.',av=True))
add('18','1100',steps('live-plano-b-se-a-internet-cair','Passo a passo de live','Plano B se a ^internet cair^ na live','Para não passar aperto',
 [('Tenha um segundo caminho','Dados móveis ou outro Wi-Fi ajudam a voltar rápido.'),
  ('Avise o público','Quando voltar, diga o que aconteceu e retome do ponto em que parou.'),
  ('Teste antes de começar','Cinco minutos de teste de som, luz e internet evitam a maioria dos sustos.')],
 'Plano B para a live: segundo caminho de internet, aviso ao público e teste antes de começar. Salve para não passar aperto.','Salve para ^não passar aperto^','E conta qual é o seu plano B.'))
add('18','1400',steps('ia-agenda-de-posts-para-black-friday','IA para vendedor','Agenda de posts da ^Black Friday^ com IA','Para os dias até 27/11',
 [('Defina as ofertas','Escolha 3 produtos, preço mínimo e prazo. A IA organiza, a decisão é sua.'),
  ('Use este prompt','Crie uma agenda de posts e lives para os 9 dias antes da Black Friday, com tema diário, chamada e horário sugerido.'),
  ('Ajuste ao seu ritmo','Corte o que não cabe na sua rotina e deixe só o que você consegue cumprir.')],
 'Como usar IA para montar a agenda de posts até a Black Friday (27/11), em 3 passos. Comente BLACK.','Quer o ^plano^ completo?','Comente a palavra abaixo e eu te chamo no direct.','BLACK',HIA))
add('18','1900',enq('enquete-vai-fazer-live-na-black-friday','Você vai fazer live na Black Friday?',['Sim, já planejei','Sim, mas falta planejar','Ainda estou pensando','Vou só postar vídeo'],'Enquete: você vai fazer live na Black Friday? Comente a letra: A sim, já planejei, B sim, mas falta planejar, C ainda estou pensando ou D vou só postar vídeo.'))
add('18','2100',J('resumo-da-semana-12-a-18-11',[
 {'k':'Resumo da semana','t':'^7 novidades^ para não perder','b':'Do que saiu de 12 a 18/11 aqui no perfil'},
 {'l':'list','k':'Salve este resumo','t':'Parte *1*','items':[{'a':'TikTok','t':'Black Friday marcada de 12/11 a 03/12'},{'a':'Abiacom','t':'Projeta R$ 16,6 bi na semana da Black Friday'},{'a':'Shopee','t':'Diz reunir 20 mil lives de vendas por dia'},{'a':'CNDL/SPC','t':'85% compraram online em 12 meses'}],'src':'Fontes: Brasil Inovador, E-Commerce Brasil, PHANT (Exame), Guairá News'},
 {'l':'list','k':'Salve este resumo','t':'Parte *2*','items':[{'a':'Meta One','t':'Assinatura para empresas e criadores'},{'a':'Shopee','t':'Sorteio de R$ 30 mil em créditos'},{'a':'Adcos','t':'Live de até 12 horas no TikTok Shop'}],'src':'Fontes: Gazeta Web, Portal G, Propmark (out/2026)'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: 7 novidades de TikTok Shop, Shopee, Instagram e Black Friday. Salve e envie para um amigo que vende online.'))

for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
