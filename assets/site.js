const PAGES = [
  ['como-funciona', 'Como funciona'],
  ['artistas', 'Artistas'],
  ['eventos', 'Eventos'],
  ['parceiros', 'Parceiros'],
  ['duvidas', 'Dúvidas']
];
const START = [
  ['cadastro-banda', 'Cadastrar banda'],
  ['solicitar-proposta', 'Solicitar proposta'],
  ['seja-parceiro', 'Quero ser parceiro'],
  ['acesso-antecipado', 'Acesso antecipado']
];
const current = document.body.dataset.page;
const href = slug => `${slug}.html`;

customElements.define('n-header', class extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `<div class="wrap"><nav class="nav-in" aria-label="Principal">
      <a class="logo" href="index.html"><img src="assets/logo-nrota.png" alt="N’ROTA · início" width="203" height="44"></a>
      <ul id="menu">${PAGES.map(([s, l]) => `<li><a href="${href(s)}"${s === current ? ' aria-current="page"' : ''}>${l}</a></li>`).join('')}
        <li class="only-m"><a href="${href('cadastro-banda')}">Cadastrar banda</a></li></ul>
      <a class="btn btn-o btn-sm" href="${href('cadastro-banda')}">Cadastrar banda</a>
      <button class="menu-btn" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M2 5h14M2 9h14M2 13h14"/></svg>
      </button></nav></div>`;
    const btn = this.querySelector('.menu-btn');
    btn.addEventListener('click', () => btn.setAttribute('aria-expanded', this.classList.toggle('open')));
  }
});

customElements.define('n-footer', class extends HTMLElement {
  connectedCallback() {
    const list = items => `<ul>${items.map(([s, l]) => `<li><a href="${href(s)}">${l}</a></li>`).join('')}</ul>`;
    this.innerHTML = `<footer class="site"><div class="wrap foot">
      <div><a class="logo" href="index.html"><img src="assets/logo-nrota-slogan.png" alt="N’ROTA · Seu som merece ir mais longe." width="239" height="64"></a>
        <p class="tri"><b>Um catálogo</b> para descobrir.<br><b>Uma vitrine</b> para valorizar.<br><b>Uma ponte</b> para conectar.</p></div>
      <div><h4>A plataforma</h4>${list(PAGES)}</div>
      <div><h4>Comece</h4>${list(START)}</div>
      <div class="foot-base"><span>Brasília/DF · atendimento nacional</span><span>© 2026 N’ROTA</span></div>
    </div></footer>`;
  }
});

const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
const wait = ms => new Promise(r => setTimeout(r, ms));

const LANES = {
  ask: [
    ['MA', 'Casamento em Pirenópolis', 'Rock acústico · 120 convidados', 'Busca'],
    ['RT', 'Tributo a Queen', 'Festival · Goiânia/GO', 'Busca'],
    ['LP', 'Happy hour corporativo', 'Pop rock · Brasília/DF', 'Busca'],
    ['JC', '“Everlong” no repertório', 'Qualquer formação · DF', 'Busca'],
    ['BS', 'Bar com música ao vivo', 'Sextas à noite · Taguatinga/DF', 'Busca'],
    ['CF', 'Aniversário de 40 anos', 'Rock nacional anos 80', 'Busca']
  ],
  art: [
    ['VE', 'Vinil Elétrico', 'Rock alternativo · Brasília/DF', 'Perfil revisado'],
    ['RN', 'Rádio Nacional', 'Rock clássico · 32 músicas', 'Perfil revisado'],
    ['DS', 'Duo Setlist', 'Pop rock · duo acústico', 'Perfil revisado'],
    ['CM', 'Contramão', 'Hard rock · aceita viagens', 'Perfil revisado'],
    ['A6', 'Acústico 61', 'Pop rock · casamentos', 'Perfil revisado'],
    ['FL', 'Fuzz Leste', 'Punk rock · Ceilândia/DF', 'Perfil revisado']
  ]
};
document.querySelectorAll('[data-lane]').forEach(track => {
  const kind = track.dataset.lane;
  const html = LANES[kind].map(([a, t, s, p]) => `<div class="card ${kind}"><span class="av">${a}</span><div><strong>${t}</strong><span>${s}</span><span class="pill">${p}</span></div></div>`).join('');
  track.innerHTML = html + html.replaceAll('class="card', 'aria-hidden="true" class="card');
});

const search = document.querySelector('[data-search-demo]');
if (search) {
  const DEMO = [
    { q: 'Everlong', k: 'música no repertório', r: [['VE', 'Vinil Elétrico', 'Rock alternativo · Brasília/DF', 'Everlong (Foo Fighters)'], ['CM', 'Contramão', 'Hard rock · Goiânia/GO', 'Everlong (Foo Fighters)']] },
    { q: 'Legião Urbana', k: 'artista no repertório', r: [['RN', 'Rádio Nacional', 'Rock clássico · Brasília/DF', '14 músicas de Legião Urbana'], ['A6', 'Acústico 61', 'Pop rock · Taguatinga/DF', '9 músicas de Legião Urbana']] },
    { q: 'casamento acústico', k: 'tipo de evento e formato', r: [['DS', 'Duo Setlist', 'Pop rock · Brasília/DF', 'Duo acústico · casamentos'], ['VE', 'Vinil Elétrico', 'Rock alternativo · Brasília/DF', 'Acústico ou elétrico']] }
  ];
  const [query, kind, list] = ['[data-q]', '[data-k]', '[data-r]'].map(s => search.querySelector(s));
  const paint = d => {
    query.textContent = d.q;
    kind.textContent = d.k;
    list.innerHTML = d.r.map(([a, n, m, hit]) => `<li><span class="sc-av">${a}</span><div><strong>${n}</strong><span>${m} · <mark>${hit}</mark></span></div></li>`).join('');
  };
  paint(DEMO[0]);
  if (!calm) (async () => {
    for (let i = 1; ; i = (i + 1) % DEMO.length) {
      await wait(3200);
      for (let n = query.textContent.length; n >= 0; n--) { query.textContent = query.textContent.slice(0, n); await wait(28); }
      for (let n = 1; n <= DEMO[i].q.length; n++) { query.textContent = DEMO[i].q.slice(0, n); await wait(70); }
      paint(DEMO[i]);
    }
  })();
}
