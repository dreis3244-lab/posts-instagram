import json,sys
HT='#tiktokshop #shopee #rendadigital #livesell #afiliados #vendasonline'
AV='Os resultados variam de pessoa para pessoa e dependem de constância, produto e execução. Confira sempre as regras atuais de cada plataforma.'
END='Salva esse post e manda para quem quer começar'
def P(slug,k,t,mid,endt,cap,b=None):
    s=[{'k':k,'t':t}]
    if b:s[0]['b']=b
    for m in mid:s.append({'t':m[0],'b':m[1]} if isinstance(m,tuple) else {'t':m})
    s.append({'k':'Para guardar','t':endt,'follow':True})
    return {'slug':slug,'slides':s,'cap':cap+'\n\n'+AV+'\n\n'+HT,'style':'foto'}
D={}
D['qui-05-11']=[
 P('tiktok-afiliado-sem-produto','TikTok Shop','Como ganhar dinheiro no TikTok Shop *sem ter produto*',
  [('Você divulga o produto de outra loja','Quando alguém compra pelo seu link ou vídeo, você recebe uma comissão.'),
   ('Escolha produtos que você usaria','Vende mais quem mostra o produto de verdade, em uso.'),
   ('Mostre antes e depois, ou o passo a passo','Um vídeo simples que resolve um problema chama mais atenção do que um discurso.')],
  END,'Dá para começar no TikTok Shop como afiliado, sem estoque e sem produto próprio. O segredo é escolher bem e mostrar o produto em uso. Salva para consultar depois.'),
 P('tiktok-do-zero-3-passos','Do zero','O que eu faria hoje se começasse *do zero* no TikTok Shop',
  [('1. Escolher um nicho só','Quem fala com todo mundo não fala com ninguém.'),
   ('2. Postar vídeo curto todo dia','Treino vem da repetição, não da vontade.'),
   ('3. Fazer uma live pequena por semana','Mesmo com pouca gente. Você aprende o ritmo.')],
  END,'Se eu estivesse começando agora no TikTok Shop, seria assim: um nicho, vídeo curto com frequência e uma live pequena por semana. Qual passo você ainda não fez?'),
 P('tiktok-3-erros-iniciantes','Atenção','3 erros que travam quem começa no *TikTok Shop*',
  [('Erro 1: mudar de nicho toda semana','O algoritmo precisa entender quem é o seu público.'),
   ('Erro 2: copiar sem adaptar','Use a ideia, mas fale do seu jeito, com a sua cara.'),
   ('Erro 3: desistir antes de testar','Poucos vídeos não dizem nada. Teste, compare, ajuste.')],
  END,'Três erros comuns de quem começa no TikTok Shop. Marca nos comentários o que você já cometeu, todo mundo começa assim.'),
]
D['sex-06-11']=[
 P('tiktok-afiliado-ou-vendedor','TikTok Shop','Afiliado ou vendedor: qual escolher *primeiro*?',
  [('Afiliado: sem estoque','Menos risco e menos custo para testar. Você aprende a vender.'),
   ('Vendedor: margem maior','Exige produto, envio, atendimento e organização.'),
   ('Meu conselho: comece como afiliado','Aprenda o que vende, depois decida se vale ter o seu produto.')],
  END,'Afiliado ou vendedor no TikTok Shop? Cada caminho tem seu momento. Para quem está começando, afiliado costuma ser a porta de entrada mais leve.'),
 P('live-escolher-produto','Live','Como escolher o produto para vender em *live*',
  [('Que seja fácil de mostrar','Se dá para demonstrar em 30 segundos, já ajuda.'),
   ('Que resolva um problema claro','A pessoa precisa entender o motivo de comprar.'),
   ('Que tenha preço que cabe no impulso','Teste faixas de preço e veja onde o público responde.')],
  END,'Escolher o produto certo faz metade do trabalho em uma live. Salva esse checklist para a próxima vez.'),
 P('shopee-ou-tiktok-onde-comecar','Comparativo','Shopee ou TikTok Shop: *por onde começar?*',
  [('Shopee: o público já chega para comprar','Busca e catálogo fazem parte do dia a dia.'),
   ('TikTok Shop: o vídeo e a live descobrem o cliente','Entretenimento que vira compra.'),
   ('Dá para usar os dois','Comece por um, aprenda o processo e depois expanda.')],
  END,'Shopee e TikTok Shop funcionam de formas diferentes. O melhor começo é o que você consegue manter com constância.'),
]
D['sab-07-11']=[
 P('tiktok-primeiro-video-roteiro','Roteiro','Seu primeiro vídeo no TikTok Shop em *4 passos*',
  [('Passo 1: gancho nos 3 primeiros segundos','Mostre o problema ou o resultado logo de cara.'),
   ('Passo 2: mostre o produto em uso','Sem enrolação. Mão na massa.'),
   ('Passo 3: diga por que vale','Um benefício claro, sem exagero e sem promessa.'),
   ('Passo 4: chame para o link','Deixe claro onde a pessoa clica.')],
  END,'Roteiro simples para gravar seu primeiro vídeo vendendo no TikTok Shop. Gravou? Me conta como foi.'),
 P('live-primeiros-5-minutos','Live','O que falar nos *primeiros 5 minutos* da live',
  [('Diga quem você é e o que vai mostrar','Quem entra precisa entender rápido.'),
   ('Mostre o produto logo','Não deixe para o final.'),
   ('Faça uma pergunta ao público','Pergunta simples gera comentário e comentário gera entrega.')],
  END,'Os primeiros minutos decidem quem fica na live. Use esse roteiro na próxima e veja a diferença.'),
 P('mito-live-perfeita','Mito','"A live precisa ser *perfeita* para vender"',
  [('Não precisa','Quem espera ficar perfeito nunca começa.'),
   ('Constância ganha de perfeição','Cada live ensina algo que a anterior não ensinou.'),
   ('Melhore uma coisa por vez','Voz, iluminação, roteiro. Um ajuste de cada vez.')],
  END,'Eu mesmo aprendi fazendo, e melhorando a cada live. Perfeição não é pré-requisito.'),
]
D['dom-08-11']=[
 P('tiktok-constancia-vale-mais','Rotina','*Constância* vale mais que horas no TikTok Shop',
  [('Todo dia um pouco','Um vídeo curto por dia vale mais que um dia inteiro por mês.'),
   ('Defina um horário fixo','Rotina tira a decisão do caminho.'),
   ('Anote o que funcionou','Em duas semanas você já tem dados para ajustar.')],
  END,'Quem começa costuma achar que precisa de muitas horas. Na prática, o que muda o jogo é rotina.'),
 P('ia-roteiro-video-produto','IA','Como usar *IA* para criar roteiro de vídeo de produto',
  [('Dê contexto para a IA','Diga o produto, o público e o tom que você quer.'),
   ('Peça 3 versões de gancho','Escolha a que soa mais natural para você.'),
   ('Adapte para o seu jeito','A IA ajuda a começar, a sua voz faz a diferença.')],
  END,'A IA ajuda a sair do branco na hora de criar roteiros. Dá o contexto, pede opções e ajusta com a sua cara.'),
 P('resumo-3-licoes-da-semana','Resumo','3 lições para revisar neste *domingo*',
  [('Escolha um nicho e fique nele','Foco ajuda o público a te reconhecer.'),
   ('Mostre o produto em uso','Demonstração vende mais do que descrição.'),
   ('Planeje a semana em 10 minutos','Defina 3 vídeos e 1 live antes de segunda.')],
  END,'Revisão rápida para começar a semana organizado. Qual dessas três você vai aplicar primeiro?'),
]
D['seg-09-11']=[
 P('shopee-afiliados-como-funciona','Shopee','Shopee Afiliados: como funciona, em *4 passos*',
  [('1. Faça seu cadastro no programa','Confira as regras atuais dentro do app.'),
   ('2. Escolha produtos para divulgar','Pense no que o seu público realmente compraria.'),
   ('3. Gere o seu link e divulgue','Em vídeo, post ou live.'),
   ('4. Acompanhe os resultados','Veja o que funcionou e repita.')],
  END,'Passo a passo geral de como funciona o Shopee Afiliados. Sempre confira as regras atuais do programa.'),
 P('tiktok-1-produto-5-videos','Conteúdo','Como transformar *1 produto* em 5 vídeos',
  [('Vídeo 1: o problema que ele resolve',''),
   ('Vídeo 2: o produto em uso',''),
   ('Vídeo 3: comparação com outro modelo',''),
   ('Vídeo 4: dúvida mais comum de quem compra','')],
  END,'Um produto rende muito conteúdo. Salva essas 5 ideias para quando faltar assunto.'),
 P('comissao-nao-e-lucro','Atenção','Comissão não é *lucro*: o que olhar antes de divulgar',
  [('Veja a qualidade do produto','Produto ruim gera reclamação e some a confiança.'),
   ('Confira as avaliações do vendedor','Quem compra pelo seu link espera uma boa experiência.'),
   ('Considere seu tempo e investimento','Gravar, editar e divulgar também custa tempo.')],
  END,'Antes de divulgar, pense além do percentual de comissão. Confiança do público é o seu maior ativo.'),
]
D['ter-10-11']=[
 P('black-friday-o-que-preparar','Black Friday','O que preparar *desde já* para a Black Friday',
  [('Escolha 3 produtos que você vai divulgar','Foco em poucos, bem trabalhados.'),
   ('Grave vídeos com antecedência','Na semana da data o tempo aperta.'),
   ('Aqueça o público antes','Avise que vem oferta e quando.')],
  END,'Quem se organiza antes chega mais calmo na Black Friday. Começa com poucos produtos, bem trabalhados.'),
 P('comentarios-que-viram-venda','Atendimento','Como responder comentário que *vira venda*',
  [('Responda rápido','Quem comenta está com a dúvida na mão.'),
   ('Responda de forma curta e clara','Preço, prazo e benefício principal.'),
   ('Use a dúvida para criar um novo vídeo','Se uma pessoa perguntou, outras também querem saber.')],
  END,'Comentário é conversa com o cliente. Quem responde bem vende mais e constrói comunidade.'),
 P('video-ou-live-tiktok-shop','Comparativo','Vídeo ou live: o que muda no *TikTok Shop*?',
  [('Vídeo: você edita e controla a mensagem','Bom para alcance e para ser descoberto.'),
   ('Live: interação em tempo real','Bom para tirar dúvida e fechar a venda.'),
   ('Juntos funcionam melhor','O vídeo atrai, a live converte.')],
  END,'Vídeo e live se complementam. Usa cada um para o que faz de melhor.'),
]
D['qua-11-11']=[
 P('data-11-11-3-coisas','11.11','Dia *11.11*: 3 coisas para fazer hoje',
  [('Poste pelo menos um vídeo de produto','Aproveite o movimento de busca da data.'),
   ('Faça uma live curta','Responda dúvidas e mostre ofertas.'),
   ('Anote o que funcionou','Esse aprendizado vai para a Black Friday.')],
  END,'Datas promocionais movimentam o público. Mas planejamento vale mais que correria de última hora.'),
 P('live-checklist-antes-de-ligar','Checklist','Checklist antes de *ligar a live*',
  [('Luz, som e internet testados','Pequenos problemas afastam público.'),
   ('Produtos separados à mão','Nada de procurar durante a live.'),
   ('Roteiro dos 5 primeiros minutos','Saber o que vai falar dá segurança.')],
  END,'Cinco minutos de preparação evitam muita dor de cabeça. Salva esse checklist.'),
 P('plano-7-dias-tiktok-shop','Plano','Plano de *7 dias* para começar no TikTok Shop',
  [('Dia 1 a 2: escolha o nicho e 3 produtos',''),
   ('Dia 3 a 5: grave 1 vídeo por dia',''),
   ('Dia 6: faça uma live curta',''),
   ('Dia 7: revise e ajuste o que aprendeu','')],
  END,'Um plano simples de uma semana para sair da ideia e começar. Qual dia você começa?'),
]
SL=[1100,1900,2100]
SL=['1100','1900','2100']
jobs=[];idx=0
for d,ps in D.items():
    dd='2026-11-'+d.split('-')[1]
    for t,p in zip(SL,ps):
        p=dict(p);p['d']=dd;p['n']=t;
        for s in p['slides']:
            if s.get('b')=='':s.pop('b')
        jobs.append(p)
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
print(len(jobs))
