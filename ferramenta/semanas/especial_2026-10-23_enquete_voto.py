import json,sys
# Post especial 23/10/2026: enquete neutra do 2o turno (sem hashtags de nicho, legenda propria)
cap=('Em quem você vota no domingo (25/10)? Comente a letra: A Lula, B Flávio Bolsonaro, C branco ou nulo, D ainda indeciso.\n\n'
'Aqui cabe todo mundo. Respeito é regra. Voto é secreto, então responder é opcional. Isto não é pesquisa eleitoral, é só uma conversa.\n\n'
'Siga @{H} para mais conteúdo de TikTok Shop, Shopee, Instagram Shop e IA.\n\n#eleicoes2026 #segundoturno #diegoreisads')
slides=[
 {'k':'Enquete','t':'Em quem você ^vota^ no domingo?','b':'Segundo turno, 25/10'},
 {'l':'enquete','k':'Escolha','t':'Qual é a *sua* letra?','b':'\n'.join(['Lula','Flávio Bolsonaro','Branco ou nulo','Ainda indeciso'])},
 {'k':'Regra da casa','t':'Aqui cabe *todo mundo*','b':'Comente só a letra, se quiser. Sem ofensa e sem briga: respeito é regra. Voto é secreto, responder é opcional.'},
 {'t':'Seja qual for o seu voto, ^vote com consciência^','b':'Isto não é pesquisa eleitoral. É só uma conversa entre quem me segue.','follow':True}]
jobs=[{'d':'2026-10-23','slot':'1545','n':'1545','slug':'enquete-voto-segundo-turno','slides':slides,'cap':cap}]
json.dump(jobs,open(sys.argv[1],'w'),ensure_ascii=False)
