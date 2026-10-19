import json,sys
AV='Os resultados variam de pessoa para pessoa e dependem de constância, produto e execução. Confira sempre as regras atuais de cada plataforma.'
HT='#tiktokshop #shopee #rendadigital #livesell #afiliados #vendasonline'
END='Salve este post e *siga* para mais'
def P(n,slug,slides,cap,srcs):
    return {'d':'tendencias','n':n,'slug':slug,'style':'foto','slides':slides+[{'k':'Para guardar','t':END,'follow':True}],
            'cap':cap+'\n\nFontes: '+srcs+'\n\n'+AV+'\n\n'+HT}
EX='Fonte: Exame (01/10/2026)'
BP='Fonte: BPMoney (30/09/2026)'
DM='Fonte: Diário da Mídia (09/10/2026)'
jobs=[
P('01','tiktok-como-ser-afiliado',[
 {'k':'TikTok Shop','t':'Como virar *afiliado* no TikTok Shop','b':'Passo a passo com os requisitos atuais'},
 {'t':'Requisito 1: ter *18 anos* ou mais','b':'E a conta em situação regular.','src':DM},
 {'t':'Requisito 2: *1.000 seguidores*','b':'Com menos, dá para usar o Linkshare, mas a verificação também é necessária.','src':DM},
 {'t':'Passo 1: abra o *TikTok Studio*','b':'Perfil, menu de três linhas, TikTok Studio e "TikTok Shop para criadores".','src':DM},
 {'t':'Passo 2: faça a *verificação de identidade*','b':'CPF e documento válido. Aprovado, você acessa a Central do Criador.','src':DM}],
 'Como virar afiliado do TikTok Shop, com os requisitos atuais: 18 anos ou mais, 1.000 seguidores e verificação de identidade. Confira as regras dentro do app, porque elas podem mudar.',
 'Diário da Mídia (09/10/2026)'),
P('02','tiktok-black-friday-calendario',[
 {'k':'Black Friday','t':'Black Friday no *TikTok Shop*: o calendário','b':'Campanha de 27/10 a 12/12'},
 {'t':'A campanha vai de *27/10 a 12/12*','b':'Com temas por dia, como Casa e cozinha em 27/10.','src':BP},
 {'t':'Período principal: *19 a 30/11*','b':'Descontos de até 70%, frete grátis e parcelamento em até 12x sem juros.','src':BP},
 {'t':'*R$ 100 milhões* em cupons e subsídios previstos','b':'Anunciado pelo TikTok Shop em 30/09/2026.','src':'Fonte: Clube MarTech (08/10/2026)'},
 {'t':'Criadores: *mais de 1.000 seguidores*','b':'E ao menos um conteúdo publicado nos 30 dias anteriores.','src':BP},
 {'t':'O que fazer agora: *gravar com antecedência*','b':'Escolha poucos produtos e prepare os vídeos antes de 19/11.'}],
 'O calendário da Black Friday no TikTok Shop: campanha de 27/10 a 12/12, com período principal de 19 a 30/11. Quem quer divulgar precisa se preparar antes.',
 'BPMoney (30/09/2026); Clube MarTech (08/10/2026)'),
P('03','tiktok-comissao-afiliado',[
 {'k':'Afiliado','t':'Quanto o afiliado *costuma ganhar* por venda?','b':'Entenda antes de divulgar'},
 {'t':'Quem define a comissão é o *lojista*','b':'Não existe um valor único para todos os produtos.','src':EX},
 {'t':'Segundo a Serasa, costuma ficar entre *8% e 15%*','b':'Do valor do item.','src':'Fonte: Exame, citando a Serasa (01/10/2026)'},
 {'t':'Conta de exemplo: item de R$ 100 com 10% rende *R$ 10*','b':'É só um cálculo ilustrativo, não uma promessa de ganho.'},
 {'t':'Comissão *não é lucro*','b':'Conte o seu tempo para gravar, editar e divulgar.'}],
 'A comissão do afiliado no TikTok Shop é definida pelo lojista. Segundo a Serasa, costuma ficar entre 8% e 15% do item. O exemplo do post é só um cálculo ilustrativo.',
 'Exame (01/10/2026), citando a Serasa'),
P('04','tiktok-nichos-que-mais-saem',[
 {'k':'Nichos','t':'5 nichos que *mais saem* no TikTok Shop','b':'O TikTok não divulga um ranking oficial'},
 {'t':'Beleza e cuidados pessoais','b':'Produtos entre R$ 40 e R$ 180.','src':EX},
 {'t':'Moda e acessórios','b':'Bolsas, bijuterias, conjuntos casuais e calçados.','src':EX},
 {'t':'Casa e decoração','b':'Itens entre R$ 30 e R$ 120.','src':EX},
 {'t':'Tecnologia simples e pets','b':'Microfones de lapela, fones e carregadores; mordedores, petiscos e camas compactas.','src':EX}],
 'Nichos citados como de maior saída no TikTok Shop. Importante: o TikTok não divulga um ranking oficial. Escolha um e teste.',
 'Exame (01/10/2026)'),
P('05','tiktok-live-vende',[
 {'k':'Live','t':'Por que a *live* vende tanto no TikTok Shop?','b':'Números divulgados pela empresa'},
 {'t':'GMV de lives cresceu *161 vezes* desde a chegada ao Brasil','b':'Dado divulgado pelo TikTok Shop.','src':BP},
 {'t':'*91%* dos usuários usam lives para tirar dúvidas','b':'Levantamento da própria empresa.','src':BP},
 {'t':'*60%* preferem comprar em live por causa de ofertas exclusivas','b':'Levantamento da própria empresa.','src':BP},
 {'t':'O que isso muda para você: *responda ao vivo*','b':'Quem tira dúvidas em tempo real tem mais chance de vender.'}],
 'Por que a live vende no TikTok Shop? Os números abaixo foram divulgados pela própria empresa, não são de um estudo independente.',
 'BPMoney (30/09/2026), com dados divulgados pelo TikTok Shop'),
P('06','tiktok-lojista-nova-comissao',[
 {'k':'Lojista','t':'A comissão do *lojista* mudou no TikTok Shop','b':'Valores em vigor desde 15/07/2026'},
 {'t':'Produtos abaixo de R$ 50: *10% + R$ 4* por item','b':'Antes era 6% + R$ 4.','src':EX},
 {'t':'Produtos a partir de R$ 50: *6% + R$ 6* por item','b':'Antes era 6% + R$ 4.','src':EX},
 {'t':'Novos lojistas: *0% por 60 dias*','b':'Para quem cumpre as missões iniciais, com limite de R$ 17 mil.','src':EX},
 {'t':'Faça a conta *antes de definir o preço*','b':'Some comissão, frete e custo do produto.'}],
 'A comissão do lojista no TikTok Shop mudou em 15/07/2026. Antes de definir o preço de um produto, faça a conta completa.',
 'Exame (01/10/2026)'),
]
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs))
