import json
HT='#tiktokshop #shopee #instagramshop #livesell #vendasonline #empreendedorismo'
def J(slug,slides,cap,tags=HT):return {'slug':slug,'slides':slides,'cap':cap+'\n\nCurta, salve e siga @{H} para mais conteúdo de TikTok Shop, Shopee, Instagram Shop e IA.\n\n'+tags}
def end(t,b,cta=None):
    d={'t':t,'b':b,'follow':True}
    if cta:d['cta']=cta
    return d
SF='Fonte: Exame (31/08/2026)'
SG='Fonte: Mercado&Consumo (09/09/2026)'
SH='Fonte: Central do Varejo (11/08/2026)'
SI='Fonte: JCN News (24/08/2026)'
jobs=[]
def add(day,slot,j):
    j['d']=day;j['slot']=slot;jobs.append(j)
def enq(slug,q,opts,cap):
    return J(slug,[{'k':'Enquete','t':q,'b':'Comente a letra'},{'l':'enquete','k':'Escolha','t':'Qual é a *sua*?','b':'\n'.join(opts)},{'k':'Próximo post','t':'Eu respondo a *mais votada*','b':'Conte nos comentários qual é a sua letra e por quê.'},end('Comente a sua ^letra^','Curta, salve e siga para ver a resposta.')],cap)
def lst(slug,k,title,items,cap,tail_t,tail_b,cta=None,tags=HT):
    return J(slug,[{'k':k,'t':title,'b':''},{'l':'list','k':'Passo a passo','t':'Veja *como*','items':[{'a':str(i+1),'t':x} for i,x in enumerate(items)]},end(tail_t,tail_b,cta)],cap,tags)

# ===== SEG 12/10 =====
d='seg-12-10'
add(d,'0800',J('novidade-mercado-livre-live',[
 {'k':'Novidade: Mercado Livre','t':'Mercado Livre lança ^Live^ dentro do app','b':'Dá para comprar o produto durante a transmissão, sem sair da plataforma'},
 {'k':'O que mudou','t':'Vendedores, afiliados e criadores *podem usar*','b':'O acesso está sendo liberado aos poucos. O Brasil é o primeiro país; outros da América Latina vêm depois.','src':SF},
 {'k':'Resultados nos testes','t':'*Beleza* e *casa e decoração* se destacaram','b':'Tecnologia, autopeças e alimentos e bebidas também tiveram casos de sucesso.','src':SF},
 {'k':'Para você','t':'Live deixou de ser coisa de *uma* plataforma','b':'Quem aprende a vender ao vivo leva a habilidade para TikTok Shop, Shopee, Instagram e agora Mercado Livre.'},
 end('Quer aprender a ^vender em live^?','Comente a palavra abaixo e eu te chamo no direct.','LIVE')],
 'O Mercado Livre começou a liberar o Mercado Livre Live no Brasil, com compra durante a transmissão. Beleza e casa e decoração foram os destaques nos testes. Fonte: Exame (31/08/2026). Comente LIVE.'))
add(d,'1100',J('live-pos-dia-das-criancas',[
 {'k':'Hoje é Dia das Crianças','t':'A data é hoje, mas a ^venda^ continua','b':'Como aproveitar o pós-data na sua live'},
 {'l':'list','k':'Faça hoje','t':'O que *vender* agora','items':[{'a':'1','t':'Ofertas finais dos produtos de data'},{'a':'2','t':'Kits com preço fechado'},{'a':'3','t':'Presentes para as próximas datas'}]},
 {'k':'Olhe adiante','t':'A próxima grande data é a *Black Friday*','b':'Em 27 de novembro. Use as próximas semanas para criar hábito de live e juntar público.','src':SH},
 end('Salve para ^planejar^','E me conta o que você vai vender nesta semana.')],
 'Hoje é Dia das Crianças, mas a venda continua. Veja o que fazer na sua live e como se preparar para a Black Friday (27/11). Fonte: Central do Varejo.'))
add(d,'1400',J('ia-roteiro-de-live-em-5-minutos',[
 {'k':'IA para vendedor','t':'Roteiro de live em ^5 minutos^ com IA','b':'Sem página em branco'},
 {'k':'Passo 1','t':'Conte o *contexto*','b':'Diga a categoria, o produto, o preço e o público. Quanto mais específico, melhor o roteiro.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Crie um roteiro de live de 30 minutos para vender este produto, com abertura, 3 demonstrações, 2 chamadas para ação e encerramento.'},
 {'k':'Passo 3','t':'Ajuste e *ensaie*','b':'Leia em voz alta, corte o que soar robótico e deixe só os tópicos. Na live, converse; não leia.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como criar um roteiro de live em 5 minutos com IA, em 3 passos. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-onde-vender','Onde você vende ou quer vender?',['TikTok Shop','Shopee','Instagram','Mercado Livre'],'Enquete: onde você vende ou quer vender? Comente a letra: A TikTok Shop, B Shopee, C Instagram ou D Mercado Livre.'))
add(d,'2100',J('minha-regra-da-constancia',[
 {'k':'Para começar a semana','t':'^Constância^ vence talento','b':'O que eu repito para os alunos'},
 {'k':'A regra','t':'*Um* horário. *Uma* melhoria.','badge':'+20 MIL|ALUNOS','b':'Escolha um horário fixo para a live e melhore uma coisa por semana: luz, áudio, oferta ou abertura.'},
 {'k':'Por que funciona','t':'Seu público *aprende* a te encontrar','b':'Quem aparece sempre no mesmo horário cria hábito em quem acompanha.'},
 end('Comente ^EU VOU^','Se você vai fazer uma live esta semana.')],
 'A regra da constância: um horário fixo e uma melhoria por semana. Comente EU VOU se você vai fazer uma live esta semana.'))

# ===== TER 13/10 =====
d='ter-13-10'
add(d,'0800',J('novidade-mercado-livre-estudio-live',[
 {'k':'Novidade: Mercado Livre','t':'Mercado Livre abre ^estúdio de live^ em São Paulo','b':'Espaço para criadores, vendedores e afiliados'},
 {'l':'list','k':'O que tem lá','t':'Os *números* do estúdio','items':[{'a':'193 m²','t':'De área, na Vila Leopoldina'},{'a':'9','t':'Espaços independentes para transmissão'},{'a':'Grátis','t':'Equipamentos: luz, tripé, celular e internet'}],'src':SG},
 {'k':'Quem pode usar','t':'Por enquanto, uma *lista selecionada*','b':'A empresa planeja abrir a agenda a todos os parceiros depois.','src':SG},
 {'k':'Para você','t':'Você *não precisa* de estúdio para começar','b':'Luz de janela, celular na vertical e um fundo limpo já fazem uma live profissional.'},
 end('Quer o ^kit de cenário^ barato?','Comente a palavra abaixo e eu te chamo no direct.','CENARIO')],
 'O Mercado Livre abriu um estúdio de live commerce em São Paulo, com 193 m², 9 espaços e equipamentos gratuitos. Fonte: Mercado&Consumo (09/09/2026). Comente CENARIO.'))
add(d,'1100',lst('live-estrutura-de-30-minutos','Passo a passo de live','Estrutura de uma live de ^30 minutos^',['0-5 min: abertura, gancho e o que vai acontecer','5-20 min: demonstração de 3 produtos','20-27 min: oferta com prazo','27-30 min: recap e convite para a próxima live'],'Estrutura simples para uma live de 30 minutos. Salve e use na próxima.','Salve e ^teste hoje^','E me conta como foi.'))
add(d,'1400',J('ia-descricao-de-produto',[
 {'k':'IA para vendedor','t':'Descrição de produto que ^vende^','b':'Com IA, sem texto genérico'},
 {'k':'Passo 1','t':'Liste *características*','b':'Material, tamanho, uso, diferenciais e garantia. Sem enfeite.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Escreva uma descrição para marketplace com título, 5 benefícios em tópicos e uma pergunta frequente. Tom direto e sem exagero.'},
 {'k':'Passo 3','t':'Confira os *fatos*','b':'Revise medidas, material e prazos. A IA ajuda a escrever; quem responde pelo produto é você.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como usar IA para escrever descrições de produto para marketplace, com revisão dos fatos. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-live-ou-video','Você prefere vender por live ou por vídeo?',['Live','Vídeo curto','Os dois','Ainda não sei'],'Enquete: live ou vídeo curto? Comente a letra: A live, B vídeo curto, C os dois ou D ainda não sei.'))
add(d,'2100',J('o-que-eu-faria-hoje',[
 {'k':'Se eu estivesse começando','t':'O que eu faria ^hoje^','b':'Em 4 passos'},
 {'l':'list','k':'Do zero','t':'Faça nesta *ordem*','items':[{'a':'1','t':'Escolha uma categoria'},{'a':'2','t':'Escolha 5 produtos'},{'a':'3','t':'Faça uma live curta'},{'a':'4','t':'Repita no mesmo horário'}]},
 {'k':'Importante','t':'Comece *pequeno*','badge':'+20 MIL|ALUNOS','b':'O primeiro mês é de aprendizado. Observe o que o público pergunta e melhore a cada live.'},
 end('Quer o ^plano completo^?','Comente a palavra abaixo e eu te chamo no direct.','COMECAR')],
 'O que eu faria hoje se estivesse começando a vender online, em 4 passos. Comente COMECAR.'))

# ===== QUA 14/10 =====
d='qua-14-10'
add(d,'0800',J('novidade-black-friday-27-de-novembro',[
 {'k':'Calendário 2026','t':'Black Friday cai em ^27/11^','b':'E a Cyber Monday em 30/11'},
 {'l':'list','k':'Datas','t':'Marque no *calendário*','items':[{'a':'27/11','t':'Black Friday'},{'a':'30/11','t':'Cyber Monday'},{'a':'27/10','t':'TikTok Shop começa as ofertas da campanha'}],'src':'Fontes: Central do Varejo e Agência Estado'},
 {'k':'Preparação','t':'Planeje com *60 dias*','b':'A Linx Commerce recomenda começar com cerca de 60 dias de antecedência: estoque, fornecedores e metas.','src':SH},
 {'k':'Para você','t':'Se não começou, *comece agora*','b':'Defina produtos de oferta, margem mínima e prazo de entrega antes da data.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'Black Friday 2026 cai em 27/11 e a Cyber Monday em 30/11. Veja como se preparar. Fonte: Central do Varejo (11/08/2026). Comente BLACK.'))
add(d,'1100',J('live-31-por-cento-ja-compraram',[
 {'k':'Dado','t':'^31%^ dos consumidores já compraram em live','b':'Segundo pesquisa CNDL/SPC com Offerwise'},
 {'k':'O que isso diz','t':'Quase *1 em cada 3* brasileiros','b':'A live já é canal de compra para boa parte do público, e a tendência é crescer.','src':SF},
 {'k':'O que fazer','t':'Entre *antes* da maioria','b':'Quem constrói audiência agora chega na Black Friday com público e prova social.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 '31% dos consumidores brasileiros já compraram em live, segundo pesquisa CNDL/SPC com Offerwise citada pela Exame (31/08/2026).'))
add(d,'1400',J('ia-responder-cliente',[
 {'k':'IA para vendedor','t':'Responda clientes ^mais rápido^','b':'Sem perder o tom humano'},
 {'k':'Passo 1','t':'Junte as *dúvidas*','b':'Liste as 10 perguntas que mais chegam: prazo, tamanho, troca, pagamento.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Escreva respostas curtas, educadas e claras para estas 10 perguntas, no tom de uma loja amiga.'},
 {'k':'Passo 3','t':'Personalize *sempre*','b':'Use as respostas como base e acrescente o nome do cliente e o detalhe do pedido.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como usar IA para responder clientes mais rápido mantendo o tom humano. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-maior-duvida','Qual é a sua maior dúvida sobre vender online?',['Escolher produto','Como fazer live','Como usar IA','Como ter clientes'],'Enquete: qual é a sua maior dúvida? Comente a letra: A escolher produto, B como fazer live, C como usar IA ou D como ter clientes.'))
add(d,'2100',J('3-habitos-de-quem-vende',[
 {'k':'Para refletir','t':'3 hábitos de quem ^vende todo mês^','b':'O que eu observo nos alunos'},
 {'l':'list','k':'Hábitos','t':'Simples e *repetidos*','items':[{'a':'1','t':'Aparece todo dia, mesmo sem vontade'},{'a':'2','t':'Mede o que funcionou'},{'a':'3','t':'Aprende com cada venda perdida'}]},
 {'k':'Resumo','t':'Resultado é *rotina*','badge':'+20 MIL|ALUNOS','b':'Quem trata a venda como rotina melhora mais rápido do que quem espera motivação.'},
 end('Qual hábito ^você precisa^?','Comente o número.')],
 'Três hábitos de quem vende todo mês. Comente o número do hábito que você precisa melhorar.'))

# ===== QUI 15/10 =====
d='qui-15-10'
add(d,'0800',J('novidade-black-friday-2025-4-76-bi',[
 {'k':'Para ter como referência','t':'Black Friday 2025 faturou ^R$ 4,76 bi^','b':'Alta de 11,2% sobre 2024'},
 {'l':'list','k':'Números de 2025','t':'O que *aconteceu*','items':[{'a':'4,76 bi','t':'Faturamento do dia (Confi Neotrust)'},{'a':'+11,2%','t':'Sobre a Black Friday de 2024'},{'a':'10 bi+','t':'De sexta a segunda'}],'src':SH},
 {'k':'Para 2026','t':'Use como *meta de comparação*','b':'Olhe seu resultado do ano passado, defina uma meta realista e ajuste produtos e estoque.'},
 end('Quer a ^planilha de meta^?','Comente a palavra abaixo e eu te chamo no direct.','META')],
 'A Black Friday 2025 faturou R$ 4,76 bi, alta de 11,2%, segundo a Confi Neotrust. Fonte: Central do Varejo (11/08/2026). Comente META.'))
add(d,'1100',lst('live-como-fechar-venda','Passo a passo de live','Como ^fechar a venda^ ao vivo',['Mostre o produto funcionando','Diga o preço e o que acompanha','Responda a objeção mais comum','Dê um prazo claro para a oferta','Mostre onde clicar para comprar'],'Cinco passos para fechar venda durante a live. Salve e use na próxima.','Salve para usar na ^próxima live^','E me conta se funcionou.'))
add(d,'1400',J('ia-10-nomes-de-oferta',[
 {'k':'IA para vendedor','t':'10 nomes de ^oferta^ em 1 minuto','b':'Para live e anúncio'},
 {'k':'Passo 1','t':'Conte a *oferta*','b':'Diga o produto, o desconto e o prazo.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Crie 10 nomes curtos para esta oferta, sem exagero e sem prometer o que não existe.'},
 {'k':'Passo 3','t':'Teste *dois*','b':'Escolha dois nomes, use em dias diferentes e veja qual gera mais cliques e comentários.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como criar 10 nomes de oferta em 1 minuto com IA. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('quiz-tempo-de-live','Quanto tempo deve durar uma live?',['15 minutos','30 minutos','1 hora','Depende'],'Quiz: quanto tempo deve durar uma live? Comente a letra e eu respondo no próximo post.'))
add(d,'2100',J('quem-eu-ajudo',[
 {'k':'Quem eu ajudo','t':'Quem quer vender com ^live^','b':'E está começando do zero'},
 {'k':'Para quem é','t':'*Iniciantes* e quem já vende','badge':'+20 MIL|ALUNOS','b':'Quem quer renda digital com TikTok Shop, Shopee, Instagram Shop e IA.'},
 {'k':'Como funciona','t':'Método, *prática* e rotina','b':'Passo a passo para escolher produto, fazer live e criar conteúdo com ajuda da IA.'},
 end('Quer falar ^comigo^?','Comente a palavra abaixo e eu te chamo no direct.','QUERO')],
 'Quem eu ajudo: quem quer vender com live e está começando. Comente QUERO e eu te chamo.'))

# ===== SEX 16/10 =====
d='sex-16-10'
add(d,'0800',J('novidade-tiktok-logistica-111-milhoes',[
 {'k':'Novidade: TikTok Shop','t':'TikTok cria empresa de logística com ^R$ 111 mi^ de capital','b':'TikTok Logistics Brazil Ltda.'},
 {'k':'O que é','t':'Apoio à operação do *TikTok Shop*','b':'A empresa cuida de transporte, custos e prazos. Os termos oficiais de logística já valem desde fevereiro de 2026.','src':SI},
 {'k':'Atenção','t':'Isso *não* significa frota própria','b':'O modelo atual ainda usa transportadoras parceiras. Não há troca imediata.','src':SI},
 {'k':'Para você','t':'Cuide do *prazo* e da embalagem','b':'Postar rápido e embalar bem reduz atraso e reclamação.'},
 end('Quer o ^checklist^ de envio?','Comente a palavra abaixo e eu te chamo no direct.','ENVIO')],
 'O TikTok criou a TikTok Logistics Brazil Ltda., com R$ 111 milhões de capital, para apoiar o TikTok Shop. Fonte: JCN News (24/08/2026). Comente ENVIO.'))
add(d,'1100',J('live-3-ofertas-por-live',[
 {'k':'Estratégia de live','t':'Quantas ofertas ^por live^?','b':'Poucas e bem explicadas'},
 {'l':'list','k':'Sugestão','t':'Para *começar*','items':[{'a':'1','t':'Uma oferta principal'},{'a':'2','t':'Uma oferta de apoio'},{'a':'3','t':'Uma oferta relâmpago no final'}]},
 {'k':'Por quê','t':'Menos opções, *mais decisão*','b':'Muita oferta confunde. O público precisa entender o que comprar agora.'},
 end('Salve para ^testar^','E me conta o resultado.')],
 'Quantas ofertas colocar por live? Comece com uma principal, uma de apoio e uma relâmpago. Salve e teste.'))
add(d,'1400',J('ia-calendario-de-conteudo',[
 {'k':'IA para vendedor','t':'Calendário de conteúdo em ^5 minutos^','b':'Para a semana inteira'},
 {'k':'Passo 1','t':'Defina o *nicho*','b':'Diga o que vende, para quem e quantos posts quer por dia.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Monte um calendário de 7 dias com ideias de post, live e story para este nicho, variando entre educar, provar e vender.'},
 {'k':'Passo 3','t':'Escolha o *essencial*','b':'Não faça tudo. Selecione o que cabe na sua rotina e cumpra.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como montar um calendário de conteúdo de 7 dias com IA. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-quando-assiste','Qual é o melhor horário para você assistir live?',['Manhã','Tarde','Noite','Madrugada'],'Enquete: qual é o melhor horário para você assistir live? Comente a letra.'))
add(d,'2100',J('mito-precisa-aparecer',[
 {'k':'Mito','t':'"Preciso ^aparecer^ para vender"','b':'Nem sempre'},
 {'k':'Realidade','t':'Dá para vender *mostrando o produto*','b':'Muitas lives focam mãos, produto e demonstração. O importante é ser claro e útil.'},
 {'k':'Mas','t':'Rosto *ajuda* na confiança','b':'Com o tempo, aparecer pode aumentar a conexão. Comece no seu ritmo.'},
 end('Qual é a sua ^dúvida^?','Comente abaixo.')],
 'Mito: preciso aparecer para vender. Dá para começar mostrando o produto, e aparecer ajuda na confiança com o tempo.'))

# ===== SAB 17/10 =====
d='sab-17-10'
add(d,'0800',J('novidade-tiktok-envio-pela-plataforma',[
 {'k':'Entenda: TikTok Shop','t':'Quem escolhe a ^transportadora^?','b':'No TikTok Shop, não é o vendedor'},
 {'l':'list','k':'Como funciona','t':'*Envio pela plataforma*','items':[{'a':'Padrão','t':'É o modelo de envio principal'},{'a':'Parceiras','t':'Transportadoras como J&T, Correios e iMile'},{'a':'Sem escolha','t':'A plataforma atribui a transportadora'}],'src':SI},
 {'k':'Para você','t':'Foque no que *controla*','b':'Prazo de postagem, embalagem e descrição correta do produto.'},
 end('Quer o ^checklist^ de envio?','Comente a palavra abaixo e eu te chamo no direct.','ENVIO')],
 'No TikTok Shop o modelo padrão é o envio pela plataforma, e o vendedor não escolhe a transportadora livremente. Fonte: JCN News (24/08/2026). Comente ENVIO.'))
add(d,'1100',lst('live-cenario-de-1-real','Passo a passo de live','Cenário de live com ^pouco dinheiro^',['Luz de janela ou uma luz branca','Celular na vertical, firme no tripé','Fundo limpo e organizado','Áudio limpo, sem eco','Produto bem iluminado'],'Cinco itens para montar um cenário de live gastando pouco. Salve.','Salve para ^montar o seu^','E me conta como ficou.'))
add(d,'1400',J('ia-ideias-de-conteudo',[
 {'k':'IA para vendedor','t':'30 ideias de ^conteúdo^ em um prompt','b':'Para nunca ficar sem pauta'},
 {'k':'Passo 1','t':'Diga o *nicho*','b':'Produto, público e objetivo.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Liste 30 ideias de conteúdo para este nicho, separando em dúvidas, bastidores, demonstrações e provas.'},
 {'k':'Passo 3','t':'Grave em *lote*','b':'Escolha 5 ideias e grave tudo no mesmo dia para ganhar tempo.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como gerar 30 ideias de conteúdo com um prompt de IA. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-maior-meta','Qual é a sua meta para a Black Friday?',['Primeira venda','Vender todo dia','Bater recorde','Montar loja'],'Enquete: sua meta para a Black Friday? Comente a letra.'))
add(d,'2100',J('se-eu-pudesse-voltar',[
 {'k':'Reflexão','t':'O que eu diria a quem está ^começando^','b':'Cinco palavras'},
 {'k':'A mensagem','t':'*Comece.* Ajuste. Repita.','badge':'+20 MIL|ALUNOS','b':'Quem espera o momento perfeito demora mais. Quem começa aprende com o mercado.'},
 {'k':'Hoje','t':'Qual será o seu *primeiro passo*?','b':'Escolha um produto, uma live ou um post.'},
 end('Comente ^COMECEI^','Se você deu o primeiro passo.')],
 'Comece, ajuste e repita. Comente COMECEI se você deu o primeiro passo hoje.'))

# ===== DOM 18/10 =====
d='dom-18-10'
add(d,'0800',J('novidade-ecommerce-2026-259-bi',[
 {'k':'Projeção do ano','t':'E-commerce deve chegar a ^R$ 259,8 bi^ em 2026','b':'Projeção da Abiacom'},
 {'l':'list','k':'Números','t':'O que *se espera*','items':[{'a':'259,8 bi','t':'Faturamento projetado'},{'a':'R$ 562,15','t':'Ticket médio'},{'a':'460,87 mi','t':'De pedidos'}],'src':SH},
 {'k':'Outra projeção','t':'ABComm vê *mais de R$ 258 bi*','b':'Com ticket de R$ 564,96 e 2 milhões de novos compradores.','src':SH},
 {'k':'Para você','t':'O mercado *está crescendo*','b':'Há espaço para novos vendedores que cuidam de produto, atendimento e prazo.'},
 end('Quer entrar nesse ^mercado^?','Comente a palavra abaixo e eu te chamo no direct.','QUERO')],
 'A Abiacom projeta R$ 259,8 bi para o e-commerce brasileiro em 2026, com ticket de R$ 562,15 e 460,87 milhões de pedidos. Fonte: Central do Varejo (11/08/2026). Comente QUERO.'))
add(d,'1100',lst('live-resumo-do-que-medir','Passo a passo de live','4 números para ^medir^ após cada live',['Tempo médio de permanência','Comentários por minuto','Cliques no produto','Pedidos gerados'],'Quatro números para medir depois de cada live. Salve.','Salve e ^meça^ hoje','E me conta o que descobriu.'))
add(d,'1400',J('ia-resumo-de-reclamacoes',[
 {'k':'IA para vendedor','t':'Transforme avaliações em ^melhorias^','b':'Peça um resumo à IA'},
 {'k':'Passo 1','t':'Copie as *avaliações*','b':'Junte avaliações positivas e negativas dos últimos 30 dias.'},
 {'k':'Passo 2','t':'Use este *prompt*','b':'Resuma os 5 principais elogios e as 5 principais queixas e sugira uma melhoria para cada queixa.'},
 {'k':'Passo 3','t':'Aja em *uma*','b':'Corrija a queixa mais comum primeiro, como embalagem, descrição ou prazo.'},
 end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 'Como usar IA para resumir avaliações e transformar queixas em melhorias. Comente PROMPT.',HT+' #ia'))
add(d,'1900',enq('enquete-categoria-semana','Qual categoria você mais quer ver aqui?',['Moda','Beleza','Casa','Eletrônicos'],'Enquete: qual categoria você mais quer ver aqui? Comente a letra.'))
add(d,'2100',J('resumo-da-semana-2',[
 {'k':'Resumo da semana','t':'^5 novidades^ para não perder','b':'Do que saiu de 12 a 18 de outubro'},
 {'l':'list','k':'Salve este resumo','t':'O que *mudou*','items':[{'a':'ML','t':'Mercado Livre lança Live no app'},{'a':'193 m²','t':'Estúdio de live commerce em São Paulo'},{'a':'27/11','t':'Black Friday 2026'},{'a':'111 mi','t':'Capital da TikTok Logistics Brazil'},{'a':'259,8 bi','t':'Projeção do e-commerce em 2026'}],'src':'Fontes: Exame, Mercado&Consumo, Central do Varejo, JCN News'},
 {'k':'Próxima semana','t':'Eu trago *mais* novidades','b':'Siga para acompanhar TikTok Shop, Shopee, Instagram Shop e IA.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: 5 novidades de vendas online, live e marketplaces. Salve e envie para um amigo.'))

for n,j in enumerate(jobs,1):j['n']=n
json.dump(jobs,open('jobs35b.json','w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
