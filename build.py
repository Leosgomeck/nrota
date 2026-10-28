import pathlib, sys

ROOT = pathlib.Path(__file__).parent
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Instrument+Serif:ital@1&family=Onest:wght@400;500;600&display=swap">'
ICON = {
    'search': '<path d="m12.2 12.2 3.8 3.8"/><circle cx="8" cy="8" r="5.5"/>',
    'check': '<path d="M3 9.5 7 13l8-8"/>',
    'chat': '<path d="M3 4h12v8H8l-4 3v-3H3z"/>',
}
svg = lambda name: f'<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.8">{ICON[name]}</svg>'


def hero(eyebrow, title, lead, ctas=''):
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow"><i></i>{eyebrow}</span>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
  {f'<div class="ctas">{ctas}</div>' if ctas else ''}
</div></section>'''


def section(eyebrow, title, body, lead='', side=''):
    head = f'<span class="eyebrow"><i></i>{eyebrow}</span><h2>{title}</h2>' + (f'<p class="lead">{lead}</p>' if lead else '')
    head = f'<div class="s-head row"><div style="display:grid;gap:14px">{head}</div>{side}</div>' if side else f'<div class="s-head">{head}</div>'
    return f'<section class="s"><div class="wrap">{head}{body}</div></section>'


def band(title, text, cta):
    return f'<section class="s"><div class="wrap"><div class="band"><div><h2>{title}</h2><p class="lead">{text}</p></div>{cta}</div></div></section>'


def boxes(items, cols='g3', cls='box'):
    return f'<div class="grid {cols}">' + ''.join(f'<div class="{cls}"><h3>{t}</h3>{body if body.startswith("<") else f"<p>{body}</p>"}</div>' for t, body in items) + '</div>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def steps(items, cls='', start=0):
    return f'<ol class="steps {cls}" style="counter-reset:st {start}">' + ''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in items) + '</ol>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'


btn = lambda href, label, kind='o': f'<a class="btn btn-{kind}" href="{href}">{label}</a>'

PLANS = '''<div class="grid g3">
  <article class="box plan"><span class="k">N’ROTA Start</span><span class="price">Grátis</span>
    <ul><li>Perfil no catálogo nacional</li><li>Repertório pesquisável, fotos e vídeos</li><li>Contato direto de quem contrata</li></ul>
    <a class="btn btn-g btn-sm" href="cadastro-banda.html">Cadastrar banda</a></article>
  <article class="box plan hl"><span class="k">N’ROTA Destaque</span><span class="price">R$ 50 <small>pagamento único</small></span>
    <ul><li>Post de apresentação no feed do gênero</li><li>Story salvo no Destaque do seu estilo</li><li>Sem vencimento automático</li></ul>
    <a class="btn btn-o btn-sm" href="cadastro-banda.html">Quero aparecer no feed</a></article>
  <article class="box plan"><span class="k">N’ROTA Impulso</span><span class="price">Sob orçamento</span>
    <ul><li>Reels de performance e trajetória</li><li>Stories e calendário editorial</li><li>Campanhas com verba de mídia à parte</li></ul>
    <a class="btn btn-g btn-sm" href="solicitar-proposta.html">Pedir orçamento</a></article>
</div>
<div class="grid g2" style="margin-top:16px">
  <article class="box plan"><span class="k">N’ROTA Pro · sob proposta</span><h3>Posicionamento e material comercial</h3>
    <ul><li>Diagnóstico artístico, release e portfólio</li><li>Acompanhamento e planejamento de divulgação</li></ul></article>
  <article class="box plan"><span class="k">N’ROTA Agency · sob contrato</span><h3>Representação e negociação</h3>
    <ul><li>Prospecção de casas, festivais e empresas</li><li>Comissão só sobre negócio fechado, combinada antes</li></ul></article>
</div>'''

FLOW = 'Cadastro', 'A banda cria o perfil gratuito, com repertório música a música.'

PAGES = {}

PAGES['index'] = ('N’ROTA', 'inicio', f'''
<section class="hero wrap">
  <div class="hero-grid">
    <div>
      <span class="eyebrow"><i></i>Rock N’ Rota · primeiro capítulo</span>
      <h1>Seu som merece <em class="acc">ir mais longe.</em></h1>
      <p class="lead">Catálogo nacional de artistas com repertório pesquisável e perfil profissional. Quem contrata encontra pela música, pelo estilo, pelo evento ou pela cidade.</p>
      <div class="ctas">{btn("cadastro-banda.html", "Cadastrar minha banda")}{btn("solicitar-proposta.html", "Fazer meu evento", "g")}</div>
      <p class="fine">Cadastro gratuito. Contato direto com a banda, sem comissão.</p>
    </div>
    <div class="search-card" data-search-demo aria-label="Prévia ilustrativa da busca">
      <div class="sc-top"><span>Busca no catálogo</span><span>Prévia ilustrativa</span></div>
      <div class="sc-field">{svg("search")}<span><span data-q></span><span class="caret"></span></span></div>
      <p class="sc-kind">Encontrado por <b data-k></b></p>
      <ul class="sc-list" data-r></ul>
    </div>
  </div>
  <div class="genres">
    <span class="lbl">Estilos</span>
    <span class="chip on">Rock <small>ativo</small></span>
    {''.join(f'<a class="chip" href="acesso-antecipado.html#{g.lower()}">{g} <small>em breve</small></a>' for g in ['Samba','Pagode','Pop','Sertanejo','MPB'])}
  </div>
</section>

<section class="s">
  <div class="wrap flow">
    <div class="flow-txt">
      <span class="eyebrow"><i></i>Uma vitrine viva</span>
      <h2>Quem procura encontra <em class="acc">quem toca.</em></h2>
      <p class="lead">Cada perfil vira filtro: estilo, repertório, formação, região e agenda habitual. Cada busca chega a bandas que realmente atendem aquele pedido.</p>
      <ul class="ticks">
        <li>{svg("search")}<span><b>Busca pelo repertório</b>Por artista ou música, não só pelo nome da banda.</span></li>
        <li>{svg("check")}<span><b>Perfis revisados</b>Dados e materiais conferidos antes de publicar.</span></li>
        <li>{svg("chat")}<span><b>Contato sem atrito</b>Direto com a banda ou com apoio do produtor.</span></li>
      </ul>
      <span class="tag-note">Cards ao lado: exemplos ilustrativos</span>
    </div>
    <div class="stage" aria-label="Exemplos ilustrativos de buscas e perfis">
      <div class="lane"><div class="lane-track" data-lane="ask"></div></div>
      <div class="lane rev"><div class="lane-track" data-lane="art"></div></div>
    </div>
  </div>
</section>

{section("Escolha seu caminho", "Uma plataforma, <em class='acc'>três jornadas.</em>", '''<div class="grid g3">
  <a class="box" href="artistas.html"><span class="k">Para artistas</span><h3>Perfil gratuito no catálogo</h3><p>Repertório pesquisável, fotos, vídeos e contato direto. Divulgação opcional no Instagram.</p><span class="more">Conhecer →</span></a>
  <a class="box" href="eventos.html"><span class="k">Para quem contrata</span><h3>Do artista ao evento completo</h3><p>Bandas, DJs, som, luz, palco, audiovisual e produção coordenada.</p><span class="more">Conhecer →</span></a>
  <a class="box" href="parceiros.html"><span class="k">Para fornecedores</span><h3>Rede de profissionais de eventos</h3><p>Receba pedidos compatíveis com seu nicho e sua região.</p><span class="more">Conhecer →</span></a>
</div>''')}

{section("Como funciona", "Da banda ao palco em <em class='acc'>cinco passos.</em>", steps([
    FLOW,
    ('Validação', 'Nossa equipe revisa dados e materiais antes de publicar.'),
    ('Catálogo', 'O perfil entra nos filtros por estilo, evento, formação e região.'),
    ('Descoberta', 'Quem contrata pesquisa por artista, música, cidade ou data habitual.'),
    ('Contato', 'Direto com a banda ou com apoio do produtor N’ROTA.'),
]), side='<a class="more" href="como-funciona.html">Ver em detalhes →</a>')}

{band("O catálogo abre em breve.", "Entre na lista e seja avisado quando a busca completa estiver no ar.", btn("acesso-antecipado.html", "Quero acesso antecipado"))}
''', [])

PAGES['como-funciona'] = ('Como funciona | N’ROTA', 'como-funciona', f'''
{hero("Como funciona", "Uma plataforma, <em class='acc'>duas entradas.</em>", "Quem oferece música e quem procura música se encontram num catálogo organizado, revisado e pesquisável.", btn("cadastro-banda.html", "Cadastrar minha banda") + btn("solicitar-proposta.html", "Fazer meu evento", "g"))}

{section("A jornada", "Da banda ao <em class='acc'>palco.</em>", steps([
    ('Cadastro', 'A banda preenche um formulário em etapas, com campos que mudam conforme as respostas. Dá para salvar e continuar depois.'),
    ('Validação', 'Nossa equipe confere dados, fotos e repertório antes de tornar o perfil público.'),
    ('Catálogo', 'As respostas viram categorias pesquisáveis, não textos soltos.'),
    ('Descoberta', 'Quem contrata pesquisa por estilo, música, artista, evento, cidade ou agenda habitual.'),
    ('Contato', 'Direto com a banda pelo canal que ela autorizou, ou com apoio do produtor.'),
]))}

{section("Busca", "Filtros que fazem a <em class='acc'>plataforma funcionar.</em>", boxes([
    ('Estilo', 'Hard rock, rock clássico, punk, metal, indie, pop rock e os próximos gêneros.'),
    ('Artistas e músicas', 'Queen, Legião Urbana, Foo Fighters. Cada música do repertório é pesquisável.'),
    ('Evento', 'Casamento, festa particular, corporativo, bar, festival, evento público.'),
    ('Formação', 'Solo, duo, trio ou banda completa.'),
    ('Agenda', 'Dias habituais, turnos e antecedência mínima.'),
    ('Região', 'Cidade-base, outros estados e disponibilidade para viajar.'),
    ('Formato', 'Acústico, elétrico, tributo ou autoral.'),
    ('Orçamento', 'Faixa indicativa, só quando a banda autoriza.'),
], 'g4', 'box top'))}

{section("O diferencial", "O repertório é <em class='acc'>pesquisável.</em>", '''<div class="grid g2">
  <div class="box"><span class="k">Como a banda cadastra</span><p class="example">Música: <span>Everlong</span><br>Artista: <span>Foo Fighters</span><br>Década: <span>1990</span> · Estilo: <span>rock alternativo</span></p><p>A mesma música pode entrar em mais de um setlist, como casamento ou festival.</p></div>
  <div class="box"><span class="k">Como o contratante encontra</span><p class="example">Busca: <span>“Foo Fighters”</span> ou <span>“Everlong”</span></p><p>O resultado mostra as bandas cujo repertório tem aquele artista ou aquela música. PDFs e links continuam aceitos como complemento.</p></div>
</div>''', "Guardamos cada música com o artista original, em vez de um PDF anexado.")}

{section("Contratação", "Dois caminhos. <em class='acc'>Você escolhe.</em>", '''<div class="grid g2">
  <div class="box dash"><h3>Contato com a banda <small>Sem comissão</small></h3><p>Abre o canal autorizado pela banda. A negociação acontece direto entre as partes.</p></div>
  <div class="box dash"><h3>Fale com o produtor <small>Opcional</small></h3><p>Você envia o briefing do evento, recebe sugestões e pode contar com intermediação, mediante autorização e condições acordadas.</p></div>
</div>
<p class="rule"><strong>Disponibilidade não é reserva.</strong> Os dias e turnos do perfil orientam a busca. Toda data precisa ser confirmada com a banda.</p>''')}

{section("Confiança", "Regras claras <em class='acc'>para todos.</em>", '''<div class="grid g3">
  <div class="box"><h3>Revisão antes de publicar</h3><p>Dados e materiais são conferidos antes de o perfil ficar público.</p></div>
  <div class="box"><h3>Dados comerciais privados</h3><p>Cachê e condições nunca aparecem no perfil público.</p></div>
  <div class="box"><h3>Autorização expressa</h3><p>Fotos, vídeos e contatos só são usados com o seu aceite.</p></div>
  <div class="box"><h3>Sem prazo de vencimento</h3><p>O perfil e o post de Destaque não expiram por pacote.</p></div>
  <div class="box"><h3>Sem promessas</h3><p>Nenhuma garantia de audiência, contratação ou posição nos resultados.</p></div>
  <div class="box"><h3>Seus dados, seu controle</h3><p>Você pode pedir correção ou exclusão dos seus dados quando quiser.</p></div>
</div>''')}

{band("Pronto para começar?", "Cadastre sua banda gratuitamente ou conte o que você precisa para o seu evento.", f'<div class="ctas">{btn("cadastro-banda.html", "Cadastrar banda")}{btn("solicitar-proposta.html", "Solicitar proposta", "g")}</div>')}
''', [])

PAGES['artistas'] = ('Para artistas | N’ROTA', 'artistas', f'''
{hero("Para artistas", "Seu trabalho inteiro <em class='acc'>em um só lugar.</em>", "Um perfil profissional gratuito, com repertório pesquisável, para ser encontrado por quem contrata em todo o Brasil. Sem exclusividade e sem comissão no contato direto.", btn("cadastro-banda.html", "Cadastrar minha banda") + btn("#planos", "Ver planos", "g"))}

{section("Seu perfil", "O que o contratante <em class='acc'>vê.</em>", boxes([
    ('História e influências', 'Quem é a banda, de onde vem e o que inspira o som.'),
    ('Fotos, vídeos e links', 'Material oficial e redes num só lugar.'),
    ('Setlist e repertórios especiais', 'Música por música, por ocasião e por tema.'),
    ('Eventos e formações', 'Onde você toca e em quais formatos.'),
    ('Duração e agenda habitual', 'Sets, intervalos, dias e turnos.'),
    ('Rider e região', 'Estrutura técnica e até onde você vai.'),
]))}

{section("O cadastro", "Dez etapas, <em class='acc'>no seu tempo.</em>", steps([
    ('Identificação', 'Nome, responsável, contatos de gestão, cidade, links e fotos.'),
    ('Identidade musical', 'Estilo principal, secundários, proposta e referências.'),
    ('Repertório', 'Música, artista original, década e estilo.'),
    ('Eventos', 'Casamentos, bares, festivais, corporativos e mais.'),
    ('Formações', 'Integrantes, formatos, duração e sets.'),
]) + '<div style="height:28px"></div>' + steps([
    ('Disponibilidade', 'Dias, turnos, antecedência e datas bloqueadas.'),
    ('Deslocamento', 'Cidade-base, estados atendidos e viagens.'),
    ('Estrutura técnica', 'Rider, mapa de palco e equipamentos.'),
    ('Condições comerciais', 'Cachê e pagamento. Sempre privado.'),
    ('Autorizações', 'Contato exibido, aceites e serviços opcionais.'),
], start=5), "Os campos mudam conforme suas respostas. O progresso fica salvo e você continua depois.")}

<div id="planos"></div>
{section("Planos", "Comece grátis. <em class='acc'>Cresça no seu ritmo.</em>", PLANS + '<p class="rule"><strong>Seu perfil não depende de plano pago.</strong> Os serviços são opcionais e não interferem na presença no catálogo. Valores sujeitos a validação antes do lançamento.</p>')}

{section("Instagram", "Cada formato com <em class='acc'>uma função.</em>", boxes([
    ('Feed', 'Apresentação institucional da banda, sem data de show.'),
    ('Reels', 'Performance, trajetória, entrevistas e repertório. Nunca divulgação de datas.'),
    ('Stories', 'Datas, locais, horários e chamadas dos seus shows.'),
    ('Destaques', 'Por estilo: bandas. Por mês: agenda de eventos.'),
], 'g4', 'box top'), "O feed apresenta bandas. A agenda de shows aparece só nos Stories e nos Destaques do mês.")}

{section("Agenciamento", "Representação com <em class='acc'>regras claras.</em>", '''<div class="grid g2">
  <div class="box"><h3>Como funciona</h3><ul><li>Adesão opcional e sujeita à avaliação da equipe</li><li>A produtora prospecta casas, festivais, empresas e eventos</li><li>Apresenta propostas, negocia e acompanha cada oportunidade</li></ul></div>
  <div class="box"><h3>Remuneração e contrato</h3><ul><li>Referência inicial de 10% sobre negócios fechados por intermediação, a negociar</li><li>Prazo, território e exclusividade definidos em contrato</li><li>Sem promessa de quantidade mínima de shows</li></ul></div>
</div>''', "Representação comercial é diferente de comprar um pacote de divulgação.")}

{band("Sua banda no catálogo, de graça.", "Leva alguns minutos por etapa. Nossa equipe revisa e avisa quando o perfil for publicado.", btn("cadastro-banda.html", "Cadastrar minha banda"))}
''', [])

PAGES['eventos'] = ('Faça seu evento | N’ROTA', 'eventos', f'''
{hero("Faça seu evento com a gente", "Do artista ao <em class='acc'>evento completo.</em>", "Seu evento merece o som certo, a estrutura adequada e profissionais em quem confiar. Precisa só de uma banda ou quer ajuda com toda a produção? Conte o que você imagina.", btn("solicitar-proposta.html", "Solicitar proposta"))}

<section class="s"><div class="wrap"><div class="grid g3">
  <a class="box" href="solicitar-proposta.html#artista"><span class="k">Atração</span><h3>Quero um artista</h3><p>Bandas, artistas solo, DJs, tributos e formatos acústicos.</p><span class="more">Solicitar proposta →</span></a>
  <a class="box" href="solicitar-proposta.html#estrutura"><span class="k">Estrutura</span><h3>Preciso de estrutura</h3><p>Som, luz, palco, painéis de LED, foto e vídeo.</p><span class="more">Solicitar proposta →</span></a>
  <a class="box" href="solicitar-proposta.html#completo"><span class="k">Produção</span><h3>Quero o evento completo</h3><p>Coordenação de fornecedores, cronograma e acompanhamento.</p><span class="more">Solicitar proposta →</span></a>
</div></div></section>

{section("O que você pode contratar", "Serviços avulsos <em class='acc'>ou combinados.</em>", boxes([
    ('Atrações artísticas', 'Bandas, artistas solo, DJs, tributos, repertórios e formatos acústicos.'),
    ('Som e iluminação', 'PA, consoles, microfones, monitores, iluminação de palco e operadores.'),
    ('Estruturas para eventos', 'Palcos, praticáveis, coberturas, tendas, grids, treliças e montagem.'),
    ('Audiovisual profissional', 'Painéis de LED, projetores, telões, transmissão e técnicos.'),
    ('Conteúdo e registro', 'Videomakers, fotografia, aftermovie, multicâmeras e edição.'),
    ('Produção e operação', 'Coordenação, fornecedores, logística, cronograma e acompanhamento.'),
], 'g3', 'box top'), "Conforme a disponibilidade dos artistas e parceiros, em Brasília e em outras regiões do Brasil.")}

{section("Como funciona", "Quatro passos até <em class='acc'>o palco.</em>", steps([
    ('Escolha o que precisa', 'Artistas, DJ, som e luz, palco, foto e vídeo ou produção completa.'),
    ('Conte sobre o evento', 'Tipo, data, local, público, formato e faixa de investimento.'),
    ('Receba um retorno', 'Triagem da equipe, esclarecimentos e proposta ou indicação de profissionais.'),
    ('Confirme a contratação', 'Orçamento detalhado, responsabilidades, contrato, pagamento e cronograma.'),
], 's4'))}

{section("Modelos de atendimento", "Transparência <em class='acc'>desde o início.</em>", '''<div class="grid g2">
  <div class="box dash"><h3>Conexão e indicação <small>Modelo A</small></h3><p>Recebemos o briefing e apresentamos artistas ou fornecedores. A contratação pode ser direta entre você e o parceiro, com papéis, valores e eventual remuneração de indicação informados antes.</p></div>
  <div class="box dash"><h3>Produção N’ROTA <small>Modelo B</small></h3><p>Nossa equipe monta uma proposta integrada e, se contratada, coordena parceiros, cronograma e entregas. Taxa de produção, escopo e responsabilidades ficam em contrato.</p></div>
</div>
<p class="rule"><strong>Sem promessas sem confirmação.</strong> Preço, disponibilidade e entrega só valem depois do retorno do artista ou fornecedor.</p>''', "Intermediar fornecedores não é o mesmo que produzir o evento. Você sabe qual modelo está contratando.")}

{band("Conte o que você imagina.", "O briefing leva poucos minutos e organiza tudo o que a equipe precisa para responder.", btn("solicitar-proposta.html", "Solicitar proposta"))}
''', [])

PAGES['parceiros'] = ('Parceiros | N’ROTA', 'parceiros', f'''
{hero("Profissionais e fornecedores", "Faça parte da <em class='acc'>rede de eventos.</em>", "Uma vitrine para pessoas, equipes e empresas de eventos. Receba pedidos compatíveis com sua especialidade e sua região. Cadastro gratuito para pessoa física ou empresa.", btn("seja-parceiro.html", "Quero ser parceiro"))}

{section("Nichos", "Organizados para <em class='acc'>orçamentos certeiros.</em>", boxes([
    ('Produção', ul(['Produtores executivos e técnicos', 'Coordenadores e assistentes', 'Stage managers e produtores de palco'])),
    ('Montagem e estrutura', ul(['Montadores, cenografia e praticáveis', 'Palco, tendas, grades e geradores', 'Logística, carga e descarga'])),
    ('Técnica e audiovisual', ul(['PA, monitores, luz e LED', 'Operadores de som, luz e vídeo', 'Videomakers, fotógrafos e streaming'])),
    ('Hospitalidade e apoio', ul(['Catering e camarins', 'Roadies e backline', 'Recepção, brigada e apoio operacional'])),
], 'g4', 'box top'))}

{section("Como funciona", "Do cadastro aos <em class='acc'>pedidos.</em>", boxes([
    ('Cadastro', 'Nome comercial, responsável, cidades atendidas, contatos, portfólio e referências.'),
    ('Catálogo de serviços', 'Categorias, equipamentos, capacidade, equipe técnica, cobertura e disponibilidade.'),
    ('Validação', 'Documentação aplicável, segurança, experiência e capacidade operacional.'),
    ('Oportunidades', 'Briefings compatíveis com seu nicho e região, sem promessa de demanda.'),
    ('Condições comerciais', 'Comissão, taxa de indicação ou fee de produção definidos em contrato, quando houver.'),
    ('Avaliação contínua', 'Pontualidade, atendimento, qualidade de entrega e atualização cadastral.'),
]))}

{section("A jornada do cliente", "Como você <em class='acc'>é encontrado.</em>", steps([
    ('Encontrar', 'Busca por especialidade, cidade e data.'),
    ('Comparar', 'Perfis, portfólios, escopo e área atendida.'),
    ('Solicitar', 'Briefing com local, data, público e necessidades.'),
    ('Contratar', 'Contato direto ou mediação N’ROTA, conforme a opção.'),
    ('Produzir', 'Se contratado, coordenação e acompanhamento da equipe.'),
]))}

{section("Confiança", "Cadastrado <em class='acc'>não é verificado.</em>", '''<div class="grid g2">
  <div class="box"><h3>Perfil cadastrado</h3><p>Seus dados revisados pela equipe e publicados no catálogo de parceiros.</p></div>
  <div class="box"><h3>Parceiro verificado <small>Opcional</small></h3><p>Selo após verificação documental. Quem contrata vê a diferença na busca.</p></div>
</div>
<p class="rule"><strong>Sem promessas.</strong> A N’ROTA não promete qualidade, disponibilidade ou seguro sem validação prévia, nem volume mínimo de pedidos.</p>''')}

{band("Sua equipe na rede N’ROTA.", "Cadastro gratuito em três etapas.", btn("seja-parceiro.html", "Quero ser parceiro"))}
''', [])

PAGES['duvidas'] = ('Dúvidas | N’ROTA', 'duvidas', f'''
{hero("Dúvidas", "Antes de <em class='acc'>começar.</em>", "Respostas diretas sobre cadastro, contratação, parcerias e privacidade.",
     '<div class="toc"><a class="chip" href="#artistas-faq">Artistas</a><a class="chip" href="#contratantes-faq">Contratantes</a><a class="chip" href="#parceiros-faq">Parceiros</a><a class="chip" href="#privacidade-faq">Privacidade</a></div>')}
<section class="s"><div class="wrap">
  <div class="faq-group" id="artistas-faq"><h2>Para artistas</h2>{faq([
    ('O cadastro da banda é pago?', 'Não. Cadastro e presença no catálogo são gratuitos e não dependem de nenhum serviço pago ou de agenciamento.'),
    ('A N’ROTA garante shows?', 'Não. A plataforma organiza seu trabalho e facilita o contato com quem contrata, mas não garante contratação, audiência ou posição na busca.'),
    ('Meu cachê aparece no perfil?', 'Não. Condições comerciais ficam privadas e só são usadas em propostas que você autorizar.'),
    ('O que é o plano Destaque?', 'Por R$ 50, pagamento único, sua banda ganha um post de apresentação no feed e um Story salvo no Destaque do seu estilo, sem vencimento automático. <a href="artistas.html#planos">Ver planos</a>.'),
    ('Posso divulgar a data de um show?', 'Sim, nos Stories e nos Destaques do mês. O feed e os Reels são reservados à apresentação das bandas.'),
    ('Como atualizo meu perfil?', 'Por enquanto, pelo atendimento da equipe. A área Minha banda, para atualizar sozinho, chega numa próxima fase.'),
    ('Só aceitam rock?', 'O primeiro capítulo é o Rock N’ Rota. Samba, pagode, pop, sertanejo e MPB chegam em seguida. <a href="acesso-antecipado.html">Entre na lista</a> e marque seu estilo.'),
  ])}</div>
  <div class="faq-group" id="contratantes-faq"><h2>Para quem contrata</h2>{faq([
    ('Vocês cobram comissão?', 'No contato direto com a banda, não. A intermediação pelo produtor é opcional e tem condições combinadas por escrito antes de cada negócio.'),
    ('Disponibilidade no perfil é data confirmada?', 'Não. Os dias e turnos informados orientam a busca. Toda data precisa ser confirmada com a banda.'),
    ('Atendem fora do Distrito Federal?', 'Sim. Artistas, parceiros e eventos de todo o Brasil.'),
    ('Posso contratar estrutura além da banda?', 'Sim. Som, luz, palco, audiovisual, foto e vídeo, ou a produção completa. <a href="eventos.html">Veja como funciona</a>.'),
    ('Qual a diferença entre indicação e produção?', 'Na indicação, você contrata o parceiro diretamente. Na produção N’ROTA, nossa equipe coordena tudo, com taxa e escopo em contrato.'),
  ])}</div>
  <div class="faq-group" id="parceiros-faq"><h2>Para parceiros</h2>{faq([
    ('Quanto custa entrar na rede?', 'O cadastro é gratuito. Comissões ou taxas, quando houver, são definidas em contrato antes de qualquer serviço.'),
    ('Vou receber pedidos?', 'Você recebe briefings compatíveis com seu nicho e região. Não há promessa de volume mínimo.'),
    ('O que é o selo de verificado?', 'Um selo opcional, concedido após verificação documental, que diferencia seu perfil na busca.'),
  ])}</div>
  <div class="faq-group" id="privacidade-faq"><h2>Privacidade</h2>{faq([
    ('Quem vê meus dados?', 'O perfil público mostra só o que você autorizou. CPF, CNPJ, contatos de gestão e condições comerciais ficam restritos à equipe.'),
    ('Posso corrigir ou excluir meus dados?', 'Sim, a qualquer momento, pelo atendimento da equipe.'),
    ('Vou receber e-mails de marketing?', 'Só se você autorizar, em um aceite separado do cadastro.'),
  ])}</div>
</div></section>
{band("Ainda com dúvida?", "Envie um briefing e nossa equipe responde pelo canal que você preferir.", btn("solicitar-proposta.html", "Falar com o produtor"))}
''', [])

for slug, title in [('cadastro-banda', 'Cadastre sua banda'), ('solicitar-proposta', 'Solicitar proposta'), ('seja-parceiro', 'Quero ser parceiro'), ('acesso-antecipado', 'Acesso antecipado')]:
    PAGES[slug] = (f'{title} | N’ROTA', 'form', f'<div class="wrap" data-form="{slug}"></div>', ['forms'])


def render(slug, standalone):
    title, page, body, extra = PAGES[slug]
    scripts = '<script src="assets/site.js"></script>' + ''.join(f'<script src="assets/{s}.js"></script>' for s in extra)
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n<link rel="stylesheet" href="assets/nrota.css">'
    content = f'<n-header></n-header>\n<main>{body}</main>\n<n-footer></n-footer>\n{scripts}'
    if slug == 'index' and not standalone:
        return f'{head}\n<script>document.body.dataset.page="{page}"</script>\n{content}\n'
    return f'<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n{head}\n</head>\n<body data-page="{page}">\n{content}\n</body>\n</html>\n'


out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
standalone = len(sys.argv) > 1
for slug in PAGES:
    (out / f'{slug}.html').write_text(render(slug, standalone), encoding='utf-8')
print(len(PAGES), 'páginas em', out)
