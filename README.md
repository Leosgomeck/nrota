# N'ROTA

Plataforma de catálogo, divulgação e contratação musical. Primeiro capítulo: **Rock N' Rota**.

> Seu som merece ir mais longe.

Site estático da Fase 1: landing page, páginas de conteúdo e formulários em etapas. Sem banco de dados nesta fase.

## Páginas

| Arquivo | Conteúdo |
|---|---|
| `index.html` | Início |
| `como-funciona.html` | Jornada, filtros, repertório pesquisável, contratação e regras |
| `artistas.html` | Perfil, cadastro em 10 etapas, planos, Instagram e agenciamento |
| `eventos.html` | Faça seu evento com a gente |
| `parceiros.html` | Rede de profissionais e fornecedores |
| `performance.html` | Artes performáticas |
| `cadastro-performance.html` | Formulário de performance |
| `rebeca.html` | Perfil da Rebeca Catarina |
| `duvidas.html` | Perguntas frequentes |
| `cadastro-banda.html` | Formulário de cadastro da banda (10 etapas) |
| `solicitar-proposta.html` | Briefing do evento (4 etapas) |
| `seja-parceiro.html` | Cadastro de parceiro (3 etapas) |
| `acesso-antecipado.html` | Lista de acesso ao catálogo |

Atalhos com seleção prévia: `solicitar-proposta.html#artista`, `#estrutura`, `#completo` e `acesso-antecipado.html#samba` (ou outro estilo).

## Estrutura

```
assets/
  nrota.css            estilos e tokens da marca
  site.js              cabeçalho e rodapé (<n-header>, <n-footer>), vitrine animada, busca demonstrativa
  forms.js             esquema dos formulários + motor de renderização, validação e envio
  logo-nrota*.png      logo oficial
  img/                 retratos de artistas fictícios (gerados por IA, ilustrativos)
build.py               gera os .html a partir do conteúdo das páginas
```

Para editar textos das páginas, altere `build.py` e rode:

```bash
python3 build.py .
```

## Envio dos formulários

`assets/forms.js` envia um JSON por `POST` para a constante `ENDPOINT` (vazia nesta fase):

```json
{ "formulario": "cadastro-banda", "protocolo": "NR-XXXXXX", "enviadoEm": "ISO-8601", "dados": { } }
```

Pronto para um Web App do Google Apps Script (`doPost`). Rascunhos ficam no `localStorage` do navegador. Anexos são registrados só pelo nome até existir armazenamento.

## Pendências antes do lançamento

- Termos de uso e Política de privacidade (citados nos aceites)
- Validação de preços de Stories, Reels e combos
- Taxonomia oficial de subgêneros e cores
- Destino do `ENDPOINT` e armazenamento de anexos
