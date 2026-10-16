import json,sys
HT='#tiktokshop #shopee #instagramshop #livesell #vendasonline #empreendedorismo'
def J(slug,slides,cap,tags=HT):return {'slug':slug,'slides':slides,'cap':cap+'\n\nCurta, salve e siga @{H} para mais conteúdo de TikTok Shop, Shopee, Instagram Shop e IA.\n\n'+tags}
def end(t,b,cta=None):
    d={'t':t,'b':b,'follow':True}
    if cta:d['cta']=cta
    return d
jobs=[]
def add(day,slot,j):
    j['d']=day;j['slot']=slot;jobs.append(j)
def enq(slug,q,opts,cap):
    return J(slug,[{'k':'Enquete','t':q,'b':'Comente a letra'},{'l':'enquete','k':'Escolha','t':'Qual é a *sua*?','b':'\n'.join(opts)},{'k':'Próximo post','t':'Eu respondo a *mais votada*','b':'Conte nos comentários qual é a sua letra e por quê.'},end('Comente a sua ^letra^','Curta, salve e siga para ver a resposta.')],cap)
def quiz(slug,q,opts,rt,rb,cap):
    return J(slug,[{'k':'Quiz','t':q,'b':'Comente a letra'},{'l':'enquete','k':'Alternativas','t':'Qual é a *certa*?','b':'\n'.join(opts)},{'k':'Resposta','t':rt,'b':rb},end('Você ^acertou^?','Conte nos comentários.')],cap)
def live(slug,title,items,tk,tt,tb,cap,endt,endb):
    return J(slug,[{'k':'Passo a passo de live','t':title,'b':''},{'l':'list','k':'Passo a passo','t':'Veja *como*','items':[{'a':str(i+1),'t':x} for i,x in enumerate(items)]},{'k':tk,'t':tt,'b':tb},end(endt,endb)],cap)
def ia(slug,title,sub,p1t,p1b,prompt,p3t,p3b,cap):
    return J(slug,[{'k':'IA para vendedor','t':title,'b':sub},{'k':'Passo 1','t':p1t,'b':p1b},{'k':'Passo 2','t':'Use este *prompt*','b':prompt},{'k':'Passo 3','t':p3t,'b':p3b},end('Quer mais ^prompts^ prontos?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],cap+' Comente PROMPT.',HT+' #ia')
def lst3(slug,k,title,items,tk,tt,tb,cap,endt,endb,cta=None,b0=''):
    return J(slug,[{'k':k,'t':title,'b':b0},{'l':'list','k':'Faça assim','t':'Em *três* passos','items':[{'a':str(i+1),'t':x} for i,x in enumerate(items)]},{'k':tk,'t':tt,'b':tb},end(endt,endb,cta)],cap)

# ===== QUI 05/11 =====
d='qui-05-11'
SB='Fonte: Giro News (14/10/2026), projeção Confi/Neotrust'
add(d,'0800',J('novidade-black-friday-13-bi',[
 {'k':'Projeção Black Friday 2026','t':'Black Friday deve movimentar ^R$ 13,3 bi^','b':'Projeção para o e-commerce brasileiro'},
 {'l':'list','k':'Os números','t':'O que a *projeção* diz','items':[{'a':'13,3 bi','t':'Faturamento projetado'},{'a':'+20,7%','t':'Sobre os 4 dias de 2025'},{'a':'69,4 mi','t':'Produtos vendidos'}],'src':SB},
 {'k':'Período','t':'A conta vale para *26 a 29/11*','b':'São quatro dias de evento. A Black Friday em si cai em 27 de novembro.','src':SB},
 {'k':'Para você','t':'Projeção *não é garantia*','b':'Use como referência. Ajuste estoque, preço e live ao que você consegue entregar.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'A Black Friday 2026 deve movimentar R$ 13,3 bilhões no e-commerce brasileiro, segundo projeção da Confi/Neotrust (26 a 29/11). É uma projeção. Fonte: Giro News (14/10/2026). Comente BLACK.'))
add(d,'1100',live('live-checagem-tecnica-5-minutos','Checagem de ^5 minutos^ antes da live',['Bateria carregada e celular no carregador','Internet testada no local da live','Luz de frente, sem janela atrás de você','Áudio testado com uma gravação curta','Produtos em ordem e ao alcance da mão'],'Dica','Teste *antes* de ligar','Dois minutos de teste evitam interrupção no meio da oferta.','Cinco itens para checar antes de abrir a live. Salve e use na próxima.','Salve para ^usar hoje^','E me conta se ajudou.'))
add(d,'1400',ia('ia-video-de-15-segundos','Roteiro de vídeo de ^15 segundos^','Com IA, em 3 passos','Diga o *produto*','Informe o que é, para quem serve e o principal benefício.','Escreva um roteiro de 15 segundos com gancho, demonstração e chamada para ação para este produto.','Grave e *corte*','Grave em partes curtas e corte as pausas. A IA ajuda no texto; a demonstração é sua.','Como criar um roteiro de vídeo de 15 segundos com IA.'))
add(d,'1900',enq('enquete-o-que-faz-comprar-em-live','O que faz você comprar numa live?',['Ver o produto funcionando','Preço especial','Confiança no vendedor','Tirar dúvidas ao vivo'],'Enquete: o que faz você comprar numa live? Comente a letra: A ver o produto funcionando, B preço especial, C confiança no vendedor ou D tirar dúvidas ao vivo.'))
add(d,'2100',J('uma-plataforma-de-cada-vez',[
 {'k':'Foco','t':'Uma plataforma de ^cada vez^','b':'Para quem está começando'},
 {'k':'O erro comum','t':'Abrir *quatro* lojas ao mesmo tempo','b':'Dividir a energia em tudo faz você aprender pouco em cada canal.'},
 {'k':'A alternativa','t':'Escolha uma e dê *30 dias*','b':'Aprenda as regras, o público e os números. Depois expanda com calma.'},
 end('Qual você ^escolhe^?','Conte nos comentários: TikTok Shop, Shopee, Instagram ou Mercado Livre.')],
 'Uma plataforma de cada vez: escolha uma e dê 30 dias para aprender antes de expandir. Qual você escolhe?'))

# ===== SEX 06/11 =====
d='sex-06-11'
SM='Fonte: Mercado&Consumo (15/10/2026)'
add(d,'0800',J('novidade-magalu-na-shopee',[
 {'k':'Novidade: Shopee','t':'Magalu leva ^Magazine Luiza e KaBuM!^ para a Shopee','b':'Vendas de estoque próprio nas Lojas Oficiais'},
 {'l':'list','k':'O que muda','t':'Começou em *15/10*','items':[{'a':'Magalu','t':'Eletrônicos, móveis e eletrodomésticos'},{'a':'KaBuM!','t':'Games e hardware'},{'a':'Magalog','t':'Faz a entrega'}],'src':SM},
 {'k':'Contexto','t':'Marcas grandes na *mesma vitrine*','b':'Segundo a matéria, a Shopee tem cerca de 90 milhões de brasileiros acessando por mês.','src':SM},
 {'k':'Para você','t':'A concorrência *sobe*','b':'Quem vende na Shopee precisa cuidar de título, foto, prazo e atendimento para se destacar.'},
 end('Quer aprender a ^vender na Shopee^?','Comente a palavra abaixo e eu te chamo no direct.','SHOPEE')],
 'Magazine Luiza e KaBuM!, do Magalu, passaram a vender produtos de estoque próprio nas Lojas Oficiais da Shopee desde 15/10. Fonte: Mercado&Consumo (15/10/2026). Comente SHOPEE.'))
add(d,'1100',live('live-avisar-o-publico','Como ^avisar o público^ da live',['Poste o aviso 24 horas antes, com dia e horário','Faça um story de lembrete no dia','Conte o que vai acontecer e qual é a oferta','Abra a live no horário combinado'],'Importante','Cumpra o *horário*','Quem confia no horário volta nas próximas lives.','Quatro passos para avisar o público da sua live. Salve.','Salve para ^a próxima live^','E me conta o horário que você escolheu.'))
add(d,'1400',ia('ia-ideias-de-presente-de-natal','Ideias de presente por ^faixa de preço^','Para o Natal','Diga o *público*','Por exemplo: mães, casais, crianças ou colegas de trabalho.','Sugira 10 ideias de presente de Natal por faixa de preço para este público, com um motivo para cada.','Valide a *demanda*','Antes de escolher o produto, confira se há procura e se a margem fecha depois de taxas e frete.','Como pedir à IA ideias de presente de Natal por faixa de preço.'))
add(d,'1900',quiz('quiz-o-que-e-gmv','O que significa GMV?',['Lucro líquido da loja','Volume total de vendas','Número de seguidores','Taxa cobrada pela plataforma'],'GMV é o *volume total vendido*','Em geral, é o valor das vendas antes de descontar taxas, devoluções e custos. Não é lucro.','Quiz: o que significa GMV? Comente a letra: A lucro líquido, B volume total de vendas, C número de seguidores ou D taxa da plataforma. Resposta no último slide.'))
add(d,'2100',lst3('tres-perguntas-para-revisar-a-semana','Fim de semana','3 perguntas para ^revisar a semana^',['O que funcionou e vale repetir?','O que vou parar de fazer?','Qual melhoria entra na semana que vem?'],'Resumo','Revisar é *aprender*','Cinco minutos de revisão por semana mostram o que ajustar.','Três perguntas para revisar a sua semana de vendas. Salve e responda hoje.','Qual é a sua ^resposta^?','Conte nos comentários.'))

# ===== SAB 07/11 =====
d='sab-07-11'
SC='Fonte: Mercado&Consumo (11/10/2026)'
add(d,'0800',J('novidade-black-dos-correios',[
 {'k':'Novidade: envios','t':'Correios dão desconto de ^15% a 35%^ na Black Friday','b':'Para clientes com contrato'},
 {'l':'list','k':'Como funciona','t':'O que a *campanha* traz','items':[{'a':'15-35%','t':'De desconto, conforme o volume postado'},{'a':'Contrato','t':'Planos Platinum e Diamante'},{'a':'App','t':'Sem contrato, condições pelo App Correios'}],'src':SC},
 {'k':'Capacidade','t':'Nova *máquina de triagem* em Guarulhos','b':'Deve operar por completo em novembro e processar até 520 mil itens em 20 horas.','src':SC},
 {'k':'Para você','t':'Frete *entra na conta*','b':'Antes de montar a oferta, calcule frete e prazo para não perder margem na Black Friday.'},
 end('Quer a ^conta de margem^?','Comente a palavra abaixo e eu te chamo no direct.','MARGEM')],
 'Os Correios lançaram o Black dos Correios 2026, com descontos de 15% a 35% para clientes com contrato (planos Platinum e Diamante). Fonte: Mercado&Consumo (11/10/2026). Comente MARGEM.'))
add(d,'1100',live('live-ritmo-da-fala','Ritmo da fala na ^live^',['Fale mais devagar do que no dia a dia','Faça uma pausa após cada informação importante','Repita o preço e o benefício principal','Use frases curtas e diretas'],'Por quê','Quem entra no meio *precisa entender rápido*','Repetir com calma ajuda quem chegou agora a acompanhar a oferta.','Quatro dicas de ritmo de fala para a sua live. Salve e treine.','Salve para ^treinar^','E me conta qual dica você vai testar.'))
add(d,'1400',ia('ia-reaproveitar-conteudo','Um conteúdo, ^três formatos^','Reaproveite com IA','Escolha o *conteúdo*','Pode ser o roteiro de uma live ou um texto que já funcionou.','Transforme este roteiro em um carrossel de 5 slides, um roteiro de story e três legendas curtas.','Ajuste à *sua voz*','Troque palavras que você não usaria e revise os fatos antes de publicar.','Como reaproveitar um conteúdo em três formatos com IA.'))
add(d,'1900',J('mito-so-vende-quem-tem-produto-proprio',[
 {'k':'Mito','t':'"Só vende quem tem ^produto próprio^"','b':'Nem sempre'},
 {'k':'Realidade','t':'Existem *programas de afiliados*','b':'Plataformas como TikTok Shop e Shopee têm programas em que o afiliado divulga produtos de terceiros. As regras mudam, então confira no programa.'},
 {'k':'Mas','t':'Afiliado também precisa de *público*','b':'Conteúdo útil, constância e confiança continuam sendo a base.'},
 end('Qual é a sua ^dúvida^?','Comente abaixo.')],
 'Mito: só vende quem tem produto próprio. Existem programas de afiliados em plataformas como TikTok Shop e Shopee; confira as regras de cada um.'))
add(d,'2100',lst3('como-lidar-com-semana-fraca','Para refletir','Semana fraca de vendas? ^Calma^',['Revise a oferta e o preço','Veja quais perguntas o público fez','Faça uma pequena mudança e repita'],'Lembre','Uma semana *não define* o seu negócio','Olhe a tendência de várias semanas e ajuste uma coisa por vez.','Semana fraca de vendas? Três passos para ajustar sem desanimar.','Você ^não está sozinho^','Conte nos comentários como foi a sua semana.'))

# ===== DOM 08/11 =====
d='dom-08-11'
SG='Fonte: Mercado&Consumo (14/10/2026), Global Payments'
add(d,'0800',J('novidade-uso-de-ia-nas-compras',[
 {'k':'Novidade: IA','t':'Agentes de IA nas compras: ^72%^ no Brasil','b':'Já testaram ou estão dispostos a deixar a IA comprar por eles'},
 {'l':'list','k':'Os números','t':'O que a *pesquisa* mostra','items':[{'a':'72%','t':'Já testaram ou topam usar (39% em 2025)'},{'a':'24%','t':'Já testaram'},{'a':'48%','t':'Usariam agora ou em 12 meses'}],'src':SG+', maio/2026'},
 {'k':'Receios','t':'Quem compra ainda *tem cautela*','b':'50% citam segurança dos dados de pagamento e 45% citam privacidade.','src':SG},
 {'k':'Para você','t':'Descrição clara *ajuda*','b':'Título, medidas e benefícios bem escritos facilitam a compra para o cliente e para quem pesquisa com IA.'},
 end('Quer aprender a usar ^IA^ nas vendas?','Comente a palavra abaixo e eu te chamo no direct.','PROMPT')],
 '72% dos consumidores brasileiros já testaram ou estão dispostos a permitir que agentes de IA comprem por eles (39% em 2025), segundo o Agentic Commerce Report 2026, da Global Payments, com 8.027 consumidores em 7 países. Fonte: Mercado&Consumo (14/10/2026). Comente PROMPT.',HT+' #ia'))
add(d,'1100',live('live-perguntas-para-o-publico','Perguntas que mantêm o ^chat vivo^',['Qual cor você prefere?','Você já usou esse produto antes?','Quer ver de perto? Digite SIM','Qual dúvida eu respondo agora?'],'Dica','Pergunta *simples* gera resposta','Perguntas fáceis de responder aumentam os comentários e mantêm o público.','Quatro perguntas para manter o chat da live ativo. Salve.','Salve para ^usar na live^','E me conta qual pergunta funcionou.'))
add(d,'1400',ia('ia-bio-do-instagram','Bio do Instagram que ^explica^ o que você vende','Com IA, em 3 passos','Conte *o essencial*','Diga o que você vende, para quem e qual ação quer que a pessoa faça.','Escreva 5 opções de bio de até 150 caracteres que digam o que eu vendo, para quem e como chamar para a ação.','Teste *uma semana*','Escolha uma opção e veja se aumentam as visitas e mensagens.','Como criar a bio do Instagram com ajuda da IA.'))
add(d,'1900',enq('enquete-horas-por-dia','Quanto tempo por dia você dedica a vender online?',['Menos de 1 hora','1 a 2 horas','3 a 4 horas','Mais de 4 horas'],'Enquete: quanto tempo por dia você dedica a vender online? Comente a letra: A menos de 1 hora, B 1 a 2 horas, C 3 a 4 horas ou D mais de 4 horas.'))
SR='Fontes: Giro News, Mercado&Consumo'
add(d,'2100',J('resumo-da-semana-5',[
 {'k':'Resumo da semana','t':'^4 novidades^ para não perder','b':'Do que saiu de 5 a 8 de novembro'},
 {'l':'list','k':'Salve este resumo','t':'O que *mudou*','items':[{'a':'13,3 bi','t':'Projeção da Black Friday 2026'},{'a':'Magalu','t':'Lojas oficiais na Shopee'},{'a':'15-35%','t':'Desconto dos Correios p/ contrato'},{'a':'72%','t':'Testam ou topam usar IA para comprar'}],'src':SR},
 {'k':'Próxima semana','t':'Eu trago *mais* novidades','b':'Siga para acompanhar TikTok Shop, Shopee, Instagram Shop e IA.'},
 end('Salve e ^envie^ para um amigo','Quem vende online precisa ver isso.')],
 'Resumo da semana: 4 novidades de vendas online, marketplaces e IA (Black Friday, Magalu na Shopee, Correios e IA nas compras). Salve e envie para um amigo.'))

# ===== SEG 09/11 =====
d='seg-09-11'
SS='Fonte: Mercado&Consumo (07/10/2026), dados da Shopee'
add(d,'0800',J('novidade-shopee-logistica',[
 {'k':'Novidade: Shopee','t':'Shopee amplia logística: centros vão de ^16 para 26^','b':'Segundo a empresa, em 2026'},
 {'l':'list','k':'Rede logística','t':'Os *números* da Shopee','items':[{'a':'26','t':'Centros de distribuição (eram 16)'},{'a':'5 mil+','t':'Shopee Agências'},{'a':'45 mil+','t':'Motoristas parceiros'}],'src':SS},
 {'k':'Modalidades','t':'Entrega Rápida, *Full* e Turbo','b':'No Full, o produto fica em centro da Shopee. O Turbo promete entrega em até 4 horas na Grande São Paulo.','src':SS},
 {'k':'Atenção','t':'São *dados da empresa*','b':'Prazos dependem de região e elegibilidade. Confira as regras na Central do Vendedor.'},
 end('Quer o ^checklist^ de envio?','Comente a palavra abaixo e eu te chamo no direct.','ENVIO')],
 'A Shopee diz ter ampliado seus centros de distribuição de 16 para 26 em 2026 e expandido modalidades como Entrega Rápida, Full e Turbo. Dados da empresa. Fonte: Mercado&Consumo (07/10/2026). Comente ENVIO.'))
add(d,'1100',live('live-testar-horarios','Como achar o melhor ^horário^ de live',['Teste 3 horários diferentes em 3 semanas','Mantenha o mesmo dia da semana no teste','Anote visualizações e comentários de cada live','Fique com o melhor e repita'],'Lembre','Não existe horário *mágico*','O melhor horário é o que o seu público consegue assistir.','Quatro passos para descobrir o melhor horário de live para o seu público. Salve.','Salve para ^testar^','E me conta qual horário você vai testar.'))
add(d,'1400',ia('ia-planilha-de-margem','Entenda sua ^margem^ com ajuda da IA','Sem inventar número','Pegue as *taxas reais*','Confira comissão e tarifas atuais na Central do Vendedor. Não use número de memória.','Monte uma tabela para calcular preço de venda, comissão, frete, custo e lucro por unidade. Explique cada fórmula.','Confira *a conta*','Teste com um produto real e confira o resultado à mão antes de usar.','Como usar IA para montar uma planilha de margem, usando as taxas reais da plataforma.'))
add(d,'1900',J('mito-preciso-ser-expert-em-ia',[
 {'k':'Mito','t':'"Preciso ser ^expert^ para usar IA"','b':'Não precisa'},
 {'k':'Realidade','t':'Comece com *um prompt simples*','b':'Diga o que você vende, para quem e o que quer. Depois ajuste a resposta.'},
 {'k':'Mas','t':'*Revise* sempre','b':'A IA pode errar. Confira fatos, preços e promessas antes de publicar.'},
 end('Qual é a sua ^dúvida^ sobre IA?','Comente abaixo.')],
 'Mito: preciso ser expert para usar IA. Comece com um prompt simples e revise sempre antes de publicar.',HT+' #ia'))
add(d,'2100',lst3('comecar-a-semana-com-3-metas','Segunda-feira','3 metas para ^a semana^',['Fazer uma live no mesmo horário','Publicar conteúdo em dias fixos','Revisar os números na sexta'],'Dica','Meta *pequena* se cumpre','Metas pequenas e claras ajudam a manter a constância.','Três metas simples para começar a semana. Salve e escolha as suas.','Qual meta você ^escolhe^?','Conte nos comentários.'))

# ===== TER 10/11 =====
d='ter-10-11'
SP='Fonte: Central do Varejo (08/10/2026), relatório Appmax'
add(d,'0800',J('novidade-pix-black-friday-appmax',[
 {'k':'Pagamentos','t':'Na Black Friday 2025, o ^Pix^ foi quase metade dos pedidos','b':'Dados da Appmax'},
 {'l':'list','k':'Black Friday 2025','t':'Como o cliente *pagou*','items':[{'a':'47,9%','t':'Dos pedidos foram no Pix'},{'a':'51,7%','t':'Dos pedidos foram no cartão'},{'a':'R$ 347','t':'Ticket médio no cartão (R$ 198 no Pix)'}],'src':SP},
 {'k':'Em 2026','t':'No 1º semestre, o Pix *passou o cartão*','b':'Em número de transações na Appmax: 51,4% contra 47,9%.','src':SP},
 {'k':'Atenção','t':'São dados de *uma* empresa','b':'Números da Appmax não representam o mercado todo. Use como pista, não como regra.'},
 end('Quer o ^plano^ da Black Friday?','Comente a palavra abaixo e eu te chamo no direct.','BLACK')],
 'Na Black Friday 2025, o Pix respondeu por 47,9% dos pedidos na Appmax e o cartão por 51,7%. Dados de uma plataforma de pagamentos, não do mercado todo. Fonte: Central do Varejo (08/10/2026). Comente BLACK.'))
add(d,'1100',live('live-repetir-a-oferta','Como repetir a oferta sem ^cansar^',['Repita a oferta a cada 5 a 10 minutos','Mude a forma: benefício, prova ou prazo','Mostre onde clicar para comprar','Responda uma dúvida junto da repetição'],'Por quê','Sempre entra *gente nova*','Quem chegou agora não viu o começo e precisa entender a oferta.','Quatro formas de repetir a oferta na live sem cansar o público. Salve.','Salve para ^a próxima live^','E me conta o que você vai testar.'))
add(d,'1400',ia('ia-perguntas-para-enquete','Enquetes e perguntas com ^IA^','Para falar com o público','Diga o *nicho*','Conte o que você vende e quem acompanha você.','Crie 10 perguntas curtas de enquete para eu fazer nos stories, sobre este nicho.','Use as *respostas*','Veja o que mais aparece e transforme em conteúdo ou em oferta.','Como criar perguntas de enquete para os stories com IA.'))
add(d,'1900',enq('enquete-meta-de-natal','Qual é a sua meta para o Natal?',['Primeira venda','Dobrar as vendas','Montar uma loja nova','Fazer live toda semana'],'Enquete: qual é a sua meta para o Natal? Comente a letra: A primeira venda, B dobrar as vendas, C montar uma loja nova ou D fazer live toda semana.'))
add(d,'2100',J('checklist-da-vespera-do-11-11',[
 {'k':'Véspera do 11.11','t':'Checklist ^rápido^ para amanhã','b':'Quatro itens'},
 {'l':'list','k':'Confira hoje','t':'Antes de *dormir*','items':[{'a':'1','t':'Produtos e estoque conferidos'},{'a':'2','t':'Preço e margem calculados'},{'a':'3','t':'Live agendada e avisada'},{'a':'4','t':'Respostas prontas sobre frete'}]},
 {'k':'Lembre','t':'Não prometa o que *não entrega*','b':'Prazo, estoque e condições claros evitam reclamação depois.'},
 end('Salve para ^conferir^','E me conta o que ainda falta.')],
 'Checklist rápido para a véspera do 11.11: estoque, preço, live e respostas sobre frete. Salve e confira hoje.'))

# ===== QUA 11/11 =====
d='qua-11-11'
add(d,'0800',J('novidade-11-11-projecao',[
 {'k':'Hoje é 11.11','t':'Projeção do 11.11: ^R$ 3,17 bi^','b':'Alta projetada de 21%'},
 {'l':'list','k':'Os números','t':'O que a *projeção* diz','items':[{'a':'3,17 bi','t':'Projeção do 11.11 no e-commerce'},{'a':'+21%','t':'Crescimento projetado'},{'a':'322,6 bi','t':'Faturado de jan. a set. de 2026'}],'src':SB},
 {'k':'Ano até aqui','t':'E-commerce cresceu *16,9%*','b':'De janeiro a setembro de 2026, segundo os dados citados na matéria.','src':SB},
 {'k':'Para você','t':'Hoje, *observe*','b':'Anote quais produtos e horários tiveram mais cliques. Isso ajuda a planejar a Black Friday.'},
 end('Quer a ^planilha de meta^?','Comente a palavra abaixo e eu te chamo no direct.','META')],
 'O 11.11 deve movimentar R$ 3,17 bilhões no e-commerce em 2026, alta projetada de 21%, segundo a Confi/Neotrust. É uma projeção. Fonte: Giro News (14/10/2026). Comente META.'))
add(d,'1100',live('live-tematica-de-data','Live temática: como aproveitar uma ^data^',['Escolha a data: 11.11, Black Friday ou Natal','Combine nome da live e cenário com o tema','Defina 3 produtos e o preço mínimo de cada','Avise o público com antecedência'],'Dica','Tema *simples* e claro','O público precisa entender em segundos por que a live é especial.','Quatro passos para fazer uma live temática de data. Salve.','Salve para ^a Black Friday^','E me conta qual data você vai usar.'))
add(d,'1400',ia('ia-resumir-regras-da-plataforma','IA para entender as ^regras^ da plataforma','Com cuidado','Cole o *texto oficial*','Copie a política direto da Central do Vendedor ou do programa.','Resuma em tópicos simples este texto de regras e liste as dúvidas que devo confirmar com a plataforma.','Confirme na *fonte*','A IA pode errar. Antes de decidir, releia a regra oficial.','Como usar IA para entender as regras de uma plataforma, sempre confirmando na fonte oficial.'))
add(d,'1900',quiz('quiz-ticket-medio','O que é ticket médio?',['Valor médio gasto por pedido','Número de pedidos por dia','Preço do frete','Custo do produto'],'Ticket médio é o *valor médio por pedido*','Exemplo: 3 pedidos que somam R$ 300 têm ticket médio de R$ 100.','Quiz: o que é ticket médio? Comente a letra: A valor médio gasto por pedido, B número de pedidos por dia, C preço do frete ou D custo do produto. Resposta no último slide.'))
add(d,'2100',lst3('o-que-anotar-depois-do-11-11','Depois do 11.11','O que ^anotar^ hoje',['Produtos que mais receberam cliques','Horários com mais comentários','Perguntas mais repetidas e pedidos cancelados'],'Para quê','Dado vira *plano*','Com essas notas, você ajusta oferta, horário e respostas antes da Black Friday.','O que anotar depois do 11.11 para planejar a Black Friday. Salve.','Salve para ^a Black Friday^','E me conta o que você notou hoje.'))

for n,j in enumerate(jobs,1):j['n']=n
out=sys.argv[1] if len(sys.argv)>1 else 'jobs.json'
json.dump(jobs,open(out,'w'),ensure_ascii=False)
print(len(jobs),sum(len(j['slides']) for j in jobs))
