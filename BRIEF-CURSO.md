# Briefing do curso — Motion em código com o Método RISE (Opus 5.5)

Fonte para gerar o curso com `/formato-curso-v6`. Tudo aqui já está em PT-BR e sem marcas de terceiros.

## Regras de conteúdo (não negociáveis)

- **Pode citar:** Claude Opus 5.5 (o modelo), Claude Code (o agente de código), ferramentas abertas genéricas (Chrome headless, ffmpeg, Whisper, Web Audio) e fontes abertas (Inter, Newsreader, Anton, Plus Jakarta Sans).
- **NÃO citar:** o criador do material original, o produto/comunidade dele ("biblioteca de motion", "sistema operacional agêntico", links de descrição), serviços de scraping pelo nome, sites de curadoria pelo nome, nem empresas/marcas usadas nos exemplos originais. Usar "extrator de identidade visual", "site de curadoria de design", "marca A/B/C", "sua marca".
- Todos os prompts do curso vêm de `prompts/` — copiar de lá, não reescrever.

## Tese

Um bom prompt de criação não diz só **o que** gerar: diz **como produzir, como testar e quando está pronto**. O RISE transforma o prompt de descrição em **especificação operacional**. Com o Opus 5.5 (mais barato e mais rápido que o modelo topo anterior, com qualidade comparável), dá para gerar motion graphics inteiros em código, numa tentativa, com esse método.

## Público

Iniciante 30+, que usa IA mas nunca fez animação. Não precisa saber programar: o modelo escreve o código; o aluno escreve o prompt e confere os frames.

## Estrutura sugerida (trilhas → aulas)

**Trilha 1 — O método**
1. O que é motion em código (e por que não é vídeo gerado por IA): tudo é desenhado por uma função.
2. RISE: R Referências (fonte de verdade), I Ideia (início → uma mudança → fim; último frame = primeiro), S Estilo (aparência E movimento), E Examinar (render → olhar → corrigir). → `prompts/00-template-rise.md`
3. `render(t)`: mesmo t = mesmo frame. Determinismo, testabilidade, automação, escala. Por que evitar `Math.random` (usar semente/hash/ruído determinístico).
4. QA de 5 frames (0/25/50/75/100%; ex. 5 s → 0; 1,25; 2,5; 3,75; 5) + as 10 falhas. → `prompts/99-checklist-10-falhas.md`

**Trilha 2 — Os 7 níveis** (um por aula, cada um com prompt pronto em `prompts/niveis/`)
1. Slide animado (feixe na timeline)
2. Hero de site que ganha vida (extrair identidade; texto em HTML, decoração no canvas)
3. Reel com animação em cima + vídeo embaixo + legenda por palavra (máx. 3 palavras, palavra falada acende)
4. Uma cena em 16:9, 9:16 e 1:1 — reorganizar, nunca recortar; parâmetro no topo (`const BEBIDA`)
5. Logo animado com jingle em código — "qual movimento representa esta marca?"; sempre o arquivo real do logo
6. Pegar o estilo de uma referência, não a imagem — "primeiro escreva como é, depois construa"
7. Produção em escala — 100 sites → 100 mp4 + mural 10x10; TESTE (5) → VALIDAÇÃO → ESCALA

**Trilha 3 — Biblioteca de estilos** (6 estilos com prompt RISE completo em `prompts/estilos/`)
01 Gráfico editorial · 02 Lousa documental · 03 Tipografia suíça · 04 Tinta sumi · 05 Papel recortado · 06 Risografia.
Mostrar a anatomia do prompt completo: hex exatos, tempos em segundos, easing nomeado, regras numeradas, checagens específicas no E.

**Trilha 4 — Levando para agentes**
- Dividir em papéis: Diretor (mensagem/narrativa/duração) → Diretor de arte (paleta/tipo/textura/composição) → Motion designer (movimentos/easing/timing) → Programador (`render(t)`) → Avaliador (5 frames) → Corretor.
- Loop: EXECUTAR → OBSERVAR → AVALIAR → CORRIGIR → RENDERIZAR → VALIDAR. O valor está no loop de melhoria, não só na geração.
- O padrão reaproveitável fora de motion: CONTEXTO + OBJETIVO + REGRAS + EXECUÇÃO + AVALIAÇÃO + CORREÇÃO (vale para imagem, slides, páginas, dashboards, relatórios, software, anúncios, conteúdo educacional).

## Onde o método mostrou limites (ser honesto no curso)

- Reel do nível 3: a primeira versão ficou carregada demais e a fonte "rabiscada" — precisou de ajuste de sistema. Menos é mais.
- Nível 6: nem toda referência sai perfeita numa tentativa; às vezes precisa de 1–2 frases de refinamento, e para fidelidade total de imagem um gerador de imagem ajuda.
- Logos: IA desenhando logo de memória erra — use o arquivo.

## Visuais para as aulas

As demos animadas das aulas podem ser geradas com os próprios prompts de `prompts/estilos/` (cada um já pede um HTML único com `render(ctx, t, theme, w, h)`), salvas em `exemplos/`.
