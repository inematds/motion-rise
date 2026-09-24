# Motion em código — Método RISE

Curso e biblioteca de prompts para criar motion graphics desenhados em código com o **Claude Opus 5.5**.

**RISE** = **R**eferências · **I**deia · **S**tyle (estilo) · **E**xaminar.
Um prompt que não diz só *o que* gerar, mas *como produzir, como testar e quando está pronto*.

## Prompts prontos (`prompts/`)

| Arquivo | O que é |
|---|---|
| `00-template-rise.md` | O prompt em branco (curto e completo) |
| `niveis/nivel-1…7` | Os 7 níveis: slide animado, hero de site, reel com legenda, uma cena em vários formatos, logo com jingle, estilo de uma referência, produção em escala |
| `estilos/estilo-01…06` | 6 estilos com prompt RISE completo: gráfico editorial, lousa documental, tipografia suíça, tinta sumi, papel recortado, risografia |
| `99-checklist-10-falhas.md` | As 10 falhas de uma animação amadora + versão em prompt |

## Curso

**https://inematds.github.io/motion-rise/** — 10 aulas de ~15 min (formato v6, iniciante 30+).

- `landing.html` (página do curso) → `curso.html` (as aulas; montado por `montar-curso.py` a partir de `aulas/aula-N.html`)
- `exemplos/` — animações reais em `render(t)` embutidas nas aulas (slide com feixe, pôster suíço)
- `context/` — currículo, leitor simulado, descrições das cenas

Conteúdo aberto e gratuito — INEMA.CLUB.
