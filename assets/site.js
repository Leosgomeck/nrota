document.documentElement.classList.add('js');

const IMG = name => `assets/img/${name}.webp`;
const PAGES = [
  ['como-funciona', 'Como funciona'],
  ['artistas', 'Artistas'],
  ['eventos', 'Eventos'],
  ['parceiros', 'Parceiros'],
  ['rebeca', 'Rebeca'],
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
const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;
const wait = ms => new Promise(r => setTimeout(r, ms));

customElements.define('n-header', class extends HTMLElement {
  connectedCallback() {
    const aria = s => s === current ? ' aria-current="page"' : '';
    this.innerHTML = `<div class="wrap"><nav class="nav-in" aria-label="Principal">
      <a class="logo" href="index.html"><img src="assets/logo-nrota.png" alt="N’ROTA · início" width="203" height="44"></a>
      <ul class="nav-links">${PAGES.map(([s, l]) => `<li><a href="${href(s)}"${aria(s)}>${l}</a></li>`).join('')}</ul>
      <a class="btn btn-o btn-sm" href="${href('cadastro-banda')}">Cadastrar banda</a>
      <button class="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="menuPanel"><i></i></button>
    </nav></div>
    <div class="menu-panel" id="menuPanel">
      <a class="big" href="index.html" style="--i:0"${aria('inicio')}><span>00</span>Início</a>
      ${PAGES.map(([s, l], i) => `<a class="big" href="${href(s)}" style="--i:${i + 1}"${aria(s)}><span>0${i + 1}</span>${l}</a>`).join('')}
      <a class="btn btn-o" href="${href('cadastro-banda')}">Cadastrar minha banda <span class="arr">→</span></a>
    </div>`;
    const btn = this.querySelector('.burger');
    const toggle = open => {
      this.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
      btn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      document.body.style.overflow = open ? 'hidden' : '';
    };
    btn.addEventListener('click', () => toggle(!this.classList.contains('open')));
    this.querySelector('.menu-panel').addEventListener('click', e => e.target.closest('a') && toggle(false));
    document.addEventListener('keydown', e => e.key === 'Escape' && toggle(false));
  }
});

customElements.define('n-footer', class extends HTMLElement {
  connectedCallback() {
    const list = items => `<ul>${items.map(([s, l]) => `<li><a href="${href(s)}">${l}</a></li>`).join('')}</ul>`;
    this.innerHTML = `<footer class="site"><div class="wrap foot">
      <div><a class="logo" href="index.html"><img src="assets/logo-nrota-slogan.png" alt="N’ROTA · Seu som merece ir mais longe." width="239" height="64"></a>
        <p class="tri"><b>Um catálogo</b> para descobrir.<br><b>Uma vitrine</b> para valorizar.<br><b>Uma ponte</b> para conectar.</p></div>
      <div class="foot-cols"><div><h4>A plataforma</h4>${list(PAGES)}</div><div><h4>Comece</h4>${list(START)}</div></div>
      <div class="foot-base"><span>Brasília/DF · atendimento nacional</span><span>© 2026 N’ROTA</span></div>
    </div><span class="giant" aria-hidden="true">N’ROTA</span></footer>
    <div class="dock"><a class="btn btn-o" href="${href('cadastro-banda')}">Cadastrar banda</a><a class="btn btn-g" href="${href('solicitar-proposta')}">Fazer evento</a></div>`;
  }
});

document.querySelectorAll('img[data-img]').forEach(img => { img.src = IMG(img.dataset.img); });
document.querySelectorAll('[data-aside-img]').forEach(el => el.style.setProperty('--aside-img', `url("${IMG(el.dataset.asideImg)}")`));

const LANES = {
  ask: [
    ['CA', 'Casamento em Pirenópolis', 'Rock acústico · 120 convidados'],
    ['FE', 'Tributo a Queen', 'Festival · Goiânia/GO'],
    ['CO', 'Happy hour corporativo', 'Pop rock · Brasília/DF'],
    ['RE', '“Everlong” no repertório', 'Qualquer formação · DF'],
    ['BA', 'Bar com música ao vivo', 'Sextas à noite · Taguatinga/DF'],
    ['AN', 'Aniversário de 40 anos', 'Rock nacional anos 80']
  ],
  art: [
    ['artista-cantora', 'Íris Monteiro', 'Soul rock · Brasília/DF'],
    ['artista-guitarrista', 'Los Faroles', 'Hard rock · Goiânia/GO'],
    ['artista-baterista', 'Mei & Os Satélites', 'Indie · São Paulo/SP'],
    ['artista-baixista', 'Groove Cerrado', 'Blues rock · Brasília/DF'],
    ['artista-violao', 'Anaya Rao', 'Acústico · Belo Horizonte/MG'],
    ['artista-vocalista', 'Contramão', 'Rock nacional · Brasília/DF']
  ]
};
document.querySelectorAll('[data-lane]').forEach(track => {
  const kind = track.dataset.lane;
  const html = LANES[kind].map(([a, t, s]) => `<div class="lc ${kind}">${kind === 'art' ? `<img src="${IMG(a)}" alt="" loading="lazy">` : `<span class="av">${a}</span>`}<div><strong>${t}</strong><span>${s}</span><span class="pill">${kind === 'art' ? 'Perfil revisado' : 'Busca'}</span></div></div>`).join('');
  track.innerHTML = html + html.replaceAll('class="lc', 'aria-hidden="true" class="lc');
});

const typer = document.querySelector('[data-typer]');
if (typer) {
  const words = ['Everlong', 'Legião Urbana', 'casamento acústico', 'hard rock · GO', 'Foo Fighters'];
  if (!calm) (async () => {
    for (let i = 1; ; i = (i + 1) % words.length) {
      await wait(2600);
      for (let n = typer.textContent.length; n >= 0; n--) { typer.textContent = typer.textContent.slice(0, n); await wait(30); }
      for (const ch of words[i]) { typer.textContent += ch; await wait(75); }
    }
  })();
}

const reveal = new IntersectionObserver(entries => entries.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
}), { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('[data-reveal]').forEach(el => {
  el.getBoundingClientRect().top < innerHeight ? el.classList.add('in') : reveal.observe(el);
});

if (finePointer && !calm) {
  document.querySelectorAll('.card,.artist,.perfil-foto').forEach(el => {
    el.addEventListener('pointermove', e => {
      const r = el.getBoundingClientRect();
      el.style.setProperty('--ry', `${((e.clientX - r.left) / r.width - .5) * 8}deg`);
      el.style.setProperty('--rx', `${((e.clientY - r.top) / r.height - .5) * -8}deg`);
    });
    el.addEventListener('pointerleave', () => { el.style.removeProperty('--rx'); el.style.removeProperty('--ry'); });
  });
}

const deck = document.querySelector('.deck');
let ticking = false;
addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    document.body.classList.toggle('past', scrollY > 420);
    if (deck && !calm) deck.style.transform = `translate3d(0,${Math.min(scrollY, 600) * -0.12}px,0) rotateX(${Math.min(scrollY, 600) * 0.012}deg)`;
    ticking = false;
  });
}, { passive: true });
