import pathlib, sys

ROOT = pathlib.Path(__file__).parent
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Familjen+Grotesk:wght@400;500;600&family=Martian+Mono:wght@400;500&display=swap">')
ICON = {
    'search': '<circle cx="8" cy="8" r="5.5"/><path d="m12.2 12.2 3.8 3.8"/>',
    'check': '<path d="M3 9.5 7 13l8-8"/>',
    'chat': '<path d="M3 4h12v8H8l-4 3v-3H3z"/>',
    'note': '<path d="M6 14V4l9-2v10"/><circle cx="4" cy="14" r="2"/><circle cx="13" cy="12" r="2"/>',
}
svg = lambda name, s=18: f'<svg width="{s}" height="{s}" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>'
btn = lambda href, label, kind='o': f'<a class="btn btn-{kind}" href="{href}">{label}{" <span class=arr>→</span>" if kind == "o" else ""}</a>'
EQ = '<span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>'

ARTISTS = [
    ('artista-cantora', 'Íris Monteiro', 'Soul rock · Brasília/DF'),
    ('artista-guitarrista', 'Los Faroles', 'Hard rock · Goiânia/GO'),
    ('artista-baterista', 'Mei & Os Satélites', 'Indie · São Paulo/SP'),
    ('artista-baixista', 'Groove Cerrado', 'Blues rock · Brasília/DF'),
    ('artista-violao', 'Anaya Rao', 'Acústico · Belo Horizonte/MG'),
    ('artista-vocalista', 'Contramão', 'Rock nacional · Brasília/DF'),
    ('artista-tecladista', 'Vera Prisma', 'Synth rock · Curitiba/PR'),
]
STYLES = ['Rock clássico', 'Hard rock', 'Blues rock', 'Indie', 'Metal', 'Pop rock', 'Punk rock']
SOON = ['Samba', 'Pagode', 'Pop', 'Sertanejo', 'MPB']


def ticker(words, cls):
    run = ''.join(f'<span>{w}</span>' for w in words)
    return f'<div class="ticker {cls}" aria-hidden="true"><div class="track">{run}{run}</div></div>'


def heading(label, title, lead='', side=''):
    head = f'<span class="label" data-reveal>{label}</span><h2 data-reveal style="--d:1">{title}</h2>' + (f'<p class="lead" data-reveal style="--d:2">{lead}</p>' if lead else '')
    return f'<div class="s-head row"><div style="display:grid;gap:18px">{head}</div>{side}</div>' if side else f'<div class="s-head">{head}</div>'


def section(label, title, body, lead='', side='', sid=''):
    return f'<section class="s"{f" id={sid}" if sid else ""}><div class="wrap">{heading(label, title, lead, side)}{body}</div></section>'


def phero(label, title, lead, img, ctas=''):
    return f'''<section class="phero">
  <div class="bg"><img data-img="{img}" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <span class="label">{label}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    {f'<div class="ctas">{ctas}</div>' if ctas else ''}
    <span class="credit">Imagem ilustrativa · artista fictício</span>
  </div>
</section>'''


def band(title, text, ctas):
    return f'<section class="s"><div class="wrap"><div class="band" data-reveal><div><span class="label">{EQ} N’ROTA</span><h2>{title}</h2><p class="lead">{text}</p></div><div class="ctas">{ctas}</div><span class="vinyl" aria-hidden="true"></span></div></div></section>'


def cards(items, cols='g3', cls='card'):
    out = ''
    for i, (t, body) in enumerate(items):
        body = body if body.startswith('<') else f'<p>{body}</p>'
        out += f'<div class="{cls}" data-reveal style="--d:{i % 4}"><h3>{t}</h3>{body}</div>'
    return f'<div class="grid {cols}">{out}</div>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def steps(items, cls='', start=0):
    return f'<ol class="steps {cls}" style="counter-reset:st {start}">' + ''.join(f'<li data-reveal style="--d:{i}"><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(items)) + '</ol>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'


def reel(artists=ARTISTS):
    figs = ''.join(f'<figure class="artist" data-reveal style="--d:{i % 4}"><img data-img="{img}" alt="{name}, artista fictício" loading="lazy"><span class="tag glass">Exemplo</span><figcaption class="glass"><strong>{name}</strong><span>{meta}</span></figcaption></figure>' for i, (img, name, meta) in enumerate(artists))
    return f'<div class="reel">{figs}</div><p class="reel-note">Artistas e imagens fictícios, criados para ilustrar o catálogo. Arraste para o lado.</p>'


PLANS = f'''<div class="snap fit">
  <article class="card"><span class="label">Start</span><span class="price">Grátis</span>
    {ul(['Perfil no catálogo nacional', 'Repertório pesquisável, fotos e vídeos', 'Contato direto de quem contrata'])}
    {btn("cadastro-banda.html", "Cadastrar banda", "g")}</article>
  <article class="card hl"><span class="label">Destaque</span><span class="price">R$ 50<small>pagamento único</small></span>
    {ul(['Post de apresentação no feed do gênero', 'Story salvo no Destaque do seu estilo', 'Sem vencimento automático'])}
    {btn("cadastro-banda.html", "Quero aparecer")}</article>
  <article class="card"><span class="label">Impulso</span><span class="price">Sob orçamento</span>
    {ul(['Reels de performance e trajetória', 'Stories e calendário editorial', 'Campanhas com verba de mídia à parte'])}
    {btn("solicitar-proposta.html", "Pedir orçamento", "g")}</article>
</div>
<div class="grid g2" style="margin-top:14px">
  <article class="card dash" data-reveal><span class="label">Pro · sob proposta</span><h3>Posicionamento e material comercial</h3>{ul(['Diagnóstico artístico, release e portfólio', 'Acompanhamento e planejamento de divulgação'])}</article>
  <article class="card dash" data-reveal style="--d:1"><span class="label">Agency · sob contrato</span><h3>Representação e negociação</h3>{ul(['Prospecção de casas, festivais e empresas', 'Comissão só sobre negócio fechado, combinada antes'])}</article>
</div>'''

PAGES = {}

PAGES['index'] = ('N’ROTA', 'inicio', f'''
<section class="hero">
  <div class="beams" aria-hidden="true"><span class="beam b1"></span><span class="beam b2"></span><span class="beam b3"></span></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="label">{EQ} Rock N’ Rota · capítulo 01</span>
      <h1><span>Seu som</span><span class="stroke">merece</span><span class="lil">ir mais</span><span>longe.</span></h1>
      <p class="lead">Catálogo nacional de artistas com repertório pesquisável. Quem contrata encontra pela música, pelo estilo, pelo evento ou pela cidade.</p>
      <div class="ctas">{btn("cadastro-banda.html", "Cadastrar minha banda")}{btn("solicitar-proposta.html", "Fazer meu evento", "g")}</div>
      <p class="fine">Cadastro gratuito · contato direto sem comissão</p>
    </div>
    <div class="deck" aria-label="Artistas fictícios ilustrativos">
      <div class="ph p1"><img data-img="artista-guitarrista" alt="" fetchpriority="high"></div>
      <div class="ph p2"><img data-img="artista-cantora" alt="" fetchpriority="high"></div>
      <div class="ph p3"><img data-img="artista-baterista" alt="" fetchpriority="high"></div>
      <div class="chip-f glass c1"><span class="dot">{svg("search", 16)}</span><div><small>Busca no repertório</small><strong data-typer>Everlong</strong><span class="caret"></span></div></div>
      <div class="chip-f glass c2"><span class="dot">{svg("note", 16)}</span><div><small>Estilo</small><strong>Soul rock · DF</strong></div></div>
      <div class="chip-f glass c3"><span class="dot">{svg("check", 16)}</span><div><small>Status</small><strong>Perfil revisado</strong></div></div>
    </div>
  </div>
</section>

<div class="tickers">{ticker(STYLES, "t-org")}
{ticker([f"{g} · em breve" for g in SOON] + ["Rock · ativo"], "t-lil alt")}</div>

{section("01 — Vitrine", "Talentos de <span class='stroke'>todo</span> canto.", reel(), "Cada perfil reúne história, repertório, fotos, vídeos e formas de contato. Um lugar para ser descoberto por quem contrata.")}

<section class="s">
  <div class="wrap flow">
    <div style="display:grid;gap:18px;align-content:start">
      <span class="label" data-reveal>02 — Busca</span>
      <h2 data-reveal style="--d:1">Quem procura acha <span class="lil">quem toca.</span></h2>
      <p class="lead" data-reveal style="--d:2">Cada resposta do cadastro vira filtro: estilo, repertório, formação, região e agenda habitual.</p>
      <ul class="ticks" data-reveal style="--d:3">
        <li><span class="ico">{svg("search")}</span><span><b>Busca pelo repertório</b>Por artista ou música, não só pelo nome da banda.</span></li>
        <li><span class="ico">{svg("check")}</span><span><b>Perfis revisados</b>Dados e materiais conferidos antes de publicar.</span></li>
        <li><span class="ico">{svg("chat")}</span><span><b>Contato sem atrito</b>Direto com a banda ou com apoio do produtor.</span></li>
      </ul>
    </div>
    <div class="stage" aria-label="Exemplos ilustrativos de buscas e perfis">
      <div class="lane"><div class="lane-track" data-lane="art"></div></div>
      <div class="lane rev"><div class="lane-track" data-lane="ask"></div></div>
    </div>
  </div>
</section>

{section("03 — Caminhos", "Escolha a <span class='org'>sua</span> entrada.", f'''<div class="snap fit">
  <a class="card photo" href="artistas.html" data-reveal><img data-img="artista-baixista" alt="" loading="lazy"><div class="in"><span class="label">Para artistas</span><h3>Perfil gratuito no catálogo</h3><p>Repertório pesquisável e divulgação opcional no Instagram.</p><span class="more">Conhecer →</span></div></a>
  <a class="card photo" href="eventos.html" data-reveal style="--d:1"><img data-img="palco-banda" alt="" loading="lazy"><div class="in"><span class="label">Para quem contrata</span><h3>Do artista ao evento completo</h3><p>Bandas, DJs, som, luz, palco e produção coordenada.</p><span class="more">Conhecer →</span></div></a>
  <a class="card photo" href="parceiros.html" data-reveal style="--d:2"><img data-img="artista-tecladista" alt="" loading="lazy"><div class="in"><span class="label">Para fornecedores</span><h3>Rede de profissionais de eventos</h3><p>Pedidos compatíveis com seu nicho e sua região.</p><span class="more">Conhecer →</span></div></a>
</div>''')}

{section("04 — Como funciona", "Da banda ao <span class='stroke'>palco.</span>", steps([
    ('Cadastro', 'A banda cria o perfil gratuito, com repertório música a música.'),
    ('Validação', 'Nossa equipe revisa dados e materiais antes de publicar.'),
    ('Catálogo', 'O perfil entra nos filtros por estilo, evento, formação e região.'),
    ('Descoberta', 'Quem contrata pesquisa por artista, música, cidade ou agenda.'),
    ('Contato', 'Direto com a banda ou com apoio do produtor N’ROTA.'),
]), side='<a class="more" href="como-funciona.html">Ver em detalhes →</a>')}

{band("O catálogo abre em breve.", "Entre na lista e seja avisado quando a busca completa estiver no ar.", btn("acesso-antecipado.html", "Quero acesso antecipado"))}
''', [])

PAGES['como-funciona'] = ('Como funciona | N’ROTA', 'como-funciona', f'''
{phero("Como funciona", "Uma plataforma. <span class='lil'>Duas entradas.</span>", "Quem oferece música e quem procura música se encontram num catálogo organizado, revisado e pesquisável.", "palco-banda", btn("cadastro-banda.html", "Cadastrar minha banda") + btn("solicitar-proposta.html", "Fazer meu evento", "g"))}

{section("01 — Jornada", "Da banda ao <span class='stroke'>palco.</span>", steps([
    ('Cadastro', 'Formulário em etapas, com campos que mudam conforme as respostas. Dá para salvar e continuar depois.'),
    ('Validação', 'A equipe confere dados, fotos e repertório antes de tornar o perfil público.'),
    ('Catálogo', 'As respostas viram categorias pesquisáveis, não textos soltos.'),
    ('Descoberta', 'Busca por estilo, música, artista, evento, cidade ou agenda habitual.'),
    ('Contato', 'Direto com a banda pelo canal autorizado, ou com apoio do produtor.'),
]))}

{section("02 — Filtros", "O que faz a busca <span class='org'>funcionar.</span>", cards([
    ('Estilo', 'Hard rock, rock clássico, punk, metal, indie, pop rock e os próximos gêneros.'),
    ('Artistas e músicas', 'Queen, Legião Urbana, Foo Fighters. Cada música do repertório é pesquisável.'),
    ('Evento', 'Casamento, festa particular, corporativo, bar, festival, evento público.'),
    ('Formação', 'Solo, duo, trio ou banda completa.'),
    ('Agenda', 'Dias habituais, turnos e antecedência mínima.'),
    ('Região', 'Cidade-base, outros estados e disponibilidade para viajar.'),
    ('Formato', 'Acústico, elétrico, tributo ou autoral.'),
    ('Orçamento', 'Faixa indicativa, só quando a banda autoriza.'),
], 'g4'))}

{section("03 — Diferencial", "Repertório <span class='stroke'>pesquisável.</span>", f'''<div class="grid g2">
  <div class="card" data-reveal><span class="label">Como a banda cadastra</span><p class="example">Música → <span>Everlong</span><br>Artista → <span>Foo Fighters</span><br>Década → <span>1990</span><br>Estilo → <span>rock alternativo</span></p><p>A mesma música pode entrar em mais de um setlist, como casamento ou festival.</p></div>
  <div class="card" data-reveal style="--d:1"><span class="label">Como o contratante encontra</span><p class="example">Busca → <span>“Foo Fighters”</span><br>ou → <span>“Everlong”</span></p><p>O resultado mostra as bandas cujo repertório tem aquele artista ou aquela música. PDFs e links continuam aceitos como complemento.</p></div>
</div>''', "Guardamos cada música com o artista original, em vez de um PDF anexado.")}

{section("04 — Contratação", "Dois caminhos. <span class='lil'>Você escolhe.</span>", f'''<div class="grid g2">
  <div class="card dash" data-reveal><h3>Contato com a banda <small>Sem comissão</small></h3><p>Abre o canal autorizado pela banda. A negociação acontece direto entre as partes.</p></div>
  <div class="card dash" data-reveal style="--d:1"><h3>Fale com o produtor <small>Opcional</small></h3><p>Você envia o briefing, recebe sugestões e pode contar com intermediação, mediante autorização e condições acordadas.</p></div>
</div>
<p class="rule"><strong>Disponibilidade não é reserva.</strong> Os dias e turnos do perfil orientam a busca. Toda data precisa ser confirmada com a banda.</p>''')}

{section("05 — Confiança", "Regras claras <span class='org'>para todos.</span>", cards([
    ('Revisão antes de publicar', 'Dados e materiais são conferidos antes de o perfil ficar público.'),
    ('Dados comerciais privados', 'Cachê e condições nunca aparecem no perfil público.'),
    ('Autorização expressa', 'Fotos, vídeos e contatos só são usados com o seu aceite.'),
    ('Sem prazo de vencimento', 'O perfil e o post de Destaque não expiram por pacote.'),
    ('Sem promessas', 'Nenhuma garantia de audiência, contratação ou posição nos resultados.'),
    ('Seus dados, seu controle', 'Você pode pedir correção ou exclusão quando quiser.'),
]))}

{band("Pronto para começar?", "Cadastre sua banda gratuitamente ou conte o que você precisa para o seu evento.", btn("cadastro-banda.html", "Cadastrar banda") + btn("solicitar-proposta.html", "Solicitar proposta", "g"))}
''', [])

PAGES['artistas'] = ('Para artistas | N’ROTA', 'artistas', f'''
{phero("Para artistas", "Seu trabalho inteiro <span class='lil'>num só lugar.</span>", "Um perfil profissional gratuito, com repertório pesquisável, para ser encontrado por quem contrata em todo o Brasil. Sem exclusividade e sem comissão no contato direto.", "artista-guitarrista", btn("cadastro-banda.html", "Cadastrar minha banda") + btn("#planos", "Ver planos", "g"))}

{section("01 — Seu perfil", "O que o contratante <span class='stroke'>vê.</span>", cards([
    ('História e influências', 'Quem é a banda, de onde vem e o que inspira o som.'),
    ('Fotos, vídeos e links', 'Material oficial e redes num só lugar.'),
    ('Setlist e repertórios', 'Música por música, por ocasião e por tema.'),
    ('Eventos e formações', 'Onde você toca e em quais formatos.'),
    ('Duração e agenda', 'Sets, intervalos, dias e turnos habituais.'),
    ('Rider e região', 'Estrutura técnica e até onde você vai.'),
]))}

{section("02 — Inspiração", "Perfis que <span class='org'>contam histórias.</span>", reel(ARTISTS[3:] + ARTISTS[:3]))}

{section("03 — Cadastro", "Dez etapas, <span class='lil'>no seu tempo.</span>", steps([
    ('Identificação', 'Nome, responsável, contatos de gestão, cidade, links e fotos.'),
    ('Identidade', 'Estilo principal, secundários, proposta e referências.'),
    ('Repertório', 'Música, artista original, década e estilo.'),
    ('Eventos', 'Casamentos, bares, festivais, corporativos e mais.'),
    ('Formações', 'Integrantes, formatos, duração e sets.'),
]) + '<div style="height:20px"></div>' + steps([
    ('Agenda', 'Dias, turnos, antecedência e datas bloqueadas.'),
    ('Deslocamento', 'Cidade-base, estados atendidos e viagens.'),
    ('Técnica', 'Rider, mapa de palco e equipamentos.'),
    ('Comercial', 'Cachê e pagamento. Sempre privado.'),
    ('Autorizações', 'Contato exibido, aceites e serviços opcionais.'),
], start=5), "Os campos mudam conforme suas respostas. O progresso fica salvo e você continua depois.")}

{section("04 — Planos", "Comece grátis. <span class='stroke'>Cresça.</span>", PLANS + '<p class="rule"><strong>Seu perfil não depende de plano pago.</strong> Os serviços são opcionais e não interferem na presença no catálogo. Valores sujeitos a validação antes do lançamento.</p>', sid="planos")}

{section("05 — Instagram", "Cada formato, <span class='lil'>uma função.</span>", cards([
    ('Feed', 'Apresentação institucional da banda, sem data de show.'),
    ('Reels', 'Performance, trajetória, entrevistas e repertório. Nunca divulgação de datas.'),
    ('Stories', 'Datas, locais, horários e chamadas dos seus shows.'),
    ('Destaques', 'Por estilo: bandas. Por mês: agenda de eventos.'),
], 'g4'), "O feed apresenta bandas. A agenda de shows aparece só nos Stories e nos Destaques do mês.")}

{section("06 — Agenciamento", "Representação com <span class='org'>regras claras.</span>", f'''<div class="grid g2">
  <div class="card" data-reveal><h3>Como funciona</h3>{ul(['Adesão opcional e sujeita à avaliação da equipe', 'A produtora prospecta casas, festivais, empresas e eventos', 'Apresenta propostas, negocia e acompanha cada oportunidade'])}</div>
  <div class="card" data-reveal style="--d:1"><h3>Remuneração e contrato</h3>{ul(['Referência inicial de 10% sobre negócios fechados por intermediação, a negociar', 'Prazo, território e exclusividade definidos em contrato', 'Sem promessa de quantidade mínima de shows'])}</div>
</div>''', "Representação comercial é diferente de comprar um pacote de divulgação.")}

{band("Sua banda no catálogo. De graça.", "Alguns minutos por etapa. A equipe revisa e avisa quando o perfil for publicado.", btn("cadastro-banda.html", "Cadastrar minha banda"))}
''', [])

PAGES['eventos'] = ('Faça seu evento | N’ROTA', 'eventos', f'''
{phero("Faça seu evento com a gente", "Do artista ao <span class='lil'>evento completo.</span>", "O som certo, a estrutura adequada e profissionais em quem confiar. Precisa só de uma banda ou quer ajuda com toda a produção? Conte o que você imagina.", "palco-banda", btn("solicitar-proposta.html", "Solicitar proposta"))}

<section class="s"><div class="wrap"><div class="snap fit">
  <a class="card photo" href="solicitar-proposta.html#artista" data-reveal><img data-img="artista-cantora" alt="" loading="lazy"><div class="in"><span class="label">Atração</span><h3>Quero um artista</h3><p>Bandas, artistas solo, DJs, tributos e formatos acústicos.</p><span class="more">Solicitar proposta →</span></div></a>
  <a class="card photo" href="solicitar-proposta.html#estrutura" data-reveal style="--d:1"><img data-img="artista-tecladista" alt="" loading="lazy"><div class="in"><span class="label">Estrutura</span><h3>Preciso de estrutura</h3><p>Som, luz, palco, painéis de LED, foto e vídeo.</p><span class="more">Solicitar proposta →</span></div></a>
  <a class="card photo" href="solicitar-proposta.html#completo" data-reveal style="--d:2"><img data-img="palco-banda" alt="" loading="lazy"><div class="in"><span class="label">Produção</span><h3>Quero o evento completo</h3><p>Coordenação de fornecedores, cronograma e acompanhamento.</p><span class="more">Solicitar proposta →</span></div></a>
</div></div></section>

{section("01 — Serviços", "Avulsos ou <span class='stroke'>combinados.</span>", cards([
    ('Atrações artísticas', 'Bandas, artistas solo, DJs, tributos, repertórios e formatos acústicos.'),
    ('Som e iluminação', 'PA, consoles, microfones, monitores, iluminação de palco e operadores.'),
    ('Estruturas', 'Palcos, praticáveis, coberturas, tendas, grids, treliças e montagem.'),
    ('Audiovisual', 'Painéis de LED, projetores, telões, transmissão e técnicos.'),
    ('Conteúdo e registro', 'Videomakers, fotografia, aftermovie, multicâmeras e edição.'),
    ('Produção e operação', 'Coordenação, fornecedores, logística, cronograma e acompanhamento.'),
]), "Conforme a disponibilidade dos artistas e parceiros, em Brasília e em outras regiões do Brasil.")}

{section("02 — Como funciona", "Quatro passos <span class='org'>até o palco.</span>", steps([
    ('Escolha', 'Artistas, DJ, som e luz, palco, foto e vídeo ou produção completa.'),
    ('Conte', 'Tipo, data, local, público, formato e faixa de investimento.'),
    ('Receba', 'Triagem da equipe e proposta ou indicação de profissionais.'),
    ('Confirme', 'Orçamento detalhado, responsabilidades, contrato e cronograma.'),
], 's4'))}

{section("03 — Modelos", "Transparência <span class='lil'>desde o início.</span>", f'''<div class="grid g2">
  <div class="card dash" data-reveal><h3>Conexão e indicação <small>Modelo A</small></h3><p>Recebemos o briefing e apresentamos artistas ou fornecedores. A contratação pode ser direta entre você e o parceiro, com papéis, valores e eventual remuneração de indicação informados antes.</p></div>
  <div class="card dash" data-reveal style="--d:1"><h3>Produção N’ROTA <small>Modelo B</small></h3><p>A equipe monta uma proposta integrada e, se contratada, coordena parceiros, cronograma e entregas. Taxa de produção, escopo e responsabilidades ficam em contrato.</p></div>
</div>
<p class="rule"><strong>Nada sem confirmação.</strong> Preço, disponibilidade e entrega só valem depois do retorno do artista ou fornecedor.</p>''', "Intermediar fornecedores não é o mesmo que produzir o evento. Você sabe qual modelo está contratando.")}

{band("Conte o que você imagina.", "O briefing leva poucos minutos e organiza tudo o que a equipe precisa para responder.", btn("solicitar-proposta.html", "Solicitar proposta"))}
''', [])

PAGES['parceiros'] = ('Parceiros | N’ROTA', 'parceiros', f'''
{phero("Profissionais e fornecedores", "Faça parte da <span class='lil'>rede de eventos.</span>", "Uma vitrine para pessoas, equipes e empresas de eventos. Receba pedidos compatíveis com sua especialidade e região. Cadastro gratuito para pessoa física ou empresa.", "artista-tecladista", btn("seja-parceiro.html", "Quero ser parceiro"))}

{section("01 — Nichos", "Organizados para <span class='stroke'>orçar certo.</span>", cards([
    ('Produção', ul(['Produtores executivos e técnicos', 'Coordenadores e assistentes', 'Stage managers'])),
    ('Montagem e estrutura', ul(['Montadores, cenografia e praticáveis', 'Palco, tendas, grades e geradores', 'Logística, carga e descarga'])),
    ('Técnica e audiovisual', ul(['PA, monitores, luz e LED', 'Operadores de som, luz e vídeo', 'Videomakers, fotógrafos e streaming'])),
    ('Hospitalidade e apoio', ul(['Catering e camarins', 'Roadies e backline', 'Recepção, brigada e apoio'])),
], 'g4'))}

{section("02 — Como funciona", "Do cadastro <span class='org'>aos pedidos.</span>", cards([
    ('Cadastro', 'Nome comercial, responsável, cidades atendidas, contatos, portfólio e referências.'),
    ('Catálogo de serviços', 'Categorias, equipamentos, capacidade, equipe técnica, cobertura e disponibilidade.'),
    ('Validação', 'Documentação aplicável, segurança, experiência e capacidade operacional.'),
    ('Oportunidades', 'Briefings compatíveis com seu nicho e região, sem promessa de demanda.'),
    ('Condições', 'Comissão, taxa de indicação ou fee de produção definidos em contrato, quando houver.'),
    ('Avaliação contínua', 'Pontualidade, atendimento, qualidade de entrega e atualização cadastral.'),
]))}

{section("03 — Jornada do cliente", "Como você <span class='lil'>é encontrado.</span>", steps([
    ('Encontrar', 'Busca por especialidade, cidade e data.'),
    ('Comparar', 'Perfis, portfólios, escopo e área atendida.'),
    ('Solicitar', 'Briefing com local, data, público e necessidades.'),
    ('Contratar', 'Contato direto ou mediação N’ROTA, conforme a opção.'),
    ('Produzir', 'Se contratado, coordenação e acompanhamento da equipe.'),
]))}

{section("04 — Confiança", "Cadastrado <span class='stroke'>≠</span> verificado.", f'''<div class="grid g2">
  <div class="card" data-reveal><h3>Perfil cadastrado</h3><p>Dados revisados pela equipe e publicados no catálogo de parceiros.</p></div>
  <div class="card hl" data-reveal style="--d:1"><h3>Parceiro verificado <small>Opcional</small></h3><p>Selo após verificação documental. Quem contrata vê a diferença na busca.</p></div>
</div>
<p class="rule"><strong>Sem promessas.</strong> A N’ROTA não promete qualidade, disponibilidade ou seguro sem validação prévia, nem volume mínimo de pedidos.</p>''')}

{band("Sua equipe na rede N’ROTA.", "Cadastro gratuito em três etapas.", btn("seja-parceiro.html", "Quero ser parceiro"))}
''', [])

PAGES['duvidas'] = ('Dúvidas | N’ROTA', 'duvidas', f'''
{phero("Dúvidas", "Antes de <span class='lil'>começar.</span>", "Respostas diretas sobre cadastro, contratação, parcerias e privacidade.", "artista-violao",
     '<div class="toc"><a class="chip" href="#artistas-faq">Artistas</a><a class="chip" href="#contratantes-faq">Contratantes</a><a class="chip" href="#parceiros-faq">Parceiros</a><a class="chip" href="#privacidade-faq">Privacidade</a></div>')}
<section class="s"><div class="wrap">
  <div class="faq-group" id="artistas-faq"><span class="label">01</span><h2>Para artistas</h2>{faq([
    ('O cadastro da banda é pago?', 'Não. Cadastro e presença no catálogo são gratuitos e não dependem de nenhum serviço pago ou de agenciamento.'),
    ('A N’ROTA garante shows?', 'Não. A plataforma organiza seu trabalho e facilita o contato com quem contrata, mas não garante contratação, audiência ou posição na busca.'),
    ('Meu cachê aparece no perfil?', 'Não. Condições comerciais ficam privadas e só são usadas em propostas que você autorizar.'),
    ('O que é o plano Destaque?', 'Por R$ 50, pagamento único, sua banda ganha um post de apresentação no feed e um Story salvo no Destaque do seu estilo, sem vencimento automático. <a href="artistas.html#planos">Ver planos</a>.'),
    ('Posso divulgar a data de um show?', 'Sim, nos Stories e nos Destaques do mês. O feed e os Reels são reservados à apresentação das bandas.'),
    ('Como atualizo meu perfil?', 'Por enquanto, pelo atendimento da equipe. A área Minha banda, para atualizar sozinho, chega numa próxima fase.'),
    ('Só aceitam rock?', 'O primeiro capítulo é o Rock N’ Rota. Samba, pagode, pop, sertanejo e MPB chegam em seguida. <a href="acesso-antecipado.html">Entre na lista</a> e marque seu estilo.'),
  ])}</div>
  <div class="faq-group" id="contratantes-faq"><span class="label">02</span><h2>Para quem contrata</h2>{faq([
    ('Vocês cobram comissão?', 'No contato direto com a banda, não. A intermediação pelo produtor é opcional e tem condições combinadas por escrito antes de cada negócio.'),
    ('Disponibilidade no perfil é data confirmada?', 'Não. Os dias e turnos informados orientam a busca. Toda data precisa ser confirmada com a banda.'),
    ('Atendem fora do Distrito Federal?', 'Sim. Artistas, parceiros e eventos de todo o Brasil.'),
    ('Posso contratar estrutura além da banda?', 'Sim. Som, luz, palco, audiovisual, foto e vídeo, ou a produção completa. <a href="eventos.html">Veja como funciona</a>.'),
    ('Qual a diferença entre indicação e produção?', 'Na indicação, você contrata o parceiro diretamente. Na produção N’ROTA, a equipe coordena tudo, com taxa e escopo em contrato.'),
  ])}</div>
  <div class="faq-group" id="parceiros-faq"><span class="label">03</span><h2>Para parceiros</h2>{faq([
    ('Quanto custa entrar na rede?', 'O cadastro é gratuito. Comissões ou taxas, quando houver, são definidas em contrato antes de qualquer serviço.'),
    ('Vou receber pedidos?', 'Você recebe briefings compatíveis com seu nicho e região. Não há promessa de volume mínimo.'),
    ('O que é o selo de verificado?', 'Um selo opcional, concedido após verificação documental, que diferencia seu perfil na busca.'),
  ])}</div>
  <div class="faq-group" id="privacidade-faq"><span class="label">04</span><h2>Privacidade</h2>{faq([
    ('Quem vê meus dados?', 'O perfil público mostra só o que você autorizou. CPF, CNPJ, contatos de gestão e condições comerciais ficam restritos à equipe.'),
    ('Posso corrigir ou excluir meus dados?', 'Sim, a qualquer momento, pelo atendimento da equipe.'),
    ('Vou receber e-mails de marketing?', 'Só se você autorizar, em um aceite separado do cadastro.'),
  ])}</div>
</div></section>
{band("Ainda com dúvida?", "Envie um briefing e a equipe responde pelo canal que você preferir.", btn("solicitar-proposta.html", "Falar com o produtor"))}
''', [])

PAGES['rebeca'] = ('Rebeca Catarina | N’ROTA', 'rebeca', f'''
<section class="perfil wrap">
  <figure class="perfil-foto">
    <img data-img="rebeca-lilas" alt="Rebeca Catarina sorrindo ao lado do palco, em tratamento gráfico lilás" fetchpriority="high">
    <span class="glass perfil-tag">Idealização e produção</span>
  </figure>
  <div class="perfil-txt">
    <span class="label" data-reveal>Quem está por trás</span>
    <h1 data-reveal style="--d:1"><span>Rebeca</span> <span class="stroke">Catarina</span></h1>
    <p class="lead" data-reveal style="--d:2">Produtora e idealizadora da N’ROTA. Passou a vida entre passagem de som, camarim e pista, e transformou o que viu ali numa ideia simples: banda boa precisa ser encontrada.</p>
    <dl class="fatos" data-reveal style="--d:3">
      <div><dt>Função</dt><dd>Curadoria e produção</dd></div>
      <div><dt>Base</dt><dd>Brasília/DF</dd></div>
      <div><dt>Trilha</dt><dd>Rock, metal e o que vier</dd></div>
    </dl>
    <div class="ctas" data-reveal style="--d:4">{btn("solicitar-proposta.html", "Falar com a Rebeca")}{btn("cadastro-banda.html", "Cadastrar minha banda", "g")}</div>
  </div>
</section>
<section class="s"><div class="wrap">
  <blockquote class="citacao" data-reveal>“Seu som merece ir mais longe. A gente só ajuda o caminho a aparecer.”<cite>Rebeca Catarina</cite></blockquote>
  <div class="grid g3">
    <article class="card" data-reveal><span class="label">01</span><h3>Olhar de quem já esteve no palco</h3><p>Cada perfil é revisado pensando em quem toca e em quem contrata.</p></article>
    <article class="card" data-reveal style="--d:1"><span class="label">02</span><h3>Atendimento de gente</h3><p>Briefing, dúvida ou proposta: quem responde é a equipe, sem robô no meio.</p></article>
    <article class="card" data-reveal style="--d:2"><span class="label">03</span><h3>Rota aberta</h3><p>Começa no rock e abre espaço para samba, pagode, pop, sertanejo e MPB.</p></article>
  </div>
</div></section>
<section class="s"><div class="wrap">
  {heading("Bastidores", "Luz, estrada e <span class='lil'>som alto.</span>")}
  <div class="duo">
    <figure class="duo-f" data-reveal><img data-img="rebeca-palco" alt="Rebeca fotografando o público do palco, em tratamento laranja" loading="lazy"></figure>
    <figure class="duo-f" data-reveal style="--d:1"><img data-img="rebeca-luz" alt="Rebeca em contraluz sob feixes de luz do show, em tratamento violeta" loading="lazy"></figure>
  </div>
  <p class="reel-note">Perfil de exemplo, com texto ilustrativo. Fotos com tratamento gráfico.</p>
</div></section>
{band("Vamos colocar sua banda na rota?", "Cadastro gratuito e contato direto com quem produz.", btn("cadastro-banda.html", "Cadastrar banda"))}
''', [])

for slug, title in [('cadastro-banda', 'Cadastre sua banda'), ('solicitar-proposta', 'Solicitar proposta'), ('seja-parceiro', 'Quero ser parceiro'), ('acesso-antecipado', 'Acesso antecipado')]:
    PAGES[slug] = (f'{title} | N’ROTA', 'form', f'<div class="wrap" data-form="{slug}"></div>', ['forms'])


def render(slug, standalone):
    title, page, body, extra = PAGES[slug]
    scripts = '<script src="assets/site.js"></script>' + ''.join(f'<script src="assets/{s}.js"></script>' for s in extra)
    head = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="theme-color" content="#07060a">\n'
            f'<meta name="description" content="N’ROTA: catálogo, divulgação e contratação musical. Cadastro gratuito para artistas.">\n{FONTS}\n<link rel="stylesheet" href="assets/nrota.css">')
    content = f'<n-header></n-header>\n<main>{body}</main>\n<n-footer></n-footer>\n{scripts}'
    if slug == 'index' and not standalone:
        return f'{head}\n<script>document.body.dataset.page="{page}"</script>\n{content}\n'
    return f'<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n{head}\n</head>\n<body data-page="{page}">\n{content}\n</body>\n</html>\n'


out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
standalone = len(sys.argv) > 1
for slug in PAGES:
    (out / f'{slug}.html').write_text(render(slug, standalone), encoding='utf-8')
print(len(PAGES), 'páginas em', out)
