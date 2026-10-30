const ENDPOINT = '';

const UF = 'AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split(' ');
const SUBGENEROS = ['Rock clássico','Hard rock','Blues rock','Indie / alternativo','Metal / progressivo','Pop rock','Punk rock'];
const DECADAS = ['1960','1970','1980','1990','2000','2010','2020'];
const ESTRUTURA = ['Som e iluminação','Palco e estrutura','Audiovisual (LED, telões)'];
const has = (v, x) => Array.isArray(v) && v.includes(x);
const yes = v => v === 'Sim';
const needsStructure = d => ESTRUTURA.some(s => has(d.servicos, s)) || has(d.servicos, 'Produção completa');

const FORMS = {
  'cadastro-banda': {
    kicker: 'Cadastro gratuito', title: 'Cadastre sua banda', img: 'artista-vocalista',
    intro: 'Dez etapas curtas. Seu progresso fica salvo neste navegador e você pode continuar depois.',
    aside: 'Cachê e condições comerciais ficam privados. Só usamos em propostas que você autorizar.',
    done: ['Cadastro enviado.', 'Nossa equipe revisa os dados e avisa pelo WhatsApp de gestão quando o perfil for publicado.'],
    steps: [
      { t: 'Identificação', d: 'Quem é a banda e quem responde por ela.', f: [
        { k: 'text', id: 'nome', l: 'Nome artístico', req: 1 },
        { k: 'text', id: 'responsavel', l: 'Responsável', req: 1, half: 1 },
        { k: 'text', id: 'funcao', l: 'Função na banda', req: 1, half: 1, ph: 'Vocalista, empresário…' },
        { k: 'tel', id: 'whatsapp', l: 'WhatsApp de gestão', req: 1, half: 1, priv: 1, ph: '(61) 90000-0000' },
        { k: 'email', id: 'email', l: 'E-mail de gestão', req: 1, half: 1, priv: 1 },
        { k: 'text', id: 'cidade', l: 'Cidade de origem', req: 1, half: 1 },
        { k: 'select', id: 'uf', l: 'UF', req: 1, half: 1, o: UF },
        { k: 'number', id: 'ano', l: 'Ano de formação', half: 1, min: 1950, max: 2026 },
        { k: 'area', id: 'historia', l: 'História da banda', max: 800, hint: 'Até 800 caracteres.' },
        { k: 'multi', id: 'links', l: 'Links oficiais', req: 1, hint: 'Informe pelo menos um.', sub: [['instagram','Instagram','@suabanda'],['youtube','YouTube','youtube.com/…'],['spotify','Spotify','open.spotify.com/…'],['site','Site ou outro','https://…']] },
        { k: 'file', id: 'foto', l: 'Foto principal', req: 1, accept: 'image/*', hint: 'Horizontal, boa resolução.' },
        { k: 'file', id: 'logo', l: 'Logo', half: 1, accept: 'image/*' },
        { k: 'file', id: 'fotos', l: 'Outras fotos', half: 1, accept: 'image/*', multi: 1 }
      ]},
      { t: 'Identidade musical', d: 'Essas respostas alimentam os filtros e o Destaque do Instagram.', f: [
        { k: 'radio', id: 'sub_principal', l: 'Estilo principal', req: 1, o: SUBGENEROS, hint: 'Define o Destaque do Instagram onde sua banda aparece.' },
        { k: 'checks', id: 'sub_secundarios', l: 'Estilos secundários', o: SUBGENEROS, max: 3, hint: 'Até 3.', check: (v, d) => has(v, d.sub_principal) ? 'O estilo principal não precisa ser repetido aqui.' : '' },
        { k: 'checks', id: 'proposta', l: 'Proposta', req: 1, o: ['Cover','Tributo','Autoral','Misto'] },
        { k: 'text', id: 'tributo_a', l: 'Tributo a qual artista?', req: 1, when: d => has(d.proposta, 'Tributo') },
        { k: 'tags', id: 'referencias', l: 'Artistas de referência', req: 1, ph: 'Digite e tecle Enter' },
        { k: 'checks', id: 'decadas', l: 'Décadas do repertório', o: DECADAS.map(x => x + 's') },
        { k: 'checks', id: 'idiomas', l: 'Idiomas', o: ['Português','Inglês','Espanhol','Instrumental'] },
        { k: 'area', id: 'proposta_txt', l: 'Descrição da proposta artística', max: 600 }
      ]},
      { t: 'Repertório', d: 'Cada música vira termo de busca. Quem pesquisar “Foo Fighters” ou “Everlong” encontra sua banda.', f: [
        { k: 'rows', id: 'setlist', l: 'Setlist', req: 1, cols: [['musica','Música','Everlong',1],['artista','Artista original','Foo Fighters',1],['decada','Década',DECADAS],['estilo','Estilo','Rock alternativo']] },
        { k: 'checks', id: 'ocasioes', l: 'Tem repertório próprio para', o: ['Casamento','Bar e pub','Festival','Corporativo','Festa particular'] },
        { k: 'area', id: 'autorais', l: 'Músicas autorais e lançamentos', ph: 'Links do Spotify, YouTube…', when: d => has(d.proposta, 'Autoral') || has(d.proposta, 'Misto') },
        { k: 'area', id: 'tematicos', l: 'Repertórios temáticos', ph: 'Anos 80, rock nacional, acústico romântico…' },
        { k: 'file', id: 'setlist_pdf', l: 'Setlist em PDF', accept: '.pdf', hint: 'Complementar. Não substitui a lista acima.' }
      ]},
      { t: 'Tipos de eventos', d: 'Marque todos os contextos em que a banda toca.', f: [
        { k: 'checks', id: 'eventos', l: 'Eventos atendidos', req: 1, o: ['Casamentos e cerimônias','Aniversários e festas particulares','Eventos corporativos','Bares, pubs e restaurantes','Casas de shows e festivais','Eventos públicos e culturais','Eventos temáticos e tributos'] }
      ]},
      { t: 'Formações e formatos', d: 'Formações diferentes podem ter cachês diferentes.', f: [
        { k: 'number', id: 'integrantes', l: 'Número de integrantes', req: 1, half: 1, min: 1 },
        { k: 'radio', id: 'formato', l: 'Formato', req: 1, half: 1, o: ['Acústico','Elétrico','Ambos'] },
        { k: 'checks', id: 'formacoes', l: 'Formações disponíveis', req: 1, o: ['Solo','Duo','Trio','Banda completa'] },
        { k: 'number', id: 'duracao', l: 'Duração total do show (min)', req: 1, half: 1, min: 1 },
        { k: 'number', id: 'sets', l: 'Número de sets', req: 1, half: 1, min: 1 },
        { k: 'number', id: 'intervalo', l: 'Intervalo entre sets (min)', half: 1, min: 0 },
        { k: 'number', id: 'montagem', l: 'Tempo de montagem (min)', half: 1, min: 0 },
        { k: 'radio', id: 'personalizado', l: 'Monta repertório personalizado?', o: ['Sim','Não'] },
        { k: 'text', id: 'extras', l: 'DJ, participações e extras' }
      ]},
      { t: 'Disponibilidade', d: 'Sua agenda habitual orienta a busca.', f: [
        { k: 'note', l: 'Disponibilidade habitual não é reserva. Toda data é confirmada diretamente com a banda.' },
        { k: 'checks', id: 'dias', l: 'Dias', req: 1, o: ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'] },
        { k: 'checks', id: 'turnos', l: 'Turnos', req: 1, o: ['Manhã','Tarde','Noite','Madrugada'] },
        { k: 'radio', id: 'feriados', l: 'Toca em feriados?', half: 1, o: ['Sim','Não'] },
        { k: 'radio', id: 'comercial', l: 'Toca em horário comercial?', half: 1, o: ['Sim','Não'] },
        { k: 'number', id: 'antecedencia', l: 'Antecedência mínima (dias)', half: 1, min: 0 },
        { k: 'area', id: 'bloqueadas', l: 'Datas bloqueadas', ph: '12/12, 24 a 26/12…' },
        { k: 'radio', id: 'confirma', l: 'Contato para confirmar data', req: 1, o: ['WhatsApp de gestão','E-mail de gestão','Outro contato'] },
        { k: 'text', id: 'confirma_outro', l: 'Qual contato?', req: 1, when: d => d.confirma === 'Outro contato' }
      ]},
      { t: 'Deslocamento', d: 'Onde a banda pode se apresentar.', f: [
        { k: 'text', id: 'base_cidade', l: 'Cidade-base', req: 1, half: 1, from: 'cidade' },
        { k: 'select', id: 'base_uf', l: 'UF', req: 1, half: 1, o: UF, from: 'uf' },
        { k: 'checks', id: 'outras_ufs', l: 'Outros estados atendidos', o: UF },
        { k: 'radio', id: 'viaja', l: 'Aceita viagens?', req: 1, o: ['Sim','Não'] },
        { k: 'number', id: 'raio', l: 'Raio sem hospedagem (km)', half: 1, min: 0, when: d => yes(d.viaja) },
        { k: 'select', id: 'custos', l: 'Custos de viagem', half: 1, o: ['Inclusos no cachê','Cobrados à parte','Depende do evento'], when: d => yes(d.viaja) },
        { k: 'text', id: 'transporte', l: 'Transporte e hospedagem', ph: 'Van própria, 2 quartos duplos…', when: d => yes(d.viaja) },
        { k: 'text', id: 'alimentacao', l: 'Alimentação e logística', when: d => yes(d.viaja) }
      ]},
      { t: 'Estrutura técnica', d: 'Informações para avaliar a viabilidade do show.', f: [
        { k: 'file', id: 'rider', l: 'Rider técnico', half: 1, accept: '.pdf,.doc,.docx,image/*', hint: 'Recomendado.' },
        { k: 'file', id: 'mapa', l: 'Mapa de palco / input list', half: 1, accept: '.pdf,.doc,.docx,image/*', hint: 'Recomendado.' },
        { k: 'area', id: 'equipamentos', l: 'Equipamentos próprios', req: 1, ph: 'Backline completo, 2 caixas ativas, mesa 12 canais…' },
        { k: 'radio', id: 'somluz', l: 'Som e luz', o: ['Levamos completo','Levamos parte','Contratante fornece'] },
        { k: 'text', id: 'equipe', l: 'Técnico e equipe de apoio', half: 1, ph: '1 técnico de som' },
        { k: 'number', id: 'passagem', l: 'Passagem de som (min)', half: 1, min: 0 },
        { k: 'text', id: 'energia', l: 'Energia e espaço mínimo', ph: '2 tomadas 220V, palco 4×3 m' }
      ]},
      { t: 'Condições comerciais', d: 'Dados privados. Nunca aparecem no perfil público e só entram em propostas que você autorizar.', f: [
        { k: 'area', id: 'cache', l: 'Cachê de referência por formação', priv: 1, ph: 'Duo acústico: R$ … · Banda completa: R$ …' },
        { k: 'area', id: 'variacao', l: 'Variação por tipo de evento', priv: 1, ph: 'Casamento: R$ … · Bar: R$ …' },
        { k: 'text', id: 'liquido', l: 'Valor líquido pretendido', half: 1, priv: 1 },
        { k: 'radio', id: 'nf', l: 'Emite nota fiscal?', half: 1, o: ['Sim','Não'] },
        { k: 'text', id: 'sinal', l: 'Sinal e forma de pagamento', priv: 1, ph: '50% na assinatura, 50% no dia' },
        { k: 'radio', id: 'personalizadas', l: 'Aceita propostas personalizadas?', half: 1, o: ['Sim','Não'] },
        { k: 'radio', id: 'intermediacao', l: 'Autoriza intermediação pelo produtor?', half: 1, o: ['Sim','Não'], hint: 'Opcional. O contato direto segue sem comissão.' }
      ]},
      { t: 'Autorizações', d: 'Consentimentos e serviços opcionais.', f: [
        { k: 'radio', id: 'contato_publico', l: 'Contato exibido no perfil', req: 1, o: ['WhatsApp de gestão','E-mail de gestão','Instagram','Somente via produtor'] },
        { k: 'consent', id: 'c_midia', req: 1, l: 'Autorizo o uso das fotos, vídeos e textos enviados no meu perfil e nas redes da N’ROTA.' },
        { k: 'consent', id: 'c_veracidade', req: 1, l: 'Confirmo que as informações são verdadeiras e vou mantê-las atualizadas.' },
        { k: 'consent', id: 'c_termos', req: 1, l: 'Li e aceito os Termos de uso e a Política de privacidade.' },
        { k: 'consent', id: 'c_intermed', req: 1, l: 'Aceito que cada intermediação siga condições e comissão acordadas por escrito antes do negócio.', when: d => yes(d.intermediacao) },
        { k: 'sub', l: 'Opcionais' },
        { k: 'consent', id: 'feed', l: 'Quero publicar minha banda no feed por R$ 50.', hint: 'Post no feed + Story no Destaque do seu estilo. O pagamento é combinado depois da aprovação do perfil.' },
        { k: 'consent', id: 'assessoria', l: 'Tenho interesse em assessoria ou agenciamento.', hint: 'Não interfere na sua presença no catálogo.' }
      ]}
    ]
  },

  'solicitar-proposta': {
    kicker: 'Faça seu evento com a gente', title: 'Solicitar proposta', img: 'palco-banda',
    intro: 'Conte o que você imagina. Nossa equipe analisa e retorna com indicações ou uma proposta integrada.',
    aside: 'Nenhum preço ou disponibilidade é confirmado sem retorno do artista ou fornecedor.',
    presets: { artista: { servicos: ['Artista ou banda'] }, estrutura: { servicos: ['Som e iluminação'] }, completo: { servicos: ['Produção completa'] } },
    done: ['Pedido recebido.', 'Nossa equipe analisa o briefing e retorna pelo canal escolhido.'],
    steps: [
      { t: 'O que você precisa', d: 'Escolha um ou mais serviços.', f: [
        { k: 'checks', id: 'servicos', l: 'Serviços', req: 1, o: ['Artista ou banda','DJ', ...ESTRUTURA,'Foto e vídeo','Produção completa'] },
        { k: 'radio', id: 'modelo', l: 'Como prefere seguir?', o: ['Indicações e contrato direto','Produção N’ROTA','Ainda não sei'] }
      ]},
      { t: 'Sobre o evento', d: 'Dados básicos para a triagem.', f: [
        { k: 'select', id: 'tipo', l: 'Tipo de evento', req: 1, o: ['Casamento','Aniversário ou festa particular','Corporativo','Bar ou casa de shows','Festival','Evento público ou cultural','Outro'] },
        { k: 'date', id: 'data', l: 'Data', req: 1, half: 1 },
        { k: 'time', id: 'inicio', l: 'Horário de início', half: 1 },
        { k: 'text', id: 'duracao', l: 'Duração estimada', half: 1, ph: '4 horas' },
        { k: 'number', id: 'publico', l: 'Público estimado', half: 1, min: 1 },
        { k: 'text', id: 'cidade', l: 'Cidade', req: 1, half: 1 },
        { k: 'select', id: 'uf', l: 'UF', req: 1, half: 1, o: UF },
        { k: 'text', id: 'local', l: 'Local do evento', hint: 'Deixe em branco se ainda estiver a definir.' },
        { k: 'checks', id: 'local_tem', l: 'O local já tem', o: ['Som','Palco','Iluminação','Gerador ou energia'] }
      ]},
      { t: 'Preferências', d: 'Quanto mais detalhe, mais certeira a proposta.', f: [
        { k: 'text', id: 'estilo', l: 'Estilo e artistas desejados', ph: 'Rock clássico, Queen, Legião Urbana…', when: d => has(d.servicos, 'Artista ou banda') || has(d.servicos, 'DJ') },
        { k: 'text', id: 'musicas', l: 'Músicas indispensáveis', when: d => has(d.servicos, 'Artista ou banda') },
        { k: 'checks', id: 'formato_show', l: 'Formato do show', o: ['Acústico','Elétrico','Solo ou duo','Banda completa'], when: d => has(d.servicos, 'Artista ou banda') },
        { k: 'radio', id: 'porte', l: 'Porte da estrutura', o: ['Até 200 pessoas','200 a 1.000','Acima de 1.000'], when: needsStructure },
        { k: 'text', id: 'montagem', l: 'Janela de montagem e desmontagem', ph: 'Montagem a partir das 14h', when: needsStructure },
        { k: 'radio', id: 'viagem', l: 'Pode custear deslocamento e hospedagem de quem vem de fora?', o: ['Sim','Não','Depende'], when: d => has(d.servicos, 'Artista ou banda') },
        { k: 'select', id: 'orcamento', l: 'Faixa de investimento', half: 1, o: ['Até R$ 3 mil','R$ 3 mil a 10 mil','R$ 10 mil a 30 mil','Acima de R$ 30 mil','Prefiro não informar'], hint: 'Opcional, mas recomendada.' },
        { k: 'date', id: 'prazo', l: 'Receber proposta até', half: 1 },
        { k: 'area', id: 'descricao', l: 'Algo mais que devemos saber?' },
        { k: 'file', id: 'anexos', l: 'Referências e anexos', multi: 1 }
      ]},
      { t: 'Seus dados', d: 'Para retornarmos com a proposta.', f: [
        { k: 'text', id: 'nome', l: 'Nome', req: 1 },
        { k: 'radio', id: 'pessoa', l: 'Contratação como', req: 1, o: ['Pessoa física','Empresa'] },
        { k: 'text', id: 'empresa', l: 'Empresa', req: 1, when: d => d.pessoa === 'Empresa' },
        { k: 'tel', id: 'whatsapp', l: 'WhatsApp', req: 1, half: 1, ph: '(61) 90000-0000' },
        { k: 'email', id: 'email', l: 'E-mail', req: 1, half: 1 },
        { k: 'radio', id: 'canal', l: 'Canal preferido', o: ['WhatsApp','E-mail','Ligação'] },
        { k: 'consent', id: 'c_priv', req: 1, l: 'Li e aceito a Política de privacidade.' },
        { k: 'consent', id: 'c_contato', req: 1, l: 'Autorizo a N’ROTA a entrar em contato sobre este pedido.' }
      ]}
    ]
  },

  'cadastro-performance': {
    kicker: 'Artes performáticas', title: 'Cadastre seu número', img: 'palco-banda',
    intro: 'Circo, malabarismo, palhaçaria, mágica, teatro de rua, dança e outras artes ao vivo. Perfil gratuito e contato direto.',
    aside: 'CPF e cachê ficam restritos à equipe. Só aparece o que você autorizar.',
    done: ['Cadastro enviado.', 'A equipe revisa os dados e avisa quando seu perfil for publicado.'],
    steps: [
      { t: 'Identificação', d: 'Quem se apresenta.', f: [
        { k: 'radio', id: 'tipo', l: 'Você é', req: 1, o: ['Artista solo','Dupla ou trupe','Companhia'] },
        { k: 'text', id: 'nome', l: 'Nome artístico ou da trupe', req: 1 },
        { k: 'text', id: 'responsavel', l: 'Responsável', req: 1, half: 1 },
        { k: 'text', id: 'doc', l: 'CPF ou CNPJ', req: 1, half: 1, priv: 1, hint: 'Usado só na verificação.' },
        { k: 'tel', id: 'whatsapp', l: 'WhatsApp', req: 1, half: 1 },
        { k: 'email', id: 'email', l: 'E-mail', req: 1, half: 1 },
        { k: 'text', id: 'cidade', l: 'Cidade', req: 1, half: 1 },
        { k: 'select', id: 'uf', l: 'UF', req: 1, half: 1, o: UF },
        { k: 'multi', id: 'links', l: 'Redes e vídeos', sub: [['instagram','Instagram','@seuperfil'],['video','Vídeo de apresentação','https://…']] }
      ]},
      { t: 'Seu número', d: 'Organiza a busca de quem contrata.', f: [
        { k: 'checks', id: 'modalidades', l: 'Modalidades', req: 1, o: ['Malabarismo','Acrobacia','Aéreos','Perna de pau','Palhaçaria','Mágica e ilusionismo','Mímica','Teatro de rua','Dança','Fogo e LED','Bonecos','Contação de histórias','Cantor ou DJ de apoio','Outra'] },
        { k: 'text', id: 'outra', l: 'Qual outra modalidade?', when: d => (d.modalidades || []).includes('Outra') },
        { k: 'area', id: 'proposta', l: 'Descreva o número', req: 1, ph: 'Como é a apresentação, o clima e o que o público vê.' },
        { k: 'checks', id: 'publico', l: 'Público', o: ['Livre','Infantil','Adulto','Família','Corporativo'] },
        { k: 'checks', id: 'eventos', l: 'Eventos', req: 1, o: ['Shows e festivais','Casamentos','Aniversários','Corporativos','Escolas','Ruas e praças','Bares e casas noturnas','Feiras e lojas'] },
        { k: 'number', id: 'duracao', l: 'Duração do número (min)', half: 1, min: 1 },
        { k: 'number', id: 'integrantes', l: 'Integrantes', half: 1, min: 1 },
        { k: 'radio', id: 'interacao', l: 'Interage com o público?', half: 1, o: ['Sim','Não','Depende'] },
        { k: 'file', id: 'fotos', l: 'Fotos e material', multi: 1, accept: '.pdf,image/*' }
      ]},
      { t: 'Estrutura e deslocamento', d: 'O que o espaço precisa oferecer.', f: [
        { k: 'checks', id: 'espaco', l: 'Espaço necessário', o: ['Palco','Chão plano','Pé-direito alto','Ponto de ancoragem','Área ao ar livre','Espaço fechado'] },
        { k: 'checks', id: 'tecnica', l: 'Técnica', o: ['Som','Luz','Camarim','Energia','Segurança contra fogo'] },
        { k: 'area', id: 'riscos', l: 'Cuidados e observações', ph: 'Uso de fogo, alturas, restrições de local, tempo de montagem.' },
        { k: 'radio', id: 'nacional', l: 'Viaja para outros estados?', half: 1, o: ['Sim','Não'] },
        { k: 'text', id: 'raio', l: 'Região atendida', half: 1 }
      ]},
      { t: 'Condições e autorizações', d: 'Cachê é sempre privado.', f: [
        { k: 'text', id: 'cache', l: 'Faixa de cachê', half: 1, priv: 1 },
        { k: 'text', id: 'pagamento', l: 'Forma de pagamento', half: 1 },
        { k: 'consent', id: 'c_lgpd', req: 1, l: 'Li e aceito os Termos de uso e a Política de privacidade (LGPD).' },
        { k: 'consent', id: 'c_exibicao', req: 1, l: 'Autorizo a exibição do meu perfil, fotos e contato comercial na N’ROTA.' },
        { k: 'consent', id: 'c_social', l: 'Autorizo a divulgação do meu perfil no Instagram da N’ROTA.' }
      ]}
    ]
  },
  'seja-parceiro': {
    kicker: 'Rede de parceiros', title: 'Quero ser parceiro', img: 'artista-tecladista',
    intro: 'Cadastro gratuito para profissionais autônomos e empresas de eventos.',
    aside: 'CPF e CNPJ ficam restritos à equipe e servem só para verificação.',
    done: ['Cadastro enviado.', 'Revisamos seus dados e avisamos quando o perfil entrar na rede. Você passa a receber pedidos compatíveis com seu nicho e região.'],
    steps: [
      { t: 'Identificação', d: 'Quem presta o serviço.', f: [
        { k: 'radio', id: 'tipo', l: 'Você é', req: 1, o: ['Profissional autônomo','Empresa'] },
        { k: 'text', id: 'nome', l: 'Nome comercial ou profissional', req: 1 },
        { k: 'text', id: 'doc', l: 'CPF ou CNPJ', req: 1, half: 1, priv: 1, hint: 'Usado só na verificação.' },
        { k: 'text', id: 'responsavel', l: 'Responsável', req: 1, half: 1, when: d => d.tipo === 'Empresa' },
        { k: 'tel', id: 'whatsapp', l: 'WhatsApp', req: 1, half: 1 },
        { k: 'email', id: 'email', l: 'E-mail', req: 1, half: 1 },
        { k: 'text', id: 'cidade', l: 'Cidade', req: 1, half: 1 },
        { k: 'select', id: 'uf', l: 'UF', req: 1, half: 1, o: UF },
        { k: 'multi', id: 'links', l: 'Portfólio e redes', sub: [['instagram','Instagram','@seuperfil'],['site','Site ou portfólio','https://…']] }
      ]},
      { t: 'Serviços e capacidade', d: 'Organiza sua vitrine e os pedidos que você recebe.', f: [
        { k: 'radio', id: 'nicho', l: 'Nicho principal', req: 1, o: ['Produção','Montagem e estrutura','Técnica e audiovisual','Hospitalidade e apoio'] },
        { k: 'checks', id: 'sub_producao', l: 'Especialidades', req: 1, o: ['Produção executiva','Produção técnica','Coordenação','Assistência','Stage manager'], when: d => d.nicho === 'Produção' },
        { k: 'checks', id: 'sub_estrutura', l: 'Especialidades', req: 1, o: ['Montagem','Cenografia','Praticáveis','Palco','Tendas','Grades','Geradores','Logística e carga'], when: d => d.nicho === 'Montagem e estrutura' },
        { k: 'checks', id: 'sub_tecnica', l: 'Especialidades', req: 1, o: ['PA e monitores','Iluminação','Painéis de LED','Operação de som','Operação de luz','Operação de vídeo','Videomaker','Fotografia','Streaming'], when: d => d.nicho === 'Técnica e audiovisual' },
        { k: 'checks', id: 'sub_apoio', l: 'Especialidades', req: 1, o: ['Catering','Camarins','Roadie','Backline','Recepção','Brigada','Apoio operacional'], when: d => d.nicho === 'Hospitalidade e apoio' },
        { k: 'area', id: 'servicos', l: 'Serviços e equipamentos', req: 1, ph: 'Liste o que você oferece e os principais equipamentos.' },
        { k: 'text', id: 'equipe', l: 'Tamanho da equipe', half: 1 },
        { k: 'number', id: 'raio', l: 'Raio de atendimento (km)', half: 1, min: 0 },
        { k: 'checks', id: 'porte', l: 'Porte de evento atendido', o: ['Até 200 pessoas','200 a 1.000','Acima de 1.000'] },
        { k: 'radio', id: 'nacional', l: 'Atende em outros estados?', half: 1, o: ['Sim','Não'] },
        { k: 'checks', id: 'modo', l: 'Atendimento', half: 1, o: ['Presencial','Remoto'] },
        { k: 'file', id: 'ficha', l: 'Ficha técnica ou portfólio', multi: 1, accept: '.pdf,image/*' }
      ]},
      { t: 'Privacidade', d: 'Últimos aceites.', f: [
        { k: 'note', l: 'O cadastro não garante pedidos. Você recebe briefings compatíveis com seu nicho e região, sem promessa de demanda.' },
        { k: 'consent', id: 'c_lgpd', req: 1, l: 'Li e aceito os Termos de uso e a Política de privacidade (LGPD).' },
        { k: 'consent', id: 'c_exibicao', req: 1, l: 'Autorizo a exibição do meu perfil, portfólio e contato comercial na N’ROTA.' },
        { k: 'consent', id: 'c_verif', l: 'Quero passar pela verificação documental para receber o selo de parceiro verificado.' }
      ]}
    ]
  },

  'acesso-antecipado': {
    kicker: 'Catálogo N’ROTA', title: 'Acesso antecipado', img: 'artista-cantora',
    intro: 'Entre na lista e seja avisado quando a busca completa estiver no ar.',
    aside: 'Novidades por e-mail só com a sua autorização, separada do cadastro.',
    presets: Object.fromEntries(['Samba','Pagode','Pop','Sertanejo','MPB','Rock'].map(s => [s.toLowerCase(), { estilos: [s] }])),
    done: ['Você está na lista.', 'Avisamos por e-mail quando o catálogo completo abrir.'],
    steps: [
      { t: 'Seus dados', d: 'Leva menos de um minuto.', f: [
        { k: 'text', id: 'nome', l: 'Nome', req: 1 },
        { k: 'email', id: 'email', l: 'E-mail', req: 1 },
        { k: 'radio', id: 'perfil', l: 'Você é', req: 1, o: ['Público','Casa de shows','Produtor','Empresa','Contratante particular'] },
        { k: 'text', id: 'cidade', l: 'Cidade', hint: 'Opcional.' },
        { k: 'checks', id: 'estilos', l: 'Estilos de interesse', o: ['Rock','Samba','Pagode','Pop','Sertanejo','MPB'] },
        { k: 'consent', id: 'c_termos', req: 1, l: 'Li e aceito os Termos de uso e a Política de privacidade.' },
        { k: 'consent', id: 'c_mkt', l: 'Quero receber novidades da N’ROTA por e-mail.' }
      ]}
    ]
  }
};

const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const store = {
  get: k => { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } },
  set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  del: k => { try { localStorage.removeItem(k); } catch {} }
};

const label = (f, forId) => `<${forId ? `label for="${forId}"` : 'span class="lb"'}>${esc(f.l)}${f.req ? '<span class="req" aria-hidden="true">*</span>' : ''}${f.priv ? '<span class="badge">Privado</span>' : ''}</${forId ? 'label' : 'span'}>`;
const hint = f => (f.hint ? `<span class="hint">${esc(f.hint)}</span>` : '') + '<span class="err" aria-live="polite"></span>';
const choice = (f, type) => `<div class="opts" role="group" aria-label="${esc(f.l)}">${f.o.map(o => `<label class="opt"><input type="${type}" name="${f.id}" value="${esc(o)}"><span>${esc(o)}</span></label>`).join('')}</div>`;
const rowHTML = (f, r = {}) => `<div class="row">${f.cols.map(([id, l, ph, req]) => Array.isArray(ph)
  ? `<select data-c="${id}" aria-label="${l}"><option value="">${l}</option>${ph.map(o => `<option${r[id] === o ? ' selected' : ''}>${o}</option>`).join('')}</select>`
  : `<input type="text" data-c="${id}" placeholder="${ph}" aria-label="${l}${req ? ' (obrigatório)' : ''}" value="${esc(r[id])}">`).join('')}<button type="button" class="rm" aria-label="Remover música">×</button></div>`;

const RENDER = {
  text: f => `${label(f, 'f_' + f.id)}<input id="f_${f.id}" name="${f.id}" type="${f.k}" ${f.ph ? `placeholder="${esc(f.ph)}"` : ''} ${f.min != null ? `min="${f.min}"` : ''} ${f.max != null ? `max="${f.max}"` : ''} ${f.k === 'number' ? 'inputmode="numeric"' : ''}>${hint(f)}`,
  area: f => `${label(f, 'f_' + f.id)}<textarea id="f_${f.id}" name="${f.id}" ${f.ph ? `placeholder="${esc(f.ph)}"` : ''} ${f.max ? `maxlength="${f.max}"` : ''}></textarea>${hint(f)}`,
  select: f => `${label(f, 'f_' + f.id)}<select id="f_${f.id}" name="${f.id}"><option value="">Selecione</option>${f.o.map(o => `<option>${esc(o)}</option>`).join('')}</select>${hint(f)}`,
  radio: f => label(f) + choice(f, 'radio') + hint(f),
  checks: f => label(f) + choice(f, 'checkbox') + hint(f),
  file: f => `${label(f, 'f_' + f.id)}<input id="f_${f.id}" name="${f.id}" type="file" ${f.accept ? `accept="${f.accept}"` : ''} ${f.multi ? 'multiple' : ''}>${hint(f)}`,
  multi: f => `${label(f)}<div class="multi">${f.sub.map(([id, l, ph]) => `<input type="text" id="f_${f.id}_${id}" data-s="${id}" placeholder="${l}: ${ph}" aria-label="${l}">`).join('')}</div>${hint(f)}`,
  tags: f => `${label(f, 'f_' + f.id)}<div class="tags"><input id="f_${f.id}" type="text" placeholder="${esc(f.ph)}" enterkeyhint="done"></div>${hint(f)}`,
  rows: f => `${label(f)}<div class="rows"><div class="row row-h">${f.cols.map(c => `<span>${c[1]}${c[3] ? ' *' : ''}</span>`).join('')}<span></span></div><div data-rows></div><button type="button" class="add">+ Adicionar música</button></div>${hint(f)}`,
  consent: f => `<label class="check"><input type="checkbox" id="f_${f.id}" name="${f.id}"><span>${esc(f.l)}${f.req ? ' <span class="req">*</span>' : ''}${f.hint ? `<small>${esc(f.hint)}</small>` : ''}</span></label><span class="err" aria-live="polite"></span>`
};
['email', 'tel', 'number', 'date', 'time'].forEach(k => RENDER[k] = RENDER.text);

const READ = {
  radio: w => w.querySelector('input:checked')?.value || '',
  checks: w => [...w.querySelectorAll('input:checked')].map(i => i.value),
  consent: w => w.querySelector('input').checked,
  file: w => [...w.querySelector('input').files].map(x => ({ name: x.name, size: x.size })),
  multi: w => Object.fromEntries([...w.querySelectorAll('[data-s]')].map(i => [i.dataset.s, i.value.trim()])),
  rows: w => [...w.querySelectorAll('[data-rows] .row')].map(r => Object.fromEntries([...r.querySelectorAll('[data-c]')].map(i => [i.dataset.c, i.value.trim()]))).filter(r => Object.values(r).some(Boolean)),
  _: w => (w.querySelector('input,select,textarea')?.value || '').trim()
};

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
function error(f, v, data) {
  const empty = v == null || v === '' || v === false || (Array.isArray(v) && !v.length) || (f.k === 'multi' && !Object.values(v).some(Boolean));
  if (empty) return !f.req ? '' : ({ consent: 'Necessário para continuar.', multi: 'Informe pelo menos um link.', rows: 'Adicione pelo menos uma música com nome e artista.' })[f.k] || 'Campo obrigatório.';
  if (f.k === 'email' && !EMAIL.test(v)) return 'Confira o e-mail. Exemplo: nome@dominio.com';
  if (f.k === 'tel' && v.replace(/\D/g, '').length < 10) return 'Informe DDD e número.';
  if (f.k === 'number' && ((f.min != null && +v < f.min) || (f.max != null && +v > f.max))) return `Use um valor entre ${f.min ?? 0} e ${f.max ?? '∞'}.`;
  if (f.k === 'checks' && f.max && v.length > f.max) return `Escolha no máximo ${f.max}.`;
  if (f.k === 'rows' && v.some(r => !r.musica || !r.artista)) return 'Cada música precisa de nome e artista original.';
  return f.check?.(v, data) || '';
}

function mount(root) {
  const id = root.dataset.form, F = FORMS[id];
  const key = 'nrota:' + id;
  const defs = Object.fromEntries(F.steps.flatMap(s => s.f).filter(f => f.id).map(f => [f.id, f]));
  const multiStep = F.steps.length > 1;
  const S = { step: 0, reached: 0, data: {}, sent: false };

  const draft = store.get(key);
  S.data = { ...(draft?.data || {}) };
  const restored = Object.keys(S.data).length > 0;
  const preset = F.presets?.[location.hash.slice(1)];
  if (preset) Object.entries(preset).forEach(([k, v]) => S.data[k] = [...new Set([...(S.data[k] || []), ...v])]);

  root.innerHTML = `<div class="form-page">
    <aside class="form-aside" style="--aside-img:url('${IMG(F.img)}')">
      <span class="label">${esc(F.kicker)}</span>
      <h1>${esc(F.title)}</h1>
      <p class="muted">${esc(F.intro)}</p>
      ${multiStep ? `<ol class="steplist">${F.steps.map((s, i) => `<li><button type="button" data-go="${i}">${esc(s.t)}</button></li>`).join('')}</ol>` : ''}
      <p class="aside-note">${esc(F.aside)}</p>
    </aside>
    <div class="form-card">
      <div class="prog" ${multiStep ? '' : 'hidden'}><div class="prog-bar"></div><div class="prog-txt"><span data-n></span><b data-t></b></div></div>
      <form class="f-body" novalidate></form>
      <div class="f-foot"><span class="save"></span><div class="act">
        <button class="btn btn-g btn-sm" type="button" data-back>Voltar</button>
        <button class="btn btn-p btn-sm" type="button" data-next>Continuar</button>
      </div></div>
    </div></div>`;

  const $ = s => root.querySelector(s);
  const form = $('.f-body'), next = $('[data-next]'), back = $('[data-back]'), card = $('.form-card');
  const wrapOf = fid => form.querySelector(`[data-f="${fid}"]`);

  const read = (f, w) => f.k === 'tags' ? S.data[f.id] || [] : (READ[f.k] || READ._)(w);
  const drawTags = (f, w) => {
    const input = w.querySelector('.tags input');
    w.querySelectorAll('.tag').forEach(t => t.remove());
    (S.data[f.id] || []).forEach((t, i) => input.insertAdjacentHTML('beforebegin', `<span class="tag">${esc(t)}<button type="button" data-i="${i}" aria-label="Remover ${esc(t)}">×</button></span>`));
  };
  const drawRows = (f, w, rows) => { w.querySelector('[data-rows]').innerHTML = (rows?.length ? rows : [{}, {}, {}]).map(r => rowHTML(f, r)).join(''); };

  const WRITE = {
    radio: (w, v) => w.querySelectorAll('input').forEach(i => i.checked = [].concat(v).includes(i.value)),
    consent: (w, v) => w.querySelector('input').checked = !!v,
    multi: (w, v) => w.querySelectorAll('[data-s]').forEach(i => i.value = v[i.dataset.s] || ''),
    tags: (w, v, f) => drawTags(f, w),
    rows: (w, v, f) => drawRows(f, w, v),
    file: () => {},
    _: (w, v) => { const el = w.querySelector('input,select,textarea'); if (el) el.value = v; }
  };
  WRITE.checks = WRITE.radio;
  const write = (f, w, v) => v != null && (WRITE[f.k] || WRITE._)(w, v, f);

  const visible = () => form.querySelectorAll('.fld').forEach(w => { const f = defs[w.dataset.f]; if (f.when) w.hidden = !f.when(S.data); });

  let saveTimer;
  const persist = () => {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => store.set(key, { data: Object.fromEntries(Object.entries(S.data).filter(([k]) => defs[k]?.k !== 'file')) }), 400);
  };
  const sync = w => {
    const f = defs[w.dataset.f];
    S.data[f.id] = read(f, w);
    if (w.classList.contains('bad') && !error(f, S.data[f.id], S.data)) { w.classList.remove('bad'); w.querySelector('.err').textContent = ''; }
    visible();
    persist();
  };

  form.innerHTML = (restored ? `<div class="draft"><span>Rascunho recuperado deste navegador.</span><button type="button" data-reset>Começar do zero</button></div>` : '') +
    F.steps.map((st, i) => `<fieldset class="stp" data-step="${i}" hidden>
      <legend class="sub">${esc(st.t)}</legend>
      <p class="step-intro">${esc(st.d)}</p>
      <div class="fields">${st.f.map(f => f.k === 'note' ? `<p class="note">${esc(f.l)}</p>` : f.k === 'sub' ? `<p class="sub">${esc(f.l)}</p>` :
        `<div class="fld${f.half ? ' half' : ''}" data-f="${f.id}">${RENDER[f.k](f)}</div>`).join('')}</div>
    </fieldset>`).join('');
  form.querySelectorAll('.fld').forEach(w => {
    const f = defs[w.dataset.f];
    if (f.k === 'rows' && !S.data[f.id]) drawRows(f, w);
    write(f, w, S.data[f.id]);
  });

  const show = i => {
    S.step = i;
    S.reached = Math.max(S.reached, i);
    const n = F.steps.length;
    form.querySelectorAll('.stp').forEach(s => s.hidden = +s.dataset.step !== i);
    F.steps[i].f.filter(f => f.from && !S.data[f.id] && S.data[f.from]).forEach(f => { S.data[f.id] = S.data[f.from]; write(f, wrapOf(f.id), S.data[f.id]); });
    visible();
    $('.prog-bar').innerHTML = Array.from({ length: n }, (_, k) => `<i class="${k <= i ? 'd' : ''}"></i>`).join('');
    $('[data-n]').textContent = `Etapa ${i + 1} de ${n}`;
    $('[data-t]').textContent = F.steps[i].t;
    root.querySelectorAll('.steplist li').forEach((li, k) => {
      li.className = k === i ? 'cur' : k < S.reached || (k <= S.reached && k !== i) ? 'done' : '';
      li.querySelector('button').disabled = k > S.reached;
      li.querySelector('button').toggleAttribute('aria-current', k === i);
    });
    back.hidden = i === 0;
    next.className = `btn btn-sm ${i === n - 1 ? 'btn-o' : 'btn-p'}`;
    next.innerHTML = i === n - 1 ? 'Enviar <span class="arr">→</span>' : 'Continuar <span class="arr">→</span>';
    $('.save').textContent = multiStep ? 'Progresso salvo neste navegador' : '';
  };

  const validate = () => {
    let first = null;
    form.querySelectorAll(`.stp[data-step="${S.step}"] .fld:not([hidden])`).forEach(w => {
      const f = defs[w.dataset.f], msg = error(f, read(f, w), S.data);
      w.classList.toggle('bad', !!msg);
      w.querySelector('.err').textContent = msg;
      first ||= msg && w;
    });
    if (first) { first.scrollIntoView({ block: 'center', behavior: 'smooth' }); first.querySelector('input,select,textarea')?.focus({ preventScroll: true }); }
    return !first;
  };

  const goTo = i => { show(i); card.scrollIntoView({ block: 'start', behavior: 'smooth' }); };

  async function submit() {
    next.disabled = true; next.textContent = 'Enviando…';
    const protocolo = 'NR-' + Date.now().toString(36).toUpperCase().slice(-6);
    const payload = { formulario: id, protocolo, enviadoEm: new Date().toISOString(), dados: S.data };
    try {
      if (ENDPOINT) await fetch(ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(payload) });
      else console.info('[N’ROTA] envio', payload);
      store.del(key);
      S.sent = true;
      const [title, text] = F.done;
      form.innerHTML = `<div class="done"><div class="ico"><svg width="26" height="26" viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="2.4"><path d="m6 13.5 4.5 4.5L20 8.5"/></svg></div><h2>${title}</h2><p>${text}</p><span class="proto">Protocolo ${protocolo}</span></div>`;
      $('.prog').hidden = true;
      root.querySelectorAll('.steplist li').forEach(li => { li.className = 'done'; li.querySelector('button').disabled = true; });
      $('.f-foot').innerHTML = `<a class="btn btn-g btn-sm" href="index.html">Voltar ao início</a>`;
    } catch {
      $('.save').textContent = 'Não foi possível enviar. Verifique sua conexão e tente de novo.';
      next.disabled = false; next.textContent = 'Enviar';
    }
  }

  form.addEventListener('input', e => { const w = e.target.closest('.fld'); if (w && !e.target.closest('.tags')) sync(w); });
  form.addEventListener('change', e => { const w = e.target.closest('.fld'); if (w && !e.target.closest('.tags')) sync(w); });
  form.addEventListener('submit', e => e.preventDefault());
  form.addEventListener('keydown', e => {
    const box = e.target.closest('.tags');
    if (!box) return void (e.key === 'Enter' && e.target.tagName === 'INPUT' && e.preventDefault());
    const w = box.closest('.fld'), f = defs[w.dataset.f], list = S.data[f.id] || [];
    if (e.key === 'Enter' || e.key === ',') {
      e.preventDefault();
      const v = e.target.value.trim().replace(/,$/, '');
      if (v && !list.includes(v)) S.data[f.id] = [...list, v];
      e.target.value = '';
    } else if (e.key === 'Backspace' && !e.target.value && list.length) S.data[f.id] = list.slice(0, -1);
    else return;
    drawTags(f, w); sync(w);
  });
  form.addEventListener('click', e => {
    const t = e.target, w = t.closest('.fld'), f = w && defs[w.dataset.f];
    if (t.matches('[data-reset]')) { store.del(key); location.reload(); }
    else if (t.matches('.tag button')) { S.data[f.id].splice(+t.dataset.i, 1); drawTags(f, w); sync(w); }
    else if (t.matches('.add')) { w.querySelector('[data-rows]').insertAdjacentHTML('beforeend', rowHTML(f)); w.querySelector('[data-rows] .row:last-child input')?.focus(); }
    else if (t.matches('.rm')) {
      const row = t.closest('.row');
      row.parentElement.children.length > 1 ? row.remove() : row.querySelectorAll('[data-c]').forEach(i => i.value = '');
      sync(w);
    }
  });
  root.querySelector('.steplist')?.addEventListener('click', e => {
    const go = e.target.closest('[data-go]');
    if (go && !go.disabled && +go.dataset.go !== S.step && (+go.dataset.go < S.step || validate())) goTo(+go.dataset.go);
  });
  next.addEventListener('click', () => validate() && (S.step < F.steps.length - 1 ? goTo(S.step + 1) : submit()));
  back.addEventListener('click', () => goTo(S.step - 1));

  show(0);
}

document.querySelectorAll('[data-form]').forEach(mount);
