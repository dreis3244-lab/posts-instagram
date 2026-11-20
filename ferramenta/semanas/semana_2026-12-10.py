import json,sys
# Semana 10/12 a 16/12/2026 (35 carrosseis, 5 por dia: 08h, 11h, 14h, 19h, 21h)
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

# ===================== QUI 10/12 =====================
D='2026-12-10'
S='Fonte: Times Brasil (17/11/2026), dados da TOTVS'
add(D,'0800',news('novidade-totvs-marketplaces-24-por-cento','Novidade: marketplaces','Marketplaces ^cresceram^ em novembro, diz a TOTVS','Dados da base de clientes da empresa de software',
 [('+24%','Pedidos por marketplaces na primeira quinzena de novembro, ante o mesmo período de 2025'),('+30%','Itens vendidos nesses canais no mesmo período'),('+12%','Vendas por marketplaces no 11.11, ante o 11.11 de 2025')],S,
 ('É dado de *uma* empresa','A TOTVS usa a base dos seus clientes, sem identificar as empresas. A matéria não detalha a metodologia.'),
 ('Mais *canal*, mais *concorrência*','Mais gente comprando em marketplace também significa mais lojas disputando atenção. Foto, prazo e atendimento fazem diferença.'),
 'Segundo a TOTVS, os pedidos por marketplaces cresceram 24% na primeira quinzena de novembro de 2026 ante o mesmo período de 2025. Dados da base de clientes da empresa. Fonte: Times Brasil (17/11/2026). Comente LIVE.'))
add(D,'1100',steps('live-pedir-para-compartilhar','Passo a passo de live','Peça para o público ^compartilhar^ a live','Sem insistir e sem parecer desespero',
 [('Dê um motivo','Diga o que a pessoa ganha: avisar um amigo que procura aquele produto, por exemplo.'),
  ('Peça uma vez, no meio','Faça o pedido depois de mostrar algo bom, não na abertura. Uma vez basta.'),
  ('Agradeça em voz alta','Cite quem entrou pelo convite de alguém. Isso estimula os outros.')],
 'Como pedir para o público compartilhar a live em 3 passos: dê um motivo, peça uma vez e agradeça. Salve e teste.','Salve para ^testar^ na live','E me conta como foi.'))
add(D,'1400',ia('ia-organizar-pedidos-do-dia','Organize os ^pedidos^ do dia com IA','Para não perder nenhum detalhe',
 [('Junte as informações','Cole os pedidos do dia em um texto: produto, quantidade, cidade e observações. Retire dados pessoais sensíveis.'),
  ('Use este prompt','Organize estes pedidos em uma tabela com produto, quantidade, prazo combinado e pendências. Marque o que está faltando.'),
  ('Confira com a plataforma','A IA organiza, mas o painel da plataforma é a fonte oficial. Compare antes de enviar.')],
 'Como usar IA para organizar os pedidos do dia em uma tabela, em 3 passos, sem expor dados sensíveis. Comente PROMPT.'))
add(D,'1900',enq('enquete-produto-de-natal','Qual produto você mais quer vender no Natal?',['Presentes até R$ 50','Kits e combos','Casa e decoração','Beleza e cuidados'],'Enquete: qual produto você mais quer vender no Natal? Comente a letra: A presentes até R$ 50, B kits e combos, C casa e decoração ou D beleza e cuidados.'))
add(D,'2100',lst('15-dias-para-fechar-o-ano','Para refletir','^15 dias^ para fechar o ano com clareza',
 ['Liste o que funcionou em novembro','Corte uma tarefa que não trouxe resultado','Escolha uma meta pequena para o Natal'],
 'Quinze dias para fechar o ano com clareza: o que funcionou, o que cortar e uma meta pequena. Salve e escolha o seu primeiro passo.','Salve e ^escolha um^ passo','E me conta qual será.',cb='Sem pressa e com foco',tip=('Por quê','Poucas decisões *bem feitas*','Em dezembro o tempo é curto. Menos tarefas, mais atenção ao que já funciona.')))

# ===================== SEX 11/12 =====================
D='2026-12-11'
S='Fonte: Mobile Time (27/10/2026), estudo da Venda.ai'
add(D,'0800',news('novidade-venda-ai-58-por-cento-fora-do-horario','Novidade: pesquisa','^58%^ das compras online ocorrem fora do horário comercial','Estudo da Venda.ai com conversas entre consumidores e agentes de IA',
 [('58,2%','Das vendas no comércio online ocorrem fora do horário comercial'),('30%','Ficam entre 18h e 23h'),('27%','Acontecem nos fins de semana')],S,
 ('Base do estudo e *limites*','Foram analisadas mais de 241,5 mil interações entre julho e setembro de 2026. É um estudo de uma empresa de IA, não um número do mercado todo.'),
 ('A resposta *rápida* conta','Segundo o estudo, nas conversas em que a resposta demorou mais de dez minutos, a conversão em compras caiu 98%. Deixe respostas prontas para a noite e o fim de semana.'),
 'Estudo da Venda.ai: 58,2% das vendas online ocorrem fora do horário comercial, 30% entre 18h e 23h. Análise de mais de 241,5 mil interações entre julho e setembro de 2026. Fonte: Mobile Time (27/10/2026). Comente PROMPT.',cta='PROMPT',et='Quer ^prompts^ de resposta rápida?'))
add(D,'1100',steps('shopee-modelos-de-resposta-rapida','Shopee','Modelos de ^resposta rápida^ no chat','Para responder mais rápido sem soar robótico',
 [('Liste as 5 perguntas mais comuns','Prazo, tamanho, material, troca e forma de uso. Anote as que mais aparecem no seu chat.'),
  ('Escreva uma resposta curta para cada','Dois ou três parágrafos curtos, com tom cordial e só informação que você confirma.'),
  ('Revise toda semana','Troque o que gerou nova dúvida e confira se as regras da plataforma continuam as mesmas.')],
 'Como montar modelos de resposta rápida para o chat da Shopee em 3 passos. Confira sempre as regras atuais da plataforma. Salve e use.','Salve para ^montar^ os seus','E me conta qual pergunta mais aparece.'))
add(D,'1400',ia('ia-resposta-fora-do-horario','Resposta para ^fora do horário^ com IA','Mensagem automática cordial e honesta',
 [('Defina o que prometer','Informe seu horário real de atendimento. Não prometa prazo que você não controla.'),
  ('Use este prompt','Escreva uma mensagem curta para quem escreve fora do meu horário: agradeça, diga quando respondo e indique onde ver informações do pedido na plataforma.'),
  ('Teste e ajuste','Leia como cliente. Se parecer fria, ajuste o tom. Cadastre só em canais que permitem mensagem automática.')],
 'Como usar IA para escrever uma mensagem cordial e honesta para quem chama fora do horário, em 3 passos. Comente PROMPT.'))
add(D,'1900',quiz('quiz-o-que-e-tempo-de-resposta','O que é ^tempo de resposta^?','Métrica comum no atendimento online.',
 ['O prazo de entrega do pedido','O tempo até você responder o cliente','A duração da live','O prazo de postagem'],'É a *letra B*','É o tempo que passa entre a mensagem do cliente e a sua resposta.',
 'Responda *rápido*, mas com cuidado','Resposta rápida e correta ajuda mais do que resposta rápida e errada.',
 'Quiz: o que é tempo de resposta? Resposta: B, o tempo até você responder o cliente. Comente a letra que você marcou.'))
add(D,'2100',lst('o-que-eu-faria-com-2-horas-livres','Para refletir','O que fazer com ^2 horas^ livres hoje',
 ['Responder mensagens antigas com calma','Atualizar fotos e títulos de 3 produtos','Gravar um vídeo curto de demonstração'],
 'O que fazer com duas horas livres hoje: responder mensagens, atualizar anúncios e gravar um vídeo. Salve e escolha uma.','Salve e ^escolha uma^','E me conta qual você fez.',cb='Para usar bem o tempo curto',tip=('Dica','Comece pelo que *já* existe','Melhorar o que já está no ar costuma ser mais simples do que criar do zero.')))

# ===================== SAB 12/12 =====================
D='2026-12-12'
S='Fonte: Meio & Mensagem (11/11/2026)'
add(D,'0800',news('novidade-mercado-ads-anuncios-em-video','Novidade: Mercado Livre','Mercado Ads estreia ^anúncios em vídeo^','Formato Video Catalog Ads chega ao Mercado Livre',
 [('Vídeo','O formato permite veicular catálogos dinâmicos de produtos em vídeo dentro do marketplace'),('+38%','Taxa de conversão de quem vê anúncio em vídeo, segundo a empresa'),('Até 2x','Mais vendas com anúncios de produto em vídeo, segundo a empresa')],S,
 ('Números da *própria empresa*','Os percentuais foram divulgados pelo Mercado Ads e a matéria não traz estudo independente. Anunciar exige investimento e teste.'),
 ('Vídeo está em *toda parte*','Mesmo sem anúncio pago, ter um vídeo simples do produto ajuda o cliente a entender tamanho, uso e acabamento.'),
 'O Mercado Ads estreou o Video Catalog Ads, anúncios em vídeo no Mercado Livre. A empresa diz que quem vê vídeo converte 38% mais. Dados da própria empresa. Fonte: Meio & Mensagem (11/11/2026). Comente LIVE.'))
add(D,'1100',steps('tiktok-mostrar-o-produto-em-uso','TikTok Shop','Mostre o produto ^em uso^','Em vez de só mostrar a embalagem',
 [('Escolha um problema','Mostre a situação em que o produto ajuda: guardar, limpar, decorar ou presentear.'),
  ('Grave de perto','Câmera próxima, luz de frente e a mão em cena. O público quer ver o detalhe.'),
  ('Feche com uma informação útil','Diga medida, material ou cuidado. Sem exagerar nos benefícios.')],
 'Como gravar um vídeo mostrando o produto em uso, em 3 passos: problema, câmera de perto e uma informação útil. Salve e grave hoje.','Salve para ^gravar^ hoje','E conta qual produto você vai mostrar.'))
add(D,'1400',ia('ia-tabela-de-perguntas-sobre-prazo','Tabela de ^perguntas^ sobre prazo','Respostas prontas e confirmadas',
 [('Reúna as dúvidas','Liste o que os clientes perguntam sobre envio, prazo e rastreio.'),
  ('Use este prompt','Crie uma tabela com 8 perguntas frequentes sobre envio e respostas curtas. Use só as informações que eu informar abaixo e deixe em branco o que eu não souber.'),
  ('Preencha com dados reais','Complete as lacunas com as regras atuais da plataforma e dos seus envios. Nunca invente prazo.')],
 'Como usar IA para criar uma tabela de perguntas e respostas sobre prazo de envio, sem inventar regra, em 3 passos. Comente PROMPT.'))
add(D,'1900',J('mito-video-precisa-de-edicao-profissional',[
 {'k':'Mito ou verdade','t':'Vídeo bom precisa de ^edição profissional^','b':'Será?'},
 {'k':'Mito','t':'Nem *sempre*','b':'Para mostrar um produto, luz boa, áudio limpo e uma demonstração clara costumam importar mais do que efeitos.'},
 {'k':'O que ajuda','t':'Três *básicos*','b':'Luz de frente, celular firme e uma fala simples sobre o que o produto faz.'},
 {'k':'Cuidado','t':'Cada plataforma tem *regras*','b':'Confira as regras de vídeo da plataforma onde você vende.'},
 end('Qual é a sua ^maior dúvida^?','Comente e eu respondo em um próximo post.')],
 'Mito: vídeo bom precisa de edição profissional. Para mostrar um produto, o básico bem feito costuma bastar. Comente qual é a sua maior dúvida.'))
add(D,'2100',J('pequenos-ajustes-grandes-efeitos',[
 {'k':'Para refletir','t':'^Pequenos ajustes^, grandes efeitos','b':'O que dá para melhorar hoje'},
 {'l':'list','k':'Em 10 minutos','t':'Escolha *um*','items':[{'a':'1','t':'Reescrever o primeiro parágrafo de um anúncio'},{'a':'2','t':'Trocar a foto de capa de um produto'},{'a':'3','t':'Responder uma mensagem pendente'}]},
 {'k':'Por que funciona','t':'Melhora *acumula*','b':'Um ajuste por dia vira trinta no mês. O que importa é manter o hábito.'},
 end('Qual ajuste você ^faz hoje^?','Comente 1, 2 ou 3.')],
 'Pequenos ajustes, grandes efeitos: escolha um ajuste de 10 minutos para fazer hoje. Comente 1, 2 ou 3.'))

# ===================== DOM 13/12 =====================
D='2026-12-13'
S='Fonte: Consumidor Moderno (17/11/2026), dados da Shopee'
add(D,'0800',news('novidade-shopee-lives-85-milhoes-no-11-11','Novidade: Shopee','Shopee Lives somam ^85 milhões^ de visualizações em 24 horas','Balanço da campanha 11.11 de 2026, divulgado pela empresa',
 [('85 mi','Visualizações das lives em 24 horas, mais que o dobro da Black Friday de 2025, segundo a Shopee'),('5x','Alta nos pedidos gerados pelas transmissões na mesma comparação'),('63 mil','Pessoas ao mesmo tempo no pico da live com Péricles e Nubank')],S,
 ('Dados *da própria Shopee*','A matéria não traz valores absolutos de pedidos nem a metodologia. Compara a campanha com a Black Friday de 2025.'),
 ('Audiência *não é* venda','Muita gente assistindo ajuda, mas o que converte é oferta clara, produto mostrado com calma e resposta ao chat.'),
 'A Shopee diz que as lives somaram mais de 85 milhões de visualizações em 24 horas no 11.11 de 2026, mais que o dobro da Black Friday de 2025. Dados da empresa. Fonte: Consumidor Moderno (17/11/2026). Comente LIVE.'))
add(D,'1100',steps('live-reduzir-pausas-e-silencio','Passo a passo de live','Como evitar ^silêncio^ na live','Para manter o ritmo sem falar sem parar',
 [('Tenha 3 tópicos por produto','Material, uso e cuidado. Se travar, volte a um deles.'),
  ('Mostre enquanto fala','Gire o produto, aproxime a câmera, use as mãos. A imagem ocupa o espaço.'),
  ('Leia um comentário','Quando faltar assunto, responda alguém do chat. Isso reativa a conversa.')],
 'Como evitar silêncio na live com 3 tópicos por produto, demonstração e leitura de comentários. Salve e ensaie.','Salve para ^ensaiar^','E me conta o que travou.'))
add(D,'1400',ia('ia-pos-live-resumo-para-postar','Resumo da live para ^postar^ com IA','Transforme a live em um post útil',
 [('Anote os destaques','Escreva em tópicos o que você mostrou, as dúvidas do chat e o que ficou pendente.'),
  ('Use este prompt','Com base nestas anotações, escreva uma legenda de 5 linhas resumindo a live, com um convite para a próxima. Tom cordial e sem prometer resultado.'),
  ('Revise antes de publicar','Confira nomes de produto, datas e qualquer número que a IA tenha citado.')],
 'Como usar IA para transformar as anotações da live em um resumo para postar, em 3 passos. Comente PROMPT.'))
add(D,'1900',enq('enquete-horario-da-live-em-dezembro','Qual horário você prefere para lives em dezembro?',['Manhã','Tarde','Início da noite','Fim da noite'],'Enquete: qual horário você prefere para lives em dezembro? Comente a letra: A manhã, B tarde, C início da noite ou D fim da noite.'))
add(D,'2100',lst('plano-da-semana-14-a-20-12','Plano da semana','Seu plano para ^14 a 20/12^',
 ['Segunda: responder pendências e atualizar anúncios','Quarta: fazer uma live curta com os produtos de presente','Sexta: avaliar números e ajustar a oferta'],
 'Plano simples para a semana de 14 a 20/12: pendências, uma live curta e avaliação de números. Salve e adapte.','Salve e ^adapte^ o plano','E me conta o que muda na sua semana.',cb='Uma semana leve e organizada',tip=('Dica','Poucas tarefas *fixas*','Defina dia e horário antes. Assim a semana não depende de motivação.')))

# ===================== SEG 14/12 =====================
D='2026-12-14'
S='Fonte: A Tarde (01/11/2026)'
add(D,'0800',J('novidade-mercado-livre-208-vendas-por-minuto',[
 {'k':'Novidade: Mercado Livre','t':'Afiliados do Mercado Livre: ^208 vendas^ por minuto','b':'Número do segundo trimestre de 2026, segundo a matéria'},
 {'k':'O dado','t':'*208* vendas por minuto no Brasil','b':'A matéria afirma que o programa de afiliados e criadores da plataforma registrou esse número no 2º trimestre de 2026.','src':S},
 {'k':'Como ler','t':'A matéria *não cita* a origem do dado','b':'O texto não atribui o número a um balanço ou executivo. Trate como referência e confirme no Mercado Livre.','src':S},
 {'k':'Para você','t':'Afiliado vende com *conteúdo*','b':'Quem mostra o produto com clareza e responde dúvidas tem mais chance de gerar venda. Confira as regras e comissões do programa.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'Segundo A Tarde, o programa de afiliados e criadores do Mercado Livre registrou 208 vendas por minuto no Brasil no 2º trimestre de 2026. A matéria não cita a origem do número. Fonte: A Tarde (01/11/2026). Comente LIVE.',HT,av=True))
add(D,'1100',steps('live-lista-de-presentes-por-faixa-de-preco','Passo a passo de live','Lista de presentes por ^faixa de preço^','Facilita a escolha de quem está em dúvida',
 [('Monte 3 faixas','Por exemplo: até R$ 50, até R$ 100 e acima de R$ 100. Use valores que façam sentido para a sua loja.'),
  ('Mostre um produto por faixa','Apresente cada um com uso, tamanho e material.'),
  ('Peça o orçamento no chat','Pergunte quanto a pessoa quer gastar e sugira uma opção.')],
 'Como montar uma lista de presentes por faixa de preço na live em 3 passos. Salve e use na sua próxima transmissão.','Salve para ^montar^ a sua','E me conta qual faixa vende mais.'))
add(D,'1400',ia('ia-aviso-de-ultimo-dia-para-pedir-no-natal','Aviso de ^prazo^ de Natal com IA','Sem prometer o que você não controla',
 [('Confirme o prazo','Veja as regras de postagem e entrega da plataforma e dos Correios ou da transportadora.'),
  ('Use este prompt','Escreva um aviso curto para clientes sobre o prazo para pedir antes do Natal. Use apenas a data que eu informar e lembre que a entrega depende da transportadora.'),
  ('Publique com cuidado','Atualize o aviso se o prazo mudar. Não garanta entrega em data específica.')],
 'Como usar IA para escrever um aviso de prazo de Natal sem prometer entrega, em 3 passos. Comente PROMPT.'))
add(D,'1900',J('mito-afiliado-e-so-para-quem-tem-audiencia',[
 {'k':'Mito ou verdade','t':'Afiliado é só para quem tem ^muita audiência^','b':'Será?'},
 {'k':'Mito','t':'Não é bem *assim*','b':'Programas variam, mas o que costuma pesar é a confiança de quem acompanha, não só o número de seguidores.'},
 {'k':'O que ajuda','t':'Mostre *uso real*','b':'Fale de produtos que você conhece, explique para quem serve e avise quando houver comissão.'},
 {'k':'Cuidado','t':'Leia as *regras*','b':'Cada plataforma define quem pode participar e como funcionam as comissões.'},
 end('Você já foi ^afiliado^?','Comente sim ou não.')],
 'Mito: afiliado é só para quem tem muita audiência. As regras variam, então confira as da plataforma. Você já foi afiliado? Comente sim ou não.'))
add(D,'2100',lst('o-que-nao-esquecer-antes-do-natal','Checklist','O que ^não esquecer^ antes do Natal',
 ['Estoque dos produtos mais pedidos','Prazo de postagem e aviso aos clientes','Respostas prontas para as dúvidas comuns'],
 'Checklist antes do Natal: estoque, prazo de postagem e respostas prontas. Salve e marque o que já fez.','Salve e ^marque^ o que fez','E me conta o que falta.',cb='Três itens para olhar hoje',tip=('Dica','Cheque *hoje*, não na véspera','Com tempo, você ajusta o que faltar sem correria.')))

# ===================== TER 15/12 =====================
D='2026-12-15'
S='Fonte: Times Brasil (17/11/2026), pesquisa TOTVS com Opinion Box'
add(D,'0800',news('novidade-totvs-17-por-cento-compraram-em-live','Novidade: pesquisa','^17%^ já compraram durante uma live, diz pesquisa','Pesquisa TOTVS com Opinion Box sobre a jornada de compra',
 [('17%','Já compraram durante uma transmissão'),('65%','Afirmam já ter assistido a esse tipo de conteúdo'),('2 mil+','Pessoas maiores de 18 anos ouvidas')],S,
 ('Pesquisa *declaratória*','O que as pessoas disseram, não o que fizeram. A matéria não informa o período de coleta.'),
 ('Assistir vem *antes* de comprar','A diferença entre quem assiste e quem compra mostra espaço para quem explica bem e responde ao chat.'),
 'Pesquisa TOTVS com Opinion Box: 17% já compraram durante uma live e 65% já assistiram. Mais de 2 mil pessoas ouvidas. Fonte: Times Brasil (17/11/2026). Comente LIVE.'))
add(D,'1100',steps('shopee-descricao-curta-e-clara','Shopee','Descrição ^curta e clara^ no anúncio','Para o cliente entender rápido',
 [('Comece pelo uso','Diga em uma frase para que serve o produto e para quem é.'),
  ('Liste medidas e material','Informe tamanho, material e cuidados. Confira tudo com o produto na mão.'),
  ('Evite exagero','Nada de promessa que você não possa cumprir. Siga as regras de anúncio da plataforma.')],
 'Como escrever uma descrição curta e clara no anúncio da Shopee em 3 passos. Confira as regras atuais da plataforma. Salve e revise um anúncio hoje.','Salve para ^revisar^ hoje','E me conta qual anúncio você vai melhorar.'))
add(D,'1400',ia('ia-perguntas-para-conhecer-o-cliente','Perguntas para conhecer o ^cliente^','Com ajuda da IA, sem invadir',
 [('Defina o objetivo','Quer saber o que a pessoa busca, quanto quer gastar ou como prefere ser atendida?'),
  ('Use este prompt','Crie 5 perguntas curtas e educadas para entender o que um cliente procura em presentes. Evite perguntas sobre dados pessoais.'),
  ('Use na live ou no chat','Faça uma por vez e ouça a resposta antes de oferecer produto.')],
 'Como usar IA para criar perguntas curtas e educadas que ajudam a entender o cliente, em 3 passos. Comente PROMPT.'))
add(D,'1900',quiz('quiz-o-que-e-pos-venda','O que é ^pós-venda^?','Etapa depois da compra.',
 ['Desconto para novos clientes','Atendimento depois da compra','Anúncio pago','Frete grátis'],'É a *letra B*','É o cuidado com o cliente depois da compra: acompanhar o pedido, tirar dúvidas e resolver problemas.',
 'Quem cuida, *conquista*','Um bom pós-venda ajuda a manter a confiança e pode gerar uma nova compra.',
 'Quiz: o que é pós-venda? Resposta: B, atendimento depois da compra. Comente a letra que você marcou.'))
add(D,'2100',J('cuidar-de-quem-ja-comprou',[
 {'k':'Para refletir','t':'Cuide de quem ^já comprou^','b':'É o público mais próximo da sua loja'},
 {'l':'list','k':'Como','t':'Três gestos *simples*','items':[{'a':'1','t':'Agradecer e confirmar o envio'},{'a':'2','t':'Responder dúvidas com clareza'},{'a':'3','t':'Pedir uma avaliação de forma educada'}]},
 {'k':'Por que importa','t':'Confiança *se acumula*','b':'Quem é bem atendido tende a lembrar da loja e a indicá-la.'},
 end('Qual gesto você ^reforça^?','Comente 1, 2 ou 3.')],
 'Cuide de quem já comprou: agradeça, responda com clareza e peça avaliação com educação. Qual gesto você reforça? Comente 1, 2 ou 3.'))

# ===================== QUA 16/12 =====================
D='2026-12-16'
S='Fonte: BPMoney (04/11/2026)'
add(D,'0800',J('novidade-mercado-livre-receita-45-por-cento-3t26',[
 {'k':'Novidade: Mercado Livre','t':'Receita do Mercado Livre sobe ^45%^ no 3º trimestre','b':'Balanço de julho a setembro de 2026'},
 {'l':'list','k':'Os números','t':'O que o balanço *mostrou*','items':[{'a':'US$ 10,75 bi','t':'Receita total, alta de 45%'},{'a':'US$ 448 mi','t':'Lucro líquido, abaixo do esperado pelo mercado'},{'a':'6,3%','t':'Margem operacional, ante quase 10% no 3T25'}],'src':S},
 {'k':'Para o vendedor','t':'A matéria cita *frete e logística*','b':'Menciona gastos maiores com frete grátis no Brasil e na Argentina, ampliação de centros de distribuição e taxas de frete mais altas cobradas dos lojistas.','src':S},
 {'k':'Para você','t':'Conheça os *seus* custos','b':'Taxas e frete mudam. Revise a margem dos seus produtos sempre que a plataforma atualizar as regras.'},
 end('Quer a ^conta da margem^?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'O Mercado Livre teve receita de US$ 10,75 bilhões no 3º trimestre de 2026, alta de 45%, e lucro de US$ 448 milhões. A matéria cita gastos com frete grátis e taxas de frete mais altas para lojistas. Fonte: BPMoney (04/11/2026). Comente COMECAR.',HT,av=True))
add(D,'1100',steps('live-o-que-fazer-quando-o-chat-para','Passo a passo de live','E se o chat ^ficar parado^?','Três formas de reativar a conversa',
 [('Faça uma pergunta fácil','Algo de uma palavra: sua cor favorita, ou tamanho M ou G.'),
  ('Conte uma situação de uso','Mostre como o produto resolve um problema do dia a dia.'),
  ('Nomeie quem entrou','Cumprimente quem acabou de chegar. Atenção pessoal chama resposta.')],
 'O que fazer quando o chat da live fica parado: pergunta fácil, situação de uso e cumprimentar quem entra. Salve e teste.','Salve para ^testar^','E me conta o que funcionou.'))
add(D,'1400',ia('ia-pesquisa-de-satisfacao-curta','Pesquisa de ^satisfação^ curta com IA','Três perguntas para quem comprou',
 [('Defina o objetivo','Quer saber sobre produto, entrega ou atendimento? Escolha um foco.'),
  ('Use este prompt','Crie uma pesquisa de satisfação com 3 perguntas curtas e educadas para clientes que compraram há uma semana. Sem pedir dados pessoais.'),
  ('Envie com respeito','Use apenas canais permitidos pela plataforma e só com quem aceita contato.')],
 'Como usar IA para criar uma pesquisa de satisfação de três perguntas para clientes, em 3 passos. Comente PROMPT.'))
add(D,'1900',enq('enquete-vai-fazer-live-no-natal','Você vai fazer live na semana do Natal?',['Sim, todos os dias','Sim, alguns dias','Só depois do Natal','Ainda não decidi'],'Enquete: você vai fazer live na semana do Natal? Comente a letra: A sim, todos os dias, B sim, alguns dias, C só depois do Natal ou D ainda não decidi.'))
add(D,'2100',J('resumo-da-semana-10-a-16-12',[
 {'k':'Resumo da semana','t':'^10 a 16/12^ em poucos pontos','b':'O que vimos e o que fazer'},
 {'l':'list','k':'Novidades','t':'O que *saiu* nas notícias','items':[{'a':'TOTVS','t':'Marketplaces cresceram em novembro, segundo a empresa'},{'a':'Venda.ai','t':'58,2% das compras online fora do horário comercial'},{'a':'Mercado Livre','t':'Anúncios em vídeo, afiliados e balanço do 3º trimestre'}]},
 {'k':'Para esta semana','t':'*Um passo* para cada novidade','b':'Responda rápido, mostre o produto em vídeo, cuide de quem já comprou e confira as suas margens.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: TOTVS, Venda.ai, Mercado Ads, Shopee e Mercado Livre. Salve e envie para um amigo que vende online.'))
for j in jobs:
    for s in j['slides']:
        if s.get('b')=='':s.pop('b')
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
