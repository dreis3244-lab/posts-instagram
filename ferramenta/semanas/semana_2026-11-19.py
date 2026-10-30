import json,sys
# Semana 19/11 a 25/11/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
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



# ===================== QUI 19/11 =====================
S1='Fonte: Estado de Minas (26/10/2026), com dados da Momentum Works'
add('19','0800',J('novidade-tiktok-shop-110-mil-lojas',[
 {'k':'Novidade: TikTok Shop','t':'TikTok Shop soma ^110 mil lojas^ ativas no Brasil','b':'Estimativa da Momentum Works para o 1º semestre de 2026'},
 {'l':'list','k':'Os números','t':'Quem chegou a *R$ 1 milhão*','items':[{'a':'110,2 mil','t':'Lojas ativas no país'},{'a':'3,5 mil','t':'Lojas acima de R$ 1 milhão em GMV'},{'a':'~3%','t':'Parcela das lojas que passou dessa marca'}],'src':S1},
 {'k':'Como ler','t':'GMV *não é* lucro','b':'GMV é o total vendido, antes de descontar custo, taxas e frete. Por isso a margem importa mais que o faturamento.'},
 {'k':'Para você','t':'Muita gente *começando*, pouca no topo','b':'A concorrência existe. Constância e conta de margem ajudam a se manter na disputa. Não há garantia de resultado.'},
 end('Quer começar do ^jeito certo^?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'Segundo a Momentum Works, o TikTok Shop tinha cerca de 110,2 mil lojas ativas no Brasil no 1º semestre de 2026, e cerca de 3,5 mil passaram de R$ 1 milhão em GMV. Fonte: Estado de Minas (26/10/2026). Comente COMECAR.',av=True))
add('19','1100',steps('live-falar-de-frete-e-prazo','Passo a passo de live','Como falar de ^frete e prazo^ na live','Para tirar a dúvida mais comum antes que ela apareça',
 [('Diga o prazo de postagem','Informe em quanto tempo você envia o pedido. Só prometa o que consegue cumprir.'),
  ('Explique o frete','Mostre como o cliente vê o valor ou a condição de frete na própria plataforma.'),
  ('Repita no fim da live','Quem chegou depois ouve de novo. Fixe a informação no começo, no meio e no fim.')],
 'Frete e prazo estão entre as dúvidas que mais aparecem na live. Veja como falar disso em 3 passos e confira sempre as regras atuais da plataforma.','Salve para ^usar^ na próxima live','E conta qual dúvida de frete mais chega para você.'))
add('19','1400',steps('ia-titulo-de-produto-para-busca','IA para vendedor','Título de produto que ^aparece^ na busca, com IA','Para Shopee e TikTok Shop',
 [('Liste como o cliente procura','Escreva 5 palavras que o cliente digitaria para achar o seu produto. Pense no uso, não só no nome.'),
  ('Use este prompt','Crie 5 títulos de até 80 caracteres para este produto, com as palavras que o cliente procura, sem exagero e sem prometer o que ele não faz.'),
  ('Confira o limite da plataforma','Cada plataforma tem regras de tamanho e de termos proibidos. Revise antes de publicar.')],
 'Como usar IA para criar títulos de produto pensando na busca do cliente, em 3 passos. Revise as regras da plataforma. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('19','1900',quiz('quiz-lucro-de-10-vendas','Vendeu 10 unidades a R$ 40. Quanto ^sobrou^?','Exemplo: o custo é R$ 22 por unidade e taxas com frete somam R$ 8 por unidade.',
 ['R$ 100','R$ 180','R$ 220','R$ 400'],'Sobraram *R$ 100*','Por unidade: R$ 40 menos R$ 22 de custo e R$ 8 de taxas e frete dá R$ 10. Com 10 unidades, R$ 100.',
 'Faturar *não é* lucrar','Os R$ 400 que entraram são faturamento. O que fica depois dos custos é o que paga o seu trabalho.',
 'Quiz: vendeu 10 unidades a R$ 40, custo de R$ 22 e taxas com frete de R$ 8 por unidade. Quanto sobrou? Os números são um exemplo. Comente a letra.'))
add('19','2100',lst('o-que-fazer-hoje-a-noite-antes-da-black-friday','Para guardar','3 tarefas de ^30 minutos^ para esta noite',
 ['Confira o estoque dos 3 produtos de oferta','Anote o preço mínimo de cada um','Escreva o roteiro de abertura da live'],
 'Faltam poucos dias para a Black Friday (27/11). Três tarefas curtas para fazer esta noite.','Salve e ^faça hoje^','E me conta qual você já fez.',cb='Black Friday é em 27/11',tip=('Dica','Faça *pouco*, mas faça','Três tarefas feitas valem mais que dez planejadas.')))

# ===================== SEX 20/11 =====================
S2='Fonte: Inforchannel (05/10/2026), pesquisa Nuvemshop'
add('20','0800',J('novidade-nuvemshop-tiktok-shop-44-por-cento',[
 {'k':'Novidade: pesquisa','t':'Quem já comprou no TikTok Shop saltou de 17% para ^44%^','b':'Pesquisa da Nuvemshop com 1.025 consumidores'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'17% → 44%','t':'Já compraram no TikTok Shop'},{'a':'63%','t':'Entre jovens de 16 a 24 anos'},{'a':'2% → 6%','t':'Redes sociais como canal de compra'}],'src':S2},
 {'k':'Atenção','t':'Ainda existe *desconfiança*','b':'26% não se sentem seguros comprando direto pelas redes. Atendimento claro e resposta rápida ajudam a ganhar confiança.','src':S2},
 {'k':'Para você','t':'Confiança *vende*','b':'Mostre o produto de perto, explique prazo e troca e responda rápido. Isso vale em qualquer plataforma.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Pesquisa da Nuvemshop com 1.025 consumidores: a fatia de quem já comprou no TikTok Shop subiu de 17% para 44%. Fonte: Inforchannel (05/10/2026). Comente LIVE.',av=True))
add('20','1100',steps('live-contagem-regressiva-honesta','Passo a passo de live','Contagem regressiva ^honesta^ na live','Prazo real cria decisão sem pressão falsa',
 [('Use um prazo verdadeiro','Se a oferta acaba em 10 minutos ou quando o estoque termina, diga isso. Nunca invente prazo.'),
  ('Avise nos marcos','Fale quando faltarem 10, 5 e 1 minuto. Quem estava em dúvida decide.'),
  ('Cumpra o que disse','Quando acabar, acabou. Isso constrói confiança para as próximas lives.')],
 'Prazo real ajuda o cliente a decidir sem pressão falsa. Veja como fazer uma contagem regressiva honesta na live. Salve e teste.','Salve para ^testar^ na live','E conta como o público reagiu.'))
add('20','1400',steps('ia-mensagem-para-quem-sumiu','IA para vendedor','Mensagem para quem perguntou e ^sumiu^','Retomar a conversa sem ser chato',
 [('Resuma a conversa','Anote o que o cliente perguntou e o que você respondeu. Não inclua dados pessoais na IA.'),
  ('Use este prompt','Escreva uma mensagem curta, educada e sem pressão para retomar esta conversa com um cliente que não respondeu, oferecendo ajuda.'),
  ('Envie uma vez','Mande uma mensagem e respeite a decisão. Insistir demais afasta o cliente.')],
 'Como usar IA para escrever uma mensagem educada para quem perguntou e sumiu, em 3 passos. Não envie dados pessoais para a IA. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('20','1900',enq('enquete-categoria-da-black-friday','Qual categoria você vai ofertar na Black Friday?',['Moda','Beleza','Casa','Eletrônicos ou outra'],'Enquete: qual categoria você vai ofertar na Black Friday? Comente a letra: A moda, B beleza, C casa ou D eletrônicos ou outra.'))
add('20','2100',lst('tres-perguntas-ao-fornecedor','Para guardar','3 perguntas para fazer ao ^fornecedor^',
 ['Qual é o prazo para repor o estoque?','Existe quantidade mínima por pedido?','Como funciona a troca se vier com defeito?'],
 'Antes da Black Friday, confirme prazo de reposição, quantidade mínima e troca com o seu fornecedor. Salve a lista.','Salve para ^perguntar^ hoje','E me conta se já tem as respostas.',cb='Para não ficar sem estoque',tip=('Por quê','Estoque que *acaba* é venda perdida','Saber o prazo de reposição evita prometer o que você não entrega.')))

# ===================== SAB 21/11 =====================
S3='Fonte: Mundo do Marketing (28/10/2026), dados da Shopee'
add('21','0800',J('novidade-shopee-23-por-cento-acompanham-lives',[
 {'k':'Novidade: Shopee','t':'^23%^ dos usuários da Shopee pretendem ver lives e vídeos','b':'Pesquisa da própria plataforma para a temporada de ofertas'},
 {'l':'list','k':'Segundo a Shopee','t':'Os *números* da temporada','items':[{'a':'23%','t':'Pretendem acompanhar lives e vídeos'},{'a':'+4 p.p.','t':'Acima do índice do ano anterior'},{'a':'R$ 23 mi','t':'Em cupons para a Black Friday'}],'src':S3},
 {'k':'O que isso diz','t':'A live entra no *roteiro* de compra','b':'Quase 1 em cada 4 usuários pretende assistir. O dado é da plataforma, não de um estudo independente.','src':S3},
 {'k':'Para você','t':'Prepare uma live *simples*','b':'Combine horário, escolha 3 produtos, defina preço mínimo e avise o público antes de começar.'},
 end('Quer o ^roteiro^ de live?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Segundo pesquisa da Shopee, 23% dos usuários pretendem acompanhar lives e vídeos na temporada, 4 pontos percentuais acima do ano anterior. Dados da própria empresa. Fonte: Mundo do Marketing (28/10/2026). Comente LIVE.',av=True))
add('21','1100',steps('live-produto-gancho-e-produto-lucro','Passo a passo de live','Produto-gancho e produto de ^margem^','Dois papéis na mesma live',
 [('Escolha o produto-gancho','Um item simples e fácil de entender, que atrai gente para a live.'),
  ('Escolha o produto de margem','O item em que sobra mais depois de custo, taxas e frete. É ele que sustenta o resultado.'),
  ('Mostre os dois em ordem','Comece pelo gancho, mantenha o público e apresente o de margem quando a atenção estiver alta.')],
 'Produto-gancho atrai, produto de margem sustenta. Veja como combinar os dois na mesma live. Salve e teste.','Salve para ^montar^ a sua live','E conta qual é o seu produto-gancho.'))
add('21','1400',steps('ia-o-que-o-publico-mais-pergunta','IA para vendedor','Descubra o que o público ^mais pergunta^','Agrupe os comentários em temas',
 [('Copie os comentários','Junte perguntas de lives e posts. Retire nomes e dados pessoais antes de colar na IA.'),
  ('Use este prompt','Agrupe estas perguntas por tema, conte quantas aparecem em cada um e sugira uma resposta curta para os três temas mais comuns.'),
  ('Vire conteúdo','Transforme cada tema em um vídeo curto ou em um ponto da próxima live.')],
 'Como usar IA para descobrir quais perguntas seus clientes mais fazem e transformar isso em conteúdo, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('21','1900',J('mito-black-friday-e-so-para-quem-tem-muito-estoque',[
 {'k':'Mito','t':'"Black Friday é só para quem tem ^muito estoque^"','b':'Nem sempre. Dá para participar com poucos itens'},
 {'k':'Na prática','t':'Poucos itens, *bem escolhidos*','b':'Comece com 3 produtos, defina um preço mínimo e uma quantidade que você consegue entregar.'},
 {'k':'O risco real','t':'Prometer o que *não entrega*','b':'Vender além do estoque gera cancelamento e reclamação. É melhor ofertar menos e cumprir.'},
 end('Qual é o seu ^estoque^ hoje?','Comente quantos produtos você vai ofertar.')],
 'Mito: Black Friday é só para quem tem muito estoque. Poucos itens bem escolhidos e entregues no prazo podem ser melhores que muita oferta sem estoque. Quantos produtos você vai ofertar? Comente o número.'))
add('21','2100',steps('ensaie-a-live-uma-vez','Para o fim de semana','Ensaie a live ^uma vez^ antes','Dez minutos que evitam o susto',
 [('Fale em voz alta','Apresente seus 3 produtos como se estivesse ao vivo. Perceba onde trava.'),
  ('Marque o tempo','Cronometre abertura, demonstração e oferta. Ajuste o que ficou longo.'),
  ('Anote 3 respostas','Escreva as respostas para as 3 perguntas que você acha que vão chegar.')],
 'Ensaiar a live uma vez, em voz alta, ajuda a perder o nervosismo. Salve e teste neste fim de semana.','Salve para ^ensaiar^ hoje','E conta se ajudou.'))

# ===================== DOM 22/11 =====================
S4='Fonte: InfoMoney (27/10/2026), calendário da Shopee'
add('22','0800',J('novidade-shopee-calendario-esquenta-black-friday',[
 {'k':'Novidade: Shopee','t':'Shopee marca o ^Esquenta^ da Black Friday para 22/11','b':'Calendário divulgado pela plataforma'},
 {'l':'list','k':'Calendário','t':'As *datas* para marcar','items':[{'a':'22/11','t':'Esquenta Black Friday, com ofertas antecipadas'},{'a':'27/11','t':'Black Friday, com ofertas em várias categorias'},{'a':'30/11','t':'Cyber Monday, com cupons de até R$ 100 em eletrônicos'}],'src':S4},
 {'k':'Para você','t':'Use o Esquenta para *testar*','b':'Faça uma live curta, veja quais perguntas chegam e ajuste a oferta antes do dia principal.'},
 {'k':'Importante','t':'Confira as *regras* da campanha','b':'Condições, prazos e benefícios mudam por campanha. Veja sempre na Central do Vendedor.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'A Shopee divulgou o calendário da Black Friday: Esquenta em 22/11, Black Friday em 27/11 e Cyber Monday em 30/11. Confira as condições na Central do Vendedor. Fonte: InfoMoney (27/10/2026). Comente BLACK.',av=True))
add('22','1100',steps('live-ler-o-chat-em-voz-alta','Passo a passo de live','Leia o chat em ^voz alta^','Quem comenta quer ser visto',
 [('Leia o comentário inteiro','Fale o nome da pessoa e a pergunta. Quem assiste sem ver o chat também acompanha.'),
  ('Responda na hora','Se a resposta for curta, responda ali. Se for longa, diga que vai voltar nela.'),
  ('Transforme em demonstração','Quando a pergunta for sobre o produto, mostre a resposta em vez de só falar.')],
 'Ler os comentários em voz alta faz a live parecer conversa. Veja como fazer em 3 passos. Salve e teste na próxima.','Salve para ^usar^ na live','E conta qual pergunta mais apareceu.'))
add('22','1400',steps('ia-encerramento-da-live','IA para vendedor','Encerramento de live com ^IA^','Feche a live sem enrolar',
 [('Anote o que aconteceu','Liste os produtos mostrados, a oferta principal e o horário da próxima live.'),
  ('Use este prompt','Escreva um encerramento de 40 segundos para uma live de vendas, com recap das ofertas, agradecimento e convite para a próxima live.'),
  ('Fale do seu jeito','Troque o que soar formal e confira preço e prazo antes de repetir ao vivo.')],
 'Como usar IA para escrever o encerramento da sua live, em 3 passos. Revise preço e prazo antes de falar. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('22','1900',enq('enquete-como-controla-o-estoque','Como você controla o seu estoque?',['Caderno','Planilha','Sistema ou ERP','De cabeça'],'Enquete: como você controla o seu estoque? Comente a letra: A caderno, B planilha, C sistema ou ERP ou D de cabeça.'))
add('22','2100',J('resumo-da-semana-19-a-22-11',[
 {'k':'Resumo da semana','t':'^4 novidades^ para não perder','b':'Do que saiu de 19 a 22/11 aqui no perfil'},
 {'l':'list','k':'Salve este resumo','t':'O que *aconteceu*','items':[{'a':'TikTok Shop','t':'Cerca de 110 mil lojas ativas e 3,5 mil acima de R$ 1 mi em GMV'},{'a':'Nuvemshop','t':'Compra no TikTok Shop foi de 17% para 44%'},{'a':'Shopee','t':'23% pretendem acompanhar lives e vídeos'},{'a':'Shopee','t':'Esquenta Black Friday em 22/11'}],'src':'Fontes: Estado de Minas, Inforchannel, Mundo do Marketing, InfoMoney (out/2026)'},
 {'k':'Para esta semana','t':'*Um passo* para cada novidade','b':'Calcule a margem, mostre confiança ao cliente, prepare uma live simples e use o Esquenta para testar.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: 4 novidades de TikTok Shop, Nuvemshop e Shopee. Salve e envie para um amigo que vende online.'))

# ===================== SEG 23/11 =====================
S5='Fonte: Agência O Globo, via Tribuna do Sertão (28/10/2026)'
add('23','0800',J('novidade-mercado-livre-selo-black-friday',[
 {'k':'Novidade: Mercado Livre','t':'Mercado Livre anuncia ^R$ 100 mi^ em cupons e selo Black Friday','b':'Para a temporada de promoções, do 11.11 à Black Friday'},
 {'l':'list','k':'Segundo a empresa','t':'Os *números* da temporada','items':[{'a':'R$ 100 mi+','t':'Em cupons'},{'a':'37 mi','t':'De anúncios em promoção'},{'a':'24x','t':'Parcelas sem juros no cartão Mercado Pago, após 11/11'}],'src':S5},
 {'k':'Selo Black Friday','t':'Para o *menor preço* dos últimos 60 dias','b':'Segundo o Mercado Livre, esses itens têm descontos médios 30% maiores que os sem selo.','src':S5},
 {'k':'Para você','t':'Seu histórico de preço *conta*','b':'Subir o preço antes para "descontar" depois afasta o cliente. Mantenha o histórico honesto.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'O Mercado Livre anunciou mais de R$ 100 milhões em cupons e um selo Black Friday para produtos com o menor preço dos últimos 60 dias. Dados da empresa. Fonte: Agência O Globo, via Tribuna do Sertão (28/10/2026). Comente BLACK.',av=True))
add('23','1100',steps('live-mostrar-embalagem-e-envio','Passo a passo de live','Mostre a ^embalagem^ na live','Confiança também se mostra',
 [('Mostre como embala','Faça uma embalagem ao vivo, do produto à caixa fechada. Isso reduz a dúvida do cliente.'),
  ('Diga quando posta','Informe o prazo de postagem real, sem prometer o que não controla.'),
  ('Mostre o cuidado','Fale de proteção, lacre e conferência. É um detalhe que o cliente lembra.')],
 'Mostrar a embalagem ao vivo ajuda o cliente a confiar no envio. Veja como fazer em 3 passos. Salve e teste.','Salve para ^testar^ na live','E conta como o público reagiu.'))
add('23','1400',steps('ia-roteiro-de-demonstracao-em-30-segundos','IA para vendedor','Demonstração de produto em ^30 segundos^','Roteiro curto com IA',
 [('Liste 3 fatos','Para que serve, como usa e o que o cliente leva. Só fatos verdadeiros.'),
  ('Use este prompt','Escreva um roteiro de demonstração de 30 segundos para este produto, com gancho, uso e chamada para ação, em linguagem simples.'),
  ('Teste em voz alta','Leia, corte o que for longo e grave. Se travar, simplifique.')],
 'Como usar IA para criar um roteiro de demonstração de 30 segundos, em 3 passos. Confira os fatos do produto. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('23','1900',quiz('quiz-primeiro-passo-da-oferta','Qual é o ^primeiro passo^ de uma oferta?','Antes de gravar, postar ou divulgar.',
 ['Escolher o desconto','Calcular o preço mínimo','Gravar o vídeo','Postar nos stories'],'Calcular o *preço mínimo*','Com custo, taxas e frete na conta, você descobre até onde pode baixar o preço sem ter prejuízo.',
 'O preço mínimo *define* o desconto','Só depois de saber o piso vale escolher o desconto, o prazo e a divulgação.',
 'Quiz: qual é o primeiro passo de uma oferta, antes de gravar, postar ou divulgar? Comente a letra que você marcou.'))
add('23','2100',lst('custos-que-ficam-fora-da-conta','Para guardar','Custos que ficam ^fora da conta^',
 ['Embalagem: caixa, fita e proteção','Troca ou devolução','Brindes e cupons que você oferece','O seu tempo de atendimento'],
 'Quatro custos que muita gente esquece ao calcular o preço. Salve e revise a conta antes da Black Friday.','Salve para ^revisar^ a conta','E me conta qual custo você tinha esquecido.',cb='Antes de definir o preço',tip=('Dica','Conte *tudo*, mesmo o pequeno','Custos pequenos somados podem comer a margem de uma oferta.')))

# ===================== TER 24/11 =====================
S6='Fonte: Showmetech (27/10/2026)'
add('24','0800',J('novidade-instagram-videos-de-90-minutos',[
 {'k':'Novidade: Instagram','t':'Instagram testa vídeos de até ^90 minutos^','b':'Formato horizontal chamado Features'},
 {'k':'O que é','t':'Cortes dos Reels ligados a *episódios completos*','b':'A ideia é conectar os trechos publicados nos Reels a vídeos longos.','src':S6},
 {'k':'Quem está testando','t':'Podcasters, humoristas e criadores de *programas longos*','b':'Em teste com alguns criadores no Brasil e, desde 26/10, com um grupo selecionado nos EUA. Não há data de liberação geral.','src':S6},
 {'k':'Para você','t':'Vídeo curto segue como *porta de entrada*','b':'Acompanhe se o formato chega ao seu perfil. Enquanto isso, use Reels e carrosséis para ser descoberto.'},
 end('Quer aprender a ^criar conteúdo^ que vende?','Comente a palavra abaixo e eu te chamo no direct.','QUERO')],
 'O Instagram está testando vídeos horizontais de até 90 minutos, chamados Features, com alguns criadores. Não há data de liberação geral. Fonte: Showmetech (27/10/2026). Comente QUERO.',av=True))
add('24','1100',steps('live-chamar-para-a-proxima-live','Passo a passo de live','Como chamar o público para a ^próxima live^','Faça a audiência voltar',
 [('Anuncie dia e hora','Diga a data e o horário duas vezes: no meio e no fim da live.'),
  ('Dê um motivo','Conte o que vai mostrar na próxima, como um produto novo ou uma demonstração.'),
  ('Peça o lembrete','Convide o público a ativar o lembrete, se a plataforma oferecer essa opção.')],
 'Quem assiste hoje precisa saber quando você volta. Veja como chamar o público para a próxima live. Salve e teste.','Salve para ^usar^ hoje','E conta qual horário você escolheu.'))
add('24','1400',steps('ia-ficha-de-produto-para-a-live','IA para vendedor','Ficha de produto para a ^live^ com IA','Uma folha por produto, sem decorar',
 [('Junte os dados','Preço, medidas, material, prazo e o que acompanha. Use as informações reais do anúncio.'),
  ('Use este prompt','Crie uma ficha de uma página com 5 benefícios, 3 dúvidas comuns com respostas e 1 frase de fechamento para este produto.'),
  ('Imprima ou deixe ao lado','Consulte durante a live. Se algo não bater com o anúncio, corrija antes de falar.')],
 'Como usar IA para montar uma ficha de produto para consultar durante a live, em 3 passos. Confira os dados reais. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('24','1900',enq('enquete-o-que-falta-para-a-black-friday','O que ainda falta para a Black Friday?',['Conferir o estoque','Definir preço mínimo','Escrever o roteiro da live','Testar som e luz'],'Enquete: o que ainda falta para a Black Friday? Comente a letra: A conferir o estoque, B definir preço mínimo, C escrever o roteiro da live ou D testar som e luz.'))
add('24','2100',lst('3-frases-para-acalmar-um-cliente','Atendimento','3 frases para ^acalmar^ um cliente chateado',
 ['"Entendi o que aconteceu, obrigado por avisar."','"Vou verificar agora e te respondo ainda hoje."','"Vamos resolver dentro das regras da plataforma."'],
 'Três frases simples para responder um cliente chateado, sem prometer o que você não pode cumprir. Salve e use.','Salve para ter à ^mão^','E me conta qual você mais usaria.',cb='Atendimento com calma',tip=('Cuidado','Só prometa o que *pode cumprir*','Resposta honesta e rápida vale mais que promessa que não se cumpre.')))

# ===================== QUA 25/11 =====================
add('25','0800',J('novidade-nuvemshop-ia-nas-compras-46-por-cento',[
 {'k':'Novidade: pesquisa','t':'^46%^ dos brasileiros usam IA generativa nas compras','b':'Pesquisa da Nuvemshop com 1.025 consumidores'},
 {'l':'list','k':'Os números','t':'Para que usam a *IA*','items':[{'a':'46%','t':'Usam IA generativa no processo de compra'},{'a':'48%','t':'Usam para tirar dúvidas técnicas'},{'a':'48%','t':'Usam para comparar produtos'}],'src':S2},
 {'k':'Atenção','t':'*40%* preferem esperar por uma pessoa','b':'Só 24% aceitam atendimento imediato por IA. A IA ajuda, mas o toque humano ainda pesa.','src':S2},
 {'k':'Para você','t':'Use a IA nos *bastidores*','b':'Para roteiros, respostas-base e organização. Na conversa com o cliente, seja você.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Pesquisa da Nuvemshop com 1.025 consumidores: 46% usam IA generativa no processo de compra, mas 40% preferem esperar por atendimento humano. Fonte: Inforchannel (05/10/2026). Comente PROMPT.',tags=HIA,av=True))
add('25','1100',steps('live-cuidar-da-voz-e-da-energia','Passo a passo de live','Cuide da ^voz e da energia^ na live','Para aguentar lives mais longas',
 [('Deixe água por perto','Beba entre um produto e outro. Voz seca cansa quem fala e quem ouve.'),
  ('Planeje pausas curtas','Entre as ofertas, respire, leia o chat e retome o ritmo.'),
  ('Comece com energia média','Se começar no máximo, não aguenta até o fim. Suba aos poucos na oferta principal.')],
 'Cuidar da voz e da energia ajuda a aguentar lives mais longas. Veja 3 passos simples. Salve e teste.','Salve para ^lembrar^ na live','E conta qual passo você mais esquece.'))
add('25','1400',steps('ia-balanco-da-black-friday','IA para vendedor','Balanço da Black Friday com ^IA^','Organize os números depois da campanha',
 [('Junte os números','Pedidos, valor vendido, custo, taxas e frete de cada produto. Sem dados pessoais de clientes.'),
  ('Use este prompt','Com estes números, monte um resumo: o que vendeu mais, onde a margem foi melhor e três ajustes para a próxima campanha.'),
  ('Decida com calma','A IA organiza, mas a conta e a decisão são suas. Confira cada número.')],
 'Como usar IA para organizar o balanço da sua Black Friday e planejar os próximos passos, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add('25','1900',J('mito-so-o-menor-preco-vende',[
 {'k':'Mito','t':'"Só o ^menor preço^ vende"','b':'Uma pesquisa mostra outro fator na frente'},
 {'l':'chart','k':'Maior motivador de compra','t':'O que *pesa* na decisão','data':[{'l':'Frete grátis','v':44,'d':'44%','hl':True},{'l':'Preço mais baixo','v':40,'d':'40%'}],'src':S2},
 {'k':'Como ler','t':'Pesquisa *não é regra*','b':'É um recorte de 1.025 consumidores. O que pesa muda por produto e por público.','src':S2},
 end('O que pesa mais ^para você^?','Comente: frete grátis ou preço baixo?')],
 'Mito: só o menor preço vende. Em pesquisa da Nuvemshop, o frete grátis (44%) apareceu à frente do preço mais baixo (40%) como maior motivador de compra. Fonte: Inforchannel (05/10/2026). Frete grátis ou preço baixo? Comente.'))
add('25','2100',lst('faltam-2-dias-prioridades','Para guardar','Faltam 2 dias: o que ^priorizar^',
 ['Estoque e prazo de entrega dos produtos de oferta','Preço mínimo de cada produto','Roteiro e teste de som, luz e internet','Aviso ao público: dia, hora e o que vem na live'],
 'A Black Friday é em 27/11. Se faltar tempo, priorize estoque, preço mínimo, teste da live e aviso ao público. Salve a lista.','Salve e ^confira^ hoje','E me conta o que já está pronto.',cb='A Black Friday é em 27/11',tip=('Ordem','Primeiro o que *pode dar errado*','Estoque, preço e internet vêm antes de qualquer enfeite.')))

for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
