import json,sys
# Semana 03/12 a 09/12/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
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

# ===================== QUI 03/12 =====================
D='2026-12-03'
S1='Fonte: Paraíba Total (10/11/2026)'
add(D,'0800',J('novidade-whatsapp-business-cobranca-por-resposta',[
 {'k':'Novidade: WhatsApp Business','t':'WhatsApp Business passa a ^cobrar^ respostas na API','b':'Mudança para empresas que usam a plataforma oficial'},
 {'l':'list','k':'O que a matéria conta','t':'Os pontos *principais*','items':[{'a':'1º/10','t':'Respostas de serviço, dentro da janela de 24 horas, passam a ser cobradas uma a uma'},{'a':'R$ 0,035','t':'Tarifa da plataforma no Brasil: US$ 0,0068 por mensagem'},{'a':'Sem mudança','t':'WhatsApp comum e app WhatsApp Business gratuito'}],'src':S1},
 {'k':'Atenção','t':'Vale para quem usa a *API oficial*','b':'Em geral, empresas com CRM, automação ou central de atendimento. Confira como o seu caso é tratado.','src':S1},
 {'k':'Para você','t':'Resposta *clara* economiza conversa','b':'Se você paga por mensagem, uma ficha de produto bem escrita reduz as idas e vindas com o cliente.'},
 end('Quer ^prompts^ para montar o seu FAQ?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'O WhatsApp Business passou a cobrar, desde 1º/10/2026, cada resposta de serviço enviada pela plataforma oficial (API) na janela de 24 horas. O app gratuito e o WhatsApp comum não são afetados. Fonte: Paraíba Total (10/11/2026). Comente PROMPT.',HIA,av=True))
add(D,'1100',steps('live-enquadramento-do-celular','Passo a passo de live','Enquadramento do celular em ^3 ajustes^','Para a live parecer mais profissional',
 [('Celular em pé','Deixe o aparelho na vertical, na altura dos olhos. Assim o rosto e o produto aparecem bem.'),
  ('Luz de frente','Fique de frente para a janela ou para uma luz. Evite luz forte atrás de você.'),
  ('Espaço para o produto','Enquadre você e o produto juntos, sem cortar as mãos quando mostrar a peça.')],
 'Três ajustes de enquadramento para a live: celular em pé, luz de frente e espaço para o produto. Salve e teste hoje.','Salve para ^testar^ hoje','E me conta o que você ajustou.'))
add(D,'1400',steps('ia-mensagem-de-natal-para-clientes','IA para vendedor','Mensagem de ^Natal^ para clientes','Curta, sincera e sem exagero',
 [('Escolha quem recebe','Fale com clientes que já compraram ou que pediram contato. Use só contatos que aceitam receber mensagens.'),
  ('Use este prompt','Escreva 3 mensagens curtas de fim de ano para clientes de uma loja de [seu produto]. Agradeça pela compra, sem prometer desconto nem prazo que eu não confirmei.'),
  ('Personalize e revise','Troque o que soar genérico e use o nome da pessoa. Confira tudo antes de enviar.')],
 'Como usar IA para escrever mensagens de Natal para clientes, sem exagero, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',enq('enquete-onde-atende-clientes','Onde você atende seus clientes?',['Chat da plataforma','WhatsApp','Direct do Instagram','Comentários e lives'],'Enquete: onde você atende seus clientes? Comente a letra: A chat da plataforma, B WhatsApp, C direct do Instagram ou D comentários e lives.'))
add(D,'2100',lst('o-que-parar-de-fazer-em-dezembro','Para refletir','3 coisas para ^parar de fazer^ em dezembro',
 ['Copiar oferta dos outros sem fazer a conta','Responder no impulso, sem checar estoque e prazo','Deixar o descanso para depois do fim do ano'],
 'Três coisas para parar de fazer em dezembro. Salve a lista e escolha uma para cortar hoje.','Salve e ^corte uma^ hoje','E me conta qual você vai parar.',cb='Para fechar o ano melhor',tip=('Por quê','Parar também é *avançar*','Cortar o que atrapalha libera tempo para o que funciona.')))

# ===================== SEX 04/12 =====================
D='2026-12-04'
S2='Fonte: Estado de Minas (11/11/2026), pesquisa CNDL/SPC Brasil com Offerwise (out/2026)'
add(D,'0800',J('novidade-cndl-spc-65-por-cento-temem-fraude',[
 {'k':'Novidade: pesquisa','t':'^65%^ dizem temer fraudes nas compras online','b':'Pesquisa CNDL/SPC Brasil com a Offerwise sobre a Black Friday'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'65%','t':'Temem fraudes, como roubo de dados bancários e clonagem de cartão'},{'a':'81%','t':'Planejam comprar pela internet'},{'a':'41%','t':'Citam menor preço e frete grátis, cada um, como fator'}],'src':S2},
 {'k':'Como ler','t':'É uma pesquisa de *intenção*','b':'Foi feita de 7 a 19 de outubro, com 1.133 consumidores das 27 capitais. Mostra o que as pessoas disseram, não o que vão fazer.','src':S2},
 {'k':'Para você','t':'Confiança também *vende*','b':'Mostre quem você é, a embalagem e o prazo. Oriente o cliente a pagar só pelos canais oficiais da plataforma.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Pesquisa CNDL/SPC Brasil com a Offerwise: 65% dos consumidores dizem temer fraudes nas compras online. Fonte: Estado de Minas (11/11/2026). Comente LIVE.',av=True))
add(D,'1100',steps('tiktok-video-de-unboxing','TikTok Shop','Vídeo de ^unboxing^ do produto','Mostrar o produto chegando',
 [('Abra com calma','Mostre a caixa fechada, abra devagar e deixe o produto aparecer sem pressa.'),
  ('Diga o que tem dentro','Fale como é o acabamento e para que serve, sem exagerar nas promessas.'),
  ('Termine com uma pergunta','Pergunte o que o público quer ver a seguir e responda nos comentários.')],
 'Como fazer um vídeo de unboxing do produto em 3 passos: abrir com calma, dizer o que tem dentro e terminar com uma pergunta. Salve e teste.','Salve para ^gravar^ hoje','E conta qual produto você vai abrir.'))
add(D,'1400',steps('ia-resposta-para-cliente-desconfiado','IA para vendedor','Responda o cliente ^desconfiado^','Com calma e sem inventar regra',
 [('Entenda a dúvida','Leia a mensagem e anote o que preocupa: prazo, produto, pagamento ou envio.'),
  ('Use este prompt','Escreva uma resposta curta e educada para um cliente com receio de comprar. Use só as informações que estão abaixo e convide a pessoa a seguir os canais oficiais da plataforma.'),
  ('Confira e envie','Veja se tudo é verdade. Nunca peça dados de pagamento por conversa.')],
 'Como usar IA para responder um cliente desconfiado com calma, sem inventar regra, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',quiz('quiz-o-que-e-chamada-para-acao','O que é uma ^chamada para ação^?','Aquela frase no fim do post ou da live.',
 ['Um desconto no preço','Um pedido do próximo passo','O nome do produto','A foto de capa'],'É a *letra B*','É quando você diz ao público o que fazer a seguir: comentar, salvar, clicar ou comprar.',
 'Peça *um* passo','Uma chamada clara funciona melhor do que várias ao mesmo tempo.',
 'Quiz: o que é uma chamada para ação? Resposta: B, um pedido do próximo passo, como comentar, salvar ou comprar. Comente a letra que você marcou.'))
add(D,'2100',J('confianca-se-constroi-devagar',[
 {'k':'Para refletir','t':'^Confiança^ se constrói devagar','b':'E se perde rápido'},
 {'k':'Como construir','t':'Cumpra o que *você diz*','b':'Prazo informado é prazo cumprido. Produto igual ao da live. Resposta honesta, mesmo quando é "ainda não sei".'},
 {'k':'Por que importa','t':'Quem confia *volta*','b':'Um cliente bem atendido tende a comprar de novo e a indicar. Isso leva tempo, mas é o que sustenta.'},
 end('Qual ^hábito^ você reforça?','Comente: prazo, resposta ou honestidade.')],
 'Confiança se constrói devagar: cumprir o que diz, ser honesto e responder bem. Qual hábito você vai reforçar? Comente prazo, resposta ou honestidade.'))

# ===================== SAB 05/12 =====================
D='2026-12-05'
S3='Fonte: Mercado&Consumo (28/10/2026), Panorama de Consumo 2026 do Mercado Pago'
add(D,'0800',J('novidade-mercado-pago-54-por-cento-ia-na-escolha',[
 {'k':'Novidade: pesquisa','t':'^54%^ pretendem usar IA para escolher produtos','b':'Panorama de Consumo 2026, do Mercado Pago'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'54%','t':'Pretendem usar ferramentas de IA ao escolher produtos'},{'a':'48%','t':'Era o índice em 2025'},{'a':'6,5%','t':'Deixariam um agente de IA fazer a compra'}],'src':S3},
 {'k':'Como ler','t':'Foram ouvidos *3.345 usuários*','b':'Usuários do Mercado Livre e do Mercado Pago no Brasil. Não representa todos os consumidores.','src':S3},
 {'k':'Para você','t':'A IA ajuda a escolher; a *decisão é da pessoa*','b':'Título, medidas e uso do produto bem descritos ajudam o cliente, seja ele quem pergunta para a IA ou quem lê o anúncio.'},
 end('Quer ^prompts^ prontos de IA?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Segundo o Panorama de Consumo 2026 do Mercado Pago, 54% pretendem usar IA para escolher produtos e só 6,5% deixariam um agente de IA fazer a compra. Fonte: Mercado&Consumo (28/10/2026). Comente PROMPT.',HIA,av=True))
add(D,'1100',steps('shopee-atributos-do-anuncio','Shopee','Atributos do anúncio: ^preencha tudo^','Quanto mais claro, menos dúvida',
 [('Complete os campos','Preencha material, tamanho, cor e demais atributos que a plataforma pedir.'),
  ('Use as mesmas palavras do cliente','Escreva do jeito que as pessoas falam e buscam, sem inventar característica.'),
  ('Revise com o produto na mão','Confira medidas e detalhes. Informação errada vira reclamação.')],
 'Na Shopee, preencha todos os atributos do anúncio com informações corretas. Salve e revise os seus anúncios. Confira sempre as regras atuais da plataforma.','Salve para ^revisar^ hoje','E me conta o que você corrigiu.'))
add(D,'1400',steps('ia-ideias-de-oferta-para-estoque-parado','IA para vendedor','Ideias de oferta para ^estoque parado^','Sem vender abaixo do custo',
 [('Liste o que está parado','Anote os produtos, quantas unidades e quanto custaram. Use só dados seus.'),
  ('Use este prompt','Sugira 5 ideias de oferta para estes produtos parados, como kit ou brinde, mantendo o preço acima do meu custo mínimo. Explique cada ideia em uma frase.'),
  ('Faça a conta antes','Confira taxas, frete e margem. A IA sugere; a decisão é sua.')],
 'Como usar IA para criar ideias de oferta para estoque parado sem vender abaixo do custo, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',J('mito-dezembro-so-vende-presente',[
 {'k':'Mito','t':'"Em dezembro, só vende ^presente^"','b':'O calendário das plataformas mostra mais opções'},
 {'k':'No calendário','t':'TikTok Shop tem *casa, moda e festa*','b':'No Double 12: 4 e 5/12 casa pronta para o Natal, 6 e 7/12 moda verão, 8 e 9/12 eletrônicos e itens para festas. Confira no app.','src':'Fonte: Mercado&Consumo (25/10/2026)'},
 {'k':'Na prática','t':'Veja *o que se encaixa* no seu produto','b':'Casa, verão, festa e viagem também entram no fim de ano. Pense em como o seu produto se encaixa.'},
 end('Qual é o ^seu produto^ de dezembro?','Comente o que você vai ofertar.')],
 'Mito: em dezembro só vende presente. O calendário do TikTok Shop também cita casa, moda verão e itens para festas. Fonte: Mercado&Consumo (25/10/2026). Confira as datas no app. Qual é o seu produto de dezembro? Comente.'))
add(D,'2100',J('descanso-tambem-e-estrategia',[
 {'k':'Para refletir','t':'^Descanso^ também é estratégia','b':'Sábado à noite, sem culpa'},
 {'k':'Por que','t':'Cabeça descansada *decide melhor*','b':'Quem vende todo dia precisa de pausa para responder bem, calcular direito e manter a constância.'},
 {'k':'Como','t':'Combine uma *pausa pequena*','b':'Escolha um horário sem tela por dia. Sem promessa de resultado, só cuidado com quem faz o trabalho: você.'},
 end('Qual é a sua ^pausa^ de hoje?','Conte nos comentários.')],
 'Descanso também é estratégia. Qual é a sua pausa de hoje? Conte nos comentários.'))

# ===================== DOM 06/12 =====================
D='2026-12-06'
S4='Fonte: Estado de Minas (11/11/2026), pesquisa CNDL/SPC Brasil com Offerwise (out/2026)'
add(D,'0800',J('novidade-cndl-spc-57-por-cento-parcelas-em-aberto',[
 {'k':'Novidade: pesquisa','t':'^57%^ ainda pagam outras compras parceladas','b':'Pesquisa CNDL/SPC Brasil com a Offerwise'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'57%','t':'Ainda pagam outras compras parceladas'},{'a':'22%','t':'Têm três ou mais compromissos desse tipo'},{'a':'R$ 1.053','t':'Valor médio previsto para as compras'}],'src':S4},
 {'k':'Como ler','t':'O cliente está *mais cuidadoso*','b':'Na amostra, 51% pretendiam aproveitar a Black Friday e 31% ainda não tinham decidido.','src':S4},
 {'k':'Para você','t':'Seja *claro* sobre o valor final','b':'Preço, frete e prazo explicados antes da decisão ajudam quem está contando cada real.'},
 end('Quer aprender a ^começar^ do jeito certo?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'Pesquisa CNDL/SPC Brasil com a Offerwise: 57% ainda pagam outras compras parceladas e 22% têm três ou mais. Fonte: Estado de Minas (11/11/2026). Comente COMECAR.',av=True))
add(D,'1100',steps('live-mostrar-tamanho-com-objeto-comum','Passo a passo de live','Mostre o ^tamanho^ do produto ao vivo','Menos dúvida, menos devolução',
 [('Use um objeto conhecido','Coloque o produto ao lado de algo que todo mundo conhece, como uma mão, uma caneta ou um celular.'),
  ('Mostre a medida','Segure uma régua ou fita métrica e diga a medida em voz alta.'),
  ('Repita no chat','Escreva a medida no comentário fixado para quem chegou depois.')],
 'Como mostrar o tamanho do produto na live: objeto conhecido, medida em voz alta e comentário fixado. Salve e use.','Salve para ^usar^ na live','E me conta como foi.'))
add(D,'1400',steps('ia-titulo-da-live','IA para vendedor','^Título^ de live que chama atenção','Claro, honesto e curto',
 [('Diga o que vai mostrar','Escreva o produto, o público e o que você vai ensinar ou ofertar.'),
  ('Use este prompt','Crie 5 títulos curtos para uma live sobre [produto], claros e sem exagero. Não prometa resultado nem preço que eu não confirmei.'),
  ('Escolha e teste','Fique com o mais claro. Depois da live, anote se o título trouxe gente.')],
 'Como usar IA para criar títulos de live claros e honestos, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',quiz('quiz-o-que-e-estoque-de-seguranca','O que é ^estoque de segurança^?','Pense em um produto que vende bem.',
 ['Um produto em promoção','Uma reserva para imprevistos','O estoque que sobrou','A caixa de embalagem'],'É a *letra B*','É uma pequena reserva de unidades para cobrir atraso do fornecedor ou venda acima do esperado.',
 'Evite *vender o que não tem*','Uma reserva ajuda a cumprir o prazo prometido ao cliente.',
 'Quiz: o que é estoque de segurança? Resposta: B, uma reserva de unidades para imprevistos. Comente a letra que você marcou.'))
add(D,'2100',lst('5-perguntas-para-fechar-o-ano','Para guardar','5 perguntas para ^fechar o ano^',
 ['O que funcionou e vale repetir?','O que deu trabalho e pouco resultado?','Qual produto trouxe mais perguntas?','Onde eu perdi tempo ou dinheiro?','O que eu quero fazer diferente em janeiro?'],
 'Cinco perguntas para fazer ao seu negócio antes de o ano acabar. Salve a lista.','Salve e ^responda^ no papel','E me conta qual foi a mais difícil.',cb='Antes do ano acabar',tip=('Dica','Escreva *as respostas*','Anotar ajuda a lembrar e a decidir melhor em janeiro.')))

# ===================== SEG 07/12 =====================
D='2026-12-07'
S5='Fonte: Mundo do Marketing (28/10/2026)'
add(D,'0800',J('novidade-shopee-vip-1-milhao-de-assinantes',[
 {'k':'Novidade: Shopee','t':'Shopee VIP passa de ^1 milhão^ de assinantes','b':'Dados divulgados pela própria empresa'},
 {'l':'list','k':'Os números','t':'O que a empresa *divulgou*','items':[{'a':'1 mi+','t':'Assinantes do Shopee VIP'},{'a':'R$ 25 mi','t':'Em cupons no 11.11 (R$ 23 mi na Black Friday)'},{'a':'25 h+','t':'De treinamentos ao vivo para vendedores, de 26 a 30/10'}],'src':S5},
 {'k':'Atenção','t':'São dados da *própria Shopee*','b':'Informações da empresa sobre a temporada de novembro, sem verificação independente. Confira as regras na Central do Vendedor.','src':S5},
 {'k':'Para você','t':'Cliente de plataforma *compara frete e prazo*','b':'Calcule o frete dentro do preço, cumpra o prazo de postagem e mantenha o estoque atualizado.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'A Shopee diz que o Shopee VIP passou de 1 milhão de assinantes e que liberou R$ 25 milhões em cupons no 11.11. Dados da própria empresa. Fonte: Mundo do Marketing (28/10/2026). Comente LIVE.',av=True))
add(D,'1100',steps('tiktok-capa-e-primeiro-quadro','TikTok Shop','Capa e ^primeiro quadro^ do vídeo','O que a pessoa vê antes de assistir',
 [('Escolha o produto em destaque','Use um quadro em que o produto aparece inteiro e bem iluminado.'),
  ('Coloque um texto curto','Uma frase de poucas palavras que diga o que a pessoa vai ver.'),
  ('Combine com o início do vídeo','Se a capa promete uma coisa, o começo precisa mostrar essa mesma coisa.')],
 'Capa e primeiro quadro do vídeo: produto em destaque, texto curto e coerência com o início. Salve e revise a sua próxima capa.','Salve para ^revisar^ sua capa','E conta o que você mudou.'))
add(D,'1400',steps('ia-checklist-de-fotos-do-produto','IA para vendedor','Checklist de ^fotos^ do produto','Para não esquecer nenhum ângulo',
 [('Diga qual é o produto','Escreva o que é, o tamanho e onde ele é usado.'),
  ('Use este prompt','Monte uma lista com 8 fotos que eu devo tirar deste produto para um anúncio, incluindo detalhe, tamanho em uso e embalagem. Explique o objetivo de cada foto.'),
  ('Tire e confira','Fotografe com luz natural e confira se as fotos mostram o produto real.')],
 'Como usar IA para montar um checklist de fotos do produto, em 3 passos. Confira se as fotos mostram o produto real. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',J('mito-quem-vende-bem-nao-erra',[
 {'k':'Mito','t':'"Quem vende bem ^não erra^"','b':'Na prática, quem vende bem corrige rápido'},
 {'k':'O que acontece','t':'*Todo mundo* erra, inclusive em live','b':'Erro de preço, de som, de estoque. O que muda é o que a pessoa faz depois.'},
 {'k':'O que fazer','t':'Assuma, ajuste, *siga*','b':'Fale com honestidade, corrija e anote para não repetir. O público costuma valorizar a transparência.'},
 end('Qual foi o seu ^último erro^?','Conte nos comentários o que você aprendeu.')],
 'Mito: quem vende bem não erra. Na prática, quem vende bem assume, ajusta e segue. Qual foi o seu último erro e o que você aprendeu? Comente.'))
add(D,'2100',J('pequenas-vitorias-contam',[
 {'k':'Para começar a semana','t':'^Pequenas vitórias^ contam','b':'Segunda-feira, com calma'},
 {'k':'Exemplos','t':'*Pequeno* também é progresso','b':'Fazer a live mesmo com pouca gente. Responder todos os comentários. Anotar o que funcionou.'},
 {'k':'Por que','t':'O que se *repete* cresce','b':'Resultado costuma vir da soma de pequenas ações constantes. Os resultados variam de pessoa para pessoa.'},
 end('Qual foi a sua ^vitória^ de hoje?','Conte nos comentários.')],
 'Pequenas vitórias contam. Qual foi a sua vitória de hoje? Conte nos comentários.'))

# ===================== TER 08/12 =====================
D='2026-12-08'
S6='Fonte: Mercado&Consumo (28/10/2026), Panorama de Consumo 2026 do Mercado Pago'
add(D,'0800',J('novidade-mercado-pago-pix-42-por-cento',[
 {'k':'Novidade: pesquisa','t':'^Pix^ já aparece em 42% das intenções de pagamento','b':'Panorama de Consumo 2026, do Mercado Pago'},
 {'l':'list','k':'Os números','t':'O que a pesquisa *mostrou*','items':[{'a':'46%','t':'Citam o cartão de crédito como forma mais usada'},{'a':'42%','t':'Citam o Pix, inclusive parcelado, alta de 13 pontos sobre 2025'},{'a':'50%','t':'Pretendem pagar em parcelas'}],'src':S6},
 {'k':'Como ler','t':'Amostra de *usuários* do Mercado Livre','b':'Foram ouvidos 3.345 usuários do Mercado Livre e do Mercado Pago. Não representa todo o comércio.','src':S6},
 {'k':'Para você','t':'Explique *como pagar*','b':'Confira quais formas de pagamento o seu canal oferece e explique ao cliente de forma simples.'},
 end('Quer aprender a ^começar^ do jeito certo?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'Segundo o Panorama de Consumo 2026 do Mercado Pago, o Pix, inclusive parcelado, aparece em 42% das intenções de pagamento, alta de 13 pontos sobre 2025. Fonte: Mercado&Consumo (28/10/2026). Comente COMECAR.',av=True))
add(D,'1100',steps('live-agradecer-quem-comprou','Passo a passo de live','Agradeça ^quem comprou^ na live','Um gesto simples que aproxima',
 [('Diga o nome','Quando for possível, agradeça a pessoa pelo nome ou apelido que aparece no chat.'),
  ('Explique o próximo passo','Fale o que acontece agora: confirmação, envio e como acompanhar.'),
  ('Convide para voltar','Avise o dia e a hora da próxima live.')],
 'Como agradecer quem comprou durante a live: use o nome, explique o próximo passo e convide para voltar. Salve e use.','Salve para ^usar^ na live','E me conta como foi.'))
add(D,'1400',steps('ia-ideias-de-nome-para-loja','IA para vendedor','Ideias de ^nome para loja^','Para quem está começando',
 [('Defina o estilo','Escreva o que você vende, para quem e o tom: simples, divertido ou sério.'),
  ('Use este prompt','Sugira 10 nomes curtos e fáceis de lembrar para uma loja de [produto]. Evite nomes parecidos com marcas conhecidas.'),
  ('Pesquise antes de usar','Busque o nome na internet e na plataforma para ver se já existe. Só então escolha.')],
 'Como usar IA para ter ideias de nome para a sua loja, em 3 passos. Pesquise antes de usar. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',enq('enquete-live-entre-natal-e-ano-novo','Vai fazer live entre Natal e Ano-Novo?',['Sim, em vários dias','Sim, em um dia','Ainda não decidi','Vou descansar'],'Enquete: vai fazer live entre Natal e Ano-Novo? Comente a letra: A sim, em vários dias, B sim, em um dia, C ainda não decidi ou D vou descansar.'))
add(D,'2100',lst('a-regra-dos-2-minutos','Para guardar','A regra dos ^2 minutos^',
 ['Se leva 2 minutos, faça agora','Responder uma dúvida simples do chat','Anotar o número do dia','Guardar a ficha do produto no lugar certo'],
 'A regra dos 2 minutos para vendedores: tarefa rápida se resolve na hora. Salve a lista.','Salve e ^aplique^ hoje','E me conta o que você resolveu.',cb='Tarefa pequena não precisa esperar',tip=('Cuidado','Não vire *refém* do celular','Resolva o rápido, mas reserve um horário para as tarefas importantes.')))

# ===================== QUA 09/12 =====================
D='2026-12-09'
S7='Fonte: Mundo do Marketing (28/10/2026)'
add(D,'0800',J('novidade-shopee-live-village-280-afiliados',[
 {'k':'Novidade: Shopee','t':'Shopee anunciou o ^Live Village^ com 60 horas de lives','b':'Evento para afiliados e marcas, de 7 a 11/11'},
 {'l':'list','k':'Os números','t':'O que a empresa *anunciou*','items':[{'a':'280','t':'Afiliados participantes, em números aproximados'},{'a':'15+','t':'Marcas envolvidas'},{'a':'60 h','t':'De transmissões ao vivo'}],'src':S7},
 {'k':'Atenção','t':'Programação *anunciada* em outubro','b':'A matéria é de 28/10 e descreve o que a empresa planejava para o evento. Os números são da própria Shopee.','src':S7},
 {'k':'Para você','t':'Live e afiliados *andam juntos*','b':'Plataformas investem em evento ao vivo. Quem treina a live pequena já constrói o hábito para crescer.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'A Shopee anunciou o Live Village, evento de 7 a 11/11 com cerca de 280 afiliados, mais de 15 marcas e 60 horas de lives, segundo a empresa. Fonte: Mundo do Marketing (28/10/2026). Comente LIVE.',av=True))
add(D,'1100',steps('live-semana-entre-natal-e-ano-novo','Passo a passo de live','Live entre ^Natal e Ano-Novo^','Plano simples para a semana mais parada',
 [('Escolha poucos dias','Defina um ou dois dias e um horário fixo. Melhor poucas lives bem feitas do que cansaço.'),
  ('Ofereça o que combina','Pense em itens de organização, casa, verão ou festa, se fizer sentido para o seu produto.'),
  ('Avise com antecedência','Combine a data com o público e confira o prazo de envio da plataforma antes de prometer.')],
 'Plano simples para fazer live entre Natal e Ano-Novo: poucos dias, itens que combinam e aviso antecipado. Salve e adapte.','Salve para ^planejar^ a semana','E me conta quais dias você escolheu.'))
add(D,'1400',steps('ia-metas-de-janeiro','IA para vendedor','Metas de ^janeiro^ com IA','Metas pequenas que cabem na rotina',
 [('Olhe o que já fez','Anote quantas lives, vídeos e vendas você teve nas últimas semanas.'),
  ('Use este prompt','Com estes números, sugira 3 metas realistas para janeiro: uma de conteúdo, uma de atendimento e uma de organização. Sem prometer resultado.'),
  ('Escolha uma','Fique com uma meta e um prazo. Metas demais atrapalham.')],
 'Como usar IA para definir metas realistas de janeiro, em 3 passos. Comente PROMPT.','Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT',HIA))
add(D,'1900',quiz('quiz-primeira-metrica-a-olhar','Qual ^número^ olhar primeiro depois de uma live?','Para decidir o que ajustar na próxima.',
 ['Número de seguidores novos','Pedidos e dúvidas repetidas','Quantas curtidas teve','A cor do cenário'],'É a *letra B*','Pedidos mostram o que vendeu e dúvidas repetidas mostram o que explicar melhor na próxima live.',
 'Olhe o que *muda a ação*','Seguidores e curtidas ajudam, mas pedidos e perguntas orientam o que ajustar.',
 'Quiz: qual número olhar primeiro depois de uma live? Resposta: B, pedidos e dúvidas repetidas. Comente a letra que você marcou.'))
add(D,'2100',J('resumo-da-semana-3-a-9-12',[
 {'k':'Resumo da semana','t':'^4 novidades^ para não perder','b':'Do que saiu de 03 a 09/12 aqui no perfil'},
 {'l':'list','k':'Salve este resumo','t':'O que *aconteceu*','items':[{'a':'WhatsApp','t':'Respostas via API oficial passam a ser cobradas'},{'a':'CNDL/SPC','t':'65% temem fraude e 57% pagam outras parcelas'},{'a':'Mercado Pago','t':'54% pretendem usar IA para escolher produtos'},{'a':'Shopee','t':'VIP passa de 1 milhão de assinantes, diz a empresa'}],'src':'Fontes: Paraíba Total, Estado de Minas, Mercado&Consumo, Mundo do Marketing (out e nov/2026)'},
 {'k':'Para esta semana','t':'*Um passo* para cada novidade','b':'Deixe preço e prazo claros, reforce a confiança, use IA com revisão e treine a live em horário fixo.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: novidades de WhatsApp Business, CNDL/SPC, Mercado Pago e Shopee. Salve e envie para um amigo que vende online.'))
for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
